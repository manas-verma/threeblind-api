from fastapi import APIRouter

from .create import router as create_router

router = APIRouter(prefix="/memo")
router.include_router(create_router)
