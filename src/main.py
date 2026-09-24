from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.auth.routers import router as auth_router
from src.post.routers import router as post_router
from src.pages.router import router as page_router
from src.files.router import router as file_router


app = FastAPI(title="Help Four Paws")

app.mount(
    path="/static",
    app=StaticFiles(directory="./static"),
    name="static"
)
app.mount(
    path="/templates",
    app=StaticFiles(directory="./templates"),
    name="templates"
)
app.include_router(auth_router)
app.include_router(post_router)
app.include_router(page_router)
app.include_router(file_router)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Access-Authorization'
    ]
)
