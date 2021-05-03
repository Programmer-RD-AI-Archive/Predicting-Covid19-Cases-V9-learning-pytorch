from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    MinMaxScaler,
    MaxAbsScaler,
    OneHotEncoder,
    LabelEncoder,
    Normalizer,
)
import numpy as np
import torch
import json
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from sklearn.impute import SimpleImputer

"""
the file is for other stuff that means it doesnt need its own file this will do most of the easy stuff
there is a way to passthrough as data class to torch.utils.data.DataLoader
and there is much more in the Other() class.
"""


class Other:
    def object_to_int(
        self,
        data=pd.DataFrame,
        start_index=-1,
        filepath="./info.json",
        col="index",
        verbose=1,
    ) -> "Return a list and a dictionary of the object cols int converted":
        """
        verbose :
            verbose = 0 = No output
            verbose = 1 = Output

        start_index :
            it just is like the index the convertion starts at.
            ex :
                start_index = -1
                0 : first object
                1 : second object
                so and so forth

        data :
            a pd dataframe with the column

        filepath :
            the filepath that you want to save the info_dict to.
            ex :
            {0:'A',1:'B'}

        col :
            the column that you want transformed
        """
        if data[col].dtype == int or data[col].dtype == float:
            raise f"the columns that you passed are int or float type please passthrough a object type column {data[col].dtype}"
        index = start_index
        info_list = []
        info_dict = {}
        for info in data[col]:
            if info not in info_dict:
                index += 1
                info_dict[info] = index
        for info in data[col]:
            info_list.append(info_dict[info])
        print(info_dict)
        return (index, info_list, info_dict)

    def replace_strs(
        self,
        data,
        col="index",
        what_to_convert_from="",
        to_what="",
        verbose=1,
    ) -> "the new data and the new_info(replaced)":
        """
        verbose :
            verbose = 0 = No output
            verbose = 1 = Output

        data :
            a pd dataframe with the column

        col :
            the column that you want replaces

        what_to_convert_from and to_what :
            from 1980-05-21 so you want to remove the - so you will pass - to what_to_convert_from to 19800521
            that mean from 1980-05-21 to 19800521
            what_to_convert_from = -
            to_what = ''
        """
        print("Checking if the columns dtype if object or not...")
        print(data[col].dtype)
        if data[col].dtype != object:
            raise "the column dtype needs to be object"
        print("The columns dtype if object.")
        new_info = []
        for info in data[col]:
            new_info.append(str(info).replace(what_to_convert_from, to_what))
        data[col] = new_info
        print("returning the data and the list of converted info")
        return (data, new_info)

    def shuffle_data(
        self, data, how_many_times
    ) -> "Shuffled Data for how many times you wanted":
        """
        data :
            pd.DataFrame

        how_many_times :
            how many times to shuffle
        """
        for _ in range(how_many_times):
            data = data.sample(frac=1)
        return data

    def preproccessing_methods(self) -> list:
        return [
            StandardScaler,
            RobustScaler,
            MinMaxScaler,
            MaxAbsScaler,
            OneHotEncoder,
            Normalizer,
        ]


class Turn_Data_To_Batches(Dataset):
    def __init__(self, data, X, y) -> None:
        self.data = data
        self.X = X
        self.y = y
        self.len_of_data = len(data)
        print(self.len_of_data)

    def __getitem__(self, index) -> "The indexed of the data":
        return self.X[index], self.y[index]

    def __len__(self) -> "Len of the data":
        return self.len_of_data
