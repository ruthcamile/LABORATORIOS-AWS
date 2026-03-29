#!/usr/bin/env python3
# coding: utf-8

# ==============================
# ARMAZENANDO AS SEQUÊNCIAS
# ==============================

# Armazena a sequência completa da preproinsulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Armazena partes da insulina separadamente
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Junta as partes B e A formando a insulina
insulin = bInsulin + aInsulin


# ==============================
# EXIBINDO NO CONSOLE
# ==============================

# Mostra a sequência completa
print("Sequência da preproinsulina:")
print(preproInsulin)

# Mostra apenas a cadeia A
print("Sequência da insulina (cadeia A): " + aInsulin)


# ==============================
# CÁLCULO DO PESO MOLECULAR
# ==============================

# Dicionário com o peso de cada aminoácido
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Conta quantas vezes cada aminoácido aparece na sequência
aaCountInsulin = {
    x: float(insulin.upper().count(x))
    for x in aaWeights.keys()
}

# Calcula o peso molecular somando (quantidade * peso)
molecularWeightInsulin = sum(
    aaCountInsulin[x] * aaWeights[x]
    for x in aaWeights.keys()
)

# Exibe o peso calculado (convertendo número para string)
print("Peso molecular aproximado da insulina: " + str(molecularWeightInsulin))


# ==============================
# CÁLCULO DA PORCENTAGEM DE ERRO
# ==============================

# Valor real do peso molecular
molecularWeightInsulinActual = 5807.63

# Calcula o erro percentual
erro = ((molecularWeightInsulin - molecularWeightInsulinActual) /
        molecularWeightInsulinActual) * 100

# Mostra o erro
print("Porcentagem de erro: " + str(erro))