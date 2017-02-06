import numpy as np
from zmienne import a,b,c,d

def funkcja(x,a,b,c,d):
    if abs(x)<a[0]:
        px=(np.exp((-x**2)/2))*(((c[0]*(abs(x)**6))+(c[1]*(abs(x)**5))+
                                          (c[2]*(abs(x)**4))+(c[3]*(abs(x)**3))+(c[4]*(abs(x)**2))+
                                              (c[5]*abs(x))+(c[6]))/((d[0]*(abs(x)**7))+(d[1]*(abs(x)**6))+(d[2]*(abs(x)**5))+(d[3]*(abs(x)**4))
                                                                     +(d[4]*(abs(x)**3))+(d[5]*(abs(x)**2))+(d[6]*(abs(x)**1))+(d[7])))
    elif a[0]<=abs(x)<a[1]:
         px=((np.exp(-((x**2)/2)))/b[1])*(1/(abs(x)+1/(abs(x)+2/(abs(x)+3/(abs(x)+4/(abs(x)+b[0]))))))
    return(px)

v=-3.
i=[]
for z in range(61):
    i.append(v)
    v+=0.1

lista=[]
for x in i:
    if x<-a[1]:
        lista.append(0)
    elif -a[0]<=x<0:
        lista.append(funkcja(x,a,b,c,d))
    if 0<=x<a[1]:
        lista.append(1-funkcja(x,a,b,c,d))
    if 0<=a[1]<=x:
        lista.append(1)

for omg in range(len(lista)):
    print lista[omg]
    
