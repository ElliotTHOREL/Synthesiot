from fastapi import FastAPI
from app.routes import all_routers
from app.connection import initialize_pool
from app.database.create import init_bdd
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost:8080",  # ou l'URL de ton front
        "http://127.0.0.1:8080",
        "https://a0ea2ec6-2a5a-406b-92fe-9eb840a3c23f.lovableproject.com",
        # ajoute d'autres origines si besoin
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # permet d'autoriser seulement ces origines
        allow_credentials=True,
        allow_methods=["*"],    # autorise toutes les méthodes (GET, POST, OPTIONS...)
        allow_headers=["*"],    # autorise tous les headers
    )

    # Initialisation DB
    initialize_pool()
    init_bdd()

    # Routes
    for router, prefix in all_routers:
        app.include_router(router, prefix=prefix)

    return app

app = create_app()