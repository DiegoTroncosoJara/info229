from sqlalchemy.orm import Session

from . import models, schemas


def get_new(db: Session, News_id: int):
    return db.query(models.News).filter(models.News.id == News_id).first()


def get_news_by_title(db: Session, title: str):
    return db.query(models.News).filter(models.News.title == title).first()


def get_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()





def create_news(db: Session, news: schemas.NewsCreate):
    fake_hashed_url = news.url + "notreallyhashed"
    db_user = models.User(title=news.tile, url=fake_hashed_url)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_news_category(db: Session, News: schemas.NewsCreate, new_id: int):
    db_news = models.News(**News.dict(), id2 = new_id)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news



