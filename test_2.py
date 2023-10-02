list=[("TEXT",1,2),
     ("TEXT 2",3,4),
      ("TEXT 3",5,6) ]

list_2=[]

list_2.append(list)

for x in list_2:
    for idx,num in enumerate(x):
        if idx==0:
            print(num[0])
