from fastapi import APIRouter, HTTPException
from app.schemas import HangmanStartSchema, HangmanGuessSchema
from app.services import hangman_service

# Mudamos de Blueprint para APIRouter
router = APIRouter(prefix="/hangman", tags=["Hangman"])

@router.post("/start", status_code=201)
def start(data: HangmanStartSchema):
    # O FastAPI já validou o 'data' usando o Pydantic automaticamente!
    game = hangman_service.start_new_game(data.player_id)
    
    if not game:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")

    return {
        "game_id": game.id,
        "masked_word": game.masked_word,
        "attempts_left": game.attempts_left,
        "status": game.status
    }

@router.post("/guess", status_code=200)
def guess(data: HangmanGuessSchema):
    game, message = hangman_service.process_guess(data.game_id, data.letter)
    
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado (Id incorreto ou reinício do servidor)")
    
    if message and message not in ["Vitória!", "Derrota!", "WIN", "LOSE"]:
        raise HTTPException(status_code=400, detail={"message": message, "status": game.status})

    return {
        "game_id": game.id,
        "masked_word": game.masked_word,
        "attempts_left": game.attempts_left,
        "status": game.status,
        "message": message
    }

@router.get("/status/{game_id}")
def status(game_id: int):
    game = hangman_service.get_game_status(game_id)
    
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    return {
        "game_id": game.id,
        "masked_word": game.masked_word,
        "attempts_left": game.attempts_left,
        "guessed_letters": game.guessed_letters,
        "status": game.status
    }

@router.get("/scoreboard")
def scoreboard():
    return hangman_service.get_scoreboard()