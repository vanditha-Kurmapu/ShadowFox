#Initial justice_league list
justice_league=["superman","batman","wonder woman","flash","aquaman","green lantern"]
#1. Calculate the number of memebers
print("Initial justice league: ",justice_league)
print("Number of members: ",len(justice_league))
print()
#2.Batman recruits batgirl and nightwing
justice_league.append("batgirl")
justice_league.append("nightwing")
print("After adding batgirl and nightwing: ",justice_league)
#3.move wonder woman to the beginning
justice_league.remove("wonder woman")
justice_league.insert(0,"wonder woman")
print("after making wonder woman the leader: ",justice_league)
print()
#4.seperate aquaman and flash by inserting green lantern between them
justice_league.remove("green lantern")
flash_index=justice_league.index("flash")
justice_league.insert(flash_index,"green lantern")
print("after seperating aquaman and flash: ",justice_league)
print()
#5.replace the team with new members
justice_league=["cyborg","shazam","hawkgirl","martian manhunter","green arrow"]
print("new justice league team: ",justice_league)
print()
#6.sort alphabetically
justice_league.sort()
print("new leader: ",justice_league)
#new leader
print("new leader: ",justice_league[0])