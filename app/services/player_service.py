from app.models.player import Player
from app.repositories.player_repository import player_db, next_player_id

def create_player(name: str):
    global next_player_id
    player_id = next_player_id
    new_player = Player(id=player_id, name=name, score=0)
    player_db[player_id] = new_player
    next_player_id += 1
    return new_player