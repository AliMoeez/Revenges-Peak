test=" sidfhsidfj jfjsdof;jsdl;k \n j;sdlkfjsd;lkfj sdefljsdf shjifalskd  \n sdlkjasldj lsdjfsald sdljas  asdfjnaksd slfndl"

x=test.split("\n")

text_position=[0]
message_speed=2


while True:
    for i,y in enumerate(x):
        if text_position[0]<message_speed*len(x[i]):
            text_position[0]+=2

    for idx,text in enumerate(x):
        
        print(x[idx][0:int(text_position[0])//message_speed],idx)