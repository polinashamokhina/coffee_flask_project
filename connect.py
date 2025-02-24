import requests

response = requests.get("http://127.0.0.1:5000" + "/api/farms/1")
print(response.json())

# response = requests.get("http://127.0.0.1:5000" + "/api/farms")
# print(response.json())
# response = requests.post("http://127.0.0.1:5000" + "/api/farms", {"location": "Panama", "name": "Finca Sophia", 
#                                                                    "description": "Small farm delivering high quality coffee"})
# print(response.json())

# response = requests.get("http://127.0.0.1:5000" + "/api/coffees")
# print(response.json())
# response = requests.post("http://127.0.0.1:5000" + "/api/coffees", {"farm_id": "1", "variety": "Geisha", 
#                                                                    "process": "Washed",
#                                                                    "descriptors": "Honey, Peach, Jasmine","image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR61YomAWMQci0v3lCiIaeGSgo0FFdY0pi4eA&s"})
# print(response.json())

# input()
# response = requests.get("http://127.0.0.1:5000/" + "farm")
# response = requests.post("http://127.0.0.1:5000/" + "coffee", {"farm_name":"Finca Sophia","variety": "Geisha", "process": "Washed", "descriptors": "Honey, Peach, Jasmine", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR61YomAWMQci0v3lCiIaeGSgo0FFdY0pi4eA&s"})
# print(response.json())
# input()
# response = requests.post("http://127.0.0.1:5000/" + "coffee", {"variety": "Sidra", "process": "Washed", "descriptors": "Green Tea, Strawberry, Jasmine", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR61YomAWMQci0v3lCiIaeGSgo0FFdY0pi4eA&s"})
# print(response.json())
# input()
# response = requests.post("http://127.0.0.1:5000/" + "coffee", {"variety": "Pink Bourbon", "process": "Natural", "descriptors": "Mango, Strawberry, Peach", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR61YomAWMQci0v3lCiIaeGSgo0FFdY0pi4eA&s"})
# print(response.json())
# response = requests.get("http://127.0.0.1:5000/" + "coffee")
# print(response.json())
# input()
# response = requests.get("http://127.0.0.1:5000/" + "coffee/" + "0")
# print(response.json())
# response = requests.delete("http://127.0.0.1:5000/" + "coffee/" + "2")
# print(response.json())