# Tentativa de jogo da forca
# Ideia tirada de uma postagem de um ex-professor meu de tecnologia, porém código original

from random import choice
import time

# Variáveis e listas
imagens_forca = [
"""
+---+
     |
     |
     |
     |
======
""",
"""
+---+
 |   |
     |
     |
     |
======
""",
"""
 +---+
 |   |
 O   |
     |
     |
======
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
======
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
======
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
======
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
======
""",
"""
 +---+
 |   |
 X   |
/|\  |
/ \  |
======
"""
]

lista_escolares = ["lapis","caneta","borracha","caderno","regua","mochila","estojo","livro","marcador","grampeador","tesoura","compasso","giz","apontador","pincel","cola","papel","agenda","quadro","mapa","calculadora","clipe","folha","pasta","lapiseira","fita","adesivo","cartolina","prancheta","carimbo","postit","marcatexto","canetinha","dicionario","transferidor","corretivo","tinta","grampos","resma","fichario","painel","lousa","portaobjetos","cartao","suporte","clips","estilete","envelope","apontador","bloco","esquadro","projetor","lapiseira","etiqueta","prancheta","marcador","cola","canetao","agenda","livrinho","calculadora","tabela","estoque","armario","pincel","carteira","pastel","quadrobranco","marcatexto","portaestojo","ficha","cartaz","gizcolorido","papelao","apostila","folhagem","giz","teclado","mouse","quadro","monitor","pincel","caderno","resma","marcador","clipe","projetor","caneta","lapis","borracha","estojo","mochila","regua","mapa","tesoura"]

lista_comidas = ["arroz","feijao","macarrao","pao","leite","queijo","manteiga","iogurte","ovo","carne","frango","peixe","batata","cenoura","tomate","alface","couve","espinafre","abobrinha","berinjela","cebola","alho","pimentao","ervilha","milho","ervilha","brocolis","repolho","beterraba","rabanete","morango","banana","maca","laranja","pera","uva","melancia","abacaxi","mamão","goiaba","manga","caju","kiwi","limão","tangerina","amora","framboesa","cereja","abacate","maracuja","chocolate","biscoito","bolo","torta","sorvete","pudim","gelatina","creme","mousse","brigadeiro","beijinho","cachorroquente","hamburguer","pizza","lasanha","esfirra","pastel","empada","coxinha","quibe","pipoca","amendoim","castanha","noz","paozinho","panqueca","waffle","crepe","boloformigueiro","churros","canelone","risoto","polenta","espaguete","macarronada","feijoada","farofa","vatapa","acaraje","moqueca","sushi","temaki","yakisoba","ramen","padthai","falafel","hummus","guacamole","ceviche","tacos"]

lista_aleatorias = ["arvore","cachorro","gato","carro","bicicleta","aviao","navio","computador","celular","mesa","cadeira","janela","porta","chave","relógio","espelho","chocolate","bola","livro","caneta","lapis","relogio","telefone","fotografia","futebol","tenis","sapato","meia","camisa","calca","boné","chapéu","oculos","bolsa","mochila","pijama","cobertor","travesseiro","colher","garfo","faca","prato","copo","agua","suco","leite","café","cha","bolo","torta","pudim","sorvete","pizza","hamburguer","macarrao","arroz","feijao","batata","cenoura","tomate","morango","banana","laranja","maca","uva","melancia","abacaxi","manga","kiwi","limão","estrela","lua","sol","nuvem","chuva","neve","vento","montanha","rio","lago","floresta","praia","oceano","ilha","cidade","vila","rua","avenida","parque","jardim","escola","universidade","hospital","farmacia","loja","mercado","supermercado","teatro","cinema","museu"]

def escolha():
    print("Bem vindo(a) ao jogo da forca!")
    print("Escolha um tema de palavras para começarmos:")

    while True:
        print("\n1 - Materiais escolares")
        print("2 - Alimentos")
        print("3 - Palavras aleatórias\n")
        try:
            opcao = int(input())
        except ValueError:
            print("\nDigite apenas números!")
            continue

        if opcao == 1:
            return lista_escolares
        elif opcao == 2:
            return lista_comidas
        elif opcao == 3:
            return lista_aleatorias
        else:
            print("Opção Inválida, tente novamente!")

tema = escolha()

palavra_escolhida = choice(tema)

letras = tuple(palavra_escolhida)   # Criar uma tupla da palavra escolhida ("tuple" faz com que as letras da palavra se dividam)

# print(letras)                                     # Linhas comentadas usadas apenas para testes
# print(palavra_escolhida)
# print(len(palavra_escolhida), " letras")

print("\nPalavra sorteada! Ela possui", len(palavra_escolhida), "letras...")

time.sleep(1)
print()

def jogo():
    
    erros = 0
    
    letras_jogo = tuple("_" * len(letras)) # Letras da palavra substituídas por "_"

    print("\nAgora tente adivinhar a palavra!\n")

    while True:
        
        print(imagens_forca[erros])
        print(" ".join(letras_jogo))
        tentativa = input("Digite uma letra: ").strip().lower() # Tirar espaços e colocar tudo em minúsculo (evita erros de leitura)

        if len(tentativa) != 1:
            
            print("\nDigite apenas uma letra!\n")
            continue
        
        elif not tentativa.isalpha(): # "isalpha" reconhece se o caractere utilizado é uma letra presente no alfabeto
            
            print("\nDigite apenas letras!\n")

        if tentativa in letras:     # Atualização da tupla
            
            tupla_temp = []
            
            for i in range(len(letras)):
                if letras[i] == tentativa:
                    
                    tupla_temp.append(letras[i])
                    
                else:
                    
                    tupla_temp.append(letras_jogo[i])
                    
            letras_jogo = tuple(tupla_temp)
            
        else:
            
            erros += 1
            chances = 7 - erros
            
            if erros < 7:
                
                print(f"\nVocê possui {chances} chances.\n")

        if letras_jogo == letras:       # Derrota
            
            print(imagens_forca[erros])
            print(" ".join(letras_jogo))
            return "\nFim de jogo\nVocê ganhou!!! ╰(*°▽°*)╯\n"

        if erros == 7:      # Vitória
            
            print(imagens_forca[erros])
            print("A palavra era:", "".join(letras))
            return "\nFim de jogo\nVocê Perdeu ＞︿＜\n"

print(jogo())

time.sleep(0.5)

print("\nEncerrando em 3 segundos...")

time.sleep(3)
