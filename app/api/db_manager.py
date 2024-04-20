from app.api.models import ArtistIn, ArtistOut, ArtistUpdate
from app.api.db import artists, database


async def add_artist(payload: ArtistIn):
    query = artists.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_artists():
    query = artists.select()
    return await database.fetch_all(query=query)


async def get_artist(id):
    query = artists.select(artists.c.id == id)
    return await database.fetch_one(query=query)


async def delete_artist(id: int):
    query = artists.delete().where(artists.c.id == id)
    return await database.execute(query=query)


async def update_artist(id: int, payload: ArtistIn):
    query = (
        artists
        .update()
        .where(artists.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
