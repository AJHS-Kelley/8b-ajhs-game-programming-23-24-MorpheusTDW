#example game functions project phillip henry v1.0

print("""
    *~~~~~~~~~~~~~~~~~~~~~~~~~*
     |     welcome to          |
     |     multiclash!!!       |
     |                         |
     |                         |
     |~~~~~~~~~~~~~~~~~~~~~~~~~* """)

def get_player_info(self):
        name = input("Enter your name: ")
        print(f"Welcome, {name}!")

        # Allow the player to choose a character (you can expand the character options)
        print("Choose your character:")
        print("1. kimberly")
        print("2. reaper")
        print("3. goku")
        character_choice = input("Enter the number corresponding to your choice: ")

        # Store player information
        self.players[name] = {"Character": self.get_character_name(int(character_choice))}

        def get_character_name(self, choice):
            characters = {1: "kimberly", 2: "reaper", 3: "goku"}
            return characters.get(choice, "Unknown")

   # select map
   
maps = ["City", "Forest", "Arena"]
print("Select a Map:")
print("type 1 for the city 2 for the forest and 3 for the arena")    
map_choice = int(input("Enter the number of your chosen map: "))
selected_map = ""


if map_choice <= 3 and map_choice >= 1:
      print(selected_map)
else:
      print(" L bozo your getting the arena")
      map_choice = 3
      selected_map = maps[map_choice - 1]
      print(selected_map)


    # Select Day
#days = ["Monday", "Wednesday", "Friday"]
#print("Select a Day:")
#for i, day_option in (days, 1):
#        print(f"{i}. {day_option}")
#day_choice = int(input("Enter the number of your chosen day: "))
#selected_day = days[day_choice - 1]


   
   # CODE REVIEW BY JORDAN HENRY
