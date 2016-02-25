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
class Pay(Base):
    __tablename__ = 'bill'
    payId = Column(Integer,primary_key=True)
    payNo = Column(String)
    payTime = Column(String,default=time.strftime('%Y-%m-%d %X'))
    payMoney = Column(Float)
    payType = Column(String)
    billId = Column(Integer)
    def __repr__(self):
        return "<Pay(payNo=%s,payTime=%s,payMoney=%s,payType=%s,billId=%s)>" % \
               (self.billNo,self.billTime,self.billMoney,self.billType)
###################################################################

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    apple = Pay(payNo=str(int(time.time())),payMoney='1.23',payType="",billId=0)
    session.add(apple)
    user = session.query(Pay).filter_by(billNo='1456230645').first()
    print '-----------------'
    print user
    print '-----------------'
    session.commit()