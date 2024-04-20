from pydantic import BaseModel
from typing import List, Optional


class ArtistIn(BaseModel):
    name: str
    age: int
    auditions: int
    genre: str
    labels_id: List[int]


class ArtistOut(ArtistIn):
    id: int


class ArtistUpdate(ArtistIn):
    name: Optional[str] = None
    age: Optional[int] = None
    auditions: Optional[int] = None
    genre: Optional[str] = None
    labels_id: Optional[List[int]] = None