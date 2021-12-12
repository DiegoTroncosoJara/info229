from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(50), unique=True, index=True)
    url = Column(String(50), unique=True, index=True)
    date = Column(String(50), unique=True, index=True)
    media_outlet = Column(String(50), unique=True, index=True)


    has_category = relationship("Category", back_populates="category")



class Category(Base): 

    __tablename__ = "has_category"
    id = Column(Integer, primary_key=True, index=True)
    category_content = Column(String(50), index=True)

    id2 = Column(Integer, ForeignKey("news.id"))
    
    category = relationship("News", back_populates="has_category")

