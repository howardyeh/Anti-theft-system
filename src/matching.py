import numpy as np
from numpy import linalg as LA
from dataType import humanData, itemData

''' 
Container content :

humanDataset         = {human_id1:humanData1, human_id2:humanData2, ...}
itemDataset          = {item_id1:itemData1, item_id2:itemData2, ...}
missingPeopleDataset = {feature1:humanData1, feature2:humanData2, ...}
detection            = [[upleft_x, upleft_y, downright_x, downright_y],[upleft_x, upleft_y, downright_x, downright_y]...]


function defined:

humanMatching()
itemMatching()
findClosestHuman()
setAllItemAlarmOff()
matchMissingPeople()
calculateDist()

'''

global countHuman 
global countItem 
countHuman=0
countItem=0


#temperory remove autoencoder, will add it back when finishing debuging
def humanMatching(image, detection, humanDataset, itemDataset, missingPeopleDataset):
        #Add by Shawn delete if not need
        global countHuman
	distanceThres = 10 # 10 pixel
	
	for h_n in detection:
		find_pair = False
                
		hnx = (h_n[0] + h_n[2])/2.0
		hny = (h_n[1] + h_n[3])/2.0

		for h_d in humanDataset.values():
                        print("test")
			if np.sqrt((hnx - h_d.x)**2 + (hny - h_d.y)**2) < distanceThres:
				h_d.update_position(hnx, hny)
				h_d.updated = True
				h_d.missing = False
				find_pair = true
				setAllItemAlarmOff(h_d, itemDataset)
				break

		if not find_pair:
                        matchId=None
                        #commented by shawn, un commented if needed
			#feature = encoder.encode(image[h_n[0]:h_n[2], h_n[1]:h_n[3],:]) # encode the cropped image
			#matchId = matchMissingPeople(feature, missingPeopleDataset)
			
			if matchId == None:
				countHuman = countHuman + 1
                                
				newHuman = humanData(hnx, hny, countHuman)
				humanDataset[countHuman] = newHuman
			        print("counthuman",humanDataset[countHuman].missing)
			else:
				humanDataset[matchId].updated = True
				humanDataset[matchId].missing = False
				setAllItemAlarmOff(humanDataset[matchId], itemDataset)

	for h_d in humanDataset.values():
		# what if people get occluded for a frame?
		if h_d.updated == False and h_d.missing == False:
			h_d.missing = True
                        print("h_d.missing is on", h_d.missing)

		h_d.updated = False # reset the update flag for all human in dataset


def itemMatching(detection, humanDataset,itemDataset):
        #print("item___",humanDataset)
	global countItem
        distanceThres = 10 # 10 pixel
        
	for d_n in detection:
		find_pair = False
		dnx = (d_n[0] + d_n[2])/2.0
		dny = (d_n[1] + d_n[3])/2.0

		for d_d in itemDataset.values():
			if np.sqrt((dnx - d_d.x)**2 + (dny - d_d.y)**2) < distanceThres:
				d_d.update_position(dnx, dny)
				d_d.updated = True
				d_d.missing = False
				find_pair = True
				break

		if not find_pair:
			countItem = countItem + 1
			newItem = itemData(dnx, dny, countItem) #typo originally humanData
			itemDataset[countItem] = newItem
			findClosestHuman(itemDataset[countItem], humanDataset) # link the item to human

	for d_d in itemDataset.values():
		# what if item get occluded for a frame?
                
		if d_d.updated == False and d_d.missing == False:
			d_d.missing = True

		d_d.updated = False # reset the update flag for all item in dataset


def findClosestHuman(item, humanDataset):
	min_dist = 1000
	closestHuman = None
        #print("hu",humanDataset)
	for human in humanDataset.values():
           # print("human",human)
	    dist = np.sqrt((item.x - human.x)**2 + (item.y - human.y)**2)
	    if dist < min_dist:
	        min_dist = dist
		closestHuman = human
            else:
                pass
                #print("dist,min_dist",dist,min_dist)        
	#print("man",humanDataset)
        closestHuman.itemList.append(item.id)
        #can i add a return closeHuman (do you need a range around the item?) 
        return closestHuman,dist

def setAllItemAlarmOff(human, itemDataset):
	for itemID in human.itemList:
		if itemDataset[itemID].alarm_flag is True:
			itemDataset[itemID].alarm_flag = False


def matchMissingPeople(feature, missingPeopleDataset):
	closestMatchDist = 10000
	closestMatch = None
	thresDist = 0.05
	for f in missingPeopleDataset:
		dist = calculateDist(feature, f)
		if dist < thresDist:
			if dist < closestMatchDist:
				closestMatchDist = dist
				closestMatch = missingPeopleDataset[f]
	if closestMatch is not None:
		return closestMatch.id
	else:
		return None


def calculateDist(feature1, feature2):
	return LA.norm(feature1 - feature2)



