from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, constr
from backend.database import get_db
from backend.models import Usuario
from backend.auth_services import hash_password

router = APIRouter()

# Definir el esquema de datos para el registro de usuario
class UsuarioCreate(BaseModel):
    identificacion: Annotated[str, constr(min_length=7, max_length=10, pattern="^[0-9]+$")]  # Solo números (7-10)
    email: EmailStr  # Verificación automática de formato
    password: Annotated[str, constr(min_length=8)]  # Mínimo 8 caracteres
    nombre: Annotated[str, constr(min_length=1, max_length=50)]  # No vacío, máx. 50 caracteres
    telefono: Annotated[str, constr(min_length=7, max_length=15, pattern="^[0-9]+$")]  # Solo números (7-15)
    ciudad: str  # Esto después se manejará como un desplegable en el frontend

# Ruta para registrar usuario
@router.post("/registro")
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Validar que el email e identificación no existan en la BD
    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    if db.query(Usuario).filter(Usuario.identificacion == usuario.identificacion).first():
        raise HTTPException(status_code=400, detail="La identificación ya está registrada")

    # Cifrar la contraseña con el servicio
    hashed_password = hash_password(usuario.password)

    # Crear usuario
    nuevo_usuario = Usuario(
        identificacion=usuario.identificacion,
        email=usuario.email,
        password=hashed_password,
        nombre=usuario.nombre,
        telefono=usuario.telefono,
        ciudad=usuario.ciudad,
        rol="cliente"
    )

    db.add(nuevo_usuario)
    db.commit()

    return {"mensaje": "Usuario registrado exitosamente"}