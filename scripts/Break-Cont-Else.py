list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        #break #it will break
        continue # to continue
    else:
        print(int)
else:
    print('default')
    

f0 = 0
f1 = 1
set = False
while True:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    if (fn > 100):
        set = True
    else:
        set = False
    print(fn)
    if (set == True):
        break