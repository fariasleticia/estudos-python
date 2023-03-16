AnoAtual = 2023
NascimentoA = 2007
NascimentoB = 2003

def CálculoIdade (AnoAtual, Nascimento):
    idade = AnoAtual - Nascimento
    return idade

idadeA = CálculoIdade (AnoAtual, NascimentoA)
idadeB = CálculoIdade (AnoAtual, NascimentoB)

print ("A idade de Serhumano1 é " + str(idadeA) + " anos.")
print ("A idade de Serhumano2 é " + str(idadeB) + " anos.")