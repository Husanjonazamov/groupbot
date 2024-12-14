import requests
from utils.env import BASE_URL




def getNotice():
    url = f"{BASE_URL}/notices/"
    response = requests.get(url)
    if response.status_code == 200: 
        return response.json()
    else:
        print("Xato:", response.status_code, response.text)  

    return response.json()
    


