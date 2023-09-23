list_2=[1,2]
list_3=[3,4]

list_1=list_2+list_3

for idx,number in enumerate(list_1):
    if number in list_3:
        for i,y in enumerate(list_3):
           if number==y:
               print(idx,i)
        