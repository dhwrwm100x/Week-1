a=[-1,8,3,-1,0,4,-5,177,-23567]
def count(a):
    total1=0
    total2=0
    for i in a:
        if i<0:
            total1 +=1
        else :
            total2 +=1
    return total1,total2     
neg,pos=count(a)
print('negative : ',neg)
print('positive : ',pos)
