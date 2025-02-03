import os
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv(
    "API_URL", 
    "https://api.neso.energy/api/3/action/datastore_search?resource_id=a63ab354-7e68-44c2-ad96-c6f920c30e85"
)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./auction_results.db")  
