inp = list(map(int,(input("Enter All Bid : ").split())))
inpset = list(set(inp))
inpset.sort()
if (len(inp)<2):
    print("not enough bidder")
elif (inp.count(inpset[-2])>1):
    print("error : have more than one highest bid")
else:
    print("winner bid is",inpset[-1],"need to pay",inpset[-2])