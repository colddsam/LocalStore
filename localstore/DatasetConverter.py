import pandas as pd
import os
import hashlib
import json

class Converter:
    def __init__(self) -> None:
        self.dataset=None
        self.length=None
        
    def Dataset_From_Directory(self,path:str)->None:
        dataset={}
        count=0
        try:
            for file in os.listdir(path):
                data=pd.read_csv(os.path.join(path,file))
                data=data.dropna()
                column=data.columns.values
                dataset[file[:-4].lower()] = {}
                for idx in range(len(data)):
                    try:
                        temp={}
                        hashed_value = hashlib.sha256(str(count).encode()).hexdigest()
                        for key in column:
                            temp[key.lower()]=str(data[key][idx]).lower()
                        dataset[file[:-4].lower()][hashed_value]=temp
                        count += 1
                    except Exception as p:
                        pass
                self.dataset=dataset
                self.length=count
            print("execution successful you can download it by Create_Dataset() method")
        except Exception as e:
            print(f"Error Observed : {e}")
            
    def Dataset_From_File(self,path:str)->None:
        dataset={}
        count=0
        try:
            data=pd.read_csv(path)
            data=data.dropna()
            column=data.columns.values
            dataset[path[:-4].lower()]={}
            for idx in range(len(data)):
                try:
                    temp={}
                    hashed_value = hashlib.sha256(str(count).encode()).hexdigest()
                    for key in column:
                        temp[key.lower()]=str(data[key][idx]).lower()
                    dataset[path[:-4].lower()][hashed_value]=temp
                    count+=1
                except Exception as e:
                    pass
            self.dataset=dataset
            self.length=count
            print("execution successful you can download it by Create_Dataset() method")

        except Exception as e:
            print(f"Error Observed : {e}")
        
    def Create_Dataset(self)->None:
        try:
            os.mkdir('DATASET')
        except Exception as e:
            pass
        try:
            with open('DATASET\DATASET.json','w') as f:
                json.dump(self.dataset,f)
            with open('DATASET\LENGTH.txt','w') as o:
                o.write(str(self.length))
            print("File saved at DATASET directory")
        except Exception as e:
            print(f"Error Observed : {e}")