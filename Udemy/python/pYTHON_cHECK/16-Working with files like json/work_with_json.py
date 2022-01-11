# WE CANNOT DO KEY VALUE OPERATIONS ON THIS JSON FILE
#PRINT(TYPE(FO.READ()))
# THE JSON DATA IS STRING ITSELF
# FOR PYTHON UNDERSTANDABLE DATA WE HAVE TO JSON.LOAD
# FOR JSON WE NEED TO HAVE DATA AS DICTIONARY
# FOR WRITING THE JSON FILE WE NEED JSON.DUMP()
# AND WITH INDENT="SOMENUMBER"
import json
n_f="test.json"
fo=open(n_f)
#print(fo.read())
#print(type(fo.read()))
#print(json.load(fo))
n_d=json.load(fo).get('glossary').get('GlossDiv').get('GlossList').get('GlossEntry').get('GlossDef').get('GlossSeeAlso')
print(n_d[0])
'''
for each in n_d['GlossList']:
    print(each)
'''    
fo.close()