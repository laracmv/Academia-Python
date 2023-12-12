def valida_questao(q):
    out = {}
    for k in ['titulo', 'nivel', 'opcoes', 'correta']:
        if k not in q: out[k] = 'nao_encontrado'

    if len(q) != 4:
        out['outro'] = 'numero_chaves_invalido'

    if 'titulo' in q and (len(q['titulo'].strip()) == 0):
        out['titulo'] = 'vazio'

    if 'nivel' in q and q['nivel'].strip() not in ['facil', 'medio', 'dificil']:
        out['nivel'] = 'valor_errado'

    if 'opcoes' in q:
        if len(q['opcoes']) != 4:
            out['opcoes'] = 'tamanho_invalido'
        else:
            for letra in ['A', 'B', 'C', 'D']:
                if letra not in q['opcoes']:
                    out['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    break
            if 'opcoes' not in out:
                for letra, conteudo in q['opcoes'].items():
                    if len(conteudo.strip()) == 0:
                        if 'opcoes' not in out:
                            out['opcoes'] = {}
                        out['opcoes'][letra] = 'vazia'
    if 'correta' in q:
        if q['correta'] not in ['A', 'B', 'C', 'D']:
            out['correta'] = 'valor_errado'

    return out