import os
os.chdir('C:\\Users\\Rafael\\OneDrive\\Documentos\\python')

def incluir(escritorio):
    escritorio.append(input("Produto: "))
    escritorio.append(input("Preço: "))
    escritorio.append(input("Estoque: "))

def excluir(escritorio):
    x = int(input("Escolha o numero da ficha que deseja excluir: "))
    for d in range (3):
        escritorio.pop(x)

def procura(escritorio):
    nome = input("Escolha o produto: ")
    for n in range (0,len(escritorio)):
        if nome == escritorio[n]:
            print(escritorio[n]," ",escritorio[n+1]," ",escritorio[n+2])

def mostrar(escritorio):
    for z in range(0,len(escritorio)-2,3):
        print(z,"||",escritorio[z],"||",escritorio[z+1],"||",escritorio[z+2])

def salvar(escritorio):
    b = open('teste.txt',"w")
    for n in range (len(escritorio)):
        b.write(escritorio[n]+";")

f = open("teste.txt","r")
s = (f.read())
lista = s.split(";")
lista.pop(len(lista)-1)

while True:
    print("0- Sair, 1- Incluir, 2- Excluir, 3- Procura, 4- Mostrar todos, 5- Salvar")
    e = input("Escolha a opção: ")
    if e == "0": break
    if e == "1": incluir(lista)
    if e == "2": excluir(lista)
    if e == "3": procura(lista)
    if e == "4": mostrar(lista)
    if e == "5": salvar(lista)