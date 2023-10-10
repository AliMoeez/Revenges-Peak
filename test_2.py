"""if dialogue_objective_list[0]==1:
level_1_wizard_talk=False
if dialogue_objective_list[0]==2:
talk_to_abyss_level_one=False
if dialogue_objective_list[0]==3:
investigate_object_level_one=False"""

x=True
y=True
z=True

list_bool=[x,y,z]

num=0

for i in range(len(list_bool)):
    num+=1
    if num==list_bool[i]:
        i=False
    print(list_bool)

