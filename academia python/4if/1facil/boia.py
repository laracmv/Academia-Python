import math

def will_it_float(P,R,r):
    volume=2*(math.pi)**2*R*r**2
    densidade = P*1000/volume
    if densidade <= 0.997:
        return True
    else:
        return False