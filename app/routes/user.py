from fastapi import APIRouter, status, Request, Depends
from starlette.responses import JSONResponse

from app.database.models.user import UserBasic
from app.database.services.user import UserService

router = APIRouter()


@router.post(
    "/add/user",
    name='user:add',
)
async def add_user(user: UserBasic, user_service=Depends(UserService)):
    user_id = await user_service.add_user(user=user)

    if user_id:
        return JSONResponse(
            {'user id': user_id},
            status_code=status.HTTP_201_CREATED,
        )
    else:
        return JSONResponse(
            'User was not created',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )


@router.get(
    "/get/user/{user_id}",
    name='user:get',
    status_code=status.HTTP_200_OK
)
async def get_user(user_id: int, user_service=Depends(UserService)):
    user = await user_service.get_user(user_id)
    return user if user else 'User not exist'


@router.delete(
    "/delete/user/{user_id}",
    name='user:delete',
)
async def delete_user(user_id: int, user_service=Depends(UserService)):
    user_deleted = await user_service.delete_user(user_id)

    if user_deleted:
        return JSONResponse(
            'User successfully deleted',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'User was not deleted',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )


@router.patch(
    "/update/user/{user_id}",
    name='user:update',
)
async def update_user(user_id: int, request: Request, user_service=Depends(UserService)):
    update_fields = await request.json()
    user_updated = await user_service.update_user(user_id, update_fields)

    if user_updated:
        return JSONResponse(
            'User successfully updated',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'User was not updated',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )
