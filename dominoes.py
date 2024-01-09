from copy import deepcopy


def search_number_twin(number, dominoes_list, solution_list, alternate_list):
    """
    If there exists a way how to connect the presented list of domino tuples into a chain,
    find all the solutions and tell if they create cycles. Tell if the solution does not exist.
    """

    _dominoes_list = deepcopy(dominoes_list)

    found = False
    next_element = []
    for element in _dominoes_list:
        for side in range(2):
            if element[side] == number:
                if not found:
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
    all_solutions = []
    dominoes_list = []
    last_element = list(dominoes[0])
    another_last_element = deepcopy(last_element)
    another_last_element.reverse()
    solution_list = [[last_element]]
    solution_list[0].append(0)
    dominoes.remove(dominoes[0])
    for domino in dominoes:
        dominoes_list.append(list(domino))

    alternate_list = [[[[another_last_element, 1]], deepcopy(dominoes_list)]]

    for piece in deepcopy(dominoes_list):
        remaining_alternates = deepcopy(dominoes_list)
        remaining_alternates.remove(piece)
        remaining_alternates.append(last_element)
        alternate_list.append([[[piece, 0]], deepcopy(remaining_alternates)])
        reversed_piece = deepcopy(piece)
        reversed_piece.reverse()
        alternate_list.append([[[reversed_piece, 1]], deepcopy(remaining_alternates)])

    create_cycles = False

    while dominoes_list:
        next_element = search_number_twin(last_element[1], dominoes_list, solution_list, alternate_list)
        if next_element:
            last_element = deepcopy(next_element[0])
            solution_list.append(deepcopy(next_element))
            if not dominoes_list:
                all_solutions.append(solution_list)
                if solution_list[0][0][0] == solution_list[-1][0][1]:
                    create_cycles = True
        if not next_element or not dominoes_list:
            if len(alternate_list) > 0:
                solution_list = deepcopy(alternate_list[-1][0])
                last_element = deepcopy(solution_list[-1][0])
                dominoes_list = deepcopy(alternate_list[-1][1])
                alternate_list.remove(alternate_list[-1])
            elif not all_solutions:
                print("Solution does not exist.")
                exists = False
                break

    if exists:
        print(f"Found {len(all_solutions)} solutions, {"all" if create_cycles else "none"} of them create cycles:\n")
        for order, partial_solution in enumerate(all_solutions):
            solution = []
            ordered_solution = []
            for element in partial_solution:
                ordered_solution.append(tuple(element[0]))
                if element[1] == 1:
                    element[0].reverse()
                solution.append(tuple(element[0]))

            print(f"{order + 1}.solution: {ordered_solution}")
            print("Initial orientation of dominoes in this solution: ", solution, "\n")

dominoes = [(2, 1), (3, 2), (3, 4)]

'''
can_chain([ (1, 2), (2, 3), (3, 1) ])
'''

dominoes0 = [
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

