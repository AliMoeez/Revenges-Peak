text=[1,2,3,4]


for i,y in enumerate(text):
    text[i]+=1
    if text[i]>5:
        text[i]=5
    print(text)