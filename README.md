# Atividade Final - API Jogo da Forca

Projeto desenvolvido para a disciplina de Desenvolvimento Rápido. Trata-se de uma API RESTful que implementa a lógica do clássico **Jogo da Forca**.

## 📋 Sobre o Projeto
**Opção Escolhida:** Jogo de Forca (Palavra Secreta).

O sistema permite criar jogadores, iniciar novas partidas com palavras sorteadas aleatoriamente, realizar palpites (chutes) e consultar o placar geral. Todo o estado do jogo é mantido em memória durante a execução do servidor.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Framework:** FastAPI
- **Validação:** Pydantic
- **Servidor:** Uvicorn
- **Arquitetura:** MVC com camadas de Service e Repository

## 📂 Estrutura do Projeto
Jogo_da_forca/
├── app/
│   ├── controllers/   # Rotas e endpoints (API)
│   ├── models/        # Classes de objetos (Game, Player)
│   ├── repositories/  # Persistência em memória
│   ├── services/      # Regras de negócio (Lógica do jogo)
│   ├── schemas.py     # Validações Pydantic
│   └── __init__.py    # Inicialização da App
├── main.py            # Ponto de entrada
├── requirements.txt   # Dependências
└── README.md          # Documentação

## ⚙️ Como Rodar o Projeto

### 1. Clone ou baixe o repositório

### 2. Crie e ative um ambiente virtual

**Windows**
python -m venv venv
.
env\Scripts ctivate

**Linux/Mac**
python3 -m venv venv
source venv/bin/activate

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Execute o servidor
python main.py

O servidor iniciará em:
http://127.0.0.1:8000

## 📖 Documentação Interativa (Swagger UI)
Acesse:
http://127.0.0.1:8000/docs

## 🎮 Como Jogar (Exemplos de Requisições)

### 1. Criar um Jogador
POST /player/create
{
  "name": "Vinicius"
}

### 2. Iniciar Jogo
POST /hangman/start
{
  "player_id": 1
}

### 3. Fazer um Chute
POST /hangman/guess
{
  "game_id": 1,
  "letter": "A"
}

### 4. Consultar Placar
GET /hangman/scoreboard

## 🧪 Testes Manuais
Swagger UI, Postman ou Insomnia

## ✔️ Dica Final
O conteúdo cumpre tudo solicitado. Zipar o projeto sem venv e __pycache__.
