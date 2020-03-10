from .product import ProductsApi, ProductApi

def initialize_routes(api):

    api.add_resource(ProductsApi,'/api/v1/product')
    api.add_resource(ProductApi,'/api/v1/product/<id>')
