
from copy import deepcopy


def PrintPointers(nums, L=None, R=None, i=None):

    """This prints array in first line, and used pointers below"""

    array = '   '.join([str(num) for num in nums])
    pointer = [' '] * len(array)

    current = 0
    positions = []
    for num in nums:
        positions.append(current)
        current += 3 + len(str(num))

    if L is not None:
        pointer[positions[L]] = 'L'
    if R is not None:
        position = positions[R] if L != R else positions[R] + 1
        pointer[position] = 'R'
    if i is not None:
        position = positions[i] if i != L else positions[i] + 1
        position = position if i != R else position + 1
        pointer[position] = 'i'

    print(array)
    print(''.join(pointer))
    print('-' * len(pointer))
    return


if __name__ == "__main__":
    PrintPointers(nums=deepcopy([2, 10, 3, 123, 45]), L=1, R=-2, i=2)
    PrintPointers(nums=[0, 0, 0, 0, 0], L=0, R=0, i=0)
    PrintPointers(nums=deepcopy([2, 10, 3, 123, 45, 1450]), L=-1, R=1, i=3)
