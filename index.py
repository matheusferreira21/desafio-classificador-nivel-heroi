nomeHeroi = input("Digite o nome do héroi: ")
quantidadeXP = int(input("Digite a quantidade de XP do héroi: "))
nivelHeroi = ""
if quantidadeXP <= 1000:
    nivelHeroi = "Ferro"
elif quantidadeXP >= 1001 and quantidadeXP <= 2000:
    nivelHeroi = "Bronze"
elif quantidadeXP >= 2001 and quantidadeXP <= 5000:
    nivelHeroi = "Prata"
elif quantidadeXP >= 5001 and quantidadeXP <= 7000:
    nivelHeroi = "Outro"
elif quantidadeXP >= 7001 and quantidadeXP <= 8000:
    nivelHeroi = "Platina"
elif quantidadeXP >= 8001 and quantidadeXP <= 9000:
    nivelHeroi = "Ascendente"
elif quantidadeXP >= 9001 and quantidadeXP <= 10000:
    nivelHeroi = "Imortal"
elif quantidadeXP >= 10001:
    nivelHeroi = "Radiente"

print(f"O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}")



