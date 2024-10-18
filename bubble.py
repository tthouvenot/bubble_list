my_list = [125, 15, 12, 130, 0, 11, 16, 30, 1, 29]

# Le principe:
# On parcours la liste de taille N:
# Dès qu'on rencontre un élément pas dans l'ordre on les interverti
# A la fin on aura toujours le plus grand en dernier
# Puis on fait la même chose mais sur N-1

def bubble_list(list):

    list_length = len(list)

    while list_length > 0:

        for i in range(list_length - 1):

            tested_value = list[i]
            next_value = list[i + 1]

            if tested_value > next_value:
                list[i], list[i+1] = list[i+1], list[i]
        
        list_length -= 1

    return list

print(bubble_list(my_list))