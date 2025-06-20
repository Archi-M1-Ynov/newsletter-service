from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Newsletter(Base):
    __tablename__ = "newsletter"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    subscribed_at = Column(DateTime, server_default=func.now())
