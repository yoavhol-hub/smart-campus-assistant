from sqlalchemy import Column, Integer, String, Text
from app.data.db import Base


class CampusInfo(Base):
    __tablename__ = "campus_info"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False, index=True)
    topic = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=True)