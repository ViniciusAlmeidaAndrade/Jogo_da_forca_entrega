import random
from app.models.game import Game
from app.repositories.hangman_repository import games, next_game_id
from app.repositories.player_repository import player_db

WORD_LIST = ["PYTHON", "FLASK", "API", "CODIGO", "SERVIDOR", "DADOS"]

def start_new_game(player_id: int):
    global next_game_id
    
    if player_id not in player_db:
        return None

    secret_word = random.choice(WORD_LIST)
    masked_word = "_" * len(secret_word)
    
    new_game = Game(
        id=next_game_id,
        player_id=player_id,
        secret_word=secret_word,
        masked_word=masked_word,
        attempts_left=6,
        guessed_letters=[],
        status="IN_PROGRESS"
    )
    
    games[next_game_id] = new_game
    next_game_id += 1
    return new_game

def process_guess(game_id: int, letter: str):
    game = games.get(game_id)
    
    if not game:
        return None, "Game not found"

    if game.status != "IN_PROGRESS":
        return game, "Game is already finished"

    letter = letter.upper()

    if letter in game.guessed_letters:
        return game, "Letter already guessed"

    game.guessed_letters.append(letter)

    if letter in game.secret_word:
        word_list = list(game.masked_word)
        for idx, char in enumerate(game.secret_word):
            if char == letter:
                word_list[idx] = letter
        game.masked_word = "".join(word_list)
        
        if "_" not in game.masked_word:
            game.status = "WIN"
            player = player_db.get(game.player_id)
            if player:
                player.score += 1
    else:
        game.attempts_left -= 1
        if game.attempts_left <= 0:
            game.status = "LOSE"
            game.masked_word = game.secret_word 

    return game, None

def get_game_status(game_id: int):
    return games.get(game_id)

def get_scoreboard_data():
    players_list = list(player_db.values())
    players_list.sort(key=lambda p: p.score, reverse=True)
    return players_list