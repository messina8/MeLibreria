from dns.resolver import Answers
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class MeliAccount(Base):
    id = Column(Integer, primary_key=True, index=True)
    seller_username = Column(String, unique=True, index=True)
    access_token = Column(String)
    refresh_token = Column(String)
    token_expiration = Column(DateTime)

    quick_answers = relationship("QuickAnswer", back_populates="user")


class QuickAnswers(Base):
    greeting = Column(String)
    valediction = Column(String)

    user = relationship("MeliAccount", back_populates="quick_answers")

class AutomaticMessage(Base):
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    text = Column(String)
    enabled = Column(Boolean, default=True)
    description = Column(String)
    name = Column(String)
    trigger = Column(String)

class Question(Base):
    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(ForeignKey("MeliAccount.id"), nullable=False)
    date_created = Column(DateTime)
    from_id = Column(Integer)
    item_id = Column(String)
    status = Column(String)

    answer = relationship(Answers, back_populates="question")


class Answer(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date_created = Column(DateTime)
    status = Column(String)
    answer = relationship("Question", back_populates="answer")