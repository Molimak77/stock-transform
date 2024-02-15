# stock-transform
Package that provides to do the all necessary transformation to preparing the historical data of a stock ticker for train of a deep learning model

### Purpose of the package
+ The package provides the methods to load the historical data of the stock tickers comes from the yahoo finance, transforming the data according to the timestep. Creates the data matrix in 3 dimensions  and creates the target (y) and the input variables X. 

### Features 
+ The collection of the class and methods of the package. 

    - Extra\_data\_stock
        * load\_data\_stock()
        * load\_ndata\_prediction()
    - Vector\_stock 
    - Transform\_stock
        * \_add\_
        * \_iter\_
        * get\_y\_X\_stock() 
    - Stock\_processing

### Getting Started
The package is found on github or Azure factory you can install using ....

### Installation 
```terminal
pip install git+https://github.com/jkbr/httpie.git#egg=httpie
```
### Usage

""" Extra_data_stock : class to provide the method to loading the data from the yahoo finance  

Params:
------
tiker: str, the name of the symbole  
start: the date to start default, default: "2000-01-01", 
end_date: The date of the end, default: now

Usage: 
------

>>> obj_extra_data_stock = Extra_data_stock("AAPL")

"""

""" load_data_stock : the method of the class Extra_data_stock which to provide  load the data of the stock market  

Params:
------

self: object of the class Extra_data_stock

Usage:
-----

>>> obj_extra_data_stock = Extra_data_stock("AAPL")
>>> df = obj_extra_data_stock.load_data_stock()
>>> df.head()

"""

""" load_ndata_prediction: the method of the class Extra_data_stock which to provide
load the prediction data (the n last days)

Params:
------
timestep : the prediction periode
nlast_prediction_days : the n last day of the prediction

Usage:
----- 

>>> obj_extra_data_stock = Extra_data_stock("AAPL")
>>> df = obj_extra_data_stock.load_ndata_prediction(90,9)
>>> df.head()

"""

""" Vector_stock : the class to provide the methodes to manipulate the list of the stock tickers

Params:
-------
list_data : the list containing the values of the stock ticker on the market
step : the periode which considerate as the memory of the time series 

Usage:
-----

>>> values_list = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12, 24]
>>> objet_vector_stock = Vector_stock(values_list, 4)

"""

""" Vector_stock : the class that treates the list of the data (stock ticker of the market)

Params:
------
list_data: the list of the data 
step: the len of the periode

Usage:
------

>>> lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 , 24]
>>> obj = Vector_stock(lst_vector_data, 4)
>>> len(obj) 
>>> obj[0]
>>> obj[3] = [11, 22, 44, 33]
>>> print(obj)
>>> for uu in obj:
    print(uu)

"""


"""Transform_stock : the class which transforms the data stock as matrix of the aviriables 

Params:
------
list_data: list contains the value of the stock ticker
step: the timestep or the memory of the time series

Usage:
-----

>>> lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 , 24]

"""

""" get_y_X_stock: method of the class Transform_stock which extracts the matrix X and the outcom y of data

Params:
-------
self: the object of the class Transform_stock
i: the rank of the to extract the y 

Usage:
------

>>> obj1 = Transform_stock(lst_vector_data,4)
>>> obj2 = Transform_stock(lst_vector_data,4)
>>> new_obj = obj1 + obj2
>>> new_obj = new_obj.Xmatrix_3D
>>> y_train, X_train = new_obj.get_y_X_stock() 

"""

"""Stock_processing : class which provides transformation of the stock ticker variable 

Params:
------
tiker : symbol of the tiker on the market
start : the date to starting the load the historical data of a stock ticker 
end_date : the date of the end of the data hystory 

Usage:
-----

>>> obj_stock = Stock_processing('AAPL', start="2023-01-01", end_date="2023-03-01")

"""

"""stock_market_data: the method of the class Stock_processing to loading the historical data 

Params:
------

self: object of the Stock_processing

Usage:
------

>>> dico_obj_stock = obj_stock.stock_market_data()

"""

""" graph_stock: the method that represente graphicaly the differente indicators associate to stock tickers

Params:
------
indicators: 1: open, 2: high, 3: low, 4: close, 5 : volume

Usage:
------
>>> obj_stock.graph_stock(1)

"""

""" feature_scaling: the static method of the class Stock_processing

Params:
------

df: dataframe of the stock tickers 
name: name of the indicator or variable 
type: to indicate the mthod 1:MinMaxScaler or 2:StandardScaler

Usage:
------

None

"""

"""transf_featur_scaling: method of the class Stock_processing that transforms data 

Params:
------
type: indicate 1:MinMaxScaler or 2:StandardScaler by the default is 1

Usage:
------

>>> len(dico_obj_stock)
>>> data_scaler, fct_scaler = obj_stock.tranf_featur_scaling()
>>> new_scaler_byobj = data_scaler['datLow']

"""

### Contribution 
Contributions are welcon 
Notice a bug let us know. 
Thanks!

### Author
+ Main Maintainer: Molière Nguile-makao
+ moliere.nguile@gmail.com
