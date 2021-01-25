def TowerOfHanoi(n , start,buf,end): 
    if n==0:
        return 
    TowerOfHanoi(n-1,start,buf,end)
    print('move',n,'from ',start,'to',end)
    TowerOfHanoi(n-1,buf,end,start)

def display(n,start,end):
    la,lb,lc=[],[],[]


          
n=(int)(input("Enter Input :"))
TowerOfHanoi(n,'A','B','C')