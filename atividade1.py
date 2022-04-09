#1 = imposto igual a 35%, 35/100
#2 = imposto igual a 25%, 25/100
#3 = imposto igual a 15%, 15/100
#4 = imposto igual a 5%,  5/100
#5 = impsoto igual a 0%, 0/0

for n in range(4):
    CodigoEstado = int(input("Digite o código do estado de origem da carga: "))
    PesoCargaToneladas = int(input("Peso da carga do caminhão em toneladas: "))

    PesoCargaQuilos = PesoCargaToneladas * 1000
    #Aqui já converteu o peso de toneladas em quilos

    print("Peso da carga em kg: ", PesoCargaQuilos)
    #Mostrar o peso da carga convertida em quilos

    CodigoCarga = int(input("Digite o código da carga entre 10 e 40: "))
    
    #<-- Aqui vai começar as condições dependendo do codigo da carga -->
    if(CodigoCarga > 10 and CodigoCarga < 20):
        PrecoKg = PesoCargaQuilos * 100

    elif(CodigoCarga > 21 and CodigoCarga < 30):
        PrecoKg = PesoCargaQuilos * 250

    elif(CodigoCarga > 31 and CodigoCarga < 40):
        PrecoKg = PesoCargaQuilos * 340
    else:
        print("Código invalido!")

    # <-- Outra condição para calcular o imposto -->
    def impostoEtotal(imp):
        Imposto = PrecoKg * imp

        Total = (PrecoKg + Imposto)

        print("Peso da carga em Kg: " + str(PrecoKg))
        print("Imposto: R$"+ str(Imposto))
        print("Preço da carga Total: R$"+ str(Total))

    if CodigoEstado == 1:
        impostoEtotal(0.35)
    elif CodigoEstado == 2:
        impostoEtotal(0.25)
    elif CodigoEstado == 3:
        impostoEtotal(0.15)
    elif CodigoEstado == 4:
        impostoEtotal(0.05)
    elif CodigoEstado == 5:
        impostoEtotal(0.0)
    else:
        print("Código de estado inválido")

