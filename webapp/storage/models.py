from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class WordDB(Base):
    __tablename__ = 'Word'
    word_hash = Column(String(255), primary_key=True)
    word_enc = Column(Text(), nullable=False)           #   asymmetric encryption
    count = Column(Integer, nullable=False)
    website_page = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Hashed word('%s')>" % (self.word_hash)

