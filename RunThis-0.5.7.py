import xml.etree.ElementTree as ET
#Change filename on next line to run a differently named file.
xtree = ET.parse('Code.xml')
xroot = xtree.getroot()
num = 1
answer = ''
joina = ''
joinb = ''
dothis = 0
mathsa = 0
mathsb = 0
def maths(val1, op, val2):
    if (op == '+'):
        print(val1+val2)
    elif (op == '-'):
        print(val1-val2)
    elif (op == '*'):
        print(val1*val2)
    elif (op == '/' and val2 != 0):
        print(val1/val2)
    elif (val2 == 0):
        print('Error: Numbers can\'t be divided by 0.')
    else:
        print('Error: Your input isn\'t valid.')
a = '0'
b = '0'
c = '0'
d = '0'
e = '0'
f = '0'
g = '0'
h = '0'
i = '0'
j = '0'
k = '0'
l = '0'
m = '0'
n = '0'
o = '0'
p = '0'
q = '0'
r = '0'
s = '0'
t = '0'
u = '0'
v = '0'
w = '0'
x = '0'
y = '0'
z = '0'
avar = ''
bvar = ''
cvar = ''
dvar = ''
evar = ''
fvar = ''
gvar = ''
hvar = ''
ivar = ''
jvar = ''
kvar = ''
lvar = ''
mvar = ''
nvar = ''
ovar = ''
pvar = ''
qvar = ''
rvar = ''
svar = ''
tvar = ''
uvar = ''
vvar = ''
wvar = ''
xvar = ''
yvar = ''
zvar = ''
op = ''
inta = 0
intb = 0

