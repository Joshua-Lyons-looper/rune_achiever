# rune_achiever
Rune achiever is designed to get a character's skills, quests, and additional requirements to let the player know
which **Achievement Diaries** can be done given their current quests, and letting them know which requirements are missing
to complete more diaries.  The results will be sorted from CAN COMPLETE -> Lowest missing Requirements -> Most missing requirements.
If we are missing the requirements for easy, then medium -> Elite won't be listed.


**USAGE**
Ideally run this in a venv since it'll be easier to make sure you have the requirements
From the rune_achiever directory:
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

**Running the application:**
python3 main.py, follow the prompts
