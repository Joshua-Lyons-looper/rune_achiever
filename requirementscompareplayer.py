from player import Player

def get_player_requirements(character: Player, requirement_block: dict):
    playerSkills = character.getPlayerSkills()
    playerQuests = character.getPlayerQuests()
    results = {
        "met_skills": [],
        "missing_skills": [],
        "met_quests": [],
        "missing_quests": []
    }

    #Skill checks
    for skill, required_level in requirement_block.get("skill requirements", {}).items():
        player_level = int(playerSkills.get(skill, 0))
        if player_level >= required_level:
            results["met_skills"].append(skill)
        else:
            results["missing_skills"].append({
                "skill": skill,
                "required": required_level,
                "current": player_level
            })

    # Quest checks (✅ COMPLETED only counts)
    quest_lookup = {q["title"]: q["status"] for q in playerQuests}
    for quest_title in requirement_block.get("quest_requirements", []):
        if quest_lookup.get(quest_title) == "COMPLETED":
            results["met_quests"].append(quest_title)
        else:
            results["missing_quests"].append(quest_title)

    return results
