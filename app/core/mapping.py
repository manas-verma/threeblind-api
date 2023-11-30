from typing import Dict

from app.models import B, Corner, D, Edge, F, L, R, U

EDGE_BUFFER = (D, F)
EDGE_MAPPING: Dict[Edge, str] = {
    (U, F): "C",
    (D, F): "",
    (U, B): "B",
    (D, B): "X",
    (U, R): "R",
    (D, R): "W",
    (U, L): "L",
    (D, L): "V",
    (F, U): "D",
    (B, U): "A",
    (F, D): "",
    (B, D): "Y",
    (F, R): "F",
    (B, R): "O",
    (F, L): "E",
    (B, L): "N",
    (R, U): "M",
    (L, U): "H",
    (R, D): "T",
    (L, D): "U",
    (R, F): "G",
    (L, F): "K",
    (R, B): "J",
    (L, B): "S",
}
EDGE_PREFERENCE = [
    "B",
    "C",
    "X",
    "L",
    "R",
    "E",
    "F",
]

CORNER_BUFFER = (U, B, L)
CORNER_MAPPING: Dict[Corner, str] = {
    (U, B, L): "",
    (U, B, R): "A",
    (U, F, R): "B",
    (U, F, L): "C",
    (D, F, L): "S",
    (D, F, R): "T",
    (D, B, R): "U",
    (D, B, L): "V",
    (F, U, L): "H",
    (F, U, R): "I",
    (F, D, R): "J",
    (F, D, L): "K",
    (B, U, L): "",
    (B, U, R): "W",
    (B, D, R): "X",
    (B, D, L): "Y",
    (R, U, F): "L",
    (R, U, B): "M",
    (R, D, B): "N",
    (R, D, F): "O",
    (L, U, B): "",
    (L, U, F): "E",
    (L, D, F): "F",
    (L, D, B): "G",
}
CORNER_PREFERENCE = [
    "O",
    "X",
    "G",
    "K",
    "B",
    "C",
]

PARITY_EDGES = (
    (U, B),
    (U, L),
)
