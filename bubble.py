my_list = [125, 15, 12, 130, 0, 11, 16, 30, 1, 29]

# Le principe:
# On parcours la liste de taille N:
# Dès qu'on rencontre un élément pas dans l'ordre on les interverti
# A la fin on aura toujours le plus grand en dernier
# Puis on fait la même chose mais sur N-1

def bubble_list(list):

    tested_value = 0
    bigest_value = 0
    list_length = len(list)

    while list_length != 0:

        for i in range(len(list)):

            tested_value = list[i]
            print(f"Valeur: {tested_value}")

            if i == 0:
                bigest_value = tested_value
            elif tested_value > bigest_value:
                
                bigest_value = tested_value
                list.pop(i)
                list.insert(i+1, bigest_value)
            elif bigest_value > tested_value:
                list.pop(i-1)
                list.insert(i, bigest_value)

        list_length -= 1

    return list

print(bubble_list(my_list))