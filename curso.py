import statistics
print("Questão 1")
lista = [10,13,17,9,8,11,13,7]
print("Média aritmética simples : ", statistics.mean(lista))
print("Média harmonica : ", statistics.harmonic_mean(lista))
print("Média Geométrica : ", statistics.geometric_mean(lista))
print("Moda : ", statistics.mode(lista))
print("Variãncia : ", statistics.variance(lista))
print("Desvio padrão : "  , statistics.stdev(lista))


print("\nQuestão 2")
lista_2 = [67,75,63,72,77,78,81,77,80]
print("Média aritmética simples : ", statistics.mean(lista_2))
print("Harmônica : ", statistics.harmonic_mean(lista_2))
print("Geométrica : ", statistics.geometric_mean(lista_2))
print("Moda : ", statistics.mode(lista_2))
print("Mediana : ", statistics.median(lista_2))
print("Variança : ",statistics.variance(lista_2))
print("Desvio Padrão : ", statistics.stdev(lista_2))


print("\nQuestão 3")
lista_3 = [4.0,4.5,5.0,5.0,5.0,5.5,6.0,6.0,6.5,6.5,6.5,6.5,7.0,7.0,7.0,7.0,7.0,7.0,7.5,8.5,9.0,9.0,9.0,9.5,10.0,10.0,10.5,10.5,11.0,12.0,12.5,13.0,13.0]
CV = statistics.stdev(lista_3) / statistics.variance(lista_3)*100
print("Coeficiente de variação : ",(CV) , "%")

print("\nQuestão 4")
lista_4 = [12,15,18,22,17,14,18,23,29,12]
print("Prodrução media: ",statistics.mean(lista_4))
print("Mediana da produção: ", statistics.median(lista_4))
print("Desvio Padrão: ", statistics.pstdev(lista_4))