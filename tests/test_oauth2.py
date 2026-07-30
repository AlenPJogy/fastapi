from fastapi import HTTPException

from app import oauth2


def test_verify_access_token_accepts_int_user_id():
    token = oauth2.create_access_token({"user_id": 9})
    credentials_exception = HTTPException(status_code=401, detail="could not validate credentials")

    token_data = oauth2.verify_access_token(token, credentials_exception)

    assert token_data.id == 9
