from player import Player
import json
from requirementscompareplayer import get_player_requirements



def main():
    #get player details
    character_name = str(input("What is your character's name (Please include spaces): "))
    ironman = str(input("Please enter if you're an ironman (n for not iron, i for iron, h for hardcore): "))
    iron,hardcore = False, False
    match ironman.lower()[0]:
        case "i":
            iron = True
        case "h":
            hardcore = True
    
    character = Player(character_name, iron, hardcore)
    character.populate_skills()
    character.populate_quests()

    diaries_we_can_complete = []
    diaries_missing_reqs = {}

    with open("achievement_requirements.json") as f:
        requirements = json.load(f)
    
    for region, req_data in requirements.items():
        result = get_player_requirements(character, req_data)

        if not result["missing_skills"] and not result["missing_quests"]:
            diaries_we_can_complete.append(region)
        else:
            diaries_missing_reqs[region] = result
    
    # Print Diaries That Are Ready
    print("\n✅ Diaries we can complete:")
    for region in diaries_we_can_complete:
        print(f"  - {region}")

    # Print Diaries with Missing Requirements
    print("\n❌ Diaries we're missing requirements for:")
    for region, result in diaries_missing_reqs.items():
        print(f"\n{region}:")
        if result["missing_skills"]:
            print("  ❌ Missing Skills:")
            for item in result["missing_skills"]:
                print(f"    - {item['skill']} (Required: {item['required']}, You have: {item['current']})")
        if result["missing_quests"]:
            print("  ❌ Missing Quests:")
            for quest in result["missing_quests"]:
                print(f"    - {quest}")




main()