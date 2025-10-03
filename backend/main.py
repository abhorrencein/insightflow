from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from cleaners.surveycto import process_surveycto_file

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/process")
async def process_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Only XLSX files allowed")
    
    try:
        contents = await file.read()
        df = pd.read_excel(contents, sheet_name=0)
        result = process_surveycto_file(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
