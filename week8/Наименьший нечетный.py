# Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.

print(min(filter(lambda x: x % 2 == 1, map(int, input().split()))))
