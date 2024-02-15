import numpy as np
import pandas as pd
from tqdm import tqdm
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import yfinance as yf
from datetime import date


class Extra_data_stock:
    def __init__(self, tiker: str, start="2000-01-01", end_date=None):
        if end_date is None:
            end_date1 = date.today()
        else:
            end_date1 = end_date
        self.stock = tiker
        self.start_date = start
        self.end_date = end_date1
        self.name = ["Open", "Close", "High", "Low", "Volume"]

    def load_data_stock(self):
        try:
            data = yf.download(
                self.stock, start=self.start_date, end=self.end_date, prepost=True
            )
            data["date"] = data.index
            data["Date"] = data["date"].apply(
                lambda x: pd.to_datetime(str(x)).strftime("%d/%m/%Y")
            )
            data = data.reset_index(drop=True)
            data = data.drop(columns="date")
            return data
        except Exception as e:
            print(f"Error loading data {str(e)}")
            return None

    def load_ndata_prediction(self, timestep: int, nlast_prediction_days=1):
        dataload = self.load_data_stock()
        if dataload is not None:
            data_nlastpreddays = dataload.tail(
                nlast_prediction_days * timestep
                )
            return data_nlastpreddays
        else:
            return None


class Vector_stock:
    def __init__(self, list_data: list, step: int):
        if len(list_data) < step or step < 1:
            raise ValueError(f"step : {step} is uper len of list or equal 0")
        else:
            self.vector = list_data
            self.step = step

    def __getitem__(self, i: int):
        if i < 0 or i >= (len(self.vector) - self.step + 1):
            raise Exception(f"The index {i} is out bornes")
        else:
            return self.vector[i : (i + self.step)]

    def __setitem__(self, i: int, x: list):
        if i < 0 or i >= (len(self.vector) - self.step + 1):
            raise Exception(f"The index {i} is out bornes")
        else:
            if len(x) != self.step:
                raise Exception(f"length of list {x} is not equal: {self.step}")
            else:
                self.vector[i : (i + self.step)] = x

    def __len__(self):
        return len(self.vector) - self.step + 1

    def __iter__(self):
        n = self.__len__()
        i = 0
        while i < n:
            yield self.__getitem__(i)
            i += 1

    def __str__(self):
        return f"object : {self.vector}, step : {self.step}"


class Transform_stock(Vector_stock):
    def __init__(self, list_data: list, step: int):
        super().__init__(list_data, step)
        n = len(self)
        matrix = np.zeros((n, self.step))
        i = 0
        for uu in tqdm(self):
            matrix[i] = uu
            i += 1
        self.Xmatrix_3D = np.reshape(matrix, (matrix.shape[0], matrix.shape[1], 1))

    def __add__(self, obj):
        mat_modif1 = self.Xmatrix_3D
        mat_modif2 = obj.Xmatrix_3D
        n1 = mat_modif1.shape
        n2 = mat_modif2.shape
        if n1[0] != n2[0] or n1[1] != n2[1]:
            raise ValueError("the both objects haven't the same shape")
        else:
            matf = np.concatenate((mat_modif1, mat_modif2), axis=2)
            self.Xmatrix_3D = matf
            return self

    def get_y_X_stock(self, i=0):
        matrix = self.Xmatrix_3D[:, :, i]
        y = list(matrix[:, 0])[:-1]
        X = np.delete(self.Xmatrix_3D, 0, axis=0)
        return y, X


class Stock_processing(Extra_data_stock):
    def __init__(self, tiker: str, start="2000-01-01", end_date=None):
        super().__init__(tiker, start, end_date)

    def stock_market_data(self):
        dico_data = {}
        data = self.load_data_stock()
        for uu in self.name:
            dico_data["data_" + str(uu)] = data.loc[:, [str(uu), "Date"]]

        return dico_data

    def graph_stock(self, indicator=1):
        """1: open, 2: high, 3: low, 4: close, 5 : volume, 6: all"""
        dico_data = self.stock_market_data()
        if indicator == 1:
            df = dico_data["data_Open"]
            fig = px.line(
                df, x="Date", y="Open", title=f"Tiker: {self.stock}, value: Open"
            )
            fig.show()
        elif indicator == 2:
            df = dico_data["data_High"]
            fig = px.line(
                df, x="Date", y="High", title=f"Tiker: {self.stock}, value: High"
            )
            fig.show()
        elif indicator == 3:
            df = dico_data["data_Low"]
            fig = px.line(
                df, x="Date", y="Low", title=f"Tiker: {self.stock}, value: Low"
            )
            fig.show()
        elif indicator == 4:
            df = dico_data["data_Close"]
            fig = px.line(
                df, x="Date", y="Close", title=f"Tiker: {self.stock}, value: Close"
            )
            fig.show()
        elif indicator == 5:
            df = dico_data["data_Volume"]
            fig = px.line(
                df, x="Date", y="Volume", title=f"Tiker: {self.stock}, value: Volume"
            )
            fig.show()

    @staticmethod
    def feature_scaling(df, name: str, type=1):
        df1 = df[name]
        data_arr = np.array(df1).reshape(df1.size, 1)
        if type == 1:
            fct_scaling = MinMaxScaler().fit(data_arr)
            data_scaler = fct_scaling.transform(data_arr)
            data_scaler1 = list(data_scaler.flatten())
        else:
            fct_scaling = StandardScaler().fit(data_arr)
            data_scaler = fct_scaling.transform(data_arr)
            data_scaler1 = list(data_scaler.flatten())
        return data_scaler1, fct_scaling

    def transf_featur_scaling(self, type=1):
        """feature scaling if type :1 mimaxscaler 2: standard scaler"""
        dico_data = self.stock_market_data()
        dico_data_scaling = {}
        dico_scler = {}
        key = dico_data.keys()
        for name_k in key:
            dfr = dico_data[name_k]
            name_columns = dfr.columns[0]
            dfr1, fct_featurScaling = self.feature_scaling(dfr, name_columns, type=type)
            dico_data_scaling["dat" + name_columns] = dfr1
            dico_scler["fct_scalin" + name_columns] = fct_featurScaling
        return dico_data_scaling, dico_scler
