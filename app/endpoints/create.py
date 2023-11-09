from typing import Dict, Tuple

from fastapi import APIRouter
from pydantic import BaseModel

from app.core import make_memo
from app.models import Corner, Edge, Memo

router = APIRouter()
endpoint = "/create"


class Request(BaseModel):
    scramble: str
    corner_buffer: Corner
    edge_buffer: Edge
    parity_edges: Tuple[Edge, Edge]
    corner_mapping: Dict[Corner, str]
    edge_mapping: Dict[Edge, str]


class Response(BaseModel):
    memo: Memo


@router.post(endpoint)
async def handler(req: Request) -> Response:
    memo = make_memo(
        req.scramble,
        req.corner_buffer,
        req.edge_buffer,
        req.parity_edges,
        req.corner_mapping,
        req.edge_mapping,
    )
    return Response(memo=memo)
