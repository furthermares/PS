while(True):
    try:
        x = int(input())
        if x%2==0 or x%5==0 or not 1<=x<=10000:
            exit()
        i=1
        while(True):
            if(int('1'*i) % x == 0):
                print(i)
                break
            else:
                i+=1
    except:
        break