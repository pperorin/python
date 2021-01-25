def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
x,y=map(int,input('Enter Input : ').split())
if(x==0 and y==0):
    print('Error! must be not all zero.')
elif x<0 and y<0:
    if abs(x)>=abs(y):
        print('The gcd of' , x , 'and' , y ,'is :',gcd(abs(x),abs(y)),end='')
    else:
        print('The gcd of' , y , 'and' , x ,'is :',gcd(abs(y),abs(x)),end='')
elif(x>=y):
    print('The gcd of' , x , 'and' , y ,'is :',gcd(abs(x),abs(y)),end='')
elif(y>x):
    print('The gcd of' , y , 'and' , x ,'is :',gcd(abs(y),abs(x)),end='')

