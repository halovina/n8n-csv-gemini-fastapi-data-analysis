from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create a FastAPI application instance
app = FastAPI()

# Define the request body model using Pydantic
class PromptRequest(BaseModel):
    promptResponse: str

# Define the response model
class PromptResponse(BaseModel):
    status: str
    message: str
    promptResponse: str

@app.post("/api/v1/savepromptdata", response_model=PromptResponse)
def process_transaction(request: PromptRequest):
    """
    Endpoint to process and
    Receive 'promptResponse' in the request body and return a success status.
    """
    # Here, you can add your business logic.
    # For example, saving data to a database, calling another service, etc.
    # For this example, we just return a success response directly.
    
    # Simple validation (optional)
    if not request.promptResponse:
        raise HTTPException(status_code=400, detail="promptResponse must not be empty")

    # Success logic
    response_data = {
        "status": "success",
        "message": "Transaction processed successfully.",
        "promptResponse": request.promptResponse
    }
    print(f"Processed data with promptResponse: {request.promptResponse}")
    return response_data    