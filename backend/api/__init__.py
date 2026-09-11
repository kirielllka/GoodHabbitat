from fastapi import APIRouter

from .habit import router as habis_router
router = APIRouter()
router.include_router(habis_router)