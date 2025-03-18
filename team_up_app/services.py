import json
import requests

# Function to fetch champion data from the URL
def get_ddragon():
    url = "https://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json"

    try:
        response = requests.get(url)
        print(response.status_code)  # 200 means successful response

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


# Define Champion class
class Champion:
    def __init__(self, champion_data):
        self.id = champion_data['id']  # Champion name
        self.key = champion_data['key']  # Champion numeric ID
        self.img = f"/static/images/champion/{champion_data['image']['full']}"  # Image path

    def __str__(self):
        return f"Name: {self.id}, ID: {self.key}, Image Path: {self.img}"


# Fetch data and create Champion objects
champion_data = get_ddragon()
if champion_data:
    champion_objects = {}
    for champ_id, champ_info in champion_data.items():
        champion_objects[champ_id] = Champion(champ_info)

    # Print all champions for verification
    for champ_id, champ_obj in champion_objects.items():
        print(champ_obj)
