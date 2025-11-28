class Game:

    def __init__(self, id: int, player_id: int, secret_word: str, masked_word: str, attempts_left: int, guessed_letters: list, status: str):
        self.id = id
        self.player_id = player_id
        self.secret_word = secret_word
        self.masked_word = masked_word
        self.attempts_left = attempts_left
        self.guessed_letters = guessed_letters
        self.status = status