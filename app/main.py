from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import os
import time
from app.solver import solve_quiz

app = FastAPI()

# Use the same secret as in Google Form
SECRET = os.getenv("TDS_SECRET", "cheena")

@app.post("/")
async def quiz_endpoint(request: Request):
    try:
        payload = await request.json()
    except:
        return JSONResponse({"error": "Invalid JSON"}, status_code=400)
    
    # Validate required fields
    required_fields = ["email", "secret", "url"]
    for field in required_fields:
        if field not in payload:
            return JSONResponse({"error": f"Missing field: {field}"}, status_code=400)
    
    # Validate secret
    if payload["secret"] != SECRET:
        return JSONResponse({"error": "Forbidden - Invalid secret"}, status_code=403)
    
    # Start solving quiz
    start_time = time.time()
    try:
        result = await solve_quiz(
            email=payload["email"],
            secret=payload["secret"], 
            start_url=payload["url"],
            start_time=start_time
        )
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": f"Quiz solving failed: {str(e)}"}, status_code=500)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Quiz solver is ready!"}