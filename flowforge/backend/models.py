from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from pydantic import BaseModel
from enum import Enum
from typing import Optional
from database import Base


# Status choices
class TaskStatus(str, Enum):
    todo = "To Do"
    in_progress = "In Progress"
    done = "Done"


# SQLAlchemy Model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(500), nullable=True)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.todo)


# Pydantic Schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskOut(TaskBase):
    id: int

    class Config:
        from_attributes = True
