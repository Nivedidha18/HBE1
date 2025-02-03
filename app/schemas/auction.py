from pydantic import BaseModel
from datetime import datetime

class AuctionResultSchema(BaseModel):
    auction_id: str
    result: str
    timestamp: datetime

    class Config:
        orm_mode = True
