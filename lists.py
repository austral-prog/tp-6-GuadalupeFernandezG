# Replace the "ANSWER HERE" with your answer

def remove_elements (lista):
	nuevalista=lista [:]
	if len(lista)>=6:
		del nuevalista [5]
		del nuevalista [4]
		del nuevalista [0]
	elif len(lista)==5:
		del nuevalista [4]
		del nuevalista [0]
	elif len(lista)>=1 and len(lista)<=4:
		del nuevalista [0]
	return nuevalista

def add_elements (lista):
	newlista= lista [:]
	newlista.append ("Yellow")
	newlista.insert (0,"Pink")
	return newlista


def is_empty (lista): 
	if lista==[]:
		return True
	else: 
		return False

def check_lists (lista1,lista2):
	if len(lista1)>=3 and len(lista2)>=3:
		if lista1 [2] == lista2 [2]:
			return True
		if lista1 [2] != lista2 [2]:
			return False
	else: 
		return False

def list_of_lists(list_of_lists_to_modify):
	list1= list_of_lists_to_modify [0]
	list2= list_of_lists_to_modify [1]
	list3= list_of_lists_to_modify [2]

	if len(list_of_lists_to_modify)==3:
		lista1= list_of_lists_to_modify [0]
		lista2= list_of_lists_to_modify [1]
		lista3= list_of_lists_to_modify [2]

	elif len(list_of_lists_to_modify)!=3:
		return "La lista no tiene tres listas"

	if len(list1)>=2:
		lista1=lista1[0:2]

	elif len(lista1)<2:
		lista1= lista1[0:1]
		return lista1

	if len(lista2)>=4:
		lista2=lista2[1:4]
	elif len(lista2)<4:
		lista2=lista2[1:]
		return lista2
	lista3=lista3[-2:]
	return lista1, lista2, lista3
