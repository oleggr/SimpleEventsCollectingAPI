from fastapi import APIRouter, status, Request, Depends
from starlette.responses import JSONResponse

from app.database.models.tariff import TariffBasic
from app.database.services.tariff import TariffService

router = APIRouter()


@router.post(
    "/add/tariff",
    name='tariff:add',
)
async def add_tariff(tariff: TariffBasic, tariff_service=Depends(TariffService)):
    tariff_id = await tariff_service.add_tariff(tariff=tariff)

    if tariff_id:
        return JSONResponse(
            {'tariff id': tariff_id},
            status_code=status.HTTP_201_CREATED,
        )
    else:
        return JSONResponse(
            'Tariff was not created',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )


@router.get(
    "/get/tariff/{tariff_id}",
    name='tariff:get',
    status_code=status.HTTP_200_OK
)
async def get_tariff(tariff_id: int, tariff_service=Depends(TariffService)):
    tariff = await tariff_service.get_tariff(tariff_id)
    return tariff if tariff else 'Tariff not exist'


@router.delete(
    "/delete/tariff/{tariff_id}",
    name='tariff:delete',
)
async def delete_tariff(tariff_id: int, tariff_service=Depends(TariffService)):
    tariff_deleted = await tariff_service.delete_tariff(tariff_id)

    if tariff_deleted:
        return JSONResponse(
            'Tariff successfully deleted',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'Tariff was not deleted',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )


@router.patch(
    "/update/tariff/{tariff_id}",
    name='tariff:update',
)
async def update_tariff(tariff_id: int, request: Request, tariff_service=Depends(TariffService)):
    update_fields = await request.json()
    tariff_updated = await tariff_service.update_tariff(tariff_id, update_fields)

    if tariff_updated:
        return JSONResponse(
            'Tariff successfully updated',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'Tariff was not updated',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )
