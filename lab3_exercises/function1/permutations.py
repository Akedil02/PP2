from itertools import permutations

def print_permutations(input_string):
    all_permutations = permutations(input_string)

    # Print each permutation
    for perm in all_permutations:
        print(''.join(perm))