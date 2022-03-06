import datetime 
import math

class Pessoa:
    def __init__(self, nome: str, sobrenome:str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property 
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    #sobrescrever o método __str__ 
    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos"

andre = Pessoa(nome='Andre', sobrenome='Sionek', data_de_nascimento=datetime.date(1991, 1, 9))

print(andre) #Caso o método __str__não esteja sobrescrito retona algo do tipo <__main__.Pessoa object at 0x0000024FDDC13F70>
print(andre.nome)
print(andre.sobrenome)
print(andre.idade)  #Caso o método idade não possuisse o 'decorator' @property, deveria ser chamado andre.idade()
