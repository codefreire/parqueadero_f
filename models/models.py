from app import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_nombre = db.Column(db.String(100), nullable=False)
    usuario_pase = db.relationship('Pase', backref='usuarioPase', lazy=True)


class Pase(db.Model):
    __tablename__ = 'pases'
    pase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_pase_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    tipo_pase = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_compra = db.Column(db.DateTime, nullable=False)


db.create_all()
