from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, Text, Date, Boolean

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    screen_name = Column(Text)
    twitter_id = Column(Integer)
    is_following = Column(Boolean)
    last_following = Column(Date)

    def __repr__(self):
        return "<Follower %s #%s>" % \
               (self.name, self.twitter_id)
