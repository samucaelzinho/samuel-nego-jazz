musicas = [
("Musica 1", "Rock"),
("Musica 2", "pop"),
("Musica 3", "Jazz"),
("Musica 4", "Rock"),
("Musica 5", "pop"),
]

# Historico de musicas ouvidas pelo usuario
historico_usuario = ["Rock" ,"Jazz" ,"Pop" ,"Jazz" ,"Pop"]

# Funcao para recomendar musicas

def recomendar_musica(historico): 
    # Contar a frequencia de cada genero histórico 
    frequencia = {}
    for genero in historico:
        if genero in frequencia:
            frequencia[genero] += 1
        else:
            frequencia[genero] = 1

    # Encontrar o genero mais frequente
    genero_mais_frequente = max(frequencia, key=frequencia.get)   
          
    # Recordar musicas desse genero 
    recomendacoes = []
    for titulo, genero in musicas:
         if genero == genero_mais_frequente:
             recomendacoes.append(titulo)
    return recomendacoes


# obter recomendacaoes para o usuario 
recomendacoes_usuario = recomendar_musica(historico_usuario)
print("Musicas recomendandas:", recomendacoes_usuario)
