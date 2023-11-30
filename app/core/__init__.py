from typing import Dict, List, Optional, Tuple

from app.core.mapping import (CORNER_BUFFER, CORNER_MAPPING, CORNER_PREFERENCE,
                              EDGE_BUFFER, EDGE_MAPPING, EDGE_PREFERENCE,
                              PARITY_EDGES)
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
    corner_preference: Optional[List[str]] = CORNER_PREFERENCE,
    edge_preference: Optional[List[str]] = EDGE_PREFERENCE,
) -> Memo:
    corner_preference = corner_preference if corner_preference else CORNER_PREFERENCE
    edge_preference = edge_preference if edge_preference else EDGE_PREFERENCE

    cube = cube_from_scramble(scramble)
    reverse_corner_mapping: Dict[str, Corner] = {
        v: k for k, v in corner_mapping.items()
    }
    reverse_edge_mapping: Dict[str, Edge] = {v: k for k, v in edge_mapping.items()}

    corners_memo = corner_memo_mnemonic(
        cube,
        corner_buffer,
        corner_mapping,
        [
            reverse_corner_mapping[corner]
            for corner in corner_preference
            if corner in reverse_corner_mapping
        ],
    )
    updated_parity_cube = parity_switch(cube, corners_memo, parity_edges)
    print(edge_preference)
    edges_memo = edge_memo_mnemonic(
        updated_parity_cube,
        edge_buffer,
        edge_mapping,
        [
            reverse_edge_mapping[edge]
            for edge in edge_preference
            if edge in reverse_edge_mapping
        ],
    )

    return Memo(
        edges=edges_memo,
        corners=corners_memo,
        parity=len(corners_memo) % 2 != 0,
    )
