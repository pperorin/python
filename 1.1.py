print("*** Converting hh.mm.ss to seconds ***")
hh,mm,ss=map(int,input("Enter hh mm ss : ").split())
if(hh>=0 and hh<=99):
    if(mm>=0 and mm<=59):
        if(ss>=0 and ss<=59):
            if(((hh*60*60)+(mm*60)+ss)>=1000):
                print("{0:0=2d}".format(hh),":","{0:0=2d}".format(mm),":","{0:0=2d}".format(ss)," = ",((hh*60*60)+(mm*60)+ss)//1000,",",((hh*60*60)+(mm*60)+ss)%1000," seconds",sep="")
            else:
                print("{0:0=2d}".format(hh),":","{0:0=2d}".format(mm),":","{0:0=2d}".format(ss)," = ",((hh*60*60)+(mm*60)+ss)%1000," seconds",sep="")
        else:
            print("ss(",ss,")"," is invalid!",sep="")
    else:
        print("mm(",mm,")"," is invalid!",sep="")
else:
    print("hh(",hh,")"," is invalid!",sep="")

