from typing import List, Optional

from pydantic import BaseModel


class ItemCategory(BaseModel):
    value:str


class ItemCategoryCreate(ItemCategory):
    pass


class Item(ItemCategory):
    id: int
    id2: int
    class Config:
        orm_mode = True


class NewsBase(BaseModel):
    title: str
    date: str
    url: str
    media_outlet: str


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
    category: List[Item] = []
    class Config:
        orm_mode = True

