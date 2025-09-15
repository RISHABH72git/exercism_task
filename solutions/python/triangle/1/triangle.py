def equilateral(sides):
    if not is_triangles(sides):
        return False

    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not is_triangles(sides):
        return False

    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
    if not is_triangles(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]


def is_triangles(sides):
    return sum(sides) > 0 and (sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1])