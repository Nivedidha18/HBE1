from app.core.config import API_URL
from app.repositories.auction_repo import save_auction_results  
import httpx
from sqlalchemy.orm import Session  

async def fetch_and_store_auction_results(db: Session):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL)

        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")

        if 'application/json' in response.headers.get('Content-Type', ''):
            try:
                print("Raw Response Body:\n", response.text)

                auction_data = response.json()
                print("Parsed Auction Data:", auction_data)

                if isinstance(auction_data, dict) and "result" in auction_data:
                    result_data = auction_data["result"]

                    if isinstance(result_data, dict) and "records" in result_data:
                        records = result_data["records"]
                    elif isinstance(result_data, list):
                        records = result_data
                    else:
                        records = []
                    filtered_results = [
                        item for item in records
                        if isinstance(item, dict) and item.get("registeredAuctionParticipant", "").strip().upper() == "HABITAT ENERGY LIMITED"
                    ]
                    print("Filtered Results:", filtered_results)

                   
                    save_auction_results(filtered_results, db)
                    return {"status": "success", "data": filtered_results}
                else:
                    print("Unexpected response structure:", auction_data)
                    return {"status": "error", "message": "Unexpected response structure."}

            except ValueError as e:
                print("Error parsing JSON response:", str(e))
                return {"status": "error", "message": "Failed to parse auction data"}

        else:
            print(f"Unexpected Content-Type: {response.headers.get('Content-Type')}")
            return {"status": "error", "message": "Response is not JSON"}

    except httpx.RequestError as e:
        print("HTTP Request failed:", str(e))
        return {"status": "error", "message": "HTTP Request failed"}
