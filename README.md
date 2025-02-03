# Habitat Energy Auction Results

### 1. **Purpose**

This is a FastAPI-based service that fetches auction data, filters it for Habitat Energy Limited, and stores the results into an SQLite database. The service regularly retrieves auction results and ensures that only relevant data is stored.

### 2. **Requirements**

- Python 3.x
- FastAPI (pip install fastapi)
- HTTPX (pip install httpx)
- SQLAlchemy (pip install sqlalchemy)
- Pydantic (pip install pydantic)
- SQLite (used as the default database)
- Uvicorn (pip install uvicorn)
- SQLAlchemy (pip install sqlalchemy)

### 3. **Files**

- `main.py` – The entry point for running the FastAPI application.
- `auction.py` - API layer for handling auction-related operations.
- `config.py` – Configuration file for settings such as API URL, database URL.
- `database.py` – Helper functions to interact with the SQLite database and set up the connection.
- `auction_result.py` – SQLAlchemy model that defines the database schema for storing auction result.
- `auction_repo.py` – Repository layer for saving auction results into the database.
- `auction_service.py` – Service layer for fetching auction data, filtering results, and storing them.
- `auction_results.py` – API layer to expose a FastAPI endpoint that triggers the auction results fetching process.
- `schema/auction_result.py` – Schema for validating and serialising auction results.
- `auction_results.db` – SQLite database file where auction results are stored.
- `requirements.txt` – List of Python dependencies.

### 4. **Explanation of Code Structure**

- fetch_and_store_auction_results() -

* Fetches auction results from the provided API using the httpx client.
* Filters the results based on the participant name, specifically looking for Habitat Energy Limited records.
* Stores the filtered results into the SQLite database using the save_auction_results() function.

- filter_auction_results() -

* Filters the auction data to extract records related to Habitat Energy Limited.
* Ensures that only records with the correct auction participant are returned for processing.

- save_auction_results()

* Inserts the filtered auction data into the SQLite database.
* The data includes details like auction ID, participant, auction unit, service type, product, executed quantity, price, and delivery periods.

# SQLite Database →

The auction_results table stores the unit’s auction results with relevant fields:

auction_id → Unique auction identifier.
registered_auction_participant → Name of the participant.
auction_unit → The unit involved in the auction.
service_type → Type of service provided.
auction_product → The auction product category.
executed_quantity → Quantity executed in the auction.
clearing_price → Final clearing price.
delivery_start → Start time of the delivery period.
delivery_end → End time of the delivery period.
unit_result_id → Unique identifier for the auction unit’s result.
timestamp → The time when the result was stored in the database.

### 5. **Running the Script**

- Clone the repo and navigate to the project directory.
- pip install -r requirements.txt
- Set up the database- python -m app.db.create_db
- Create a .env file in the root directory and define your configuration variables.
  (API_URL="https://api.neso.energy/api/3/action/datastore_search?resource_id=a63ab354-7e68-44c2-ad96-c6f920c30e85"
  DATABASE_URL="sqlite:///./auction_results.db"
  )

# Run the FastAPI application:

uvicorn app.main:app --reload

### 6. **Execution**

When the script is run, it will:

1. Connect to the API to fetch auction data.
2. Filter the data to find Habitat Energy’s submissions for the current day.
3. Save the filtered results into a local SQLite database.

### 7. **API Endpoints**

1. GET /
   The home endpoint to check the status of the API. When you navigate to http://127.0.0.1:8000/, it will confirm that the FastAPI server is running.

**http://127.0.0.1:8000/**

2. GET /api/v1/auction/fetch-auction-results
   This endpoint triggers the process of fetching the auction results for Habitat Energy Limited, filtering them, and storing them in the SQLite database. You can call this endpoint whenever you want to manually initiate the fetching process.

**http://127.0.0.1:8000/api/v1/auction/fetch-auction-results**

### 8. **Checking the Database**

Step 1: Open the SQLite Command Line Interface (CLI)
In your terminal, navigate to the directory where your auction_results.db file is located. Run the following command to open the SQLite CLI:

- sqlite3 auction_results.db

Step 2: List All Tables in the Database
Once you're inside the SQLite CLI, you can list all the tables in the database by running:

- .tables (show all the tables in the database)

Step 3: View the Data in the auction_results Table
To view the data stored in the auction_results table, use the following SQL command:

- SELECT \* FROM auction_results; (return all the records from the auction_results table.)
  Output :
  ![Database Snapshot](Screenshot%202025-02-03%20at%2012.08.16.png)

### 9. **Conclusion**

This approach allows Habitat Energy’s auction results to be stored and processed automatically every day, ensuring that the data is always up to date without any manual intervention. You can expand the code structure later to accommodate other types of data from ESO.
