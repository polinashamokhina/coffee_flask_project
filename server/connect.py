import requests

# response = requests.get("http://127.0.0.1:5000" + "/api/farms/1")
# print(response.json())

# response = requests.get("http://127.0.0.1:5000" + "/api/farms") 
# print(response.json())

# response = requests.post("http://127.0.0.1:5000" + "/api/farms", {"location": "Ethiopia", "name": "Gesha Village", 
#                                                                    "description": "The mother-farm of the coffee trees of Gesha variety",
#                                                                    "image":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.oklaocoffee.com%2Fen%2Fcoffee%2FMTAzNw%2Fdetail&psig=AOvVaw0d1t4x4DAWflKNKt_G8YXJ&ust=1747487361421000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIimqO2HqI0DFQAAAAAdAAAAABAK"})
# print(response.json())
# response = requests.post("http://127.0.0.1:5000" + "/api/farms", {"location": "Panama", "name": "Finca Sophia", 
#                                                                    "description": "The mother-farm of the coffee trees of Gesha variety",
#                                                                    "image":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.fincasophia.com%2F&psig=AOvVaw22CurlNdyR9hqQKdp-Fivc&ust=1747487287022000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLje_MmHqI0DFQAAAAAdAAAAABAE"})
# print(response.json())
# response = requests.post("http://127.0.0.1:5000" + "/api/farms", {"location": "Panama", "name": "ABU", 
#                                                                    "description": "The mother-farm of the coffee trees of Gesha variety",
#                                                                    "image":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2Fabucoffeepanama%2F&psig=AOvVaw0QdTr6EXlMy1hCAKPtyiqo&ust=1747487587987000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLClydmIqI0DFQAAAAAdAAAAABAE"})
# print(response.json()) # !!! пока что не можем отсюда отправлять ниче тк отправляем ФОРМУ тут , а в reqparse location = json

# response = requests.get("http://127.0.0.1:5000" + "/api/coffees")
# print(response.json())
response = requests.post("http://127.0.0.1:5000" + "/api/coffees", {"farm_id": "2", "variety": "Geisha", 
                                                                   "process": "Washed",
                                                                   "descriptors": "Honey, Peach, Jasmine","image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR61YomAWMQci0v3lCiIaeGSgo0FFdY0pi4eA&s"})
print(response.json())

response = requests.post("http://127.0.0.1:5000" + "/api/coffees", {"farm_id": "1", "variety": "Geisha", 
                                                                   "process": "Natural",
                                                                   "descriptors": "Blueberry, Orange Blossom, Rose","image": "https://cdn.shopify.com/s/files/1/0017/8585/6070/files/Gesha-Hands_1024x1024.jpg?v=1568332435"})
print(response.json())

response = requests.post("http://127.0.0.1:5000" + "/api/coffees", {"farm_id": "3", "variety": "Geisha", 
                                                                   "process": "Washed",
                                                                   "descriptors": "Lemon, Pear, Guimauve","image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVSDxn-ji40mYRE8C6H4GYNat_o_zXqK75LA&s"})
print(response.json())
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