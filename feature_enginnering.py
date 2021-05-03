import pandas as pd
import numpy as np


class FeatureEnginnering:
    def __init__(self, data, col):
        self.data = data
        self.col = col

    def feature_enginner(
        self, quantile=False, std_and_mean=False, verbose=False
    ) -> "feature enginnerd data":
        print(len(self.data))
        if quantile:
            max_no = self.data[self.col].quantile(0.99)
            min_no = self.data[self.col].quantile(0.05)
            data = self.data[self.data[self.col] < max_no]
            data = self.data[self.data[self.col] > min_no]
        if std_and_mean:
            max_no = self.data[self.col].mean() + 3 * self.data[self.col].std()
            min_no = self.data[self.col].mean() + -3 * self.data[self.col].std()
            data = self.data[self.data[self.col] < max_no]
            data = self.data[self.data[self.col] > min_no]
        print(len(data))
        return data
