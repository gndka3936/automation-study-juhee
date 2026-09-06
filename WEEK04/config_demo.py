from dotenv import load_dotenv
import os
load_dotenv()
login_id = os.getenv("LOGIN_ID")

if login_id:
    print(login_id)
else:
    print("LOGIN_ID가 없습니다.")
    
#print(os.getenv("LOGIN_PASSWORD"))
print(os.getenv("BASE_URL"))