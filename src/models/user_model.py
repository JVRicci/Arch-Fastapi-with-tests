from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)
    uf = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', age={self.age}, email='{self.email}', uf='{self.uf}')>"
