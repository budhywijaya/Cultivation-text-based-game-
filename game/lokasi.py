import random
from monster import Monster, Beastmaster, BabiHutan, Unta, ManusiaIkan, Kalajengking, KambingGunung, Kepiting
def hutan(player):
    print(f"{player.nama} berada di hutan")
    monsters = [Beastmaster(), BabiHutan()]
    ketemu_monster(player, monsters)

def padang_pasir(player):
    print(f"{player.nama} berada di Padang Pasir")
    monsters = [Kalajengking(), Unta()]
    ketemu_monster(player, monsters) 

def pegunungan(player):
    print(f"{player.nama} berada di pegunungan")
    monsters = [KambingGunung()]
    ketemu_monster(player, monsters) 

def pantai(player):
    print(f"{player.nama} berada di hutan")
    monsters = [ManusiaIkan(), Kepiting()]
    ketemu_monster(player, monsters)  

def ketemu_monster(player, monsters):
    monster = random.choice(monsters)
    print(f"Kamu bertemu dengan monster {monster.nama}")
   
    while monster.hp > 0 and player.hp > 0:
        print(f"HP {player.nama}: {player.hp}")
        print(f"HP {monster.nama}: {monster.hp}")

        aksi = input("Apakah kamu ingin menyerang (a), gunakan potion (h) atau lari (r)").lower()
        if aksi == 'a':
            player.serang(monster)
            if monster.hp <= 0:
                print(f"Kamu berhasil mengalahkan {monster.nama}!")
            else:
                monster.attack(player)
                if player.hp <= 0:
                    print("Game Over!")
                    break
        elif aksi == 'h':
            player.gunakan_healing_potion()

        elif aksi == 'r':
            print("Kamu melarikan diri dari pertarungan")
            break
        else:
            print("Aksi tidak valid")
        
        if player.hp > 0 and monster.hp <= 0:
            level_difference = monster.lvl - player.cultivation
            if level_difference == 1:
                exp_poin = 20 * 2
            elif 2 < level_difference < 5:
                exp_poin = 20 * 3
            elif level_difference >= 5:
                exp_poin = 20 *5
            else:
                exp_poin = 20
            
            player.dapat_exp(exp_poin)
            print(f"Kamu mendapatkan {exp_poin} poin! Exp {player.exp}/{100}")