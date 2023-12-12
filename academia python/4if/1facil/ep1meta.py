def meta_atingida(limite_reclamacoes, limite_justica, total_reclamacoes, total_justica):

    if total_reclamacoes <= limite_reclamacoes:
        
        if total_justica <= limite_justica:
            return True 
    return False 