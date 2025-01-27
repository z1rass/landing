from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Указываем папку для шаблонов
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/blog", response_class=HTMLResponse)
async def get_blog_home(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})
