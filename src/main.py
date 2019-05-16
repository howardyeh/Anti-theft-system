class humanData:
	updated = false
	missing = false
	id = 0
	x
	y
	itemList = []
	def update_position(nx, ny):
		x = nx
		y = ny


class itemData:
	updated = false
	missing = false
	alarm_flag = false
	id = 0
	x
	y
	def update_position(nx, ny):
		x = nx
		y = ny

countHuman = 0
countItem = 0

def humanDetection(detection, humanDataset):
	for all h_n in detection:
		find_pair = false
		for all h_d in humanDataset:
			if h_n.position - h_d.position < thres:
				h_d.update_position()
				h_d.updated = true
				h_d.missing = false
				find_pair = true
				setAllItemAlarmOff(h_d)
				break
		if not find_pair:
			countHuman = countHuman + 1
			humanDataset[countHuman] = h_n
			h_n.id = countHuman

	for all h_d in humanDataset:
		if h_d.updated == false and h_d.missing == false:
			h_d.missing = true
		h_d.updated = false # reset the update flag

def itemDetection(detection, itemDataset):
	for all d_n in detection:
		find_pair = false
		for all d_d in itemDataset:
			if d_n.position - h_d.position < thres:
				d_d.update_position()
				d_d.updated = true
				d_d.missing = false
				find_pair = true
				break
		if not find_pair:
			countItem = countItem + 1
			itemDataset[countItem] = d_n
			d_n.id = countItem
			findClosestHuman(item)

	for all d_d in itemDataset:
		if d_d.updated == false and h_d.missing == false:
			d_d.missing = true
		d_d.updated = false # reset the update flag


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
				
def findClosestHuman(item):
	for all people in humanDataset:
		If people.position is close to item.position:
			People.itemList.append(item.id)

										
def Tracking_suspect(item):
	for all people in humanDataset:
		If people.position is close to item.position:
			People.suspect_label = True


def Display(people dataset):
	for all people in dataset:
		If people.suspect_label==true: bounded with red color




def main():
	humanDataset = {}
	itemDataset = {}
	while(true):
		detection = yolo(image)
		humanDetection(detection, humanDataset)
		itemDetection(detection, itemDataset)

		Scan_for_item_existing(humanDataset)
		Display(humanDataset, itemDataset)







