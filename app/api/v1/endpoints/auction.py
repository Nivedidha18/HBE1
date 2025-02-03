from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.auction_service import fetch_and_store_auction_results
from app.dependencies.database import get_db

router = APIRouter()

@router.get("/fetch-auction-results")
async def fetch_auction_results(db: Session = Depends(get_db)):
    result = await fetch_and_store_auction_results(db)
    return result
