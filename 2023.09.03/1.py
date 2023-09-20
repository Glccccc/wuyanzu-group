import chess
      
class Turn:

    """Хранит информацию о фигуре сделавшей ход, стартовое и конечное значения игрового поля"""
    
    def __init__(self, 
        piece: chess.Piece,
        start_square: chess.Square,
        end_square: chess.Square,
        turn_count: int = None
    ):
        self.turn_count = turn_count
        self.piece = piece
        
        if piece is not None:
            self.start_square = start_square
            self.end_square = end_square
        else:
            self.start_square = None
            self.end_square = None
    
    def __str__(self):

        return f'{self.turn_count}: {self.piece} {self.start_square} -> {self.end_square}'
        
        
class Game:

    """Совмещает функции инициатора и опекуна, управляет экземпляром игровой доски"""
    
    def __init__(self):
        self.board = chess.Chessboard()
        self.turn_count = 0
        self.turns: list[Turn] = []
        
    def move(self, start_square: str, end_square: str) -> None:

        """Совершает ход с клетки на клетку"""
        
        start_square = self.board[start_square]
        piece = self.board[start_square].piece
        end_square = self.board[end_square]
        piece.move(self.board[end_square])        
        turn= Turn(piece, start_square, end_square, self.turn_count+1)
        self.turns += [turn]
        self.turn_count += 1

    def history_turns(self):
        
        """Выводит все записанные ходы, нумерованные с единицы"""
        
        print(*(str(turn) for turn in self.turns), sep='\n')
           

    def rollback_game(self, turn_count: int):
        
        """Возвращает состояние игры к заданному ходу"""  
        
        self.board = chess.Chessboard()
        turns_copy = self.turns.copy()
        self.turns = []
        self.turn_count = 0
        for turn in turns_copy[:turn_count]:
           self.move(turn.start_square, turn.end_square)
           
           
           
# >>> game = Game()
# >>> game.move('a1','a3')
# >>> game.move('b1','b3')
# >>> game.move('c1','c3')
# >>> print(*(i for i in game.board.items()), sep='\n')
# ('a', {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: White Rook>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>})
# ('b', {1: <b1: None>, 2: <b2: White Pawn>, 3: <b3: White Knight>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>})
# ('c', {1: <c1: None>, 2: <c2: White Pawn>, 3: <c3: White Bishop>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>})
# ('d', {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>})
# ('e', {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>})
# ('f', {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>})
# ('g', {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>})
# ('h', {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>})
# >>> game.history_turns()
# 1: WR a1 -> a3
# 2: WK b1 -> b3
# 3: WB c1 -> c3
# >>> game.rollback_game(2)
# >>> print(*(i for i in game.board.items()), sep='\n')
# ('a', {1: <a1: None>, 2: <a2: White Pawn>, 3: <a3: White Rook>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>})
# ('b', {1: <b1: None>, 2: <b2: White Pawn>, 3: <b3: White Knight>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>})
# ('c', {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>})
# ('d', {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>})
# ('e', {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>})
# ('f', {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>})
# ('g', {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>})
# ('h', {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>})
# >>> game.history_turns()
# 1: WR a1 -> a3
# 2: WK b1 -> b3
# >>>
