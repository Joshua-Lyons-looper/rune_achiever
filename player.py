import requests
import json
 
skill_order = [
    "Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer",
    "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking",
    "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer",
    "Farming", "Runecrafting", "Hunter", "Construction", "Summoning",
    "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"
]

class Player:
    def __init__(self, name, ironman=False, hardcore=False):
        self.name = name
        self.ironman = ironman
        self.hardcore = hardcore
        self.skills = {}
        self.quests = {}
        self.achievements = {}
    

    def populate_skills(self):

        name = self.name
        url_name = name.replace(" ", "%20")
        url = f"https://secure.runescape.com/m=hiscore/index_lite.ws?player={url_name}"
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.strip().split("\n")

            #Skills populate only the first 30 lines
            for i in range(0,30):
                parts = lines[i].split(",")
                if len(parts) == 3:
                    level = parts[1]
                    skill = skill_order[i]
                    self.skills[skill] = level
            print(self.skills)
        
        else:
            print(f"Error connecting to Runescape's API: {response.status}")
    
    def populate_quests(self):
        pass

                    
            

        
        


