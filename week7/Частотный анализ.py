# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание.
#
# После того, как вы создадите словарь всех слов, вам захочется отсортироватьего по частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости словаи само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны —то по второму. Это почти то, что требуется в задаче.

d = {}

fileIn = open("input.txt")
words_list = fileIn.read().split()

for word in words_list:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
