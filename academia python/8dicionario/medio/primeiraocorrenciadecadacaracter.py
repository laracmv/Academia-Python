def primeiras_ocorrencias(s):
    ocorrencias = {}
    
    for i in range(len(s)):
        char = s[i]
        if char not in ocorrencias:
            ocorrencias[char] = i
    
    return ocorrencias

# Exemplo de uso:
entrada = 'abracadabra'
saida = primeiras_ocorrencias(entrada)
print(saida)
