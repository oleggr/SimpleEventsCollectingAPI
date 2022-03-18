from fastapi import APIRouter, status

from app.routes import user, tariff


router = APIRouter()
router.include_router(user.router)
router.include_router(tariff.router)


@router.get(
    "/hello",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def hello():
    return "Hello, world!"
