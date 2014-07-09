import os

def encode():
    x = raw_input("x = ")
    x = x.encode("hex")
    slate = open("data.ctp","w")
    slate.write(x)
    slate.close()

def decode():
    slate = open("data.ctp","r")
    z = slate.read()
    z = str(z)
    slate.close()
    z = z.decode("hex")
    print (z)
