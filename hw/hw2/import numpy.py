import numpy
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
def comb_1(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
x = np.arange(200,1000,1)
y=[]

for n in range(200,1000):
    sum=0
    for i in range(109):
        sum+=((108-i)**n)*comb_1(108,i)*((-1)**i)/(108**n)
    
    if(sum==0.9500752075064968):
        print(n)
    y.append(sum)
y=np.array(y)
plt.xlabel('n')
plt.ylabel('probability')
plt.title('Coupon Question Curve')
plt.plot(x,y)
plt.show()