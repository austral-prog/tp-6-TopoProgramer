# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):

    lista = list_to_remove_elements

    remove_elements_lista = lista[1:4] + lista[7:]

    return remove_elements_lista  # Remove this line and implement


def add_elements(list_to_add_elements):

    lista1 = list_to_add_elements

    lista1 = ["Pink"] + lista1

    lista1.append("Yellow")

    return lista1  # Remove this line and implement


def is_empty(list_to_check):

    lista2 = list_to_check

    if lista2 == []:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):

    lista3 = list_to_compare1
    lista4 = list_to_compare2



    if lista3[2:3] == lista4[2:3]:
        return True
    else: 
        return False


def list_of_lists(list_of_lists_to_modify):

    lista5 = list_of_lists_to_modify

    return [lista5[0][:2],lista5[1][1:4],lista5[2][-2:]] # Remove this line and implementls
