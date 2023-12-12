def bissesto(numero):
    d4=a%4==0
    d100=a%100==0
    d400=a%400==0
    return d4 and (not d100 or d400)

def valida_data(d,m,a):
    if d<1 or d>31: 
        return False
    if m<1 or m>12:
        return False
    if (m==2 or m==4 or m==6 or m==9 or m==1) and  d==31:
        return False

    return True