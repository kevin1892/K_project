import pandas as pd
import sklearn
import numpy as np
import math

def getVictims(poblacion, rescatados, afectados):
	victims_now = 0
	return victims_now

def getDamage(damage,cost, victims):

	return level_danger

def totalCost(initialSolve, POD):
	totalCost = 0
	for x in xrange(1,initialSolve):
		totalCost += POD.POD_Cost[initialSolve[i][1][1]]
		pass
	return totalCost

def centersOfDemandCovered(initialSolve):
	coverd = 0
	for x in xrange(1,length(initialSolve)):
		coverd += length(initialSolve[i]) - 1
		pass
	return coverd

def distance(X_POD,X_DPC,Y_POD,Y_DCP,POD,DPC):
	return 1.2*(sqrt((X_POD[POD] - X_DPC[DPC])^2+(Y_POD[POD]-Y_DPC[DPC])^2))

def distanceMatrix(PODs,DPCs):
	matrix = [ [0.0]*4 for n in range(3) ]
	return matrix # To review

def DPCsList(PODs,DPCs,matrix):
	distanceList = []
	for x in xrange(1,size(DPCs,1)):
		#To review
		pass
	return done

def updateList(region, positions, mode):
	regionCopy = region
	if mode == 0 :
		for x in xrange(1,length(positions)):
#to review			regionCopy = regionCopy[regionCopy[:POD].!= positions[x],:] 
			pass
		pass
	elif mode == 1:
		for y in xrange(1,length(positions)):
#to review			regionCopy = regionCopy[regionCopy[:DPC].!=positions[y],P:]
			pass
		pass
	return regionCopy

def initialSolve(PODs,DPCs,matrix,PO):
	listPOD = PO
	copyPOD = PODs
	listDPC = DPCs
	location = 1
	DPCsAssign = []
	DPCpositions = []
	PODpositions = []
	PODsOcupied = []
	DPCsOcupied = []
	remainingCapacity = []
	while size(listDPC,1)>0 and size(listPOD,1) > 0:
		remainingCapacityPOD = listPOD[1].capacity
		regionPOD = listDPCs(listPOD,listDPCs,matrix)
		#to review
		#push
		remainingCapacityPOD = listPOD[location].capacity - sum(regionPOD.demandDPC)
		if location == size(listDPC, 1):
			return DPCsAssign
			pass

		pass
	pass

def graphicRoute():
	pass

def copySOL():
	pass

def PODnotUsed():
	pass

def DPCnotUsed():
	pass

def whichInterchange():
	pass

def remainingCapacity():
	pass

def addDPCremaing():
	pass

def createNeightbours():
	pass

def identifyInterchange():
	pass

def update():
	pass

def evaluateMovement():
		pass	

def tabuMovement():
	pass

def localSearch():
	pass

#resouses_file 	1- vehiculos 
#				2- personas o rescatistas
#				3- carga bruta
# 				4- tiempo de busqueda 
#				5- ubicacion    
#				6- ubicacion nombre
def constructionHeuristic(file_csv, heuristic_type, enviorment, budget, victims, resouses_csv, level_danger):
	
	return cost, solve