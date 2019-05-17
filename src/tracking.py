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
    for human in humanDataset.values():
	print("aaaaa`",human,human.missing)
        if human.missing == True:  #True or false
	    for item in human.itemList:

                print("itemdataiiii`",itemDataset,item)
	        cloestHuman,dist=findClosestHuman(itemDataset[item],humanDataset)
		#print("close",cloestHuman)
                if itemDataset[item].missing == False: 
		     itemDataset[item].alarm_flag = True
                     if dist>oclussion_check_dist:
                        cloestHuman.isSuspect=True 
                        #Take by suspect explicitly
		else:
                    print(itemDataset)
                    print(humanDataset)
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
                        print("pop item when no alarm")
		        Pop_item_from_dataset(item,itemDataset)  #minor Case: disappear at same time
	    if human.itemList == []:
                print("pop human")
	        Pop_human_from_dataset(human,humanDataset)
        else:
            print("itemdata___",itemDataset)
            for item in human.itemList:
                print(item.missing)
                if itemDataset[item].missing ==True:
                    print("pop item when item missing")
                    Pop_item_from_dataset(item,itemDataset)
                else:
                    pass    

										 


def Track_and_Display(humanDataset,itemDataset):
    human_disp_list=[]
    for human in humandataset:
	if human.isSuspect==true: 
             #bounded with red color
             human_disp_list.append([human.id,"red"])
        else: 
             #bounded with black color
             human_disp_list.append([human.id,"black"])
    print(human_disp_list)


def Pop_item_from_dataset(item,itemDataset):
    itemDataset.pop(item)
def Pop_human_from_dataset(human,humanDataset):
    humanDataset.pop(human)
