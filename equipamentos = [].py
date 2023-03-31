equipamentos = []
valores = []
seriais = []
departamentos = []
reposta = "S"
while reposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Serial: ")))
    departamentos.append(input("Departamento: "))
    reposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", [indice+1])
    print("Nome.........:", equipamentos[indice])
    print("Valor........:", valores[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.:", departamentos[indice])