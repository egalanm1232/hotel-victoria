from sqlalchemy import Column, Integer, String
from backend.database import Base
from passlib.context import CryptContext

# Configuración para cifrar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String(20), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String(50), nullable=False)
    telefono = Column(String(15), nullable=False)
    ciudad = Column(String(50), nullable=False)
    rol = Column(String(20), default="cliente")

    def hash_password(self, password):
        return pwd_context.hash(password)
