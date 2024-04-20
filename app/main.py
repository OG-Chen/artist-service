from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException


app = FastAPI(openapi_url="/api/v1/artists/openapi.json", docs_url="/api/v1/artists/docs")

artists_router = APIRouter()

artists = [
    {'artists_id': 1,
     'name': 'Kany West',
     'age': '47',
     'auditions': '1 billion',
     'genre': 'rap, R&B, electronic, gospel'},
    {'artists_id': 2,
     'name': 'Валерий Меладзе',
     'age': '58',
     'auditions': '45 millions',
     'genre': 'поп, рок, эстрадная песня'},
    {'artists_id': 3,
     'name': 'Billie Eilish',
     'age': '22',
     'auditions': '300 millions',
     'genre': 'rap, pop'},
    {'artists_id': 4,
     'name': 'The Weeknd',
     'age': '34',
     'auditions': '700 millions',
     'genre': 'rap, R&B'},
    {'artists_id': 5,
     'name': 'Eminem',
     'age': '51',
     'auditions': '1 billion',
     'genre': 'rap, hip-hop'}
]


@artists_router.get("/")
async def read_artists():
    return artists


@artists_router.get("/{artists_id}")
async def read_artist(artists_id: int):
    for artist in artists:
        if artist['artists_id'] == artists_id:
            return artist
    return None

app.include_router(artists_router, prefix='/api/v1/artists', tags=['artists'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)