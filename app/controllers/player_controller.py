from fastapi import APIRouter, HTTPException
from app.schemas import PlayerCreateSchema
from app.services import player_service

router = APIRouter(prefix="/player", tags=["Player"])

@router.post("/create", status_code=201)
def create_player(data: PlayerCreateSchema):
    # Não precisa de try/except ValidationError, o FastAPI faz sozinho
    new_player = player_service.create_player(data.name)
    
    return {
        "player_id": new_player.id,
        "name": new_player.name,
        "score": new_player.score
    }