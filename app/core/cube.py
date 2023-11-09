from typing import Dict, Tuple

from app.models import (CENTERS, CLOCKWISE, CORNER, EDGES, Corner, Cube, Edge,
                        Face, Move)


def make_cube() -> Cube:
    edges = {edge: edge for edge in EDGES}
    corners = {corner: corner for corner in CORNER}
    centers = {center: center for center in CENTERS}
    return (
        centers,
        edges,
        corners,
    )


def get_edges(cube: Cube) -> Dict[Edge, Edge]:
    _, edges, _ = cube
    return edges


def counter_edge(edge: Edge) -> Edge:
    return (edge[1], edge[0])


def get_corners(cube: Cube) -> Dict[Corner, Corner]:
    _, _, corners = cube
    return corners


def order_corner(corner: Corner) -> Corner:
    return (
        corner[0],
        min([corner[1], corner[2]], key=abs),  # type: ignore
        max([corner[1], corner[2]], key=abs),  # type: ignore
    )


def counter_corners(corner: Corner) -> Tuple[Corner, Corner]:
    return (
        order_corner((corner[1], corner[0], corner[2])),
        order_corner((corner[2], corner[0], corner[1])),
    )


def rotate_sticker(sticker: Face, move: Move) -> Face:
    face, direction = move
    if sticker not in CLOCKWISE[face]:
        return sticker
    new_sticker = sticker
    rotations = (4 + direction) % 4
    for _ in range(rotations):
        new_sticker = CLOCKWISE[face][new_sticker]
    return new_sticker


def rotate_edge(edge: Edge, move: Move) -> Edge:
    if move[0] not in edge:
        return edge
    return (
        rotate_sticker(edge[0], move),
        rotate_sticker(edge[1], move),
    )


def rotate_corner(corner: Corner, move: Move) -> Corner:
    if move[0] not in corner:
        return corner
    return order_corner(
        (
            rotate_sticker(corner[0], move),
            rotate_sticker(corner[1], move),
            rotate_sticker(corner[2], move),
        )
    )


def rotate_cube(cube: Cube, move: Move) -> Cube:
    centers, edges, corners = cube
    new_edges = edges.copy()
    for edge in edges:
        new_edges[rotate_edge(edge, move)] = edges[edge]
    new_corners = corners.copy()
    for corner in corners:
        new_corners[rotate_corner(corner, move)] = corners[corner]
    return (
        centers,
        new_edges,
        new_corners,
    )
