import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    fecha_de_registro = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    imagen = Column(String(250), nullable=False)
    descripción = Column(String(250), nullable=False)
    fecha_de_publicación = Column(String(250), nullable=False)
    ubicación = Column(String(250), nullable=False)
    relationship(User)

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__='comment'
    comment_id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.user_id'))
    post_id = Column(Integer, ForeignKey('post.post_id'))
    texto = Column(String(250), nullable=False)
    fecha_de_comentario = Column(String(250), nullable=False)
    relationship(User)
    relationship(Post)

class Like(Base):
    __tablename__='like'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    post_id = Column(Integer, ForeignKey('post.post_id'))
    relationship(User)
    relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e