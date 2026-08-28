import jogodaforca
import jogodaadivinhação

def escolherjogo():
print("░░░░░░███████ ]▄▄▄▄▄▄▄▄▃")
print("▂▄▅█████████▅▄▃▂")
print("███████████████████].")
print("◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤")
print("Escolher o jogo que deseja jogar")
print("[1] - Jogo da forca")
print("[2] - Jodo de adivinhação")

jogo = int(input("Qual jogo você deseja jogar?"))
match jogo:
    case 1:
        print("Jogando Jogo da Forca")
        jogodaforca.jogar()
    case 2:
        print("Jogando Jogo de Adivinhação")
        jogodaadivinhação.jogar()
    case 3:
        print("sair")
        exit() 
if __name__ == "__main__":
    escolherjogo()
    