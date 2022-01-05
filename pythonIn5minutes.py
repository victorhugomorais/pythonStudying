#to comment

"""
to comment
with
some
breaks
"""
#python can do all math stuff
a = [1+2, 3*3,6/3]
print(a)

b = ["hello world","victor"]
print(b)
print(b + ["other string"])

print(b +[1,2,3,4])

#dicionários
dictionary = {"nome":"name","idade":"age"}

print(dictionary)

print(dictionary["nome"])

print(dictionary["idade"])

#sets não repetem seus itegrantes e não possuem índices
c={1,2,2,3,3,4,4,5,5}
print(c)

d={"pera", "maça", "uva", "goiabada", "maça", "uva"}
print(d)

#if condicional 2 PONTOSSSSS ::::::::::::::::::::::::::::::::::::::::::::::::::
if(1==1):
    print("vai printar, é verdade, 1 é igual a 1")

if(1==0):
    print("se isso printasse era doideira kk")
else:
    print("vai printar esse aqui pois é o else de um false")

#operadores lógicos
#OU
if(1 or 0):
    print("printou pois tem 1 no ou")
#E
if(1 and 0):
    print("não vai printar pois é falso")
else:
    print("aqui vai printar pois é o else do 1 and 0")

#loops repetição
#for
for i in range(0,10):
	print(i)

#while
x=10
while x > 0:
    print(x)
    x-=1

b=['helo world','ur welcome']

for i in b:
    print(i)

#try ->pesquisar, o except IndexError seguido de print substitui o erro de Index
try:
    print("b 2 é:" + b[2])
except IndexError:
    print("Item not in list")

#funções
def func():
    print("hello world")

func()
func()

#POO Classes
class Person:
    def __init__(self):
        print("new person")

p = Person()

class Victor(Person):
    def __init__(self):
        super().__init__()
        print("my name is Victor")

v = Victor()