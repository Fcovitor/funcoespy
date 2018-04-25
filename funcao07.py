#!/usr/bin/env python3
def c2f(c):
    return ((1.8*c)+32)

def f2c(f):
    return (float(f)-32)/1.8

valorF=float (input("Digite o  valor em F:"))
print("valor",valorF,"Em Farenheit corresponde a",f2c(valorF),"C")
