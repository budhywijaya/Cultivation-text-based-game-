class Monster:
    def __init__(self, nama, level, max_hp):
        self.nama = nama
        self.max_hp = max_hp
        self.lvl = level
        self.hp = max_hp
        self.defense = self.lvl*2
    
    def attack(self, player):
        damage = (self.lvl * 8) - player.defense
        if damage > 0:
            player.kena_dmg(damage)
            print(f"{self.nama} menyerang {player.nama} dengan jumlah damage {damage}")
        else:
            print(f"{self.nama} menyerang {player.nama}, tetapi serangannya tidak berpengaruh.")
    
class Beastmaster(Monster):
    def __init__(self):
        super().__init__("Beastmaster", 3, 120) 

class Unta(Monster):
    def __init__(self):
        super().__init__("Unta", 2, 70) 

class BabiHutan(Monster):
    def __init__(self):
        super().__init__("Babi Hutan", 2, 60) 

class KambingGunung(Monster):
    def __init__(self):
        super().__init__("Kambing Gunung", 2, 70) 

class Kalajengking(Monster):
    def __init__(self):
        super().__init__("Kalajengking", 2, 75) 

class ManusiaIkan(Monster):
    def __init__(self):
        super().__init__("Manusia Ikan", 5, 200)

class Kepiting(Monster):
    def __init__(self):
        super().__init__("Kepiting", 4, 200) 

