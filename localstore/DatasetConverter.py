import pandas as pd
import os
import hashlib
import json


class Converter:
    def __init__(self) -> None:
        self.dataset = None

    def Dataset_From_Directory(self, path: str, format: str = 'csv') -> None:
        dataset = {
            "length": 0,
            "items": {}
        }

        try:
            for file in os.listdir(path):
                if format == 'csv':
                    data = pd.read_csv(os.path.join(path, file))
                    ext = 4
                elif format == 'xlsx':
                    data = pd.read_excel(os.path.join(path, file))
                    ext = 5
                else:
                    print(f"{format} format is not supported")
                    exit()

                data = data.dropna()
                column = data.columns.values
                item_key = file[:-ext].lower()

                dataset["items"][item_key] = {
                    "length": 0,
                    "products": {}
                }

                for idx in range(len(data)):
                    try:
                        temp = {}
                        var = item_key + \
                            str(dataset["items"][item_key]["length"])
                        hashed_value = hashlib.sha256(var.encode()).hexdigest()

                        for key in column:
                            temp[key.lower()] = str(data[key][idx]).lower()

                        dataset["items"][item_key]["products"][hashed_value] = temp
                        dataset["items"][item_key]["length"] += 1
                        dataset["length"] += 1
                    except Exception as p:
                        print(f"{p} index has an error")

            self.dataset = dataset
            print(
                "Execution successful. You can download it by calling the Create_Dataset() method.")

        except Exception as e:
            print(f"Error Observed: {e}")

    def Dataset_From_File(self, path: str, format: str = 'csv') -> None:
        dataset = {
            "length": 0,
            "items": {}
        }

        try:
            if format == 'csv':
                data = pd.read_csv(path)
                ext = 4
            elif format == 'xlsx':
                data = pd.read_excel(path)
                ext = 5
            else:
                print(f"{format} format is not supported")
                exit()

            data = data.dropna()
            column = data.columns.values
            item_key = path[:-ext].lower()

            dataset["items"][item_key] = {
                "length": 0,
                "products": {}
            }

            for idx in range(len(data)):
                try:
                    temp = {}
                    var = item_key + str(dataset["items"][item_key]["length"])
                    hashed_value = hashlib.sha256(var.encode()).hexdigest()

                    for key in column:
                        temp[key.lower()] = str(data[key][idx]).lower()

                    dataset["items"][item_key]["products"][hashed_value] = temp
                    dataset["items"][item_key]["length"] += 1
                    dataset["length"] += 1
                except Exception as p:
                    print(f"{p} index has an error")

            self.dataset = dataset
            print(
                "Execution successful. You can download it by calling the Create_Dataset() method.")

        except Exception as e:
            print(f"Error Observed: {e}")

    def Create_Dataset(self) -> None:
        try:
            os.makedirs('CONVERTED_DATASET', exist_ok=True)

            with open('CONVERTED_DATASET/DATASET.json', 'w') as f:
                json.dump(self.dataset, f)

            with open('CONVERTED_DATASET/LENGTH.txt', 'w') as o:
                o.write(str(self.dataset["length"]))

            print("File saved at CONVERTED_DATASET directory")

        except Exception as e:
            print(f"Error Observed: {e}")
