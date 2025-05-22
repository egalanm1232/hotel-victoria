from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

# Cifrado de contraseña si tiene caracteres especiales
#password = quote_plus("1234")  # Tu contraseña de PostgreSQL

# URL de conexión correcta con usuario "postgres"
DATABASE_URL = f"postgresql://postgres:1234@localhost/bdHotelVictoria"

# Crear el motor y la sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
