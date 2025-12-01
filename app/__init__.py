from fastapi import FastAPI
from app.controllers.hangman_controller import router as hangman_router
from app.controllers.player_controller import router as player_router

def create_app():
    app = FastAPI(title="Jogo da Forca API")

    # Em vez de register_blueprint, usamos include_router
    app.include_router(hangman_router)
    app.include_router(player_router)

    return app