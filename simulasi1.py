import numpy as np
import math

"Initial parameter for layer 1"
T1 = np.zeros((100,100,100))

for n in range(0,100):
    for l in range(0,100):
        T1[0,n,l] = 10

for m in range(0,100):
    for n in range(0,100):
        T1[m,n,0] = 10
        

r = np.zeros((1,100))
r[0,0] = 0;

alpha1 = 6.4*10**(-5) ## alumunium
#alpha2 = 1.1*10**(-4)
g_0 = 500
deltar = 1
deltatheta = 0.5
deltat = 0.5
k = 104.6 ### depend on alpha
r0 = 0.1
"-------------------"

"Calculation for layer 1"

#print('T layer 1 = ')

for m in range(0,99):
    for n in range(1,99):
        for l in range(1,99):
            r[0,l]=r[0,0]+(l*deltar)
            beta = ((alpha1*deltat)/(r[0,l]*deltar))
            "T1[m+1,n,l] = T1[m,n,l]+T1[m,n-1,l]+T1[m,n,l-1]+T1[m,n+1,l]+T1[m,n,l+1]"
            g=g_0*math.exp(-0.5*m)
            T1[m+1,n,l] = T1[m,n,l]+((alpha1*deltat)/(deltar**2))*(T1[m,n,l+1]-2*T1[m,n,l]+T1[m,n,l-1])+beta*(T1[m,n,l+1]-T1[m,n,l])+(alpha1*deltat/(r[0,l]*deltatheta)**2)*(T1[m,n+1,l]-2*T1[m,n,l]+T1[m,n-1,l])+(alpha1*deltat*g/k)
            

#plot the result for constant time
indekst1 = 2 #time index
indekst2 = 10
indekst3 = 30
indekst4 = 60
indekst5 = 80
indekst6 = 98


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()


z1 = np.zeros((98))
x1 = np.zeros((98))
t1 = np.zeros((98))
z2 = np.zeros((98))
z22 = np.zeros((98))
z3 = np.zeros((98))
z4 = np.zeros((98))
z5 = np.zeros((98))
z6 = np.zeros((98))

for i in range(0,98):
    x1[i] = i

    "t1[i] = i*deltat"

indekstheta = 5
indeksr = 50

for j in range(0,98):
    a = np.int(x1[j])
    z1[j] = T1[indekst1,indekstheta,a]*10
    z22[j] = T1[indekst2,indekstheta,a]
    z3[j] = T1[indekst3,indekstheta,a]
    z4[j] = T1[indekst4,indekstheta,a]
    z5[j] = T1[indekst5,indekstheta,a]
    z6[j] = T1[indekst6,indekstheta,a]



"Initial parameter for layer 2"
T2 = np.zeros((100,100,100))

for n in range(0,100):
    for l in range(0,100):
        T2[0,n,l] = 10

for m in range(0,100):
    for n in range(0,100):
        T2[m,n,0] = T1[m,n,98]
        

r = np.zeros((1,100))
r[0,0] = 10;


alpha2 = 6.4*10**(-5) ## alumunium
g = 0
deltar = 1
deltatheta = 0.5
deltat = 0.5
#k = 401 ### depend on alpha
k = 104.6
r0 = 0.1
"-------------------"

"calculation for layer 2"


for m in range(0,99):
    for n in range(1,99):
        for l in range(1,99):
            r[0,l]=r[0,0]+(l*deltar)
            beta = ((alpha2*deltat)/(r[0,l]*deltar))
            "T1[m+1,n,l] = T1[m,n,l]+T1[m,n-1,l]+T1[m,n,l-1]+T1[m,n+1,l]+T1[m,n,l+1]"
            g=0 ## layer 2 tidak ada sumber panas
            T2[m+1,n,l] = T2[m,n,l]+((alpha2*deltat)/(deltar**2))*(T2[m,n,l+1]-2*T2[m,n,l]+T2[m,n,l-1])+beta*(T2[m,n,l+1]-T2[m,n,l])+(alpha2*deltat/(r[0,l]*deltatheta)**2)*(T2[m,n+1,l]-2*T2[m,n,l]+T2[m,n-1,l])+(alpha2*deltat*g/k)
            

#plot calculation result for constant time
indekst1 = 2 #time index
indekst2 = 10
indekst3 = 30
indekst4 = 60
indekst5 = 80
indekst6 = 98


fig = plt.figure()


z1 = np.zeros((98))
x1 = np.zeros((98))
t1 = np.zeros((98))
z2 = np.zeros((98))
z22 = np.zeros((98))
z3 = np.zeros((98))
z4 = np.zeros((98))
z5 = np.zeros((98))
z6 = np.zeros((98))

for i in range(0,98):
    x1[i] = i
    #x1[i] = r0+i*deltar
    "t1[i] = i*deltat"

indekstheta = 5
indeksr = 50

for j in range(0,98):
    a = np.int(x1[j])
    z1[j] = T2[indekst1,indekstheta,a]
    z22[j] = T2[indekst2,indekstheta,a]
    z3[j] = T2[indekst3,indekstheta,a]
    z4[j] = T2[indekst4,indekstheta,a]
    z5[j] = T2[indekst5,indekstheta,a]
    z6[j] = T2[indekst6,indekstheta,a]
    "z2[j] = T1[a,indekstheta,indeksr]*10**(6)"


indekst = [2,10,20,30,60,80,98]

suhu = np.zeros((100,len(indekst)))
suhu2 = np.zeros((100,len(indekst)))

for i in range(len(indekst)):
    suhu[:,i] = T1[indekst[i],5,:]
    suhu2[:,i] = T2[indekst[i],5,:]

from pandas import DataFrame

df = DataFrame(suhu)
df2 = DataFrame(suhu2)
df.to_csv('suhut5rlayer1sumberberubah.csv')
df2.to_csv('suhut5rlayer2sumberberubah.csv')
