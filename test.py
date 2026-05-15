#List 20 champions in the game
champions_list = [
    ("Aatrox", "Fighter", "Physical damge"),
    ("Ahri", "Mage", "Magic damage"),
    ("Aphelios", "AD", "Physical damge"),
    ("Aurelion Sol", "Mage", "Magic damage"),
    ("Yasuo", "Fighter", "Physical damage"),
    ("Jinx", "AD", "Physical damage"),
    ("Zed", "Fighter", "Physical damage"),
    ("Azir", "Mage", "Magic damage"),
    ("Viktor", "Mage", "Magic damage"),
    ("Yone", "Fighter", "Physical damage"),
    ("Leona", "Support", "Magic damage"),
    ("Alistar", "Support", "Magic damage"),
    ("Braum", "Support", "Magic damage"),
    ("Camille", "Fighter", "physical damage"),
    ("Garen", "Fighter", "Physical damage"),
    ("Gwen", "Fighter", "Magic damage"),
    ("Hwei", "Mage", "Magic damage"),
    ("K'sante", "Fighter", "Magic damage"),
    ("Karthus", "Mage", "Magic damage"),
    ("Graves", "AD", "Physical damage")
]
for index, champion in enumerate(champions_list, start=1): #Use the enumerate function to numbered all the champion that exist in the list
    print(f"{index}. {champion[0]}")                       #This help people to easily see the champion pool
#Start the banning phase
valid_champion_names = [champ[0] for champ in champions_list] #Take all the champion name in the first place in tupple
while True: #Use the loop to make the user have to rechoose the champion again
    champion = input("Banned 3 champion that exist in the list : ")
    champion_banned = champion.split() #change from a string to a list
    if "," in champion:
        print("Please remove the comma") #i need to get rid of the comma to make my code work
        continue 
    if all(name in valid_champion_names for name in champion_banned): #Use the all function to check if the champion banned exist in the champion pool
        print("Champion banned : ", champion_banned)
        break 
    else:
        print("Please choose the champion that already exist in the list") #If the champion isn't there, then you have to choose the champion again

#Start the choosing phase
print("============Start choose your champion(Choose beetwen 20 champs that's already exist in the pool)===================")
while True:
    champion_choosing1 = input("Write down your draft (Write at least 5 champs):" )
    champion_choosing2 = champion_choosing1.split()
    champion_choosing = len(champion_choosing2) 
    if champion_choosing < 5:
        print("Please choose at least 5 champion")
    elif any(name in champion_banned for name in champion_choosing2):
        print("Your champion has been banned, please choose again")
    elif all(name in valid_champion_names for name in champion_choosing2):
        print("Your draft is :", champion_choosing2)
        break 
    else:
        print("Please choose again, your champion doesn't exist in the champion pool")
#Analysis the draft
print("===== Draft Analysis =====")
physical_count = 0  #Call all the type of damage and role
magic_count = 0
role_count = {}
for champ_name in champion_choosing2:
    for champ in champions_list:
        if champ_name == champ[0]:
            role = champ[1]
            damage = champ[2]
            # Count damage type
            if "Physical" in damage or "physical" in damage:
                physical_count += 1 # plus 1 for each physical damage  #For each time one ad damage exist, plus one
            elif "Magic" in damage or "magic" in damage: #Same as the physical damage
                magic_count += 1
            # Count roles
            if role in role_count:
                role_count[role] += 1
            else:
                role_count[role] = 1

print("Physical champions:", physical_count)
print("Magic champions:", magic_count) #Print all of the type of damage that exist in the draft
print("\nRoles in your draft:")
for role, amount in role_count.items():
    print(f"{role}: {amount}")
#Giving advice
print("======Counting Damage Type Of the Team======")
if physical_count >= 4:
    print("Too much Physical Damage, the enemy can easily counter this by buying armor resistance")
    print("I recommand you too pick 3 physical damage champion and 2 magic damage, or reverse, that would be more effiency ")
elif magic_count >= 4:
    print("Too much Magical Damage, the enemy can easily counter this by buying magic resistance")
    print("I recommand you too pick 3 physical damage champion and 2 magic damage, or reverse, that would be more effiency ")






        

    
        



