#api stuff here
import json
import requests
from PIL import Image

#ddragon champion

""" what i want:
    champion Name = "id"
    chamption #id = "key"
    image/"full" = "ahri.png"
    """

def get_ddragon():
    url = "https://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json"

    try:
        response = requests.get(url)
        print(response.status_code) #200 good

  
        if response.status_code == 200:
            champions_data = response.json()
            # Access the champion data
            champion_list = champions_data['data']
            return champion_list
        else:
            print(f"Failed to retrieve data: Status code {response.status_code}")
            return None
            

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

get_ddragon()

class Champion():
    def __init__(self,champion_data):
        self.id = "champion.id" #name
        self.key = "champion.key" #id num
        self.img = (f"./{self.id}_0.img")
    
    def __str__(self):
        return f"{self.id, self.key}
    
champion_objects = {}
for champ_id, champ_data in champions.items():
    champion_objects[champ_id] = Champion(champ_data)