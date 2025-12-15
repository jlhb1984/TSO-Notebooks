import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

pi=math.pi
an=[]
bn=[]
serie_f=[]
#T=float(input("Type T value: "))
T=255
w=(2*pi)/T

a0=1/T
n=1
print(np.cos(pi))
for i in range(0,5):
    an.append((( 1/(n*pi))) * (math.sin((2*pi*n)/(255*255))))    
    bn.append(((1/(n*pi))) * (1-math.cos((2*pi*n)/(255*255))))
    n=n+1
    print(an[i])
    print(bn[i])

t=np.linspace(0,4096,100000)
y=(a0+an[0]*np.cos(w*t*1)+bn[0]*np.sin(w*t*1)+
      an[1]*np.cos(w*t*2)+bn[1]*np.sin(w*t*2)+
      an[2]*np.cos(w*t*3)+bn[2]*np.sin(w*t*3)+
      an[3]*np.cos(w*t*4)+bn[3]*np.sin(w*t*4)+
      an[4]*np.cos(w*t*5)+bn[4]*np.sin(w*t*5)
      )
plt.plot(t,y)
plt.show()