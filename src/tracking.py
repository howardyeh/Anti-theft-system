''' 
Container content :

humanDataset         = {human_id1:humanData1, human_id2:humanData2, ...}
itemDataset          = {item_id1:itemData1, item_id2:itemData2, ...}
missingPeopleDataset = {feature1:humanData1, feature2:humanData2, ...}
detection            = [[upleft_x, upleft_y, downright_x, downright_y],[upleft_x, upleft_y, downright_x, downright_y]...]


function defined:

Scan_for_item_existing()
Tracking_suspect()
Display()

'''

'''
def Scan_for_item_existing(humanDataset, itemDataset):
	for all people in humanDataset:
		if people.missing == false:
			for item in people.itemList:
				if item.missing == false: 
					item.alarm_flag = true
				else:
					if item.alarm_flag == True:
						Tracking_suspect(item)
					else:
						pop_item_from_dataset(item)
			if people.itemList == []:
				pop_people_from_dataset(people)
                 else:
                        for item in people.itemList:
                                if item.missing ==true:
                                        pop_item_from_dataset(item)    

										
def Tracking_suspect(item):
	for all people in humanDataset:
		if people.position is close to item.position:
			People.suspect_label = True


def Display(people dataset):
	for all people in dataset:
		if people.suspect_label==true: bounded with red color
             	else: bounded with black color

'''