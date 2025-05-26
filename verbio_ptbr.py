import random

#lista de verbos
verbos_servio = [
    "raditi",     # trabalhar
    "učiti",      # estudar
    "čitati",     # ler
    "gledati",    # assistir / ver
    "slušati",    # escutar
    "igrati",     # jogar
    "voziti",     # dirigir
    "nositi",     # carregar / vestir
    "pevati",     # cantar
    "živeti"      # viver
]

#dicionario de significados
dict = {
    "raditi": "trabalhar",
    "učiti": "estudar",
    "čitati": "ler",
    "gledati": "assistir / ver",
    "slušati": "escutar",
    "igrati": "jogar",
    "voziti": "dirigir",
    "nositi": "carregar / vestir",
    "pevati": "cantar",
    "živeti": "viver"
}

#pronome sérvios
pronomes = {
    "1s": ["ja"],   #Eu
    "2s": ["ti"],   #Você
    "3s": ["on", "ona", "ono"],     #ele (m, f, n)
    "1p": ["mi"],   #Nós
    "2p": ["vi"],   #Vocês
    "3p": ["oni", "one", "ona"]     #eles (m, f, n)
}

#sorteios
grupo_pronome = random.choice(list(pronomes.keys()))
pronome = random.choice(pronomes[grupo_pronome])
verbo = random.choice(verbos_servio)

ultima_letra = verbo[-3]

#resposta corretas
if grupo_pronome == "1s":
    resposta = verbo[:-2] + "m"
elif grupo_pronome == "2s":
    resposta = verbo[:-2] + "š"
elif grupo_pronome == "3s":
    resposta = verbo[:-2]
elif grupo_pronome == "1p":
    resposta = verbo[:-2] + "mo"
elif grupo_pronome == "2p":
    resposta = verbo[:-2] + "te"
elif grupo_pronome == "3p":
    if ultima_letra == "a":
        resposta = verbo[:-3] + "aju"
    elif ultima_letra == "i":
        resposta = verbo[:-3] + "e"
    elif ultima_letra == "e":
        resposta = verbo[:-3] + "u"
    else:
        resposta = "erro"  # ou outra lógica de fallback
else:
    resposta = "A resposta está errada"


print(f"Grupo: {grupo_pronome} | Pronome: {pronome} | Verbo: {verbo}")
print(pronome, verbo)
resposta_usuario = input("digite sua resposta:")

if resposta_usuario.strip() == f"{pronome} {resposta}" or resposta_usuario.strip() == f"{resposta}":
        print("✅ Correto!")
else:
        print(f"❌ Errado. A resposta certa é: {pronome} {resposta}")

print(f"A resposta correta é: {resposta}")
print(f"Aliás, {verbo} significa: {dict[verbo]}")
