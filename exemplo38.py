# Criando um set
meu_set = {"maçã", "banana", "laranja"}

# Sets ignoram itens duplicados
set_com_duplicados = {"maçã", "banana", "maçã", "uva"}
print(set_com_duplicados)
# O resultado será: {'banana', 'maçã', 'uva'}


#EXEMPLO DE SET
set_frutas = {"maçã", "banana"}
set_frutas.add("uva")
print(set_frutas) # {'maçã', 'banana', 'uva'}

set_frutas.remove("banana")
print(set_frutas) # {'maçã', 'uva'}