from localstore.Dataset import DATA,LENGTH
import hashlib
import json
import os

class LocalStore:
    def __init__(self,data:str='DATASET/DATASET.json',length:str='DATASET/LENGTH.txt') -> None:
        try:
            with open(data,'r') as f:
                self.data=json.load(f)
            with open(length,'r') as f:
                self.length=f.read()
            print("Successfully uploaded the data to the class")
        except Exception as e:
            self.length=LENGTH
            self.data=DATA
            print("Data upload unsuccessful default dataset has uploaded")
        self.response={
            "status":True,
            "response":""
        }
        
    def Show_Items(self)->dict:
        try:
            self.response["status"]=True
            self.response["response"] = list(self.data.keys())
            return self.response
        except Exception as e:
            self.response["status"]=False,
            self.response["response"]=f"Error Observed : {e}"
            
    def Show_product_List(self,product_name:str='')->dict:
        if product_name in self.data:
            self.response["status"]=True
            self.response["response"]=self.data[product_name]
            return self.response
        else:
            self.response["status"]=False
            self.response["response"]= "Product not found in the Database"
            return self.response
        
    def Show_Random_Product(self)->dict:
        try:
            temp={}
            for item in list(self.data.keys()):
                for idx in self.data[item]:
                    temp[idx]=self.data[item][idx]
                    break
            self.response["status"]=True
            self.response["response"]=temp
            return self.response
        except Exception as e:
            self.response["status"]=False
            self.response["response"]=f"Error Observed {e}"
            return self.response
        
    def Add_New_Product(self,product_name:str='',data:dict={})->dict:
        try:
            product_name=product_name.lower()
            if product_name in self.data:
                for val in self.data[product_name]:
                    indexes=[index.lower() for index in list(self.data[product_name][val].keys())]
                    break
                indexes.sort()
                keys=[val.lower() for val in list(data.keys())]
                keys.sort()
                if indexes==keys:
                    self.length+=1
                    tempid=str(self.length)
                    tempid=hashlib.sha256(tempid.encode()).hexdigest()
                    self.data[product_name][tempid]={i:data[i] for i in indexes}
                    self.response["status"]=True
                    self.response["response"]={
                        tempid:data
                    }
                    return self.response
                else:
                    self.response["status"]=False
                    self.response["response"]="Parameter not matched"
                    return self.response
            else:
                self.response["status"]=False
                self.response["response"]="Parameter not found"
                return self.response
        except Exception as e:
            self.response["status"]=False
            self.response["response"]=f"Error Observed : {e}"
            return self.response
        
    def Add_New_Item(self,product_name:str='')->dict:
        try:
            temp = list(self.data.keys())
            if product_name not in temp:
                self.data[product_name]={}
                self.response["status"]=True
                self.response["response"]=f"new Item added : {product_name}"
                return self.response
            else:
                self.response["status"]=False
                self.response["response"]=f"Item already exist : {product_name}"
                return self.response
        except Exception as e:
            self.response["status"]=False
            self.response["response"]=f"Error Observed : {e}"
            return self.response
    
    def Show_Data(self,index:str="")->dict:
        flag=False
        try:
            index=index.lower()
            for item in self.data:
                keys=list(self.data[item].keys())
                if index in keys:
                    temp={
                        index:self.data[item][index]
                    }
                    flag=True
                    break
            if flag:
                self.response["status"]=True
                self.response["response"]=temp
                return self.response
            else:
                self.response["status"]=False
                self.response["response"]=f"index doesnot found : {index}"
                return self.response
        except Exception as e:
            self.response["status"]=False
            self.response["response"]=f"Error Observed : {e}"
            return self.response
        
    def Delete_Data(self,index:str='')->dict:
        flag=False
        try:
            index=index.lower()
            for item in self.data:
                keys=list(self.data[item].keys())
                if index in keys:
                    temp=self.data[item].pop(index)
                    flag=True
                    break
            if flag:
                self.response["status"]=True
                self.response["response"]=temp
                return self.response
            else:
                self.response["status"]=False
                self.response["response"]="Index not found"
                return self.response
        except Exception as e:
            self.response["status"]=False
            self.response["response"]=f"Error Observed : {e}"
            return self.response
        
    def Write_Json(Self,textpath:str='LENGTH.txt',jsonpath:str='DATASET.json')->dict:
        try:
            os.mkdir('DATASET')
        except Exception as e:
            pass
        try:
            count=0
            for item in Self.data:
                for idx in Self.data[item]:
                    count+=1
            with open(os.path.join('DATASET',jsonpath),'w') as f:
                json.dump(Self.data,f)
                f.close()
            with open(os.path.join('DATASET',textpath),'w') as p:
                p.write(str(count))
                p.close()
            Self.response["status"]=True
            Self.response["response"]=f"json file saved at : {jsonpath} and text file saved at : {textpath}"
            return Self.response
        except Exception as e:
            Self.response["status"]=False
            Self.response["response"]=f"Error Observed : {e}"
            return Self.response