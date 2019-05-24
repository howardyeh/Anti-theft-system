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
def humanMatching(image, detection, humanDataset, itemDataset, encoder, missingPeopleDataset):

	global countHuman
	distanceThres = 20
	
	for h_n in detection:
		find_pair = False

				
		hnx = (h_n[0] + h_n[2])/2.0
		hny = (h_n[1] + h_n[3])/2.0

		# print("detected human in ", hnx, hny)
		for h_d in humanDataset.values():
			# print("dataset human in ", h_d.x, h_d.y)
			if h_d.missing == False and np.sqrt((hnx - h_d.x)**2 + (hny - h_d.y)**2) < distanceThres:
				h_d.update_position(hnx, hny)
				h_d.updated = True
				h_d.missing = False
				find_pair = True
				setAllItemAlarmOff(h_d, itemDataset)
				break

		if not find_pair:
			matchId=None
			#commented by shawn, un commented if needed
			feature = encoder.encode(image[int(h_n[0]):int(h_n[2]), int(h_n[1]):(h_n[3]),:]) # encode the cropped image
			matchId = matchMissingPeople(feature, missingPeopleDataset)
			
			if matchId == None:
				countHuman = countHuman + 1	
				newHuman = humanData(hnx, hny, countHuman, feature)
				humanDataset[countHuman] = newHuman
				print("Build up new human data id =", countHuman)

			else:
				humanDataset[matchId].updated = True
				humanDataset[matchId].missing = False
				humanDataset[matchId].update_position(hnx, hny)
				setAllItemAlarmOff(humanDataset[matchId], itemDataset)

	for h_d in humanDataset.values():
		# what if people get occluded for a frame?
		if h_d.updated == False and h_d.missing == False:
			h_d.missing = True
			missingPeopleDataset.append(h_d)
			print("Human missing! missingPeopleDataset become", missingPeopleDataset)

		h_d.updated = False # reset the update flag for all human in dataset


def itemMatching(detection, humanDataset,itemDataset):

	global countItem
	distanceThres = 20
		
	for d_n in detection:
		find_pair = False

		dnx = (d_n[0] + d_n[2])/2.0
		dny = (d_n[1] + d_n[3])/2.0


		for d_d in itemDataset.values():
			if np.sqrt((dnx - d_d.x)**2 + (dny - d_d.y)**2) < distanceThres:
				if d_d.alarm_flag == False:
					d_d.update_position(dnx, dny)
					d_d.updated = True
					d_d.missing = False
					find_pair = True
					break
				else: # if item is in alarm state, no update position
					d_d.updated = True
					d_d.missing = False
					find_pair = True
					break

		if not find_pair:
			countItem = countItem + 1
			newItem = itemData(dnx, dny, countItem)
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
	for human in humanDataset.values():
		dist = np.sqrt((item.x - human.x)**2 + (item.y - human.y)**2)
		print("distance between human",human.id, "and item", item.id, "is", dist)
		if dist < min_dist:
			min_dist = dist
			closestHuman = human
	if closestHuman!=None:
		closestHuman.itemList.append(item.id)
	#can i add a return closeHuman (do you need a range around the item?) 
	


def setAllItemAlarmOff(human, itemDataset):
	for itemID in human.itemList:
		if itemDataset[itemID].alarm_flag is True:
			itemDataset[itemID].alarm_flag = False


def matchMissingPeople(feature, missingPeopleDataset):
	closestMatchDist = 10000
	closestMatch = None
	thresDist = 0.05
	print("start to match missing people...")
	print("missingPeopleDataset = ", missingPeopleDataset)
	for h_d in missingPeopleDataset:
		dist = calculateDist(feature, h_d.feature)
		if dist < thresDist:
			if dist < closestMatchDist:
				closestMatchDist = dist
				closestMatch = h_d
	if closestMatch is not None:
		print("find closest match", closestMatch)
		missingPeopleDataset.remove(closestMatch)
		print("missingPeopleDataset now contain", missingPeopleDataset)
		return closestMatch.id
	else:
		print("no matching in missingPeopleDataset")
		return None


def calculateDist(feature1, feature2):
	return LA.norm(feature1 - feature2)




