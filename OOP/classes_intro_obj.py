from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import Carro
from classes_intro_blueprints import ba
from classes_intro_blueprints import casa
from classes_intro_blueprints import peso
 #importar classes
 
pessoa = Pessoa("Diogo", 18)
carro = Carro("Peugout")
ba = ba(2585)
casa = casa("Predio")
peso = peso(65)

 
print(pessoa.saudacao())
print(carro.informacao_do_carro())
print(ba.saudacao())
print(casa.informacao_da_casa())
print(peso.informaçao_do_peso())
