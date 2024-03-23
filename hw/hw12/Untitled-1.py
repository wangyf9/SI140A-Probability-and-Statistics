import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, truncnorm
##(1)
##because the process is calculated in class, so we directly use it
##c_beta=135/64, and f(Y)/c*g(Y)=(256/27)*Y(1-Y)^3
accepted_X=[]
x = np.linspace(0,1,1000)
for i in range(0,10000):
    U=np.random.uniform(0,1)
    Y=np.random.uniform(0,1)
    FY=(256*Y*(1-Y)**3)/27
    if(U<=FY):
        X=Y
        accepted_X.append(X)
plt.figure(1)
plt.subplot(1,2,1)
plt.hist(accepted_X,bins=50,label='sampling')
plt.legend()
##theoretical
plt.subplot(1,2,2)
theorem_pdf_beta=np.random.beta(2,4,10000)
plt.hist(theorem_pdf_beta,bins=50,label='theorem')
plt.legend()
plt.title("Beta distribution")
plt.show()
##(2)
accepted_Z=[]
x = np.linspace(-3,3,1000)
for i in range(0,10000):
    U=np.random.uniform(0,1)
    U_1=np.random.uniform(0,1)
    Y=np.random.exponential(1)##e^{-x}
    FY=np.exp(-0.5*(Y-1)**2)
    if(U<=FY):
        X=Y
        if(U_1<=0.5 and U_1>=0):
            Z=X
        elif(U_1>0.5 and U_1<=1):
            Z=-X
        accepted_Z.append(Z)
plt.figure(2)
plt.subplot(1,2,1)
plt.hist(accepted_Z,bins=50,label='sampling')
plt.legend()
##theoretical
plt.subplot(1,2,2)
theorem_pdf_beta=np.random.normal(0,1,10000)
plt.hist(theorem_pdf_beta,bins=50,label='theorem')
plt.legend()
plt.title("Standard Normal distribution")
plt.show()
##(4)
# Define the function f(Y) = I(Y > 8)
c=0
for i in range(0,100000):
    Y=np.random.normal(8,1)
    f_1=np.exp(-Y**2/2)/np.sqrt(2*np.pi)
    f_2=np.exp(-(Y-8)**2/2)/np.sqrt(2*np.pi)
    if(Y>8):
        c+=f_1/f_2
    elif(Y<=8):
        c+=0
c = c/100000
print(c)