from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import ArtistOut, ArtistIn, ArtistUpdate
from app.api import db_manager
from app.api.service import is_label_present

artist = APIRouter()

@artist.post('/', response_model=ArtistIn, status_code=201)
async def create_artist(payload: ArtistIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    artist_id = await db_manager.add_artist(payload)
    response = {
        'id': artist_id,
        **payload.dict()
    }

    return response

@artist.get('/', response_model=List[ArtistOut])
async def get_artists():
    return await db_manager.get_all_artists()

@artist.get('/{id}/', response_model=ArtistOut)
async def get_artist(id: int):
    artist = await db_manager.get_artist(id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@artist.put('/{id}/', response_model=ArtistOut)
async def update_artist(id: int, payload: ArtistUpdate):
    artist = await db_manager.get_artist(id)
    if not artist:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    artist_in_db = ArtistIn(**artist)

    updated_artist = artist_in_db.copy(update=update_data)

    return await db_manager.update_artist(id, updated_artist)

@artist.delete('/{id}/', response_model=None)
async def delete_artist(id: int):
    artist = await db_manager.get_artist(id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return await db_manager.delete_artist(id)