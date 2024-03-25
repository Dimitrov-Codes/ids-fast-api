import numpy as np

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

y_pred = np.load('y_preds.npy')
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{sysId}")
def predictIntrusion(sysId):
    return {"attacked": int(y_pred[int(sysId)]) }

