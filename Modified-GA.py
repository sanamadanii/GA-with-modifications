
# coding: utf-8

# In[21]:


import random

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
np.random.rand()


# In[22]:


def individual(chromleng,R_max,R_min):
    return list(np.random.randint(R_min,R_max,chromleng))


# In[23]:


sana=individual(5,2,-2)


# In[24]:


print(sana)


# In[25]:


def init_pop(popSize,chromleng,R_max,R_min):
     return [individual(chromleng,R_max,R_min) for x in range(popSize)]


# In[26]:


pop=init_pop(2,2,2,-2)
print(pop)


# In[27]:


def arithmetic_cross(two_parents,pcross=0.6):
    newParent=[]
    randVar= np.random.rand()
    if randVar<pcross:
        w=np.random.rand()
        p1=two_parents[0]
        p2=two_parents[1]
        
        for i in range(len(p1)):
            newParent.append(p1[i]*w + p2[i]*(1-w))
        return newParent
    else:
        return two_parents
    


# In[28]:


two_parents=[[0, -1], [0, 1]]
twoChild=arithmetic_cross(two_parents,)
print(twoChild)


# In[29]:


def fitness(pop):
    fit =[]
    for i in range(len(pop)):
        indv=pop[i]
        fit.append((8-(indv[0]+0.0317)**2 + indv[1]**2))
    return fit

def tournament(pop,fit,k):
    selected=[]
    maxx=0
    winner=0
    
    for i in range(len(pop)):
        for j in range(0,k-1):
            index= random.randint(0,len(pop)-1)
            if(fit[index]>maxx):
                maxx=fit[index]
                winner=index
        selected.append(pop[winner])
        
    return selected   
        


# In[31]:


def gaussian_mutate(Pop,R_max,R_min,sigma=0, pMut=0.05):
    indv =[]
    mutPop=[]
    for i in range(len(pop)):
        indv=pop[i]
        for j in range(len(indv)-1):
            randVar= np.random.rand()
            if randVar< pMut:
                gaussian=random.gauss((R_max-R_min),sigma)
                indv[j]=indv[j]+gaussian
            else:
                continue
                
        mutPop.append(indv)
    return mutPop  


# In[32]:


newpop=gaussian_mutate(pop,2,-2)
print(newpop)


# In[35]:


def elitism(fitness,pop):
    maxfit=0
    bestPop=[]
    for j in range(0,2,1):
        maxfit=max(fitness)
        for i in range(len(fitness)):
            if maxfit==fitness[i]:
                bestPop.append(pop[i]) 
                pop.remove(pop[i])
                fitness.remove(fitness[i])   
                break
            else:
                       continue
         
    return bestPop
    
def GARealValue(popSize,k,numOfGeneration,chromLeng,R_min,R_max,probCrossOver=0.6,probMut=0.05,sigma=0.5):
    FinalPop=[]
    best_hist=[]
    for i in range(0,numOfGeneration):
        #pop= population(4,20)[0,0,0,0]
        Pop=init_pop(popSize,chromLeng,R_max,R_min)
        
        fit=fitness(Pop)
        best=max(fit)
        for i in range(len(fit)):
            if best==fit[i]:
                best_hist.append(fit[i]) 
                break;
        
        
        el=elitism(fit,Pop)
        #print(fitness)
        selectedIndv = tournament(Pop,fit,k)
        #print(selectedIndv)
        newPopulation=[]
        for j in range(len(selectedIndv)-1):
            twoparent=[]
            twoparent.append(selectedIndv[j])
            twoparent.append(selectedIndv[j+1])
            j+=2
            newPopulation.append(arithmetic_cross(two_parents,probCrossOver))
        
        MutatedPopulation= gaussian_mutate(newPopulation,R_max,R_min,probMut,sigma)
        MutatedPopulation.append(el)
        FinalPop.append(MutatedPopulation)
    return FinalPop, best_hist


# In[46]:


runGA =GARealValue(20,18,100,2,-2,2)
print(runGA)


# In[49]:


plt.plot(runGA[1])

