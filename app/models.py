from typing import Dict, List, Literal, Tuple

from pydantic import BaseModel

Face = Literal[1, -1, 2, -2, 3, -3]
U: Face = 1
D: Face = -1
F: Face = 2
B: Face = -2
R: Face = 3
L: Face = -3


CLOCKWISE: Dict[Face, Dict[Face, Face]] = {
    U: {F: L, L: B, B: R, R: F},
    D: {F: R, R: B, B: L, L: F},
    F: {U: R, R: D, D: L, L: U},
    B: {U: L, L: D, D: R, R: U},
    R: {U: B, B: D, D: F, F: U},
    L: {U: F, F: D, D: B, B: U},
}


Center = Tuple[Face]
CENTERS: List[Center] = [
    (U,),
    (D,),
    (F,),
    (B,),
    (R,),
    (L,),
]

Edge = Tuple[Face, Face]
EDGES: List[Edge] = [
    (U, F),
    (D, F),
    (U, B),
    (D, B),
    (U, R),
    (D, R),
    (U, L),
    (D, L),
    (F, U),
    (B, U),
    (F, D),
    (B, D),
    (F, R),
    (B, R),
    (F, L),
    (B, L),
    (R, U),
    (L, U),
    (R, D),
    (L, D),
    (R, F),
    (L, F),
    (R, B),
    (L, B),
]

Corner = Tuple[Face, Face, Face]
CORNERS: List[Corner] = [
    (U, F, R),
    (U, F, L),
    (U, B, R),
    (U, B, L),
    (D, F, R),
    (D, F, L),
    (D, B, R),
    (D, B, L),
    (F, U, R),
    (F, U, L),
    (F, D, L),
    (F, D, R),
    (B, U, R),
    (B, U, L),
    (B, D, R),
    (B, D, L),
    (R, U, F),
    (R, U, B),
    (R, D, F),
    (R, D, B),
    (L, U, F),
    (L, U, B),
    (L, D, F),
    (L, D, B),
]


Cube = Tuple[Dict[Center, Center], Dict[Edge, Edge], Dict[Corner, Corner]]

Direction = Literal[-1, 1, 2, 3]

Move = Tuple[Face, Direction]


class Memo(BaseModel):
    edges: List[str]
    corners: List[str]
    parity: bool
