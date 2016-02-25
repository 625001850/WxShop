__author__ = 'Administrator'
import os
from sqlalchemy import create_engine ,__version__
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Boolean,Float
import time
basedir = os.path.abspath(os.path.dirname(__file__))
print __version__
engine = create_engine('sqlite:///test.sqlite',echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()
###################################################################
class Bill(Base):
    __tablename__ = 'bill'
    billId = Column(Integer,primary_key=True)
    billNo = Column(String)
    billTime = Column(String,default=time.strftime('%Y-%m-%d %X'))
    productId = Column(Integer)
    productNum = Column(Integer)
    def __repr__(self):
        return "<Bill(billNo=%s,billTime=%s,productId=%d,productNum=%d)>" % \
               (self.billNo,self.billTime,self.productId,self.productNum)
###################################################################

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    apple = Bill(billNo=str(int(time.time())),productId=1,productNum=2)
    session.add(apple)
    user = session.query(Bill).filter_by(billId=1).first()
    print '-----------------'
    print user
    print '-----------------'
    session.commit()

