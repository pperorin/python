class TorKham:
	def __init__(self):
		self.words = []

	def restart(self):
		self.words=[]
		return "game restarted"

	def play(self, word):
        if self.words == []:
		    self.words.append(word)
        else:
            x=self.words[-1]
            y=self.words[-2]
            if x[2:4] == y[-2:]
		return "game over"

torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
for i in S:
    if i[0]=="P":
        torkham.play(i[2:])
        print('\'',i[2:],'\'',' -> ',torkham.words,sep='')
    elif i[0]=="R":
        print(torkham.restart())
    elif i[0]=="X":
        break
    else:
        print('\'',i,'\''," is Invalid Input !!!",sep='')
        break



