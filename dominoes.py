from copy import deepcopy

def search_number_twin(number, dominoes_list, solution_list, alternate_list):
    '''
    If there exists a way how to connect the presented list of domino tuples into a chain,
    find at least one solution. Tell if this solution does not exist.
    '''
    _dominoes_list = deepcopy(dominoes_list)

    found = False
    next_element = []
    for element in _dominoes_list:
        for side in range(2):
            if element[side] == number:
                if found == False:
                    found = True
                    next_element = [deepcopy(element),0]
                    if side == 1:
                        next_element[0].reverse()
                        next_element[1] = 1
                    dominoes_list.remove(element)
                else:
                    new_alternate = [deepcopy(solution_list)]
                    new_element = [deepcopy(element), 0]
                    if side == 1:
                        new_element[0].reverse()
                        new_element[1] = 1
                    new_alternate[0].append(new_element)
                    new_dominoes_alternate = deepcopy(_dominoes_list)
                    new_dominoes_alternate.remove(element)
                    new_alternate.append(new_dominoes_alternate)
                    alternate_list.append(new_alternate)

    return next_element

def can_chain(dominoes):

    print("Initial set of dominoes to be connected into chain: ", dominoes, "\n")

    exists = True
    dominoes_list = []
    last_element = list(dominoes[0])
    last_element.reverse()
    another_last_element = deepcopy(last_element)
    another_last_element.reverse()
    solution_list = [[last_element]]
    solution_list[0].append(0)
    dominoes.remove(dominoes[0])
    for domino in dominoes:
        dominoes_list.append(list(domino))
    alternate_list = [[[[another_last_element, 1]], deepcopy(dominoes_list)]]

    while dominoes_list != []:
        next_element = search_number_twin(last_element[1], dominoes_list, solution_list, alternate_list)
        if next_element != []:
            last_element = deepcopy(next_element[0])
            solution_list.append(deepcopy(next_element))
        elif len(alternate_list) > 0:
            solution_list = alternate_list[len(alternate_list) - 1][0]
            last_element = solution_list[len(solution_list) - 1][0]
            dominoes_list = alternate_list[len(alternate_list) - 1][1]
            alternate_list.remove(alternate_list[len(alternate_list) - 1])
        else:
            print("Solution does not exist.")
            exists = False
            break

    if exists:
        solution = []
        ordered_solution = []
        for element in solution_list:
            ordered_solution.append(tuple(element[0]))
            if element[1] == 1:
                element[0].reverse()
            solution.append(tuple(element[0]))

        print("Found solution: ", ordered_solution)
        print("Initial orientation of dominoes in this solution: ", solution)

dominoes0 = [(2, 1), (3, 4), (5, 6)]

'''
can_chain([ (1, 2), (2, 3), (3, 1) ])
'''

dominoes = [
    (1, 2),
    (5, 3),
    (3, 1),
    (1, 2),
    (2, 4),
    (1, 6),
    (2, 3),
    (3, 4),
    (5, 6)
]

can_chain(dominoes)