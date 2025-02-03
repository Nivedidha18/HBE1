from sqlalchemy.orm import Session
from app.models.auction_result import AuctionResult
from datetime import datetime

def save_auction_results(results, db: Session):
    for result in results:
        try:
            
            auction_id = result.get('_id')  
            registered_auction_participant = result.get('registeredAuctionParticipant')
            auction_unit = result.get('auctionUnit')
            service_type = result.get('serviceType')
            auction_product = result.get('auctionProduct')
            executed_quantity = result.get('executedQuantity')
            clearing_price = result.get('clearingPrice')
            delivery_start = result.get('deliveryStart')
            delivery_end = result.get('deliveryEnd')
            unit_result_id = result.get('unitResultID')
            
            if delivery_start:
                delivery_start = datetime.fromisoformat(delivery_start) if isinstance(delivery_start, str) else delivery_start
            if delivery_end:
                delivery_end = datetime.fromisoformat(delivery_end) if isinstance(delivery_end, str) else delivery_end
            timestamp = datetime.utcnow()  
         
            auction_result = AuctionResult(
                auction_id=auction_id,
                registered_auction_participant=registered_auction_participant,
                auction_unit=auction_unit,
                service_type=service_type,
                auction_product=auction_product,
                executed_quantity=executed_quantity,
                clearing_price=clearing_price,
                delivery_start=delivery_start,
                delivery_end=delivery_end,
                unit_result_id=unit_result_id,
                timestamp=timestamp  
            )
   
            db.add(auction_result)

        except Exception as e:
        
            print(f"Error saving auction result: {e}")
            db.rollback()

    try:
        db.commit()
    except Exception as e:
        print(f"Error committing the transaction: {e}")
        db.rollback()
