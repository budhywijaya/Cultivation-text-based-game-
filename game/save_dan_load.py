import pickle
def save_game(player):
    try:
        with open('game_kultivasi.pkl', 'wb') as file:
            pickle.dump(player, file)
        print("Progres game berhasil tersimpan!")
    except Exception as e:
        print(f"Error ketika menyimpan progres: {e}")

def load_game():
    try:
        with open('game_kultivasi.pkl','rb') as file:
            player = pickle.load(file)
        print("Berhasil memuat progres sebelumnya!")
        return player
    except FileNotFoundError:
        print("File Save Tidak DItemukan!")
        return None
    except Exception as e:
        print(f"Error ketika memuat file: {e}")
        return None