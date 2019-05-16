import random
import math


class humanData:
    def __init__(self):
	self.updated = False
	self.missing = False
	self.id = 0
	self.x
	self.y
	self.itemList = []
	def update_position(self,nx, ny):
		self.x = nx
		self.y = ny


class itemData:
    def __init__(self):
	self.updated = False
	self.missing = False
	self.alarm_flag = False
	self.id = 0
	self.x
	self.y
	def update_position(self,nx, ny):
		self.x = nx
		self.y = ny

countHuman = 0
countItem = 0

def humanDetection(detection, humanDataset):
	for h_n in detection:
		find_pair = False
                
                #TODO: Human feature qeury when human back
               
		for h_d in humanDataset:
			if h_n.position - h_d.position < thres:
				h_d.update_position()
				h_d.updated = True
				h_d.missing = False
				find_pair = true
				setAllItemAlarmOff(h_d)
				break
		if not find_pair:
			countHuman = countHuman + 1
			humanDataset[countHuman] = h_n
			h_n.id = countHuman

	for h_d in humanDataset:
		if h_d.updated == False and h_d.missing == False:
			h_d.missing = True
		h_d.updated = False # reset the update flag

def itemDetection(detection, itemDataset):
	for d_n in detection:
		find_pair = False
		for d_d in itemDataset:
			if d_n.position - h_d.position < thres:
				d_d.update_position()
				d_d.updated = True
				d_d.missing = False
				find_pair = True
				break
		if not find_pair:
			countItem = countItem + 1
			itemDataset[countItem] = d_n
			d_n.id = countItem
			findClosestHuman(item)

	for d_d in itemDataset:
		if d_d.updated == False and h_d.missing == False:
			d_d.missing = True
		d_d.updated = False # reset the update flag

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

				
def findClosestHuman(item):
	for all people in humanDataset:
		if people.position is close to item.position:
			People.itemList.append(item.id)

										
def Tracking_suspect(item):
	for all people in humanDataset:
		if people.position is close to item.position:
			People.suspect_label = True


def Display(people dataset):
	for all people in dataset:
		if people.suspect_label==true: bounded with red color
             	else: bounded with black color

'''

def yolo(human,item,num):
    #print(num)
    x_range=[0,200]
    y_range=[0,200]
    human_list=[]
    item_list=[]
    for i in range(2):
       #print(human[i])
       if human[i][1]<x_range[1] and human[i][1]>x_range[0] and human[i][2]<y_range[1] and human[i][2]>y_range[0]:   
           human_list.append(human[i])
    if item[0][1]<x_range[1] and item[0][1]>x_range[0] and item[0][2]<y_range[1] and item[0][2]>y_range[0]:   
       item_list.append(item[0])
    return (human_list,item_list)

'''
TODO
1.Background segmentation
2.QUERY(feature matching)
3.Popping function
4.Yolov3 (detection)
5.SetAllAlarmOff
6.Findclosethuman
'''

def main():
    item0_pos=(100,100)
    item1_pos=(50,50)
    people0_pos=(105,105)
    people1_pos=(30,30)
    humanDataset = {}
    itemDataset = {}
    #Generate some data (Not complete,increment 0-10 each time step)
    item={0:["Lattop",item0_pos[0],item0_pos[1]],1:["Cell Phone",item1_pos[0],item1_pos[1]]}
    count=0
    human={0:["Human A",people0_pos[0],people0_pos[1]],1:["Human B",people1_pos[0],people1_pos[1]]}
    flag=1
    while count<100:
        #for i in range(1):
        #   for j in range(1,3):
                #item[i][j]+=random.random()%10
        if flag==0 and count<40: 
                #human[i][j]-=random.random()%5+10 
               if human[0][1]<100:
                    #print("2",count)
                    pass
               else:
                    print("A back")
                    human[0][1]-=random.random()%5+10 
        elif human[0][1]<300 and count<50:
               print("A leave")
               human[0][1]+=random.random()%5+10
        else:
               flag=0
               if count>40:
                    
                    #human[i][j]+random.random()%5+10
                    if human[1][1]>=100:
                        #print("uuuuuuuuuuuuuuuuuuu",human[1])
                        #item[0][1]=1000
                        #item[0][2]=1000
                        if count>80:
                            print("B stole and fleet")
                            human[1][2]+=random.random()%25+20
                            item[0][1]=human[1][1]
                            item[0][2]=human[1][2]
                            #human[1][2]+=random.random()%25+20
                        else:
                            print("B wait for the chance")
                    else:
                        print("A leave B close")                                  
                        human[0][1]+=random.random()%10+30
                        human[1][1]+=random.random()%5+10
                        human[1][2]+=random.random()%5+10
        detection=yolo(human,item,0)
        #detection2=yolo(human,item,1)#(random.randint(5,19)%2))
        count+=1
        print(detection)
	#detection = yolo(random.random()%2)
	#humanDetection(detection, humanDataset)
	#itemDetection(detection, itemDataset)

	#Scan_for_item_existing(humanDataset)
	#Display(humanDataset, itemDataset)



main()


