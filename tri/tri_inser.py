def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle
    return tab

print(tri_insertion([5, 2, 9, 1, 5, 6]))
print(tri_insertion([]))
print(tri_insertion([1]))
print(tri_insertion([10, 7, 8, 9, 1, 5]))