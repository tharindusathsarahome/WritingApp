from apps.authentication.emailVerification import email_use_send
import jwt
key = "flask-ai"
dataEN = {"user":True}
def encode(email):
    dataEN["user"]=email
    return jwt.encode({"user":email}, key, algorithm="HS256")
    
def decode(encoded):
    if dataEN == jwt.decode(encoded, key, algorithms="HS256"):
        return True



def send_link_(email,link):
    link = link+'newPassword?en='+encode(email)
    msg = f"""Subject: Forgotten password\n\nHello {email},\n\nI'm sorry to hear that you have forgotten your password. Please click on the link below to reset your password.\n\n{link}\n\nIf you have any further questions, please don't hesitate to contact us.\n\nKind regards,\n\nAI Content Creation"""
    email_use_send(email,msg)
    return True