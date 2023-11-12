from typing import Callable, Dict, List

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

CUBE_ROTATIONS: Dict[str, Dict[Face, Face]] = {
    "x": {U: B, F: U, D: F, B: D, R: R, L: L},
    "y": {F: R, R: B, B: L, L: F, U: U, D: D},
    "z": {U: R, L: U, D: L, R: D, F: F, B: B},
    "x'": {U: F, F: D, D: B, B: U, R: R, L: L},
    "y'": {F: L, R: F, B: R, L: B, U: U, D: D},
    "z'": {U: L, L: D, D: R, R: U, F: F, B: B},
    "x2": {U: D, F: B, D: U, B: F, R: R, L: L},
    "y2": {F: B, R: L, B: F, L: R, U: U, D: D},
    "z2": {U: D, L: R, D: U, R: L, F: F, B: B},
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
    apply_rotation = lambda move: move

    moves = []
    for move_str in scramble.split():
        if move_str in CUBE_ROTATIONS:
            rotation = CUBE_ROTATIONS[move_str]
            previous_apply_rotation = apply_rotation
            apply_rotation = lambda move: previous_apply_rotation(
                (
                    rotation[move[0]],
                    move[1],
                )
            )
        else:
            moves.append(apply_rotation(parse_move(move_str)))

    print(moves)
    return condense_moves(moves)
