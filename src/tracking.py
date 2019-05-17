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
from dataType import humanData,itemData
from matching import findClosestHuman

def Scan_for_item_existing(humanDataset, itemDataset):
	oclussion_check_dist=30   #not sure about this distance
	pop_item_list=[]
	pop_human_list=[]
	for human in humanDataset.values():
		if human.missing == True:  #True or falsue
			print("humanmissing",human.x,human.y)
			for item in human.itemList:

				cloestHuman,dist=findClosestHuman(itemDataset[item],humanDataset)
				print("item",itemDataset[item].id)
				if itemDataset[item].missing == False: 
					print("itemflag1",itemDataset[item].alram_flag)
					itemDataset[item].alarm_flag = True
					if dist>oclussion_check_dist:
						cloestHuman.isSuspect=True 
						#Take by suspect explicitly
				else:
					print("itemflag2",item,itemDataset[item].alarm_flag)
					
					if itemDataset[item].alarm_flag == True:
						#cloestHuman,dist=findCloestHuman(item,humanDataset) 
						
						if cloestHuman.isSuspect==True:
							pass 
							#Track_and_display(humanDataset) will used in main function   
						else:
							if dist>oclussion_chek_dist:
								cloestHuman.isSuspect=True
							else:
								cloestHuman.isSuspect=False    
								#Oclussion case
					else:
						print("pop item when no alarm ",item,"human pos",human.x,human.y)
						pop_item_list.append(itemDataset[item])
						#Pop_item_from_dataset(item,itemDataset)  #minor Case: disappear at same time
			if human.itemList == []:
				print("pop human",human.id,human.missing,human.x,human.y)
				pop_human_list.append(human)
				#Pop_human_from_dataset(human,humanDataset)
		else:
			print("human.item",human.id,human.itemList,human.x,human.y)
			for item in human.itemList:
				if itemDataset[item].missing ==True:
					print("pop item when item missing")
					#Pop_item_from_dataset(item,itemDataset)
					pop_item_list.append(itemDataset[item])
				else:
					pass    
	for item in pop_item_list:
		Pop_item_from_dataset(item,itemDataset)
	for human in pop_human_list:
		Pop_human_from_dataset(human,humanDataset)


def Track_and_Display(humanDataset,itemDataset):
	human_disp_list=[]
	for human in humanDataset.values():
		if human.isSuspect==True: 
			#bounded with red color
			human_disp_list.append([human.id,"red"])
		else: 
			#bounded with black color
			human_disp_list.append([human.id,"black"])
	print(human_disp_list)


def Pop_item_from_dataset(item,itemDataset):
	print("itemDataset",itemDataset)
	print("item",item.id)
	itemDataset.pop(item.id) # typo: pop() need to use key not value
def Pop_human_from_dataset(human,humanDataset):
	humanDataset.pop(human.id) # typo: pop() need to use key not value
