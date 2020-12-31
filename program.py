import json
import time
temp={}
x=input('Do you want to import master database and perform operations on it yes/no')
if(x=='yes'):
    print('Loading master database in temp...')
    with open('master.json','r') as masteropen:
        data_load=json.load(masteropen)
    temp=data_load
    print('Loaded master database')
    print(temp)
d=temp
def read(k):
    if k not in d:
        print("Error:This key is not present")
    else:
        b=d[k]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(k)+":"+str(b[0])
                return stri
            else:
                print("Error:time-to-live of",k,"has expired")
        else:
            print("Enter 1 for create, 2 for read, 3 for delete, 4 to exit, 5 to show data")
if(x==4):
      ('Invalid input')
if(x==1):
    key=input('Enter key for input')
    value=int(input('Enter its corresponding value'))
    create(key,value)
if(x==2):
    key=input('Enter key to read')
    print(read(str(key)))
if(x==3):
    key=input('Enter key')
    delete(key)
    print('key delted')
if(x==5):
    print(d)
import json
temp=d
with open('temp.json','w') as fp:
    json.dump(temp,fp)
print('Your database after operations are:')
print(temp)
x=input('is this first ever operation yes/no')
if(x=='yes'):
    with open('master.json','w') as fp:
        json.dump(temp,fp)
    print("thank you")
    exit()
x=input('Do you want to save this the master dataset yes/no:')
if(x=='yes'):
    data={}
    import json
    with open('master.json','r') as fp:
        json.dump(master,fp)
print('All task done, thanks')