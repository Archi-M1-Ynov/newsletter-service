from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from models import Newsletter
from database import SessionLocal, engine, Base

app = FastAPI()

# Créer les tables
Base.metadata.create_all(bind=engine)

# Dépendance DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schéma Pydantic
class SubscribeRequest(BaseModel):
    email: EmailStr

@app.post("/subscribe")
def subscribe(request: SubscribeRequest, db: Session = Depends(get_db)):
    existing = db.query(Newsletter).filter(Newsletter.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email déjà inscrit")
    
    entry = Newsletter(email=request.email)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return { "message": "Inscription réussie", "email": entry.email }

@app.get("/list")
def list_subscribers(db: Session = Depends(get_db)):
    return db.query(Newsletter).all()
