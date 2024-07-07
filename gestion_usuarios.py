from passlib.hash import sha256_crypt
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from flask import Flask

# Configurar la base de datos con SQLAlchemy
engine = create_engine('sqlite:///usuarios.db', echo=True)
Base = declarative_base()

# Definir el modelo de usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    contraseña = Column(String)

# Crear la tabla si no existe
Base.metadata.create_all(engine)

# Función para agregar usuario
def agregar_usuario(nombre, contraseña):
    hashed_password = sha256_crypt.hash(contraseña)
    
    try:
        usuario = Usuario(nombre=nombre, contraseña=hashed_password)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(usuario)
        session.commit()
        print(f"Usuario {nombre} agregado correctamente.")
    except IntegrityError:
        print(f"El usuario {nombre} ya existe en la base de datos. No se pudo agregar.")
        session.rollback()
    finally:
        session.close()

# Agregar usuarios de ejemplo
usuarios_ejemplo = [
    {"nombre": "Manuel Castro", "contraseña": "manuel123"},
    {"nombre": "Pablo Retamal", "contraseña": "pablo456"},
    {"nombre": "Rachel Rubilar", "contraseña": "rachel789"}
]

# Agregar usuarios a la base de datos
for usuario in usuarios_ejemplo:
    agregar_usuario(usuario["nombre"], usuario["contraseña"])

# Crear aplicación Flask
app = Flask(__name__)

# Mensaje de bienvenida
@app.route('/')
def index():
    return 'Bienvenido al sitio web de gestión de usuarios'

# Ejecutar la aplicación Flask en el puerto 5800
if __name__ == '__main__':
    app.run(port=5800)
