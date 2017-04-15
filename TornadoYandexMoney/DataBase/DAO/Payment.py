
from sqlalchemy import Column, Integer, Numeric, String, Sequence, DateTime, ForeignKey, Boolean

from TornadoYandexMoney.DataBase.DAO import Base



class Payment(Base) :

    __tablename__ = 'payments'
    id = Column(Integer, Sequence('payments_id_seq'), primary_key=True)
    user_id = Column(Integer)
    cps_email = Column(String)
    cps_phone = Column(String)
    customer_number = Column(String)
    fail_url = Column(String)
    invoice_id = Column(Integer)
    order_amount = Column(Numeric)
    order_currency = Column(Integer)
    payer_code = Column(String)
    payment_type = Column(String, default='ac')
    performed_datetime = Column(DateTime)
    pub_date = Column(DateTime)
    scid = Column(Integer)
    shop_amount = Column(Numeric)
    shop_currency = Column(Integer)
    shop_id = Column(Integer)
    status = Column(String)
    success_url = Column(String)
    article_id = Column(Integer)
