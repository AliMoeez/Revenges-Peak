import math,itertools

list_x=[12,15,120,121]
list_y=[14,17,125,125]

list_enemy=[(list_x[0],list_y[0]),(list_x[1],list_y[1]),(list_x[2],list_y[2]),(list_x[3],list_y[3])]


list_distance=[]
list_enemy_group=[]


for i in list_enemy:
    for j in list_enemy:
        distance=math.hypot(i[0]-j[0],i[1]-j[1])
        list_distance.append(distance) 
        if len(list_distance)>len(list_enemy):
            del list_distance[-1]
for i in list_distance:
    for j in list_distance:
        enemy_distance=math.isclose(i,j,abs_tol=100)
        
    

 


#print(list_enemy)
print(list_distance)

print(list_enemy_group)






