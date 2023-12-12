with open('testeteste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# Quando sai do bloco do 'with', fecha o arquivo automaticamente.]
print(conteudo)

with open('testeteste.txt', 'w') as arquivo:
    arquivo.write("Testando ando andando")

with open('testeteste.txt', 'a') as arquivo:
    arquivo.write("\n I know")


#r - read, para arquivos de textos
#rb - le binarios
# w - cria novo arquivo no modo escrita, apaga anterior
# wb - cria novo arquivo no modo escrita binario
# a (append) - adiciona palavras no final do arquivo
# ab - msm coisa q o anterior, com binario

# Cancao do exilio
with open('cancao do exilio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)

#le primeira linha
# Lendo apenas a primeira linha
with open('cancao do exilio.txt', 'r') as arquivo:
    primeira_linha = arquivo.readline()
print(primeira_linha)


with open('cancao do exilio.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    # Verificando que linhas é uma lista de strings
    print(linhas)
    # Imprimindo de linha em linha
    for linha in linhas:
        print(linha)