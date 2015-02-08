

f = open('toparse.txt','r')
x = f.read().split("\n")
f.close()


for m in x:
    m = "    " + m

print ''.join(x)
