import requests
import base64

URL = "http://localhost:5000/add_face"

with open("lena.png", "rb") as imageFile:
    img = base64.b64encode(imageFile.read())
    
response = requests.post(URL, data={"name":"lena", "img": str(img)})
print(response.content)