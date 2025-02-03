from fastapi import FastAPI
from app.api.v1.endpoints import auction
from fastapi.responses import JSONResponse

app = FastAPI()

# Include the auction endpoint
app.include_router(auction.router, prefix="/api/v1/auction", tags=["auction"])


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Habitat Energy Auction Service"}
