from flask import request, Response
from database.model import Product
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ProductAlreadyExistsError, InternalServerError, UpdateProductError, DeletingProductError

class ProductsApi(Resource):

    def get(self):
        product = Product.objects().to_json()
        return Response(product, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            product = Product(**body).save()
            id = product.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProductAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class ProductApi(Resource):

    def put(self, id):
        try:
            body = request.get_json()
            Product.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdateProductError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        try:
            Product.objects.get(id=id).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingProductError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            product = Product.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200)
        except DoesNotExist:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError