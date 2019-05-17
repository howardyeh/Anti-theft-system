import random
import math
from dataType import humanData, itemData
from autoencoder import Autoencoder
from matching import humanMatching, itemMatching
# from tracking import Scan_for_item_existing, Tracking_suspect, Display

''' 
Container content :

humanDataset         = {human_id1:humanData1, human_id2:humanData2, ...}
itemDataset          = {item_id1:itemData1, item_id2:itemData2, ...}
missingPeopleDataset = {feature1(np.array):humanData1, feature2(np.array):humanData2, ...}
detection            = [[upleft_x, upleft_y, downright_x, downright_y],[upleft_x, upleft_y, downright_x, downright_y]...]

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

def mainFunc():
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
        if flag==0 and count<40: 
               if human[0][1]<100:
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
                    
                    if human[1][1]>=100:
                        
                        if count>80:
                            print("B stole and fleet")
                            human[1][2]+=random.random()%25+20
                            item[0][1]=human[1][1]
                            item[0][2]=human[1][2]
                        else:
                            print("B wait for the chance")
                    else:
                        print("A leave B close")                                  
                        human[0][1]+=random.random()%10+30
                        human[1][1]+=random.random()%5+10
                        human[1][2]+=random.random()%5+10
        detection=yolo(human,item,0)
        count+=1
        print(detection)

    

	# humanDataset = {}
	# itemDataset = {}
	# missingPeopleDataset = {}
	# encoder = Autoencoder()

	# humanMatching(image, detection, humanDataset, itemDataset, encoder, missingPeopleDataset))
	# itemMatching(detection, itemDataset, humanDataset)
	# Scan_for_item_existing(humanDataset)
	# Display(humanDataset, itemDataset)



if name=="__main__":
	mainFunc()


