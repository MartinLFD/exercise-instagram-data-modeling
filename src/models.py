import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower' #añadir llaves foráneas o primarias 
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('u.from.id'))
    user_to_id = Column(Integer, ForeignKey('u.to.id'))
    





class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    username = Column(String(60), nullable=False, unique=True )
    first_name = Column(String(80), nullable=False )
    last_name = Column(String(80), nullable=False )
    email = Column(String(100), nullable=False, unique=True )
    







class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False )
    author_id = Column(Integer, ForeignKey('author.id'))
    post_id = Column(Integer, ForeignKey('post.id'))






class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))





class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    
    url = Column(String(400), nullable= False)
    post_id = Column(Integer, ForeignKey('post.id'))




    

    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
