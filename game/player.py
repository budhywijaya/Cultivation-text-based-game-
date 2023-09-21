class Player:
    def __init__(self, nama):
        self.nama = nama
        self.max_hp = 100
        self.hp = self.max_hp
        self.exp = 0
        self.atk = 10
        self.defense = 10
        self.cultivation = 1
    
    def serang(self, monster):
        damage = self.atk - monster.defense
        if damage > 0:
            monster.hp -= damage
            print(f"{self.nama} menyerang monster {monster.nama} dan menghasilkan damage {damage}")
        else:
            print(f"{self.nama} menyerang {monster.nama}, tetapi serangannya tidak berpengaruh.")
    
    def status(self):
        print(f"Name: {self.nama}")
        print(f"HP: {self.hp}")
        print(f"EXP: {self.exp}")
        print(f"ATK: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"Cultivation Level: {self.cultivation}")

    def gunakan_healing_potion(self):
        if self.hp < self.max_hp:
            healing_amount = 30
            self.hp += healing_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"{self.nama} menggunakan ramuan penyembuhan dan mendapatkan {healing_amount} HP.")
        else:
            print(f"{self.nama} sudah memiliki HP maksimal. Ramuan penyembuhan tidak digunakan.")

    def naik_cultivation(self):
        self.cultivation += 1
        self.exp = 0
        self.max_hp *= 2
        self.atk *= 1.2
        self.defense *=1.1
        print(f"Selamat, {self.nama} naik level {self.cultivation}")
    
    def dapat_exp(self, exp_poin):
        self.exp += exp_poin
        if self.exp > 100 :
            self.naik_cultivation()
    
    def kena_dmg(self, damage):
        self.hp -= damage
        if (self.hp <= 0):
            print(f"{self.nama} tewas")