from typing import Dict, List, Set, Tuple

from app.core.cube import (
    counter_corners,
    counter_edge,
    get_corners,
    get_edges,
    make_cube,
    rotate_cube,
)
from app.core.notation import parse_moves
from app.models import Corner, Cube, Edge


def cube_from_scramble(scramble: str) -> Cube:
    moves = parse_moves(scramble)
    cube = make_cube()
    for move in moves:
        cube = rotate_cube(cube, move)
    return cube


def edge_memo(cube: Cube, buffer: Edge, edge_preference: List[Edge]) -> List[Edge]:
    edges = get_edges(cube)
    unsolved_edges = [edge for edge in edges if edge != edges[edge]]
    for edge in reversed(edge_preference):
        if edge in unsolved_edges:
            unsolved_edges.remove(edge)
            unsolved_edges.insert(0, edge)
    print(unsolved_edges)
    N = len(unsolved_edges) + (2 if buffer not in unsolved_edges else 0)

    visited: Set[Edge] = {buffer, counter_edge(buffer)}
    memo: List[Edge] = []
    curr = buffer
    while len(visited) < N:
        curr = edges[curr]

        if curr in visited:
            curr = [edge for edge in unsolved_edges if edge not in visited][0]
            memo.append(curr)
            continue

        memo.append(curr)
        visited.add(curr)
        visited.add(counter_edge(curr))

    return memo


def edge_memo_mnemonic(
    cube: Cube, buffer: Edge, mapping: Dict[Edge, str], edge_preference: List[Edge]
) -> List[str]:
    memo = edge_memo(cube, buffer, edge_preference)
    print(edge_preference)
    return [mapping[edge] for edge in memo]


def corner_memo(
    cube: Cube, buffer: Corner, corner_preference: List[Corner]
) -> List[Corner]:
    corners = get_corners(cube)
    unsolved_corners = [corner for corner in corners if corner != corners[corner]]
    for corner in reversed(corner_preference):
        if corner in unsolved_corners:
            unsolved_corners.remove(corner)
            unsolved_corners.insert(0, corner)
    N = len(unsolved_corners) + (3 if buffer not in unsolved_corners else 0)

    visited: Set[Corner] = {buffer, *counter_corners(buffer)}

    memo: List[Corner] = []
    curr = buffer
    while len(visited) < N:
        curr = corners[curr]
        if curr in visited:
            curr = [corner for corner in unsolved_corners if corner not in visited][0]
            memo.append(curr)
            continue

        memo.append(curr)
        visited.add(curr)
        visited.add(counter_corners(curr)[0])
        visited.add(counter_corners(curr)[1])

    return memo


def corner_memo_mnemonic(
    cube: Cube,
    buffer: Corner,
    mapping: Dict[Corner, str],
    corner_preference: List[Corner],
) -> List[str]:
    memo = corner_memo(cube, buffer, corner_preference)
    return [mapping[corner] for corner in memo]


def parity_switch(
    cube: Cube, corner_memo: List[str], parity_edges: Tuple[Edge, Edge]
) -> Cube:
    if len(corner_memo) % 2 == 0:
        return cube

    edges = get_edges(cube)
    edge_a, edge_b = parity_edges
    edge_a_counter, edge_b_counter = counter_edge(edge_a), counter_edge(edge_b)
    for edge in edges:
        edges[edge] = {
            edge_a: edge_b,
            edge_b: edge_a,
            edge_a_counter: edge_b_counter,
            edge_b_counter: edge_a_counter,
        }.get(edges[edge], edges[edge])

    return cube
