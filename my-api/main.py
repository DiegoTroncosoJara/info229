from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/news/", response_model=schemas.News)
def create_user(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    db_news = crud.get_user_by_title(db, title=news.title)
    if db_news:
        raise HTTPException(status_code=400, detail="Title already registered")
    return crud.create_new(db=db, News=news)


@app.get("/news/", response_model=List[schemas.News])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db, skip=skip, limit=limit)
    return news


@app.get("/news/{news_id}", response_model=schemas.News)
def read_news(new_id: int, db: Session = Depends(get_db)):
    db_news = crud.get_new(db, News_id=new_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news


@app.post("/news/{news_id}/category/", response_model=schemas.Item)
def create_category_for_news(
    new_id: int, category: schemas.ItemCategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_news_category(db=db,category=category, new_id=new_id)


@app.get("/category/", response_model=List[schemas.Item])
def read_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = crud.get_category(db, skip=skip, limit=limit)
    return category

