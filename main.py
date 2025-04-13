from player import Player




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



main()