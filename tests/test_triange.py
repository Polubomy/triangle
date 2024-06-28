import pytest

class Rtriangle:

    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

@pytest.mark.parametrize("data", [
    (3, 2, 3, 6, 1, 2),
    (0, 0, 3, 0, 0, 4),
    (0, 0, 2, 0, 2, 2)
])
def test_get_right_triangle(data):

    x1, y1, x2, y2, x3, y3 = data
    triangle = get_rtriangle(x1, y1, x2, y2, x3, y3)

    side_1 = round(((triangle.x2 - triangle.x1)**2 + ((triangle.y2 - triangle.y1)**2))**0.5,2)
    side_2 = round(((triangle.x3 - triangle.x2)**2 + ((triangle.y3 - triangle.y2)**2))**0.5,2)
    side_3 = round(((triangle.x1 - triangle.x3)**2 + ((triangle.y1 - triangle.y3)**2))**0.5,2)

    print(f'\n1 сторона**2 - {side_1**2}, side_2**2 + side_3**2 = {round(side_2 ** 2 + side_3**2,2)}')
    print(f'2 сторона**2 - {side_2**2}, side_1**2 + side_3**2 = {round(side_1 ** 2 + side_3**2,2)}')
    print(f'3 сторона**2 - {side_3**2}, side_1**2 + side_2**2 = {round(side_1 ** 2 + side_2**2,2)}')

    assert ((side_1**2 + side_2**2) == round(side_3**2)) \
           or ((side_1**2 + side_3**2) == round(side_2**2)) \
           or ((side_2**2 + side_3**2) == round(side_1**2))


def get_rtriangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> Rtriangle:

    return Rtriangle(x1, y1, x2, y2, x3, y3)