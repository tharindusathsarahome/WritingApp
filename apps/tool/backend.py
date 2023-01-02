from apps.tool.writingTool import dataJson
from apps.tool.contentAPI import OpenAPI
def call(name,data):
    worknig = {'model':'text-davinci-002',
                    'best_of':1,
                    'temperature':1,
                    'max_tokens':4000,
                    'top_p':1,
                    'frequency_penalty':0.5,
                    'stop':[],
                    'presence_penalty':0   
                    }
    outData = {

    }
    foceTitel =dataJson[name]['data']
    for CouNum in range(int(data['rang1'])):
        if name:
            query = "Generate "
            for toolName,toolVal in foceTitel.items():
                print(toolName)
                if toolName == 'txt1': 
                    query+=toolVal
                    query+= data[toolName]
                elif toolName == 'txt2':
                    query+=toolVal
                    query+=data[toolName]
                elif toolName == 'txt3':
                    query+=toolVal
                    query+=data[toolName]
                elif toolName == 'txt4':
                    query+=toolVal
                    query+=data[toolName]
                elif toolName == 'txt5':
                    query+=toolVal
                    query+=data[toolName]
                elif toolName == 'txt6':
                    query+=toolVal
                    query+=data[toolName]
                elif toolName == 'txtA1':
                    query+=toolVal
                    query+= data[toolName] 
                elif toolName == 'txtA2':                   
                    query+=toolVal
                    query+=data[toolName] 
                elif toolName == 'selectGremar':                   
                    query+=toolVal
                    query+=data[toolName] 
                    

            print(query)
            while True:
                outCount = OpenAPI(query,worknig)
                print(outCount)
                if int(dataJson[name]['status']) < int(outCount[0]):
                    outData[CouNum]=[outCount[0],outCount[1].replace('\n','</br>')]
                    break
    return outData      


