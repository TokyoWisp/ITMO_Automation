#a: int = 5
#b: str = 'строка'
#c: list = [1, 2]
#
#def indent(s: str, width: int) -> str:
#    return " " * (max(0, width - len(s))) + s
#
#print(indent('123', 123))


a: int = 2
b: float = 3.25
c: str = 'null'
d: list = [2, 14]
e: bool = (3 < 5)

def task_1(a, b, c, d, e) -> str:
    return (a, b, c, d, e)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(task_1(3, 4.1, 'zero', [3,6], (8<3)))