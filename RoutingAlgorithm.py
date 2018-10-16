#Written by Andrew Bryden 15/10/2018
import sys
import numpy as np
import pandas as pd
import time
start = time.time()
filepath = sys.argv[1] #Take in inputs from function call
initialNode = sys.argv[2]
terminalNode = sys.argv[3]
file = open(filepath)
lst = []
for line in file:
    lst += [line.split()]
	
lst = pd.DataFrame(lst)	 # convert the read in list into pandas array for manipulation
lst.columns = ['From','To','Distance']
lst.Distance = lst.Distance.astype(float)
a = pd.concat([lst['From'],lst['To']]) #Hold to get unique values
allNodes = a.unique() #List of all unique nodes
noNodes = allNodes.size
Dist = np.array(np.ones((noNodes,1)) * np.inf)
x = pd.DataFrame()
x['NodeNames'] = allNodes
x['Distance'] = Dist
x['Route'] = allNodes
visitedSet = np.array([0])
curNode = initialNode
indx = x.loc[x.NodeNames == curNode].index.values
x.iloc[indx,1] = 0
unvisitedSet = x
while unvisitedSet.size > 0:
    curIndex = x.loc[x.NodeNames == curNode].index.values
    linkIndex = lst.loc[lst.From == curNode].index.values
    for i in range(linkIndex.size):
        distance = x.iloc[curIndex,1] + lst.iloc[linkIndex[i],2]
        toNode = lst.iloc[linkIndex[i],1]
        toIndex = x.loc[x.NodeNames == toNode].index.values
        b = x.iloc[toIndex,1]
        curRoute = x.iloc[toIndex,2]
        prevRoute = x.iloc[curIndex,2]
        x.iloc[toIndex,1] = np.where(distance<b.squeeze(),distance,b) #Replace the values with new distances if smaller
        x.iloc[toIndex,2] = np.where(distance<b.squeeze(),prevRoute + ' '+ toNode,curRoute) #Store the route taken
    unvisitedSet = x
    visitedSet = np.append(visitedSet,curNode)
    if curNode == terminalNode:
        break
    for i in range(visitedSet.size):
        unvisitedSet = unvisitedSet[unvisitedSet.NodeNames != visitedSet[i]]
    if unvisitedSet.size > 0: #Catch if the set is now empty
        minDist = unvisitedSet['Distance'].idxmin() 
        curNode = x.iloc[minDist,0] 
termIndex = x.loc[x.NodeNames == terminalNode].index.values
if len(termIndex) != 0: #Catch if there is no route
    totDist = x.iloc[termIndex,1].values
    routeTaken = x.iloc[termIndex,2].values
    print('The minimum route from', initialNode, 'to', terminalNode, 'is:', totDist)
    print('The route taken is:', routeTaken)
    end = time.time()
    print('The time taken is:', end-start)
else:
    print('There is no route between', initialNode, 'and', terminalNode)
    