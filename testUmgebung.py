
preise = [2.80, 4.70, 3.20, 6.30, 7]
preiseUmgekehrt = []

for i in range(len(preise) - 1, -1, - 1):
    preiseUmgekehrt.append(preise[i])
print(preiseUmgekehrt)