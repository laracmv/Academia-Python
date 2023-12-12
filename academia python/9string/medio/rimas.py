def classifica_rima(s1, s2, s3, s4):
    if s1 == s3 and s2 == s4 and s1!= s2:
        return "alternada"
    elif s1 == s4 and s2 == s3 and s1 != s2:
        return "interpolada"
    elif s1 == s2 and s3 == s4 and s1 != s3:
        return "emparelhada"
    else:
        return "outra"
    
print(classifica_rima("ada", "inha", "ada", "inha"))