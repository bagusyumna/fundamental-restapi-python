from .db import db


class Product(db.Document):
    kode_barang = db.StringField(required=True, unique=True)
    nama_barang = db.ListField(required=True)
    jenis_barang = db.ListField(required=True)


