from fastapi import FastAPI
from src.auth.routers import router as router_auth
from src.post.routers import router as router_post


app = FastAPI(title="Help Four Paws")
app.include_router(router_auth)
app.include_router(router_post)