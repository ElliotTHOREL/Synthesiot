from fastapi import FastAPI
from app.routes import all_routers
from app.connection import initialize_pool
from app.database.create import init_bdd

def create_app() -> FastAPI:
    app = FastAPI()

    # Initialisation DB
    initialize_pool()
    init_bdd()

    # Routes
    for router, prefix in all_routers:
        app.include_router(router, prefix=prefix)

    return app

app = create_app()