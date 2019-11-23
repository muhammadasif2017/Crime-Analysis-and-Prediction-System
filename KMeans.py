
import sys                                              
from random import shuffle,uniform
import math
from colorama import Fore,Back,Style
#Read data from dataset to be cluster#
def ReadData(fileName):                     
    f = open(fileName,'r')                  
    lines = f.read().splitlines()           
    f.close()                               
    #print(lines)
    items = []                             
    for i in range(1,len(lines)):
        line = lines[i].split(',')          
        itemFeatures = []                  
        for j in range(len(line)-1):
            v = float(line[j]);             
            itemFeatures.append(v);         

        items.append(itemFeatures)       
    shuffle(items)                        

    return items                         


def FindMinMax(items):
    n = len(items[0])
    minima = [sys.maxsize    for i in range(n)]  
    maxima = [-sys.maxsize-1 for i in range(n)]  
    
    for item in items:                            
        for f in range(len(item)):               
            if(item[f] < minima[f]):              
                minima[f] = item[f]              
                maxima[f] = item[f]               
    return minima,maxima                          

#step#02:
def InitializeMeans(items,k,cMin,cMax):             #Function for defining means which are basically clusters which are centriod to be formed 

    f = len(items[0]);                               #number of features
    means = [[0 for i in range(f)] for j in range(k)]  #comprehension list for intializing list for k cluster intializing means between them
    #print(means)
    for mean in means:
        for i in range(len(mean)):                      #as means is list of list so loop through the list for assigning random no to means 
            
            mean[i] = uniform(cMin[i]+1,cMax[i]-1)       #Uniform function for getting random mean as a centroid

    return means 
#step#03:                                         #returning means with some intialize values  
def EuclideanDistance(x,y):                               #Euclideanfunction for clculating distance between two points which decide clusters of points
    S = 0; 
    for i in range(len(x)):
        S += math.pow(x[i]-y[i],2)             
        # Formula for getting distance between two points p(x1,y1) and q(x2,y2) is given as D=((x2-x1)^2+(y2-y1)^2)^1/2
    return math.sqrt(S);  
#step#4:          #for eliminating square root
def UpdateMean(n,mean,item):         
    for i in range(len(mean)):      #after  getting distance or deciding which cluster should selected 
        m = mean[i]                 #We have to calculate mean including new point which would be different from the previous one which is already
        m = (m*(n-1)+item[i])/float(n) #hence we need to update it according to the given formula 
        mean[i] = round(m,3)          # By rounding off the mean upto the three decimal 
    return mean                       #return mean value which is updated recently  
#Step#05
def FindClusters(means,items):         #Now we have to decide which cluster should be selected for the the point  
    clusters = [[] for i in range(len(means))];  #Intializing clusters as list and then filling them with values  
    #print(clusters)
    for item in items:                     #iterate attributes from items
        #Classify item into a cluster
        index = Classify(means,item)       #Calling classify function  which return the index of cluster which offer minimum distance of data point                                  #from the clusters 
        clusters[index].append(item)        #Adding item into the suitable index index representing cluster one ,two and three.
    #print(clusters)                      
    return clusters                          #this function will return the list of clusters having further clusters in it 

def Classify(means,item):                     #This classify function will get means and item in this function parameter means represnting cluster 
    
    minimum = sys.maxsize                      #intializing the minimum variable to positive infinity for finding the minimum value
    index = -1                                 #intializing index to minus value due to the avoid from confusion
    #print(means)
    for i in range(len(means)):
        #Find distance from item to mean
        dis = EuclideanDistance(item,means[i])   #Check by passing different values of cluster means and checking them with a particular point and 
        #which cluster is closest to the given point and deciding the cluster or mean for particular point
        if(dis < minimum):            #check for minimum point
            minimum = dis
            index = i
    
    return index                       #returning suitable index upon which item should append 

def CalculateMeans(k,items,maxIterations=100):
    
    cMin, cMax = FindMinMax(items)

    means = InitializeMeans(items,k,cMin,cMax)
    #Initialize clusters, the array to hold
    #the number of items in a class
    clusterSizes = [0 for i in range(len(means))] 
#print(clusterSizes)                          #getting size of a single cluster
    #An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))]   #A list to  hold the cluster 
    #Calculate means
    for i in range(maxIterations):                #its prediction of iteration for which we achieve the equal variation for all the cluster
    #If no change of cluster occurs, halt
        noChange = True
        for i in range(len(items)):                #iterate through the items/attributes 
            item = items[i]                         
                                                #Classify item into a cluster and update the

            index = Classify(means,item)

            clusterSizes[index] += 1              #for placing next item increment to index of clusters
            means[index] = UpdateMean(clusterSizes[index],means[index],item) #it will store the updated mean to the suitable index

            if(index != belongsTo[i]):             
                noChange = False

            belongsTo[i] = index           
        if(noChange):
            break                             

    return means
def main():
    items = ReadData("C:/Users/Asif/data.txt")
    k = 3
    means = CalculateMeans(k,items)
    clusters = FindClusters(means,items)
    print(means)
    
  
    print(Fore.GREEN + "clusters")
    print(clusters)
    
    

if __name__ == "__main__":
    main()