sti = str(num)
for i in range (500):
    for x in xroot.findall('script'):
        if x.find('say'+sti) is None:
            dothis = 1
        else:
            say = x.find('say'+sti).text
            if (say=='answer'):
                print(answer)
            elif(say=='/answer'):
                print('answer')
            elif (say=='a'):
            	print(a)
            elif (say=='b'):
            	print(b)
            elif (say=='c'):
            	print(c)
            elif (say=='d'):
            	print(d)
            elif (say=='e'):
            	print(e)
            elif (say=='f'):
            	print(f)
            elif (say=='g'):
            	print(g)
            elif (say=='h'):
            	print(h)
            elif (say=='i'):
            	print(i)
            elif (say=='j'):
            	print(j)
            elif (say=='k'):
            	print(k)
            elif (say=='l'):
            	print(l)
            elif (say=='m'):
            	print(m)
            elif (say=='n'):
            	print(n)
            elif (say=='o'):
            	print(o)
            elif (say=='p'):
            	print(p)
            elif (say=='q'):
            	print(q)
            elif (say=='r'):
            	print(r)
            elif (say=='s'):
            	print(s)
            elif (say=='t'):
            	print(t)
            elif (say=='u'):
            	print(u)
            elif (say=='v'):
            	print(v)
            elif (say=='w'):
            	print(w)
            elif (say=='x'):
            	print(x)
            elif (say=='y'):
            	print(y)
            elif (say=='z'):
            	print(z)
            else:
                print(say)
    for x in xroot.findall('script'):
        if x.find('ask'+sti) is None:
            dothis = 2
        else:
            ask = x.find('ask'+sti).text
            answer = input(ask)
    for x in xroot.findall('script'):
        if x.find('a'+sti) is None:
            dothis = 3
        else:
            avar = x.find('a'+sti).text
            if (avar=='a'):
           	    a = a
            elif (avar=='b'):
           	    a = b
            elif (avar=='c'):
                a = c
            elif (avar=='d'):
           	    a = d
            elif (avar=='e'):
            	a = e
            elif (avar=='f'):
            	a = f
            elif (avar=='g'):
                a = g
            elif (avar=='h'):
            	a = h
            elif (avar=='i'):
            	a = i
            elif (avar=='j'):
           	    a = j
            elif (avar=='k'):
            	a = k
            elif (avar=='l'):
            	a = l
            elif (avar=='m'):
           	    a = m
            elif (avar=='n'):
            	a = n
            elif (avar=='o'):
            	a = o
            elif (avar=='p'):
           	    a = p
            elif (avar=='q'):
           	    a = q
            elif (avar=='r'):
           	    a = r
            elif (avar=='s'):
           	    a = s
            elif (avar=='t'):
                a = t
            elif (avar=='u'):
                a = u
            elif (avar=='v'):
                a = v
            elif (avar=='w'):
          	    a = w
            #elif (avar=='x'):
                #a = x
            elif (avar=='y'):
           	    a = y
            elif (avar=='z'):
           	    a = z
            elif (avar=='answer'):
                a = answer
            else:
                a = avar
    for x in xroot.findall('script'):
        if x.find('b'+sti) is None:
            dothis = 4
        else:
            bvar = x.find('b'+sti).text
            if (bvar=='a'):
           	    b = a
            elif (bvar=='b'):
           	    b = b
            elif (bvar=='c'):
                b = c
            elif (bvar=='d'):
           	    b = d
            elif (bvar=='e'):
            	b = e
            elif (bvar=='f'):
            	b = f
            elif (bvar=='g'):
                b = g
            elif (bvar=='h'):
            	b = h
            elif (bvar=='i'):
            	b = i
            elif (bvar=='j'):
           	    b = j
            elif (bvar=='k'):
            	b = k
            elif (bvar=='l'):
            	b = l
            elif (bvar=='m'):
           	    b = m
            elif (bvar=='n'):
            	b = n
            elif (bvar=='o'):
            	b = o
            elif (bvar=='p'):
           	    b = p
            elif (bvar=='q'):
           	    b = q
            elif (bvar=='r'):
           	    b = r
            elif (bvar=='s'):
           	    b = s
            elif (bvar=='t'):
                b = t
            elif (bvar=='u'):
                b = u
            elif (bvar=='v'):
                b = v
            elif (bvar=='w'):
          	    b = w
            #elif (bvar=='x'):
                #b = x
            elif (bvar=='y'):
           	    b = y
            elif (bvar=='z'):
           	    b = z
            elif (bvar=='answer'):
                b = answer
            else:
                b = bvar
    for x in xroot.findall('script'):
        if x.find('c'+sti) is None:
            dothis = 3
        else:
            cvar = x.find('c'+sti).text
            if (cvar=='a'):
           	    c = a
            elif (cvar=='b'):
           	    c = b
            elif (cvar=='c'):
                c = c
            elif (cvar=='d'):
           	    c = d
            elif (cvar=='e'):
            	c = e
            elif (cvar=='f'):
            	c = f
            elif (cvar=='g'):
                c = g
            elif (cvar=='h'):
            	c = h
            elif (cvar=='i'):
            	c = i
            elif (cvar=='j'):
           	    c = j
            elif (cvar=='k'):
            	c = k
            elif (cvar=='l'):
            	c = l
            elif (cvar=='m'):
           	    c = m
            elif (cvar=='n'):
            	c = n
            elif (cvar=='o'):
            	c = o
            elif (cvar=='p'):
           	    c = p
            elif (cvar=='q'):
           	    c = q
            elif (cvar=='r'):
           	    c = r
            elif (cvar=='s'):
           	    c = s
            elif (cvar=='t'):
                c = t
            elif (cvar=='u'):
                c = u
            elif (cvar=='v'):
                c = v
            elif (cvar=='w'):
          	    c = w
            #elif (cvar=='x'):
                #c = x
            elif (cvar=='y'):
           	    c = y
            elif (cvar=='z'):
           	    c = z
            elif (cvar=='answer'):
                c = answer
            else:
                c = cvar
    for x in xroot.findall('script'):
        if x.find('d'+sti) is None:
            dothis = 4
        else:
            dvar = x.find('d'+sti).text
            if (dvar=='a'):
           	    d = a
            elif (dvar=='b'):
           	    d = b
            elif (dvar=='c'):
                d = c
            elif (dvar=='d'):
           	    d = d
            elif (dvar=='e'):
            	d = e
            elif (dvar=='f'):
            	d = f
            elif (dvar=='g'):
                d = g
            elif (dvar=='h'):
            	d = h
            elif (dvar=='i'):
            	d = i
            elif (dvar=='j'):
           	    d = j
            elif (dvar=='k'):
            	d = k
            elif (dvar=='l'):
            	d = l
            elif (dvar=='m'):
           	    d = m
            elif (dvar=='n'):
            	d = n
            elif (dvar=='o'):
            	d = o
            elif (dvar=='p'):
           	    d = p
            elif (dvar=='q'):
           	    d = q
            elif (dvar=='r'):
           	    d = r
            elif (dvar=='s'):
           	    d = s
            elif (dvar=='t'):
                d = t
            elif (dvar=='u'):
                d = u
            elif (dvar=='v'):
                d = v
            elif (dvar=='w'):
          	    d = w
            #elif (dvar=='x'):
                #d = x
            elif (dvar=='y'):
           	    d = y
            elif (dvar=='z'):
           	    d = z
            elif (dvar=='answer'):
                d = answer
            else:
                d = dvar
    for x in xroot.findall('script'):
        if x.find('e'+sti) is None:
            dothis = 3
        else:
            evar = x.find('e'+sti).text
            if (evar=='a'):
           	    e = a
            elif (evar=='b'):
           	    e = b
            elif (evar=='c'):
                e = c
            elif (evar=='d'):
           	    e = d
            elif (evar=='e'):
            	e = e
            elif (evar=='f'):
            	e = f
            elif (evar=='g'):
                e = g
            elif (evar=='h'):
            	e = h
            elif (evar=='i'):
            	e = i
            elif (evar=='j'):
           	    e = j
            elif (evar=='k'):
            	e = k
            elif (evar=='l'):
            	e = l
            elif (evar=='m'):
           	    e = m
            elif (evar=='n'):
            	e = n
            elif (evar=='o'):
            	e = o
            elif (evar=='p'):
           	    e = p
            elif (evar=='q'):
           	    e = q
            elif (evar=='r'):
           	    e = r
            elif (evar=='s'):
           	    e = s
            elif (evar=='t'):
                e = t
            elif (evar=='u'):
                e = u
            elif (evar=='v'):
                e = v
            elif (evar=='w'):
          	    e = w
            #elif (evar=='x'):
                #e = x
            elif (evar=='y'):
           	    e = y
            elif (evar=='z'):
           	    e = z
            elif (evar=='answer'):
                e = answer
            else:
                e = evar
    for x in xroot.findall('script'):
        if x.find('f'+sti) is None:
            dothis = 4
        else:
            fvar = x.find('f'+sti).text
            if (fvar=='a'):
           	    f = a
            elif (fvar=='b'):
           	    f = b
            elif (fvar=='c'):
                f = c
            elif (fvar=='d'):
           	    f = d
            elif (fvar=='e'):
            	f = e
            elif (fvar=='f'):
            	f = f
            elif (fvar=='g'):
                f = g
            elif (fvar=='h'):
            	f = h
            elif (fvar=='i'):
            	f = i
            elif (fvar=='j'):
           	    f = j
            elif (fvar=='k'):
            	f = k
            elif (fvar=='l'):
            	f = l
            elif (fvar=='m'):
           	    f = m
            elif (fvar=='n'):
            	f = n
            elif (fvar=='o'):
            	f = o
            elif (fvar=='p'):
           	    f = p
            elif (fvar=='q'):
           	    f = q
            elif (fvar=='r'):
           	    f = r
            elif (fvar=='s'):
           	    f = s
            elif (fvar=='t'):
                f = t
            elif (fvar=='u'):
                f = u
            elif (fvar=='v'):
                f = v
            elif (fvar=='w'):
          	    f = w
            #elif (fvar=='x'):
                #f = x
            elif (fvar=='y'):
           	    f = y
            elif (fvar=='z'):
           	    f = z
            elif (fvar=='answer'):
                f = answer
            else:
                f = fvar
    for x in xroot.findall('script'):
        if x.find('g'+sti) is None:
            dothis = 3
        else:
            gvar = x.find('g'+sti).text
            if (gvar=='a'):
           	    g = a
            elif (gvar=='b'):
           	    g = b
            elif (gvar=='c'):
                g = c
            elif (gvar=='d'):
           	    g = d
            elif (gvar=='e'):
            	g = e
            elif (gvar=='f'):
            	g = f
            elif (gvar=='g'):
                g = g
            elif (gvar=='h'):
            	g = h
            elif (gvar=='i'):
            	g = i
            elif (gvar=='j'):
           	    g = j
            elif (gvar=='k'):
            	g = k
            elif (gvar=='l'):
            	g = l
            elif (gvar=='m'):
           	    g = m
            elif (gvar=='n'):
            	g = n
            elif (gvar=='o'):
            	g = o
            elif (gvar=='p'):
           	    g = p
            elif (gvar=='q'):
           	    g = q
            elif (gvar=='r'):
           	    g = r
            elif (gvar=='s'):
           	    g = s
            elif (gvar=='t'):
                g = t
            elif (gvar=='u'):
                g = u
            elif (gvar=='v'):
                g = v
            elif (gvar=='w'):
          	    g = w
            #elif (gvar=='x'):
                #g = x
            elif (gvar=='y'):
           	    g = y
            elif (gvar=='z'):
           	    g = z
            elif (gvar=='answer'):
                g = answer
            else:
                g = gvar
    for x in xroot.findall('script'):
        if x.find('h'+sti) is None:
            dothis = 4
        else:
            hvar = x.find('h'+sti).text
            if (hvar=='a'):
           	    h = a
            elif (hvar=='b'):
           	    h = b
            elif (hvar=='c'):
                h = c
            elif (hvar=='d'):
           	    h = d
            elif (hvar=='e'):
            	h = e
            elif (hvar=='f'):
            	h = f
            elif (hvar=='g'):
                h = g
            elif (hvar=='h'):
            	h = h
            elif (hvar=='i'):
            	h = i
            elif (hvar=='j'):
           	    h = j
            elif (hvar=='k'):
            	h = k
            elif (hvar=='l'):
            	h = l
            elif (hvar=='m'):
           	    h = m
            elif (hvar=='n'):
            	h = n
            elif (hvar=='o'):
            	h = o
            elif (hvar=='p'):
           	    h = p
            elif (hvar=='q'):
           	    h = q
            elif (hvar=='r'):
           	    h = r
            elif (hvar=='s'):
           	    h = s
            elif (hvar=='t'):
                h = t
            elif (hvar=='u'):
                h = u
            elif (hvar=='v'):
                h = v
            elif (hvar=='w'):
          	    h = w
            #elif (hvar=='x'):
                #h = x
            elif (hvar=='y'):
           	    h = y
            elif (hvar=='z'):
           	    h = z
            elif (hvar=='answer'):
                h = answer
            else:
                h = hvar
    for x in xroot.findall('script'):
        if x.find('i'+sti) is None:
            dothis = 3
        else:
            ivar = x.find('i'+sti).text
            if (ivar=='a'):
           	    i = a
            elif (ivar=='b'):
           	    i = b
            elif (ivar=='c'):
                i = c
            elif (ivar=='d'):
           	    i = d
            elif (ivar=='e'):
            	i = e
            elif (ivar=='f'):
            	i = f
            elif (ivar=='g'):
                i = g
            elif (ivar=='h'):
            	i = h
            elif (ivar=='i'):
            	i = i
            elif (ivar=='j'):
           	    i = j
            elif (ivar=='k'):
            	i = k
            elif (ivar=='l'):
            	i = l
            elif (ivar=='m'):
           	    i = m
            elif (ivar=='n'):
            	i = n
            elif (ivar=='o'):
            	i = o
            elif (ivar=='p'):
           	    i = p
            elif (ivar=='q'):
           	    i = q
            elif (ivar=='r'):
           	    i = r
            elif (ivar=='s'):
           	    i = s
            elif (ivar=='t'):
                i = t
            elif (ivar=='u'):
                i = u
            elif (ivar=='v'):
                i = v
            elif (ivar=='w'):
          	    i = w
            #elif (ivar=='x'):
                #i = x
            elif (ivar=='y'):
           	    i = y
            elif (ivar=='z'):
           	    i = z
            elif (ivar=='answer'):
                i = answer
            else:
                i = ivar
    for x in xroot.findall('script'):
        if x.find('j'+sti) is None:
            dothis = 4
        else:
            jvar = x.find('j'+sti).text
            if (jvar=='a'):
           	    j = a
            elif (jvar=='b'):
           	    j = b
            elif (jvar=='c'):
                j = c
            elif (jvar=='d'):
           	    j = d
            elif (jvar=='e'):
            	j = e
            elif (jvar=='f'):
            	j = f
            elif (jvar=='g'):
                j = g
            elif (jvar=='h'):
            	j = h
            elif (jvar=='i'):
            	j = i
            elif (jvar=='j'):
           	    j = j
            elif (jvar=='k'):
            	j = k
            elif (jvar=='l'):
            	j = l
            elif (jvar=='m'):
           	    j = m
            elif (jvar=='n'):
            	j = n
            elif (jvar=='o'):
            	j = o
            elif (jvar=='p'):
           	    j = p
            elif (jvar=='q'):
           	    j = q
            elif (jvar=='r'):
           	    j = r
            elif (jvar=='s'):
           	    j = s
            elif (jvar=='t'):
                j = t
            elif (jvar=='u'):
                j = u
            elif (jvar=='v'):
                j = v
            elif (jvar=='w'):
          	    j = w
            #elif (jvar=='x'):
                #j = x
            elif (jvar=='y'):
           	    j = y
            elif (jvar=='z'):
           	    j = z
            elif (jvar=='answer'):
                j = answer
            else:
                j = jvar
    for x in xroot.findall('script'):
        if x.find('k'+sti) is None:
            dothis = 3
        else:
            kvar = x.find('k'+sti).text
            if (kvar=='a'):
           	    k = a
            elif (kvar=='b'):
           	    k = b
            elif (kvar=='c'):
                k = c
            elif (kvar=='d'):
           	    k = d
            elif (kvar=='e'):
            	k = e
            elif (kvar=='f'):
            	k = f
            elif (kvar=='g'):
                k = g
            elif (kvar=='h'):
            	k = h
            elif (kvar=='i'):
            	k = i
            elif (kvar=='j'):
           	    k = j
            elif (kvar=='k'):
            	k = k
            elif (kvar=='l'):
            	k = l
            elif (kvar=='m'):
           	    k = m
            elif (kvar=='n'):
            	k = n
            elif (kvar=='o'):
            	k = o
            elif (kvar=='p'):
           	    k = p
            elif (kvar=='q'):
           	    k = q
            elif (kvar=='r'):
           	    k = r
            elif (kvar=='s'):
           	    k = s
            elif (kvar=='t'):
                k = t
            elif (kvar=='u'):
                k = u
            elif (kvar=='v'):
                k = v
            elif (kvar=='w'):
          	    k = w
            #elif (kvar=='x'):
                #k = x
            elif (kvar=='y'):
           	    k = y
            elif (kvar=='z'):
           	    k = z
            elif (kvar=='answer'):
                k = answer
            else:
                k = kvar
    for x in xroot.findall('script'):
        if x.find('l'+sti) is None:
            dothis = 4
        else:
            lvar = l.find('l'+sti).text
            if (lvar=='a'):
           	    l = a
            elif (lvar=='b'):
           	    l = b
            elif (lvar=='c'):
                l = c
            elif (lvar=='d'):
           	    l = d
            elif (lvar=='e'):
            	l = e
            elif (lvar=='f'):
            	l = f
            elif (lvar=='g'):
                l = g
            elif (lvar=='h'):
            	l = h
            elif (lvar=='i'):
            	l = i
            elif (lvar=='j'):
           	    l = j
            elif (lvar=='k'):
            	l = k
            elif (lvar=='l'):
            	l = l
            elif (lvar=='m'):
           	    l = m
            elif (lvar=='n'):
            	l = n
            elif (lvar=='o'):
            	l = o
            elif (lvar=='p'):
           	    l = p
            elif (lvar=='q'):
           	    l = q
            elif (lvar=='r'):
           	    l = r
            elif (lvar=='s'):
           	    l = s
            elif (lvar=='t'):
                l = t
            elif (lvar=='u'):
                l = u
            elif (lvar=='v'):
                l = v
            elif (lvar=='w'):
          	    l = w
            #elif (lvar=='x'):
                #l = x
            elif (lvar=='y'):
           	    l = y
            elif (lvar=='z'):
           	    l = z
            elif (lvar=='answer'):
                l = answer
            else:
                l = lvar
    for x in xroot.findall('script'):
        if x.find('m'+sti) is None:
            dothis = 3
        else:
            mvar = x.find('m'+sti).text
            if (mvar=='a'):
           	    m = a
            elif (mvar=='b'):
           	    m = b
            elif (mvar=='c'):
                m = c
            elif (mvar=='d'):
           	    m = d
            elif (mvar=='e'):
            	m = e
            elif (mvar=='f'):
            	m = f
            elif (mvar=='g'):
                m = g
            elif (mvar=='h'):
            	m = h
            elif (mvar=='i'):
            	m = i
            elif (mvar=='j'):
           	    m = j
            elif (mvar=='k'):
            	m = k
            elif (mvar=='l'):
            	m = l
            elif (mvar=='m'):
           	    m = m
            elif (mvar=='n'):
            	m = n
            elif (mvar=='o'):
            	m = o
            elif (mvar=='p'):
           	    m = p
            elif (mvar=='q'):
           	    m = q
            elif (mvar=='r'):
           	    m = r
            elif (mvar=='s'):
           	    m = s
            elif (mvar=='t'):
                m = t
            elif (mvar=='u'):
                m = u
            elif (mvar=='v'):
                m = v
            elif (mvar=='w'):
          	    m = w
            #elif (mvar=='x'):
                #m = x
            elif (mvar=='y'):
           	    m = y
            elif (mvar=='z'):
           	    m = z
            elif (mvar=='answer'):
                m = answer
            else:
                m = mvar
    for x in xroot.findall('script'):
        if x.find('n'+sti) is None:
            dothis = 4
        else:
            nvar = x.find('n'+sti).text
            if (nvar=='a'):
           	    n = a
            elif (nvar=='b'):
           	    n = b
            elif (nvar=='c'):
                n = c
            elif (nvar=='d'):
           	    n = d
            elif (nvar=='e'):
            	n = e
            elif (nvar=='f'):
            	n = f
            elif (nvar=='g'):
                n = g
            elif (nvar=='h'):
            	n = h
            elif (nvar=='i'):
            	n = i
            elif (nvar=='j'):
           	    n = j
            elif (nvar=='k'):
            	n = k
            elif (nvar=='l'):
            	n = l
            elif (nvar=='m'):
           	    n = m
            elif (nvar=='n'):
            	n = n
            elif (nvar=='o'):
            	n = o
            elif (nvar=='p'):
           	    n = p
            elif (nvar=='q'):
           	    n = q
            elif (nvar=='r'):
           	    n = r
            elif (nvar=='s'):
           	    n = s
            elif (nvar=='t'):
                n = t
            elif (nvar=='u'):
                n = u
            elif (nvar=='v'):
                n = v
            elif (nvar=='w'):
          	    n = w
            #elif (nvar=='x'):
                #n = x
            elif (nvar=='y'):
           	    n = y
            elif (nvar=='z'):
           	    n = z
            elif (nvar=='answer'):
                n = answer
            else:
                n = nvar
    for x in xroot.findall('script'):
        if x.find('o'+sti) is None:
            dothis = 3
        else:
            ovar = x.find('o'+sti).text
            if (ovar=='a'):
           	    o = a
            elif (ovar=='b'):
           	    o = b
            elif (ovar=='c'):
                o = c
            elif (ovar=='d'):
           	    o = d
            elif (ovar=='e'):
            	o = e
            elif (ovar=='f'):
            	o = f
            elif (ovar=='g'):
                o = g
            elif (ovar=='h'):
            	o = h
            elif (ovar=='i'):
            	o = i
            elif (ovar=='j'):
           	    o = j
            elif (ovar=='k'):
            	o = k
            elif (ovar=='l'):
            	o = l
            elif (ovar=='m'):
           	    o = m
            elif (ovar=='n'):
            	o = n
            elif (ovar=='o'):
            	o = o
            elif (ovar=='p'):
           	    o = p
            elif (ovar=='q'):
           	    o = q
            elif (ovar=='r'):
           	    o = r
            elif (ovar=='s'):
           	    o = s
            elif (ovar=='t'):
                o = t
            elif (ovar=='u'):
                o = u
            elif (ovar=='v'):
                o = v
            elif (ovar=='w'):
          	    o = w
            #elif (ovar=='x'):
                #o = x
            elif (ovar=='y'):
           	    o = y
            elif (ovar=='z'):
           	    o = z
            elif (ovar=='answer'):
                o = answer
            else:
                o = ovar
    for x in xroot.findall('script'):
        if x.find('p'+sti) is None:
            dothis = 4
        else:
            pvar = x.find('p'+sti).text
            if (pvar=='a'):
           	    p = a
            elif (pvar=='b'):
           	    p = b
            elif (pvar=='c'):
                p = c
            elif (pvar=='d'):
           	    p = d
            elif (pvar=='e'):
            	p = e
            elif (pvar=='f'):
            	p = f
            elif (pvar=='g'):
                p = g
            elif (pvar=='h'):
            	p = h
            elif (pvar=='i'):
            	p = i
            elif (pvar=='j'):
           	    p = j
            elif (pvar=='k'):
            	p = k
            elif (pvar=='l'):
            	p = l
            elif (pvar=='m'):
           	    p = m
            elif (pvar=='n'):
            	p = n
            elif (pvar=='o'):
            	p = o
            elif (pvar=='p'):
           	    p = p
            elif (pvar=='q'):
           	    p = q
            elif (pvar=='r'):
           	    p = r
            elif (pvar=='s'):
           	    p = s
            elif (pvar=='t'):
                p = t
            elif (pvar=='u'):
                p = u
            elif (pvar=='v'):
                p = v
            elif (pvar=='w'):
          	    p = w
            #elif (pvar=='x'):
                #p = x
            elif (pvar=='y'):
           	    p = y
            elif (pvar=='z'):
           	    p = z
            elif (pvar=='answer'):
                p = answer
            else:
                p = pvar
    for x in xroot.findall('script'):
        if x.find('q'+sti) is None:
            dothis = 3
        else:
            qvar = x.find('q'+sti).text
            if (qvar=='a'):
           	    q = a
            elif (qvar=='b'):
           	    q = b
            elif (qvar=='c'):
                q = c
            elif (qvar=='d'):
           	    q = d
            elif (qvar=='e'):
            	q = e
            elif (qvar=='f'):
            	q = f
            elif (qvar=='g'):
                q = g
            elif (qvar=='h'):
            	q = h
            elif (qvar=='i'):
            	q = i
            elif (qvar=='j'):
           	    q = j
            elif (qvar=='k'):
            	q = k
            elif (qvar=='l'):
            	q = l
            elif (qvar=='m'):
           	    q = m
            elif (qvar=='n'):
            	q = n
            elif (qvar=='o'):
            	q = o
            elif (qvar=='p'):
           	    q = p
            elif (qvar=='q'):
           	    q = q
            elif (qvar=='r'):
           	    q = r
            elif (qvar=='s'):
           	    q = s
            elif (qvar=='t'):
                q = t
            elif (qvar=='u'):
                q = u
            elif (qvar=='v'):
                q = v
            elif (qvar=='w'):
          	    q = w
            #elif (qvar=='x'):
                #q = x
            elif (qvar=='y'):
           	    q = y
            elif (qvar=='z'):
           	    q = z
            elif (qvar=='answer'):
                q = answer
            else:
                q = qvar
    for x in xroot.findall('script'):
        if x.find('r'+sti) is None:
            dothis = 4
        else:
            rvar = x.find('r'+sti).text
            if (rvar=='a'):
           	    r = a
            elif (rvar=='b'):
           	    r = b
            elif (rvar=='c'):
                r = c
            elif (rvar=='d'):
           	    r = d
            elif (rvar=='e'):
            	r = e
            elif (rvar=='f'):
            	r = f
            elif (rvar=='g'):
                r = g
            elif (rvar=='h'):
            	r = h
            elif (rvar=='i'):
            	r = i
            elif (rvar=='j'):
           	    r = j
            elif (rvar=='k'):
            	r = k
            elif (rvar=='l'):
            	r = l
            elif (rvar=='m'):
           	    r = m
            elif (rvar=='n'):
            	r = n
            elif (rvar=='o'):
            	r = o
            elif (rvar=='p'):
           	    r = p
            elif (rvar=='q'):
           	    r = q
            elif (rvar=='r'):
           	    r = r
            elif (rvar=='s'):
           	    r = s
            elif (rvar=='t'):
                r = t
            elif (rvar=='u'):
                r = u
            elif (rvar=='v'):
                r = v
            elif (rvar=='w'):
          	    r = w
            #elif (rvar=='x'):
                #r = x
            elif (rvar=='y'):
           	    r = y
            elif (rvar=='z'):
           	    r = z
            elif (rvar=='answer'):
                r = answer
            else:
                r = rvar
    for x in xroot.findall('script'):
        if x.find('s'+sti) is None:
            dothis = 3
        else:
            svar = x.find('s'+sti).text
            if (svar=='a'):
           	    s = a
            elif (svar=='b'):
           	    s = b
            elif (svar=='c'):
                s = c
            elif (svar=='d'):
           	    s = d
            elif (svar=='e'):
            	s = e
            elif (svar=='f'):
            	s = f
            elif (svar=='g'):
                s = g
            elif (svar=='h'):
            	s = h
            elif (svar=='i'):
            	s = i
            elif (svar=='j'):
           	    s = j
            elif (svar=='k'):
            	s = k
            elif (svar=='l'):
            	s = l
            elif (svar=='m'):
           	    s = m
            elif (svar=='n'):
            	s = n
            elif (svar=='o'):
            	s = o
            elif (svar=='p'):
           	    s = p
            elif (svar=='q'):
           	    s = q
            elif (svar=='r'):
           	    s = r
            elif (svar=='s'):
           	    s = s
            elif (svar=='t'):
                s = t
            elif (svar=='u'):
                s = u
            elif (svar=='v'):
                s = v
            elif (svar=='w'):
          	    s = w
            #elif (svar=='x'):
                #s = x
            elif (svar=='y'):
           	    s = y
            elif (svar=='z'):
           	    s = z
            elif (svar=='answer'):
                s = answer
            else:
                s = svar
    for x in xroot.findall('script'):
        if x.find('t'+sti) is None:
            dothis = 4
        else:
            tvar = x.find('t'+sti).text
            if (tvar=='a'):
           	    t = a
            elif (tvar=='b'):
           	    t = b
            elif (tvar=='c'):
                t = c
            elif (tvar=='d'):
           	    t = d
            elif (tvar=='e'):
            	t = e
            elif (tvar=='f'):
            	t = f
            elif (tvar=='g'):
                t = g
            elif (tvar=='h'):
            	t = h
            elif (tvar=='i'):
            	t = i
            elif (tvar=='j'):
           	    t = j
            elif (tvar=='k'):
            	t = k
            elif (tvar=='l'):
            	t = l
            elif (tvar=='m'):
           	    t = m
            elif (tvar=='n'):
            	t = n
            elif (tvar=='o'):
            	t = o
            elif (tvar=='p'):
           	    t = p
            elif (tvar=='q'):
           	    t = q
            elif (tvar=='r'):
           	    t = r
            elif (tvar=='s'):
           	    t = s
            elif (tvar=='t'):
                t = t
            elif (tvar=='u'):
                t = u
            elif (tvar=='v'):
                t = v
            elif (tvar=='w'):
          	    t = w
            #elif (tvar=='x'):
                #t = x
            elif (tvar=='y'):
           	    t = y
            elif (tvar=='z'):
           	    t = z
            elif (tvar=='answer'):
                t = answer
            else:
                t = tvar
    for x in xroot.findall('script'):
        if x.find('u'+sti) is None:
            dothis = 3
        else:
            uvar = x.find('u'+sti).text
            if (uvar=='a'):
           	    u = a
            elif (uvar=='b'):
           	    u = b
            elif (uvar=='c'):
                u = c
            elif (uvar=='d'):
           	    u = d
            elif (uvar=='e'):
            	u = e
            elif (uvar=='f'):
            	u = f
            elif (uvar=='g'):
                u = g
            elif (uvar=='h'):
            	u = h
            elif (uvar=='i'):
            	u = i
            elif (uvar=='j'):
           	    u = j
            elif (uvar=='k'):
            	u = k
            elif (uvar=='l'):
            	u = l
            elif (uvar=='m'):
           	    u = m
            elif (uvar=='n'):
            	u = n
            elif (uvar=='o'):
            	u = o
            elif (uvar=='p'):
           	    u = p
            elif (uvar=='q'):
           	    u = q
            elif (uvar=='r'):
           	    u = r
            elif (uvar=='s'):
           	    u = s
            elif (uvar=='t'):
                u = t
            elif (uvar=='u'):
                u = u
            elif (uvar=='v'):
                u = v
            elif (uvar=='w'):
          	    u = w
            #elif (uvar=='x'):
                #u = x
            elif (uvar=='y'):
           	    u = y
            elif (uvar=='z'):
           	    u = z
            elif (uvar=='answer'):
                u = answer
            else:
                u = uvar
    for x in xroot.findall('script'):
        if x.find('v'+sti) is None:
            dothis = 4
        else:
            vvar = x.find('v'+sti).text
            if (vvar=='a'):
           	    v = a
            elif (vvar=='b'):
           	    v = b
            elif (vvar=='c'):
                v = c
            elif (vvar=='d'):
           	    v = d
            elif (vvar=='e'):
            	v = e
            elif (vvar=='f'):
            	v = f
            elif (vvar=='g'):
                v = g
            elif (vvar=='h'):
            	v = h
            elif (vvar=='i'):
            	v = i
            elif (vvar=='j'):
           	    v = j
            elif (vvar=='k'):
            	v = k
            elif (vvar=='l'):
            	v = l
            elif (vvar=='m'):
           	    v = m
            elif (vvar=='n'):
            	v = n
            elif (vvar=='o'):
            	v = o
            elif (vvar=='p'):
           	    v = p
            elif (vvar=='q'):
           	    v = q
            elif (vvar=='r'):
           	    v = r
            elif (vvar=='s'):
           	    v = s
            elif (vvar=='t'):
                v = t
            elif (vvar=='u'):
                v = u
            elif (vvar=='v'):
                v = v
            elif (vvar=='w'):
          	    v = w
            #elif (vvar=='x'):
                #v = x
            elif (vvar=='y'):
           	    v = y
            elif (vvar=='z'):
           	    v = z
            elif (vvar=='answer'):
                v = answer
            else:
                v = vvar
    for x in xroot.findall('script'):
        if x.find('w'+sti) is None:
            dothis = 3
        else:
            wvar = x.find('w'+sti).text
            if (wvar=='a'):
           	    w = a
            elif (wvar=='b'):
           	    w = b
            elif (wvar=='c'):
                w = c
            elif (wvar=='d'):
           	    w = d
            elif (wvar=='e'):
            	w = e
            elif (wvar=='f'):
            	w = f
            elif (wvar=='g'):
                w = g
            elif (wvar=='h'):
            	w = h
            elif (wvar=='i'):
            	w = i
            elif (wvar=='j'):
           	    w = j
            elif (wvar=='k'):
            	w = k
            elif (wvar=='l'):
            	w = l
            elif (wvar=='m'):
           	    w = m
            elif (wvar=='n'):
            	w = n
            elif (wvar=='o'):
            	w = o
            elif (wvar=='p'):
           	    w = p
            elif (wvar=='q'):
           	    w = q
            elif (wvar=='r'):
           	    w = r
            elif (wvar=='s'):
           	    w = s
            elif (wvar=='t'):
                w = t
            elif (wvar=='u'):
                w = u
            elif (wvar=='v'):
                w = v
            elif (wvar=='w'):
          	    w = w
            #elif (wvar=='x'):
                #w = x
            elif (wvar=='y'):
           	    w = y
            elif (wvar=='z'):
           	    w = z
            elif (wvar=='answer'):
                w = answer
            else:
                w = wvar
    #for i in xroot.findall('script'):
     #   if i.find('x'+sti) is None:
      #      dothis = 4
       # else:
        #    xvar = i.find('x'+sti).text
         #   elif (xvar=='a'):
