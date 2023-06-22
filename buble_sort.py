# Bubble Sort
def bubble_sort(nums: list) -> list:
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            if lista[j+1] < lista[j]:
                tmp = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = tmp
    return nums


lista = [2, 8, 5, 3, 9, 4, 1]
print(lista)
print(bubble_sort(lista))
