from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Define rutas absolutas o relativas correctas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_path = os.path.join(BASE_DIR, "frontend", "static")
templates_path = os.path.join(BASE_DIR, "frontend", "templates")

# Monta carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Define carpeta de templates
templates = Jinja2Templates(directory=templates_path)

@app.get("/hotelVictoria", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})