for n in range(4):
    #Solicita o código do estado da carga
    CodigoEstado = int(input("Digite o código do estado da carga: "))

    #Solicita o peso da carga em toneladas:
    PesoCargaToneladas = int(input("Peso da carga do caminhão em toneladas: "))

    #Aqui já converteu o peso de toneladas em quilos:
    PesoCargaQuilos = PesoCargaToneladas * 1000

    #Solicita o código da carga:
    CodigoCarga = int(input("Digite o código da carga entre 10 e 40: "))
    
    #<-- Aqui vai começar as condições dependendo do codigo da carga -->
    if(CodigoCarga >= 10 and CodigoCarga <= 20): #Se "CodigoCarga" inserido for entre 10 e 20, faça:
        PrecoKg = PesoCargaQuilos * 100

    elif(CodigoCarga >= 21 and CodigoCarga <= 30):#Se "CódigoCarga" inserido for entre 21 e 30, faca:
        PrecoKg = PesoCargaQuilos * 250

    elif(CodigoCarga >= 31 and CodigoCarga <= 40):#Se "CodigoCarga" inserido for entre 31 e 40, faça:
        PrecoKg = PesoCargaQuilos * 340
    else:#Se não for nenhuma das condições anteriores, então o código será invalidado
        print("Código invalido!")

    # <-- Função para calcular o imposto, o total e exibir o resultado total -->
    def impostoEtotal(imp):
        Imposto = PrecoKg * imp
        Total = (PrecoKg + Imposto)

        print(f'Peso da carga em Kg:{PesoCargaQuilos} \nPreço da carga do caminhão: R${PrecoKg} \nImposto: R${Imposto} \nPreço carga total{Total}')

    # <-- Condição para verificar o "CodigoEstado" da carga -->
    if CodigoEstado == 1: #Se "CodigoEstado" for igual a 1, faça:
        impostoEtotal(0.35)
    elif CodigoEstado == 2: #Se "CodigoEstado" for igual a 2, faça:
        impostoEtotal(0.25)
    elif CodigoEstado == 3: #Se "CodigoEstado" for igual a 3, faça:
        impostoEtotal(0.15)
    elif CodigoEstado == 4: #Se "CodigoEstado" for igual a 4, faça:
        impostoEtotal(0.05)
    elif CodigoEstado == 5: #Se "CodigoEstado" for igual a 5, faça:
        impostoEtotal(0.0)
    else: #Caso o "CodigoEstado" não for nenhuma das anteriores ele será invalidado
        print("Código de estado inválido")

    

