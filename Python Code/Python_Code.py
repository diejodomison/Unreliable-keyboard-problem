x=input()
k=0
n=0
for i in x:
    if "l"==i:
        k+=1
    if "o" ==i:
        n+=1
        
if n==0 and k==0:
    print("No mistakes")
else:
    print(n+k," mistakes")
    x=x.replace("l","1")
    x=x.replace("o","0")
    print(x)




    


