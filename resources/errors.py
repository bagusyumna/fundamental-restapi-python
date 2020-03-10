from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class ProductAlreadyExistsError(HTTPException):
    pass

class UpdateProductError(HTTPException):
    pass

class DeletingProductError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ProductAlreadyExistsError": {
        "message": "Product with given code already exist",
        "status": 400
    },
    "UpdateProductError": {
        "message": "Updating product added by other user is forbidden",
        "status": 403
    },
    "DeletingProductError": {
        "message": "Deleting product added by other user is forbidden",
        "status": 403
    },
}
