"""
Aim : To plot a linear regression with multiple variables for a given data set
Author : Nandan Nayak
Date : 12/June/2016
"""
#import all modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


#define global variables
doc="ex1data2.txt"


#define functions
def Normalize(inList):
    temp_arr=np.array(inList)
    avg=temp_arr.mean()
    stdd=temp_arr.std()
    temp_arr=(temp_arr-avg)/stdd
    return list(temp_arr)

def Scatter(x,y,hyp,dot_color,line_color,x_label,flag):
    if flag:
        plt.scatter(x[1],y,color=dot_color)
        plt.plot(x[1],hyp,color=line_color)
    else:
        plt.scatter(x[2],y,color=dot_color)
        plt.plot(x[1],hyp,color=line_color)
    plt.xlabel(x_label)
    plt.ylabel("Price of House")

def costFunction(diff,m):
    diff_sq=diff*diff
    return (1/(2*m)*diff_sq.sum())
    
    


#define main
if __name__=="__main__":
    myFile=open(doc)
    x=[[],[],[]]
    y=[]
    for line in myFile:
        line=line.replace("\n","")
        line=line.split(",")
        x[0].append(1)
        x[1].append(int(line[0]))
        x[2].append(int(line[1]))
        y.append(int(line[2]))
        
    """Normalize the input features"""
    x[1]=Normalize(x[1])
    x[2]=Normalize(x[2])

    """Maintain a feature matrix to compute the dot product with theta"""
    m=len(y)
    x_feat=[]
    for i in range(m):
        templist=[]
        templist.append(x[0][i])
        templist.append(x[1][i])
        templist.append(x[2][i])
        x_feat.append(templist)

    
    x=np.array(x)
    y=np.array(y)
    theta=np.zeros(3)
    x_feat=np.array(x_feat)
    diff=np.empty((3,m))

    
    loops=500
    alpha=0.1
    hyp=np.empty(m)
    J=np.empty(loops)
    for j in range(loops):
        for i in range(m):
            hyp[i]=np.dot(theta.T,x_feat[i])

        tempDiff=hyp-y

        
        for i in range(diff.shape[0]):
            if i==0:
                diff[i]=tempDiff
                
            else:
                diff[i]=tempDiff*x[i]
            theta[i]=theta[i]-(alpha/m*diff[i].sum())

        """Computing variation of Cost function with iterations"""
        J[j]=costFunction(diff[0],m)
        
    print "The model parameters generated using Gradient Descent:"
    print theta

    #Using Normal Equation
    theta_lin=np.empty(3)
    theta_new= np.linalg.pinv(np.dot(x.T,x))
    theta_new=np.dot(theta_new,x.T)

    theta_new=theta_new.T
    for i in range(3):
        theta_lin[i]=np.dot(theta_new[i],y)
   

    print "\nThe model parameters generated using Normal Equation:"
    print theta_lin

    
    
    plt.subplot(2,1,1)
    plt.title("Training data with Linear Regression fit (multiple features)")
    Scatter(x,y,hyp,"orange","red","Size of house (sq. feet)",1)
    
    plt.subplot(2,1,2)
    Scatter(x,y,hyp,"blue","red","No. of Bedrooms",0)
    plt.show()

    
    plt.plot(range(loops),J)
    plt.xlabel("No. of iterations")
    plt.ylabel("Cost Function")
    plt.title("Convergence of Gradient Descent with 0.1 learning rate")
    plt.show()
    
    
        
