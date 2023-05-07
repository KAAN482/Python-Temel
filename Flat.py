newlist=[]

def flat(liste):
    
    for i in liste:
        if isinstance(i,list):
            flat(i)

        else:
            newlist.append(i)


flat([[[1,'a',['cat'],2],[[[3]],'dog'],4,5]])

print(newlist)
