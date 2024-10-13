# Cell 1: Installation and Imports
# Make sure to run this cell to install python-chess and import necessary libraries
import chess
import chess.pgn
import chess.svg
import pandas as pd
from IPython.display import display, SVG

# Cell 2: Load and Visualize PGN File
# This cell will load a PGN file and visualize the board at the end of the game.
def load_and_visualize_pgn(filename):
    # Lade die PGN-Datei
    with open(filename) as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    
    # Gehe alle Züge durch, um die finale Stellung zu erhalten
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)
    
    # Visualisiere das Schachbrett
    display(SVG(chess.svg.board(board=board)))

# Example usage:
# load_and_visualize_pgn('path/to/your/file.pgn')

# Cell 3: Load and Visualize FEN String
# This cell will load a FEN string and visualize the board.
def load_and_visualize_fen(fen_string):
    # Lade die FEN-Stellung
    board = chess.Board(fen_string)
    
    # Visualisiere das Schachbrett
    display(SVG(chess.svg.board(board=board)))

# Example usage:
# load_and_visualize_fen('r1bqkbnr/pppppppp/n7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 2 3')

# Cell 4: Material Evaluation
# This cell evaluates the material value of the board state.
def evaluate_material(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3.5,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    white_material_value = sum(len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type] for piece_type in piece_values)
    black_material_value = sum(len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type] for piece_type in piece_values)
    material_value = white_material_value - black_material_value
    return white_material_value, black_material_value, material_value

# Cell 5: Pawn Structure Evaluation
# This cell evaluates the pawn structure of the board state.
def evaluate_pawn_structure(board, color):
    value = 0
    pawns = board.pieces(chess.PAWN, color)
    files = [chess.square_file(pawn) for pawn in pawns]
    
    # Doppelbauern bestrafen
    for file in set(files):
        if files.count(file) > 1:
            value -= 0.5 * (files.count(file) - 1)
    
    # Isolierte Bauern bestrafen
    for pawn in pawns:
        file = chess.square_file(pawn)
        if not any(chess.square_file(other_pawn) in [file - 1, file + 1] for other_pawn in pawns):
            value -= 0.5
    
    return value

# Cell 6: King Safety Evaluation
# This cell evaluates the safety of the king based on open lines.
def evaluate_king_safety(board, color):
    value = 0
    king_square = board.king(color)
    king_file = chess.square_file(king_square)
    
    # Offene Linien in der Nähe des Königs bestrafen
    for file_offset in [-1, 0, 1]:
        file = king_file + file_offset
        if 0 <= file <= 7:
            for rank in range(8):
                if board.piece_at(chess.square(file, rank)):
                    value -= 0.5
    
    return value

# Cell 7: Rook Activity Evaluation
# This cell evaluates the activity of rooks based on open and half-open files.
def evaluate_rook_activity(board, color):
    value = 0
    rooks = board.pieces(chess.ROOK, color)
    for rook in rooks:
        file = chess.square_file(rook)
        if not any(board.piece_at(chess.square(file, rank)) for rank in range(8)):
            value += 0.5
    
    return value

# Cell 8: Center Control Evaluation
# This cell evaluates the control of the center squares.
def evaluate_center_control(board, color):
    value = 0
    center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
    for square in center_squares:
        if board.piece_at(square) and board.piece_at(square).color == color:
            value += 0.5
    
    return value

# Cell 9: Mobility Evaluation
# This cell evaluates the mobility of pieces.
def evaluate_mobility(board, color):
    value = 0
    for piece in board.piece_map().values():
        if piece.color == color:
            value += len(list(board.legal_moves)) * 0.1
    
    return value

# Cell 10: Piece Coordination Evaluation
# This cell evaluates the coordination of pieces.
def evaluate_piece_coordination(board, color):
    value = 0
    for square in board.piece_map():
        piece = board.piece_at(square)
        if piece and piece.color == color:
            for move in board.legal_moves:
                if move.to_square == square:
                    value += 0.05
    
    return value

# Cell 11: Combined Board Evaluation
# This cell combines all evaluations to give a full analysis of the board state.
def evaluate_board(board):
    white_material_value, black_material_value, material_value = evaluate_material(board)
    white_pawn_structure_value = evaluate_pawn_structure(board, chess.WHITE)
    black_pawn_structure_value = evaluate_pawn_structure(board, chess.BLACK)
    pawn_structure_value = white_pawn_structure_value - black_pawn_structure_value
    white_king_safety_value = evaluate_king_safety(board, chess.WHITE)
    black_king_safety_value = evaluate_king_safety(board, chess.BLACK)
    king_safety_value = white_king_safety_value - black_king_safety_value
    white_rook_activity_value = evaluate_rook_activity(board, chess.WHITE)
    black_rook_activity_value = evaluate_rook_activity(board, chess.BLACK)
    rook_activity_value = white_rook_activity_value - black_rook_activity_value
    white_center_control_value = evaluate_center_control(board, chess.WHITE)
    black_center_control_value = evaluate_center_control(board, chess.BLACK)
    center_control_value = white_center_control_value - black_center_control_value
    white_mobility_value = evaluate_mobility(board, chess.WHITE)
    black_mobility_value = evaluate_mobility(board, chess.BLACK)
    mobility_value = white_mobility_value - black_mobility_value
    white_piece_coordination_value = evaluate_piece_coordination(board, chess.WHITE)
    black_piece_coordination_value = evaluate_piece_coordination(board, chess.BLACK)
    piece_coordination_value = white_piece_coordination_value - black_piece_coordination_value
    
    data = {
        'Kriterium': [
            'Materialbewertung', 'Bauernstruktur', 'Königssicherheit', 'Aktivität der Türme',
            'Zentrumskontrolle', 'Figurenmobilität', 'Figurenkoordination'
        ],
        'Schwarz': [
            black_material_value, black_pawn_structure_value, black_king_safety_value,
            black_rook_activity_value, black_center_control_value, black_mobility_value,
            black_piece_coordination_value
        ],
        'Weiß': [
            white_material_value, white_pawn_structure_value, white_king_safety_value,
            white_rook_activity_value, white_center_control_value, white_mobility_value,
            white_piece_coordination_value
        ],
        'Total': [
            material_value, pawn_structure_value, king_safety_value, rook_activity_value,
            center_control_value, mobility_value, piece_coordination_value
        ]
    }
    
    # Gesamte Stellungsbewertung
    total_value = sum(data['Total'])
    data['Kriterium'].append('Gesamtbewertung')
    data['Schwarz'].append('-')
    data['Weiß'].append('-')
    data['Total'].append(total_value)
    
    # Erstelle DataFrame und Ausgabe als Tabelle
    df = pd.DataFrame(data)
    display(df)

# Example usage:
# board = chess.Board() # You can pass in any board state here
# evaluate_board(board)