# Data Dictionaries

## battles.csv
1. **name:** String variable. The name of the battle.
2. **year:** Numeric variable. The year of the battle.
3. **battle_number:** Numeric variable. A unique ID number for the battle.
4. **attacker_king:** Categorical. The attacker's king. A slash indicators that the king charges over the course of the war. For example, "Joffrey/Tommen Baratheon" is coded as such because one king follows the other in the Iron Throne.
5. **defender_king:** Categorical variable. The defender's king.
6. **attacker_1:** String variable. Major house attacking.
7. **attacker_2:** String variable. Major house attacking.
8. **attacker_3:** String variable. Major house attacking.
9. **attacker_4:** String variable. Major house attacking.
10. **defender_1:** String variable. Major house defending.
11. **defender_2:** String variable. Major house defending.
12. **defender_3:** String variable. Major house defending.
13. **defender_4:** String variable. Major house defending.
14. **attacker_outcome:** Categorical variable. The outcome from the perspective of the attacker. Categories: win, loss, draw.
15. **battle_type:** Categorical variable. A classification of the battle's primary type. Categories: *pitched_battle*: Armies meet in a location and fight. This is also the baseline category. ambush: A battle where stealth or subterfuge was the primary means of attack. siege: A prolonged of a fortied position. razing: An attack against an undefended position
16. **major_death:** Binary variable. If there was a death of a major figure during the battle.
17. **major_capture:** Binary variable. If there was the capture of the major figure during the battle.
18. **attacker_size:** Numeric variable. The size of the attacker's force. No distinction is made between the types of soldiers such as cavalry and footmen.
19. **defender_size:** Numeric variable. The size of the defenders's force. No distinction is made between the types of soldiers such as cavalry and footmen.
20. **attacker_commander:** String variable. Major commanders of the attackers. Commander's names are included without honoric titles and commandders are seperated by commas.
21. **defender_commander:** String variable. Major commanders of the defener. Commander's names are included without honoric titles and commandders are seperated by commas.
22. **summer:** Binary variable. Was it summer?
23. **location:** String variable. The location of the battle.
24. **region:** Categorical variable. The region where the battle takes place. Categories: Beyond the Wall, The North, The Iron Islands, The Riverlands, The Vale of Arryn, The Westerlands, The Crownlands, The Reach, The Stormlands, Dorne
25. **note:** String variable. Coding notes regarding individual observations.

## character-deaths.csv
1. **Name:** character name
2. **Allegiances:** character house
3. **Death Year:** year character died
4. **Book of Death:** book character died in
5. **Death Chapter:** chapter character died in
6. **Book Intro Chapter:** chapter character was introduced in
7. **Gender:** 1 is male, 0 is female
8. **Nobility:** 1 is nobel, 0 is a commoner
9. **GoT:** Appeared in first book
10. **CoK:** Appeared in second book
11. **SoS:** Appeared in third book
12. **FfC:** Appeared in fourth book
13. **DwD:** Appeared in fifth book