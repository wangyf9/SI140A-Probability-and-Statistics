import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import multivariate_normal
##(1)
###unif
u1=np.random.random(100000)
u2=np.random.random(100000)
x1 = np.linspace(0 - 4 , 0 + 4, 1000)
R=np.sqrt(-2*np.log(u1))
theta=2*np.pi*u2
x=R*np.cos(theta)
y=R*np.sin(theta)
theorem=(1/np.sqrt(2*np.pi))*np.exp(-(x1**2)/2)
plt.figure(1)
plt.subplot(1,3,1)
plt.hist(x,bins=100,range=(-4,4),density=True)
plt.title("Box-Muller Samples X")
plt.subplot(1,3,2)
plt.hist(y,bins=100,range=(-4,4),density=True)
plt.title("Box-Muller Samples Y")
plt.subplot(1,3,3)
plt.title("theorem standard normal pdf")
plt.plot(x1,theorem)
plt.show()
##(2)
##because x y are independent so ro=0
ro=0
##(Z,W) is the MVN which we have learned in class
z=x
w=ro*x+np.sqrt(1-ro**2)*y
plt.figure(2)
plt.subplot(1,3,1)
plt.hist(z,bins=100,range=(-4,4),density=True)
plt.title("Z")
plt.subplot(1,3,2)

plt.hist(w,bins=100,range=(-4,4),density=True)
plt.title("W")
plt.subplot(1,3,3)
plt.scatter(z,w)
plt.title("sampling points")
plt.show()
##(3)
##set ro
ro_vector=[0,0.3,0.5,0.7,0.9]
##initial other parameters
cov=[[1,0],[0,1]]
u=[0,0]
x2 = np.linspace(0 - 4 , 0 + 4, 1000)
x3 = np.linspace(0 - 4 , 0 + 4, 1000)
Z,W=np.meshgrid(x2,x3)
space=np.empty(Z.shape+(2,))
space[:,:,0]=Z
space[:,:,1]=W
plt.figure(3)
for i in range(5):
    ##set parameters
    ro=ro_vector[i]
    cov[1][0]=ro
    cov[0][1]=ro
    #generate mvn
    generate_mvn=multivariate_normal(u,cov)
    U=generate_mvn.pdf(space)
    plt.subplot(1,5,i+1)
    plt.contour(Z,W,U)
    plt.title(f"ro={ro}")
plt.show()
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_zlim(0,0.2)
wframe=None
##set parameters
ro=ro_vector[0]
cov[1][0]=ro
cov[0][1]=ro
#generate mvn
generate_mvn=multivariate_normal(u,cov)
U=generate_mvn.pdf(space)
wframe=ax.plot_wireframe(Z,W,U)

plt.title(f"ro={ro}")
plt.show()
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_zlim(0,0.2)
wframe=None
##set parameters
ro=ro_vector[1]
cov[1][0]=ro
cov[0][1]=ro
#generate mvn
generate_mvn=multivariate_normal(u,cov)
U=generate_mvn.pdf(space)
wframe=ax.plot_wireframe(Z,W,U)

plt.title(f"ro={ro}")
plt.show()
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_zlim(0,0.2)
wframe=None
##set parameters
ro=ro_vector[2]
cov[1][0]=ro
cov[0][1]=ro
#generate mvn
generate_mvn=multivariate_normal(u,cov)
U=generate_mvn.pdf(space)
wframe=ax.plot_wireframe(Z,W,U)

plt.title(f"ro={ro}")
plt.show()
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_zlim(0,0.2)
wframe=None
##set parameters
ro=ro_vector[3]
cov[1][0]=ro
cov[0][1]=ro
#generate mvn
generate_mvn=multivariate_normal(u,cov)
U=generate_mvn.pdf(space)
wframe=ax.plot_wireframe(Z,W,U)

plt.title(f"ro={ro}")
plt.show()
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_zlim(0,0.4)
wframe=None
##set parameters
ro=ro_vector[4]
cov[1][0]=ro
cov[0][1]=ro
#generate mvn
generate_mvn=multivariate_normal(u,cov)
U=generate_mvn.pdf(space)
wframe=ax.plot_wireframe(Z,W,U)

plt.title(f"ro={ro}")
plt.show()




