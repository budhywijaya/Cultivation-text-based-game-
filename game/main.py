from player import Player
from lokasi import hutan, padang_pasir, pantai, pegunungan
from save_dan_load import save_game, load_game
def Main():
    load_choice = input("Apakah kamu ingin memuat(load) game kamu sebelumnya? (yes/no)").lower()
    if load_choice == 'yes':
        player = load_game()
        if player is None:
            return
    
    else: 
        nama_pemain = input("Masukkan nama kamu: ")
        player = Player(nama_pemain)
    

    while player.cultivation <= 10:
        print("\nPilih lokasi:")
        print("1. Hutan")
        print("2. Padang Pasir")
        print("3. Pegunungan")
        print("4. Pantai")
        print("5. Cek Status (s)")
        print("6. Gunakan Healing Potion (h)")
        print("7. Save Game")
        print("8. Load Game")
        print("9. Exit Game")
        aksi = input("Masukkan pilihan (1/2/3/4/5/6/7/8/9): ").lower()

        if aksi == '1':
            hutan(player)
        elif aksi == '2':
            padang_pasir(player)
        elif aksi == '3':
            pegunungan(player)
        elif aksi == '4':
            pantai(player)
        elif aksi == '5':
            player.status()
        elif aksi == '6':
            player.gunakan_healing_potion()
        elif aksi == '7':
            save_game(player)
            print('Game berhasil tersimpan')
        elif aksi == '8':
            player = load_game()
            if player is None:
                return
            print("Game Progress Loaded")
        elif aksi == '9':
            exit()
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__== "__main__":
    Main()