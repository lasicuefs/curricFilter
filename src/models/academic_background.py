from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database_config import database_config

class AcademicBackground(database_config.base):
    __tablename__ = "academic_background"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    institution = Column(String, nullable=False)
    course = Column(String, nullable=False)
    start_year = Column(Integer)
    end_year = Column(Integer)
    researcher_id = Column(Integer, ForeignKey("researcher.id", ondelete="CASCADE"), nullable=False)

    researcher = relationship("Researcher", back_populates="academic_background")
    knowledge_area = relationship("KnowledgeArea", back_populates="academic_background", cascade="all, delete-orphan")
