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
        self.tags = champion_data['tags']
        self.title = champion_data['title']
        self.blurb = champion_data['blurb']
        self.img = f"/static/images/champion/{champion_data['image']['full']}"  # Image path

    def __str__(self):
        return f"Name: {self.id}, ID: {self.key}, Image Path: {self.img}, Title: {self.title}, Blurb {self.blurb}, Tags {self.tags}"


# Fetch data and create Champion objects
champion_data = get_ddragon()
if champion_data:
    champion_objects = {}
    for champ_id, champ_info in champion_data.items():
        champion_objects[champ_id] = Champion(champ_info)

    # Print all champions for verification
    for champ_id, champ_obj in champion_objects.items():
        print(champ_obj)
        
    print(f"{type(champion_data)}QQQQQQQQQQQQQQQQQ")
    print(champion_data)

    
    def get_alphabet():
        alphabet_champ = {}
        for champ_name, data in champion_data.items():
            champion_id = champion_data[champ_name]["id"]
            print(f"{champ_name}'s ID is: {champion_id}")
            first_letter = champ_name[0]
            if first_letter not in alphabet_champ:
                alphabet_champ[first_letter] = [champ_name]
            else:
                alphabet_champ[first_letter].append(champ_name)
        print (alphabet_champ) #already alphabatized because json was alphabetical
        return alphabet_champ
    alphabet = get_alphabet()
            
"""     for champ,data in champion_data.items():
        champ_name = data.id
        print (champ_name)
        first_letter = data[0].upper()
        if first_letter not in alphabet_champ:
            alphabet_champ[first_letter]= [champ]
        else:
            alphabet_champ[first_letter].append(champ)
    print(f"ALPHABETCHAMP {alphabet_champ}") """