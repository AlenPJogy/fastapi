from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import database, schemas, models, utils, oauth2
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from oauth2 import oauth2_scheme
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model= schemas.Token)
def Login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):


    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()


    if user == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    
    access_token = oauth2.create_access_token(data= {"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}




@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verify your user credentials here
    if form_data.username != "admin" or form_data.password != "secret":
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Swagger UI strictly requires a JSON response with "access_token" and "token_type"
    return {"access_token": "your_generated_jwt_token_here", "token_type": "bearer"}

@router.get("/protected-data")
async def get_protected_data(token: str = Depends(oauth2_scheme)):
    # The token is automatically extracted from the header
    return {"message": "Success", "token_received": token}
