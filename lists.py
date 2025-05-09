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
	elif len(lista)>=1 and len(lista)<=3:
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
    return "ANSWER HERE"  # Remove this line and implement
