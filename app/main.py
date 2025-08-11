from fastapi import FastAPI
from app.routes import all_routers

app = FastAPI()

for router, prefix in all_routers:
    app.include_router(router, prefix=prefix)