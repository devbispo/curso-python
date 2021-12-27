import statistics
print("Questão 1 ")
lista_matematica = [60,58,73,51,54,75,48,72,75,83,62,52]
lista_musica = [80,62,70,83,62,92,79,88,54,82,64,69]
print("Coeficiente de correlação: ",statistics.correlation(lista_musica,lista_matematica))

print("\nQuestão 2")
livros = [1,2,3,4,5,6,7,8,9,10,11,12]
print(statistics.linear_regression(livros))


