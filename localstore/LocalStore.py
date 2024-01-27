from localstore.Dataset import DATA
import hashlib
import json
import os

class LocalStore:
    def __init__(self, data_path: str='CONVERTED_DATASET/DATASET.json') -> None:
        try:
            with open(data_path, 'r') as f:
                self.data = json.load(f)
            print("Successfully uploaded the data to the class")
        except Exception as e:
            self.data = DATA
            print("Data upload unsuccessful default dataset has uploaded")
        self.response = {
            "status": True,
            "response": ""
        }
        
    def Show_Items(self) -> dict:
        try:
            self.response["status"] = True
            self.response["response"] = list(self.data["items"].keys())
            return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
            
    def Show_product_List(self, product_name: str = '') -> dict:
        if product_name in self.data["items"]:
            self.response["status"] = True
            self.response["response"] = self.data["items"][product_name]
            return self.response
        else:
            self.response["status"] = False
            self.response["response"] = "Product not found in the Database"
            return self.response
        
    def Show_Random_Product(self) -> dict:
        try:
            temp = {}
            for item in list(self.data["items"].keys()):
                for idx in self.data["items"][item]["products"]:
                    temp[idx] = self.data["items"][item]["products"][idx]
                    break
            self.response["status"] = True
            self.response["response"] = temp
            return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
        
    def Add_New_Product(self, item_name: str = '', data: dict = {}) -> dict:
        try:
            item_name = item_name.lower()
            if item_name in self.data["items"]:
                for validx in self.data["items"][item_name]["products"]:
                    indexes = [index.lower() for index in list(self.data["items"][item_name]["products"][validx].keys())]
                    break
                indexes.sort()
                keys = [val.lower() for val in list(data.keys())]
                keys.sort()
                if indexes == keys:
                    self.data["length"] += 1
                    self.data["items"][item_name]["length"] += 1
                    tempid = item_name + str(self.data["items"][item_name]["length"])
                    tempid = hashlib.sha256(tempid.encode()).hexdigest()
                    self.data["items"][item_name]["products"][tempid] = {i: data[i] for i in indexes}
                    self.response["status"] = True
                    self.response["response"] = {
                        tempid: data
                    }
                    return self.response
                else:
                    self.response["status"] = False
                    self.response["response"] = "Parameter not matched"
                    return self.response
            else:
                self.response["status"] = False
                self.response["response"] = "Parameter not found"
                return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
        
    def Add_New_Item(self, item_name: str = '') -> dict:
        try:
            temp = list(self.data["items"].keys())
            if item_name not in temp:
                self.data["items"][item_name] = {}
                self.response["status"] = True
                self.response["response"] = f"new Item added: {item_name}"
                return self.response
            else:
                self.response["status"] = False
                self.response["response"] = f"Item already exists: {item_name}"
                return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
    
    def Show_Data(self, index: str = "") -> dict:
        flag = False
        try:
            index = index.lower()
            for item in self.data["items"]:
                keys = list(self.data["items"][item]["products"].keys())
                if index in keys:
                    temp = {
                        index: self.data["items"][item]["products"][index]
                    }
                    flag = True
                    break
            if flag:
                self.response["status"] = True
                self.response["response"] = temp
                return self.response
            else:
                self.response["status"] = False
                self.response["response"] = f"Index does not found: {index}"
                return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
        
    def Delete_Data(self, index: str = '') -> dict:
        flag = False
        try:
            index = index.lower()
            for item in self.data["items"]:
                keys = list(self.data["items"][item]["products"].keys())
                if index in keys:
                    temp = self.data["items"][item]["products"].pop(index)
                    flag = True
                    self.data["items"][item]["length"] -= 1
                    self.data["length"] -= 1
                    break
            if flag:
                self.response["status"] = True
                self.response["response"] = temp
                return self.response
            else:
                self.response["status"] = False
                self.response["response"] = "Index not found"
                return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
        
    def Write_Json(self, textpath: str = 'LENGTH.txt', jsonpath: str = 'DATASET.json') -> dict:
        try:
            os.makedirs('CONVERTED_DATASET', exist_ok=True)
        except Exception as e:
            pass
        try:
            with open(os.path.join('DATASET', jsonpath), 'w') as f:
                json.dump(self.data, f)
            with open(os.path.join('DATASET', textpath), 'w') as p:
                p.write(str(self.data["length"]))
            self.response["status"] = True
            self.response["response"] = f"JSON file saved at: {jsonpath} and text file saved at: {textpath}"
            return self.response
        except Exception as e:
            self.response["status"] = False
            self.response["response"] = f"Error Observed: {e}"
            return self.response
