from pydantic import BaseModel, Field

class PlayerCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=20)

class HangmanStartSchema(BaseModel):
    player_id: int

class HangmanGuessSchema(BaseModel):
    game_id: int
    letter: str = Field(..., min_length=1, max_length=1, pattern="^[a-zA-Z]$")