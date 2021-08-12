#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pandas.core import frame
import seaborn as sns
import random
import math
import streamlit as st
import time

#app programme that will be called when page is loaded
def app():
    st.title('Simulation')
    iterations=1000
    samples=374
    if 'iters' not in st.session_state:
        st.session_state['iters']=1000
    else:
        iterations=st.session_state['iters']
    if 'samples' not in st.session_state:
        st.session_state['samples']=374
    else:
        samples=st.session_state['samples']
    vs=VarianceVisualizer(iterations,samples)
    vs.visualize()

class VarianceVisualizer:

    def __init__(self,maxIter=1000,sampleSize=374):
        '''
        This is the constructor. 
        maxIter: maximum number of iterations to visualize , default=1000
        sampleSize: specifies the population size for the data, default=374
        returns -> None

        '''
        self.maxIter=int(maxIter)
        self.sampleSize=int(sampleSize)

    #function that will generate samples
    
    def generateSamples(self,population,number):
        '''
        Generates random samples for a population
        population: list containing the population
        number: number of samples to be generated
        returns -> list

        '''
        sampleArr=random.choices(self,population,k=number)
        return sampleArr

    #function that will calculate mean
    def calcMean(self,population):
        '''
        Calculated mean of a list
        population:list containing numeric values
        returns-> number

        '''
        pop=np.array(population)
        return np.mean(pop)

    #function that will calculate the biased variance
    def calcBiasedVariance(self,population,mean):
        '''
        Calculates biased variance for list of values
        population: list containing numeric information
        mean: mean of the numeric information
        returns -> number

        '''
        total=0
        for ele in population:
            total+=math.pow((ele-mean),2)
        total/=len(population)
        return total

    def visualize(self):
        '''
        Visualizes the sample variance/ population variance vs the sample size
        returns-> None

        '''
        #generating a population
        population=random.choices(range(1,21),k=self.sampleSize)

        #number of iteration/number of samples that will be generated
        iters=self.maxIter

        #sample size array
        sizes=np.arange(2,11,1,dtype=np.uint64)

        #hashmap for the sample sizes
        data={}
        for ele in sizes:
            data[ele]=[]

        #population mean and variance
        popVar=self.calcBiasedVariance(population,self.calcMean(population))
        st.write("Population Size: {}".format(len(population)))
        st.write("Population Variance: {}".format(popVar))
        #iterate and generate graph
        fig=plt.figure()
        X=([])
        heights=[]
        for ele in data:
            X.append(ele)
            heights.append(200)
        palette = list(reversed(sns.color_palette("Set2").as_hex()))
        rects=plt.bar(x=X,height=heights,color=palette)
        plt.title("Graph showing sample size vs variance ratio.")
        plt.xlabel("Sample Size")
        plt.ylabel("Sample Variance/Population Variance (%)")
        plt.xticks(X)
        the_plt=st.pyplot(plt)
        def animate(frame):
            sampleSize=random.choices(sizes,k=1)[0]
            sample=random.choices(population,k=sampleSize)
            #calculate mean of sample
            sampleMean=self.calcMean(sample)
            #cacluate variance
            sampleVariance=self.calcBiasedVariance(sample,sampleMean)
            #ratio
            ratio=(sampleVariance/popVar)*100
            data[sampleSize].append(ratio)
            Y=[]
            #generating parameters for graph
            for sample_size in data:
                if(len(data[sample_size])==0):
                    Y.append(0)
                    continue
                mean=np.mean(data[sample_size])
                Y.append(mean)
            
            #update bar
            for idx,rect in enumerate(rects):
                rect.set_height(Y[idx])
            the_plt.pyplot(plt)
            
        
        #animation runner
        speed=0
        if 'speed' not in st.session_state:
            st.session_state['speed']=0.1
        else:
            speed=st.session_state['speed']
        t=st.empty()
        for i in range(iters):
            t.write('Iteration : {}'.format(i+1))
            animate(i)
            time.sleep(speed)





