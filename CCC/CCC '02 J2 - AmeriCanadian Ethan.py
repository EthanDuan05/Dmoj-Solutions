con = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z'
new = []
while True:
    line = input()
    if line == 'quit!':
        break
    elif line != 'quit':
        if len(line) > 3:
            if line[len(line)-3] in con:
                if line[len(line)-2:len(line)] == 'or':
                    new.append(line.replace('or', 'our'))
                elif line[len(line)-2:len(line)] != 'or':
                    new.append(line)
            else:
                new.append(line)
        else:
            new.append(line)
for k in new:
    print(k)