#           	    x = a
 #           elif (xvar=='b'):
  #         	    x = b
   #         elif (xvar=='c'):
    #            x = c
     #       elif (xvar=='d'):
      #     	    x = d
       #     elif (xvar=='e'):
        #    	x = e
         #   elif (xvar=='f'):
          #  	x = f
           # elif (xvar=='g'):
           #     x = g
          #  elif (xvar=='h'):
         #   	x = h
        #    elif (xvar=='i'):
         #   	x = i
          #  elif (xvar=='j'):
#           	    x = j
 #           elif (xvar=='k'):
  #          	x = k
   #         elif (xvar=='l'):
    #        	x = l
     #       elif (xvar=='m'):
      #     	    x = m
       #     elif (xvar=='n'):
        #    	x = n
         #   elif (xvar=='o'):
          #  	x = o
           # elif (xvar=='p'):
           	#    x = p
#            elif (xvar=='q'):
 #          	    x = q
  #          elif (xvar=='r'):
   #        	    x = r
    #        elif (xvar=='s'):
     #      	    x = s
      #      elif (xvar=='t'):
       #         x = t
        #    elif (xvar=='u'):
         #       x = u
          #  elif (xvar=='v'):
           #     x = v
            #elif (xvar=='w'):
          	 #   x = w
            #elif (xvar=='x'):
                #x = x
