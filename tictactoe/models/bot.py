from langchain.chat_models import HuggingFaceChat
from langchain.prompts import ChatPromptTemplate
import json
import re

from models.board import Board
from models.player import Player

class BotPlayer(Player):
    def __init__(self, player: Player):
        # Use ChatHuggingFace from chat_models
        self.llm = HuggingFaceChat(
            repo_id="HuggingFaceH4/zephyr-7b-alpha",
            model_kwargs={"temperature": 0.2, "max_new_tokens": 128}
        )

        self.name = player.name
        self.symbol = player.symbol
        self.player_choose = player.player_choose

        # Prompt for Tic Tac Toe
        self.prompt = ChatPromptTemplate.from_template("""
You are an expert Tic Tac Toe player.
Current board state:

{board}

Rules:
- "O" = Bot (your move)
- "X" = Human
- " " = Empty
- Respond ONLY with valid JSON: {{"row": number, "col": number}}

Your turn: Pick the best move for O.
""")

        self.chain = self.prompt | self.llm

    def get_move(self, board_obj):
        board_str = board_obj.to_llm_string()
        result = self.chain.invoke({"board": board_str})
        try:
            json_str = re.search(r"\{.*\}", result, re.DOTALL).group()
            move = json.loads(json_str)
            return move["row"], move["col"]
        except Exception as e:
            print("Error parsing LLM response:", e)
            return self.fallback_move(board_obj)

    def fallback_move(self, board_obj):
        for r in range(board_obj.size):
            for c in range(board_obj.size):
                if board_obj.board[r][c] == " ":
                    return r, c
        return -1, -1

# Example usage
test_player = Player("Bot", "O", "Bot")
bot = BotPlayer(test_player)

testboard = Board(3)
row, col = bot.get_move(testboard)
print(row, col)
