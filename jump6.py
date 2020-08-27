a=0
for a in range(1,30):
    if a%6==0 or a%10==6 or a//10==6 :
        continue
    else:
        print(a)
