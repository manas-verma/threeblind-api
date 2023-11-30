from typing import Dict, List, Optional, Tuple

from fastapi import APIRouter
from pydantic import BaseModel

from app.core import make_memo
from app.models import CORNERS, EDGES, Corner, Edge, Memo

router = APIRouter()
endpoint = "/create"


class Request(BaseModel):
    scramble: str
    corner_buffer: Corner
    edge_buffer: Edge
    parity_edges: Tuple[Edge, Edge]
    reverse_corner_mapping: Dict[str, Corner]
    reverse_edge_mapping: Dict[str, Edge]
    edge_preference: Optional[List[str]] = None
    corner_preference: Optional[List[str]] = None


class Response(BaseModel):
    memo: Memo


@router.post(endpoint)
async def handler(req: Request) -> Response:
    corner_mapping: Dict[Corner, str] = {
        v: k for k, v in req.reverse_corner_mapping.items()
    }
    for corner in CORNERS:
        corner_mapping[corner] = corner_mapping.get(corner, "")

    edge_mapping: Dict[Edge, str] = {v: k for k, v in req.reverse_edge_mapping.items()}
    for edge in EDGES:
        edge_mapping[edge] = edge_mapping.get(edge, "")

    memo = make_memo(
        req.scramble,
        req.corner_buffer,
        req.edge_buffer,
        req.parity_edges,
        corner_mapping,
        edge_mapping,
        req.corner_preference,
        req.edge_preference,
    )
    return Response(memo=memo)
