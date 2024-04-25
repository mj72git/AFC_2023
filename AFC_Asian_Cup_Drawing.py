import random
import time
import pandas as pd
# pip install pandas
# pip install openpyxl

afc=pd.read_excel('afc.xlsx')


glist=[[],[],[],[],[],[]]
kh=[]
p=0
g=0
print()

while True:
   
    if (len(glist[0])==0):
        glist[0].append('QAT')
        kh.append('QAT')
        g+=1
    else:
        t=random.choice(afc.iloc[:,p])
    
        if t not in kh:
            glist[g].append(t)
            kh.append(t)
            g+=1
            
        else:
            pass

        if g==6:
            p+=1
            g-=6
            if p>3:
                break
   
Groups=['A','B','C','D','E','F']

print()
print('         AFC ASIAN CUP 2023 DRAW!')
print('---------------------------------------------------------------')
print()
time.sleep(1)
for i in range(len(Groups)):
    time.sleep(1)
    print('Group %s : %s ' %(Groups[i],glist[i]))
    print()
print('---------------------------------------------------------------')
time.sleep(1)
print(" It's finished! please email us and tell your comments about this event.")
print("AFC2023@gmai.com ")
print()
print("MJ Shadfar")
dic={}
for i in range(len(glist)):
    dic[Groups[i]]=glist[i]

d=pd.DataFrame(dic)
d.to_excel('Final_Draw.xlsx',sheet_name='AFC Draw',index=False)




