import math 


def reflexao_total_interna(n1,n2,o2):
    
    senoo1 = (math.sin(math.radians(o2))*n2)/n1
       # foi de graus para radiano, já que o math.sin so aceita valores em radiano
    if senoo1 > 1:
        return True
    else:
        return False
