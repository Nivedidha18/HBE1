from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AuctionResult(Base):
    __tablename__ = "auction_results"
    
    id = Column(Integer, primary_key=True, index=True)
    auction_id = Column(String, index=True)
    registered_auction_participant = Column(String)  
    auction_unit = Column(String)  
    service_type = Column(String)  
    auction_product = Column(String)  
    executed_quantity = Column(Float) 
    clearing_price = Column(Float) 
    delivery_start = Column(DateTime)  
    delivery_end = Column(DateTime)  
    unit_result_id = Column(String)  
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AuctionResult(auction_id={self.auction_id}, participant={self.registered_auction_participant}, price={self.clearing_price}, timestamp={self.timestamp})>"
