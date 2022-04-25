# WE CANNOT DO KEY VALUE OPERATIONS ON THIS JSON FILE
#PRINT(TYPE(FO.READ()))
# THE JSON DATA IS STRING ITSELF
# FOR PYTHON UNDERSTANDABLE DATA WE HAVE TO JSON.LOAD
# FOR JSON WE NEED TO HAVE DATA AS DICTIONARY
# FOR WRITING THE JSON FILE WE NEED JSON.DUMP()
# AND WITH INDENT="SOMENUMBER"
import json
my_dict={'Name':'samantha','skill':['python','shell','linux_admin']}
req_file= "samantha.json"
fo=open(req_file,"w")
json.dump(my_dict,fo,indent=4)
fo.close()