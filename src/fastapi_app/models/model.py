from sqlalchemy import BigInteger, Index, MetaData, Column, String, Integer, Date, func, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_pass = Column(String, nullable=False)

    tasks = relationship(
        'Tasks', back_populates='user', lazy='select'
    )

    __table_args__ = (
        Index('idx_username', 'username'),
    )


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    create_data = Column(Date, server_default=func.now())
    due_data = Column(DateTime, default=None)
    ended = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(
        'User', back_populates='tasks'
    )
