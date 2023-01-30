from passlib.context import CryptContext


pwd_text = CryptContext(schemes=['bcrypt'],deprecated="auto")

def password_hash(password):
    hashed_password = pwd_text.hash(password)
    return hashed_password

def verify_password(plain_password,hashed_password):
    if(pwd_text.verify(plain_password,hashed_password) == True):
        return True
    return False
