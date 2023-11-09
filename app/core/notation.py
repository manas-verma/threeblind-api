from typing import Dict, List

from app.models import B, D, Direction, F, Face, L, Move, R, U

FACE_NOTATION: Dict[str, Face] = {
    "U": U,
    "D": D,
    "F": F,
    "B": B,
    "R": R,
    "L": L,
}

DIRECTION_NOTATION: Dict[str, Direction] = {
    "": 1,
    "'": -1,
    "2": 2,
}


def condense_moves(moves: List[Move]) -> List[Move]:
    condensed_moves: List[Move] = []
    for move in moves:
        if condensed_moves and condensed_moves[-1][0] == move[0]:
            new_direction: Direction = (condensed_moves[-1][1] + move[1]) % 4  # type: ignore
            condensed_moves[-1] = (move[0], new_direction)
        else:
            condensed_moves.append(move)

    return condensed_moves


def parse_move(move_str: str) -> Move:
    return (FACE_NOTATION[move_str[0]], DIRECTION_NOTATION[move_str[1:]])


def parse_moves(scramble: str) -> List[Move]:
    return condense_moves([parse_move(move_str) for move_str in scramble.split()])
