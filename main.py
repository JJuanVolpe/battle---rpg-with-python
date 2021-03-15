from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Air", "cost": 10, "dmg": 60}]


player = Person(490, 90, 47, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running =  True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
     print("================================")
     player.choose_action()
     choice = input("Choose action:")
     index = int(choice) - 1


     if index == 0:
         dmg = player.generate_Damage()
         enemy.take_dmg(dmg)
         print("You attacked for:", dmg, "points of damage. Enemy PH:", enemy.get_hp())

     enemy_choice = 1
     enemy_dmg = enemy.generate_Damage()
     player.take_dmg(enemy_dmg)
     print("Enemy attacks for", enemy_dmg, "player HP", player.get_hp())