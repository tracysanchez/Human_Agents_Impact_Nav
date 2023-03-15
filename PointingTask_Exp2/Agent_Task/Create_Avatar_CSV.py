import json
import pandas as pd
import os

import json
filepath = os.path.join("E:/HumanA/Data/Exp2/") 
#AllAvatars = pd.read_csv('/Users/tracysanchezpacheco/Documents/Resources/02_all_buildings_list.csv')
#AllAvatars = pd.read_csv('E:/HumanA/Data/Exp2/AvatarsList_PointingTask.csv')
with open(filepath + 'AllAvatarsList_Coordinates_Exp2.json') as file:
    #test = json_file
    AllAvatars = json.load(file)
#AllAvatars = pd.DataFrame(AllAvatars)
#test = pd.DataFrame(AllAvatars.explode('AvatarCenterWorld', ignore_index=True))
df = pd.DataFrame()
for avatar in AllAvatars:
    
    # reduce the additional depth of the dictionary to one  
    AllAvatars[avatar]['AgentCenterWorld.x'] = AllAvatars[avatar]["AvatarCenterWorld"]['x']
    AllAvatars[avatar]['AgentCenterWorld.z'] = AllAvatars[avatar]["AvatarCenterWorld"]['z']
    #add a distance measure to the center (Coordinates 0,0 -> distance calculated with euclidean distance)
    #AllAvatars[avatar]['DistanceToCenter'] = math.sqrt((AllAvatars[avatar]['AvatarPositionGlobal.X'])**2
    #+ (AllAvatars[avatar]['AvatarPositionGlobal.Z'])**2)
        #create dataframe for each agent

    ##remove unneccessary data columns
    AllAvatars[avatar].pop("AvatarCenterWorld")
    AllAvatars[avatar].pop("AvatarPositionGlobal")
    AllAvatars[avatar].pop("AvatarPositionLocal")
    AllAvatars[avatar].pop("AvatarRotationGlobal")
    AllAvatars[avatar].pop("AvatarRotationLocal")
    AllAvatars[avatar].pop("AvatarRotationVector3Global")
    AllAvatars[avatar].pop("AvatarRotationVector3Local")
    AllAvatars[avatar].pop("AvatarForwardDirection")
    AllAvatars[avatar].pop("AvatarLossyScale")
    AllAvatars[avatar].pop("AvatarLocalScale")
    AllAvatars[avatar].pop("AvatarUpDirection")
    AllAvatars[avatar].pop("AvatarRightDirection")

    avatardf = pd.DataFrame(AllAvatars[avatar], [0])
    df = pd.concat([df, avatardf], ignore_index=True)

os.chdir('E:/HumanA/Data')
df.to_csv('Data_Tracy/AllAvatars_Coordinates.csv')

print()