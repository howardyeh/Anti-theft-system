import random
import math
import numpy as np
from dataType import humanData, itemData
from autoencoder import Autoencoder
from matching import humanMatching, itemMatching
from tracking import Scan_for_item_existing,Track_and_Display
import os
import argparse
import re
import string 
# from tracking import Scan_for_item_existing, Tracking_suspect, Display

''' 
Container content :

humanDataset         = {human_id1:humanData1, human_id2:humanData2, ...}
itemDataset          = {item_id1:itemData1, item_id2:itemData2, ...}
missingPeopleDataset = {feature1(np.array):humanData1, feature2(np.array):humanData2, ...}
detection            = [[upleft_x, upleft_y, downright_x, downright_y],[upleft_x, upleft_y, downright_x, downright_y]...]

'''
class Simulation:
	def __init__(self):
		self.flag=1
		self.item0_pos=(100,100)
		self.item1_pos=(50,50)
		self.people0_pos=(105,105)
		self.people1_pos=(30,30)
		#Generate some data (Not complete,increment 0-10 each time step)
		self.item={0:["Lattop",self.item0_pos[0],self.item0_pos[1]],1:["Cell Phone",self.item1_pos[0],self.item1_pos[1]]}
		
		self.human={0:["Human A",self.people0_pos[0],self.people0_pos[1]],1:["Human B",self.people1_pos[0],self.people1_pos[1]]}
		
	def yolo(self):
		#print(num)
		x_range=[0,200]
		y_range=[0,200]
		human_list=[]
		item_list=[]
		res_human=[]
		res_item=[]
		for i in range(2):
		   #print(human[i])
		   if self.human[i][1]<x_range[1] and self.human[i][1]>x_range[0] and self.human[i][2]<y_range[1] and self.human[i][2]>y_range[0]:   
			   human_list.append(self.human[i])
		if self.item[0][1]<x_range[1] and self.item[0][1]>x_range[0] and self.item[0][2]<y_range[1] and self.item[0][2]>y_range[0]:   
		   item_list.append(self.item[0])
		for human in human_list:
			print("in yolo",human)
			res_human.append([human[1]-20,human[2]-50,human[1]+20,human[2]+50])
		for item in item_list:
			print("in yolo",item)
			res_item.append([item[1]-20,item[2]-20,item[1]+20,item[2]+20])
		return (res_human,res_item)

	def iteration(self,count):
		
		print("=================")
		print("time stamp:",count)
		if self.flag==0 and count<20: 
			if self.human[0][1]<100:
				pass
			else:
				print("A back")
				self.human[0][1]-=random.random()%5+10 
		elif self.human[0][1]<200 and count<50:
			print("A leave")
			self.human[0][1]+=random.random()%5+10
		else:
			self.flag=0
			if count>20:
					
				if self.human[1][1]>=100:
						
					if count>30:
						print("B stole and fleet")
						self.human[1][2]+=random.random()%5+10
						self.item[0][1]=self.human[1][1]
						self.item[0][2]=self.human[1][2]
					else:
						print("B wait for the chance")
				else:
					print("A leave B close")                                  
					self.human[0][1]+=random.random()%10+30
					self.human[1][1]+=random.random()%5+10
					self.human[1][2]+=random.random()%5+10
		detection=self.yolo()
		print("detect val",detection)
		return detection


'''
TODO
1.Background segmentation
2.QUERY(feature matching)
3.Popping function
4.Yolov3 (detection)
5.SetAllAlarmOff
6.Findclosethuman
'''



def arg_parse():

	parser = argparse.ArgumentParser(description='Anti-theft system')
   
	parser.add_argument("--dataset",dest="dataset",help="bouding box info",
		default="../dataset/data1.txt")
	return parser.parse_args()

def mainFunc():
	args = arg_parse()
	dir_name=args.dataset
	print("---",dir_name)
	f= open(dir_name,'r')
	line =f.readlines()


	humanDataset = {}
	image=np.zeros((2000,2000,3))
	itemDataset = {}
	missingPeopleDataset = []
	#test=Simulation()
	#count=0
	
	encoder = Autoencoder()

	#while count<40:
	count=0
	for detection in line:
		print("=================")
		print("time stamp:",count)
		print(detection)
		detection = detection[2:-3]
		detection=detection.split('],[')
		detection_list=[]
		human_list=[]
		item_list=[]
		item_class=[]
		for detect in detection:
			detect=detect.split(', ')
			det_pos=[int(i) for i in detect[0:-1]]
			det_class=detect[-1].strip("''")		
			detection_list.append([det_pos,det_class])

		for dect in detection_list:
			
			if dect[-1]=='person':
				human_list.append(dect[0:-1])
			else:
				item_list.append(dect[0:-1])
				item_class.append(dect[-1])
			
		if human_list!=[]:
			humanMatching(image, human_list[0], humanDataset, itemDataset, encoder, missingPeopleDataset)
		print("human",humanDataset.keys())
		if item_list!=[]:
			itemMatching(item_list[0], humanDataset,itemDataset)
		print("item",itemDataset.keys())
		count+=1
			
		#print("global11111",humanDataset)
		#print("item22222",itemDataset)
		#Scan_for_item_existing(humanDataset,itemDataset)
		#Track_and_Display(humanDataset, itemDataset)
		#count+=1



if __name__=="__main__":
	mainFunc()


