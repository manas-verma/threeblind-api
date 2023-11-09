from typing import Dict, Tuple

from app.core.mapping import (CORNER_BUFFER, CORNER_MAPPING, EDGE_BUFFER,
                              EDGE_MAPPING, PARITY_EDGES)
from app.core.memo import (corner_memo_mnemonic, cube_from_scramble,
                           edge_memo_mnemonic, parity_switch)
from app.models import Corner, Edge, Memo


def make_memo(
    scramble: str,
    corner_buffer: Corner = CORNER_BUFFER,
    edge_buffer: Edge = EDGE_BUFFER,
    parity_edges: Tuple[Edge, Edge] = PARITY_EDGES,
    corner_mapping: Dict[Corner, str] = CORNER_MAPPING,
    edge_mapping: Dict[Edge, str] = EDGE_MAPPING,
) -> Memo:
    cube = cube_from_scramble(scramble)
    corners_memo = corner_memo_mnemonic(cube, corner_buffer, corner_mapping)
    updated_parity_cube = parity_switch(cube, corners_memo, parity_edges)
    edges_memo = edge_memo_mnemonic(updated_parity_cube, edge_buffer, edge_mapping)

    return Memo(
        edges=edges_memo,
        corners=corners_memo,
        parity=len(corners_memo) % 2 != 0,
    )
