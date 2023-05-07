def cevir(liste):
    for i in liste:
        if isinstance(i,list):
            i.reverse()
        

    liste.reverse()




x=[[1, 2], [3, 4], [5, 6, 7]]
cevir(x)
print(x)