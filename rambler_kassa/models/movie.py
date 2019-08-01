from datetime import date
from pydantic import BaseModel, validator
from typing import List, Optional


class Movie(BaseModel):
    OriginalName: str
    Genre: List[str]
    Country: List[str]
    ViewCountDaily: int
    AgeRestriction: str
    Thumbnail: Optional[str]
    Cast: List[str]
    Description: str
    Director: List[str]
    CreatorName: Optional[str]
    CreatorObjectID: Optional[int]
    Year: str
    Duration: str
    HorizonalThumbnail: Optional[str]
    IsNonStop: bool
    SubCreationIDs: List[int]
    Rating: str
    Trailers: Optional[List[str]]
    Frames: Optional[List[str]]
    ReleaseDate: date
    KinoplanID: Optional[int]
    ObjectID: int
    ClassType: str
    Name: str
    AfishaClassID: Optional[int]
    AfishaObjectID: Optional[int]

    @validator('Genre', 'Country', 'Cast', 'Director', pre=True, whole=True)
    def str_to_list(cls, v):
        res = v.split(',')
        if not res or not res[0]:
            return []
        return [i.strip() for i in res]

    @validator('Trailers', pre=True, whole=True)
    def trailers(cls, v):
        return [i[2:] if '//' in i[0:2] else i for i in v]