#            elif (xvar=='y'):
 #          	    x = y
  #          elif (xvar=='z'):
   #        	    x = z
    #        elif (xvar=='answer'):
     #           x = answer
	  #	     else:
	   #	     x = xvar
    for x in xroot.findall('script'):
        if x.find('y'+sti) is None:
            dothis = 3
        else:
            yvar = x.find('y'+sti).text
            if (yvar=='a'):
           	    y = a
            elif (yvar=='b'):
           	    y = b
            elif (yvar=='c'):
                y = c
            elif (yvar=='d'):
           	    y = d
            elif (yvar=='e'):
            	y = e
            elif (yvar=='f'):
            	y = f
            elif (yvar=='g'):
                y = g
            elif (yvar=='h'):
            	y = h
            elif (yvar=='i'):
            	y = i
            elif (yvar=='j'):
           	    y = j
            elif (yvar=='k'):
            	y = k
            elif (yvar=='l'):
            	y = l
            elif (yvar=='m'):
           	    y = m
            elif (yvar=='n'):
            	y = n
            elif (yvar=='o'):
            	y = o
            elif (yvar=='p'):
                y = p
            elif (yvar=='q'):
                y = q
            elif (yvar=='r'):
                y = r
            elif (yvar=='s'):
                y = s
            elif (yvar=='t'):
                y = t
            elif (yvar=='u'):
                y = u
            elif (yvar=='v'):
                y = v
            elif (yvar=='w'):
          	    y = w
            #elif (yvar=='x'):
                #y = x
            elif (yvar=='y'):
           	    y = y
            elif (yvar=='z'):
           	    y = z
            elif (yvar=='answer'):
                y = answer
            else:
                y = yvar
    for x in xroot.findall('script'):
        if x.find('z'+sti) is None:
            dothis = 4
        else:
            zvar = x.find('z'+sti).text
            if (zvar=='a'):
           	    z = a
            elif (zvar=='b'):
           	    z = b
            elif (zvar=='c'):
                z = c
            elif (zvar=='d'):
           	    z = d
            elif (zvar=='e'):
            	z = e
            elif (zvar=='f'):
            	z = f
            elif (zvar=='g'):
                z = g
            elif (zvar=='h'):
            	z = h
            elif (zvar=='i'):
            	z = i
            elif (zvar=='j'):
           	    z = j
            elif (zvar=='k'):
            	z = k
            elif (zvar=='l'):
            	z = l
            elif (zvar=='m'):
           	    z = m
            elif (zvar=='n'):
            	z = n
            elif (zvar=='o'):
            	z = o
            elif (zvar=='p'):
           	    z = p
            elif (zvar=='q'):
           	    z = q
            elif (zvar=='r'):
           	    z = r
            elif (zvar=='s'):
           	    z = s
            elif (zvar=='t'):
                z = t
            elif (zvar=='u'):
                z = u
            elif (zvar=='v'):
                z = v
            elif (zvar=='w'):
                z = w
            #elif (zvar=='x'):
                #z = x
            elif (zvar=='y'):
           	    z = y
            elif (zvar=='z'):
           	    z = z
            elif (zvar=='answer'):
                z = answer
            else:
                z = zvar
        for x in xroot.findall('script'):
            if x.find('mathsa'+sti) is None:
                dothis = 2
            else:
                mathsa = x.find('mathsa'+sti).text
        for x in xroot.findall('script'):
            if x.find('op'+sti) is None:
                dothis = 2
            else:
                op = x.find('op'+sti).text
        for x in xroot.findall('script'):
            if x.find('mathsb'+sti) is None:
                dothis = 2
            else:
                mathsb = x.find('mathsb'+sti).text
            if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
                if int(mathsa) is None:
                    dothis = 0
                else:
                    if int(mathsb) is None:
                        dothis = 9
                    else:
                        maths(int(mathsa), op, int(mathsb))
    num += 1
    sti = str(num)
