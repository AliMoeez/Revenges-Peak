import math,itertools

list_x=[12,15,120,121]
list_y=[14,17,125,125]

list_enemy=[(list_x[0],list_y[0]),(list_x[1],list_y[1]),(list_x[2],list_y[2]),(list_x[3],list_y[3])]

list_distance=[]

for i in list_enemy:
    list_distance.append([])
    for k in list_distance:
        for j in list_enemy:
            k.append(j)

list_z=list_x+list_y




print(list_z)