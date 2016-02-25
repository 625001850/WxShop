__author__ = 'Administrator'
import os
from sqlalchemy import create_engine ,__version__
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Boolean
basedir = os.path.abspath(os.path.dirname(__file__))
print __version__
engine = create_engine('sqlite:///test.sqlite',echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()
###################################################################
class Admin(Base):
    __tablename__ = 'admin'
    adminId = Column(Integer,primary_key=True)
    adminName = Column(String)
    password = Column(String)
    adminEmail = Column(String)
    adminIsAllow = Column(Boolean)
    def __repr__(self):
        return "<admin(adminName=%s,password=%s,adminEmail=%s,adminIsAllow=%s)>" % \
               (self.adminName,self.password,self.adminEmail,self.adminIsAllow)
###################################################################

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    sxm = Admin(adminName='sxm',password='123456',adminEmail='625001850@qq.com',adminIsAllow=True)
    session.add(sxm)
    user = session.query(Admin).filter_by(adminName='sxm').first()
    print user
    session.commit()