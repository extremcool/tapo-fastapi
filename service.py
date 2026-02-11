from fastapi import FastAPI, HTTPException, Response, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import cv2
import os
from dotenv import load_dotenv

load_dotenv()

TAPO_USER = os.getenv("TAPO_USER")
TAPO_PASS = os.getenv("TAPO_PASS")
TAPO_IP   = os.getenv("TAPO_IP")
API_TOKEN = os.getenv("API_TOKEN")
API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")

app = FastAPI()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # prüfe ob token korrekt ist
    token = credentials.credentials
    if token != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

def get_camera_frame():
    rtsp_url = f"rtsp://{TAPO_USER}:{TAPO_PASS}@{TAPO_IP}:554/stream1"
    print(f"verbinde mit {TAPO_IP}...")
    
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        cap.release()
        raise Exception("kamera nicht erreichbar, rtsp stream offline oder so")

    for _ in range(10):
        cap.read()

    success, frame = cap.read()
    cap.release()

    if not success:
        raise Exception("bild konnte nicht gelesen werden")

    ret, buffer = cv2.imencode('.jpg', frame)
    
    if not ret:
        raise Exception("bild konnte nicht encodet werden")
        
    return buffer.tobytes()

# nur erlauben wenn bearer token korrekt ist
@app.get("/snapshot", dependencies=[Depends(verify_token)])
def take_snapshot():
    try:
        image_bytes = get_camera_frame()
        return Response(content=image_bytes, media_type="image/jpeg")
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=int(API_PORT))
