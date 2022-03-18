from fastapi import APIRouter, status, Request, Depends
from starlette.responses import JSONResponse

from app.database.models.event import EventBasic
from app.database.services.event import EventService

router = APIRouter()


@router.post(
    "/add/event",
    name='event:add',
)
async def add_event(event: EventBasic, event_service=Depends(EventService)):
    event_id = await event_service.add_event(event=event)

    if event_id:
        return JSONResponse(
            {'event id': event_id},
            status_code=status.HTTP_201_CREATED,
        )
    else:
        return 'Event was not recorded'


@router.get(
    "/get/event/{event_id}",
    name='event:get',
    status_code=status.HTTP_200_OK
)
async def get_event(event_id: int, event_service=Depends(EventService)):
    event = await event_service.get_event(event_id)
    return event if event else 'Event not exist'


@router.delete(
    "/delete/event/{event_id}",
    name='tariff:delete',
)
async def delete_event(event_id: int, event_service=Depends(EventService)):
    event_deleted = await event_service.delete_event(event_id)

    if event_deleted:
        return JSONResponse(
            'Event successfully deleted',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'Event was not deleted',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )


@router.patch(
    "/update/event/{event_id}",
    name='event:update',
)
async def update_event(event_id: int, request: Request, event_service=Depends(EventService)):
    update_fields = await request.json()
    event_updated = await event_service.update_event(event_id, update_fields)

    if event_updated:
        return JSONResponse(
            'Event successfully updated',
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            'Event was not updated',
            status_code=status.HTTP_304_NOT_MODIFIED,
        )
