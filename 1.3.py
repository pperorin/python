print("*** Reading E-Book ***")
text , highlight=input("Text , Highlight : ").split(',')
for i in text:
    if i == highlight:
        i='['+highlight+']'
    print(i,end='')

