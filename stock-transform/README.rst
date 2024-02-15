stock-transform
===============

Package that provides to do the all necessary transformation to
preparing the historical data of a stock ticker for train of a deep
learning model

Purpose of the package
----------------------

-  The package provides the methods to load the historical data of the
   stock tickers comes from the yahoo finance, transforming the data
   according to the timestep. Creates the data matrix in 3 dimensions
   and creates the target (y) and the input variables X.

Features
--------

-  The collection of the class and methods of the package.

   -  Extra_data_stock

      -  load_data_stock()
      -  load_ndata_prediction()

   -  Vector_stock
   -  Transform_stock

      -  \_add\_
      -  \_iter\_
      -  get_y_X_stock()

   -  Stock_processing

Getting Started
---------------

The package is found on github or Azure factory you can install using ….

Installation
------------

.. code:: terminal

   pip install git+https://github.com/jkbr/httpie.git#egg=httpie

Usage
-----

““” Extra_data_stock : class to provide the method to loading the data
from the yahoo finance

Params:
-------

| tiker: str, the name of the symbole
| start: the date to start default, default: “2000-01-01”, end_date: The
  date of the end, default: now

.. _usage-1:

Usage:
------

         obj_extra_data_stock = Extra_data_stock(“AAPL”)

““”

““” load_data_stock : the method of the class Extra_data_stock which to
provide load the data of the stock market

.. _params-1:

Params:
-------

self: object of the class Extra_data_stock

.. _usage-2:

Usage:
------

         obj_extra_data_stock = Extra_data_stock(“AAPL”) df =
         obj_extra_data_stock.load_data_stock() df.head()

““”

““” load_ndata_prediction: the method of the class Extra_data_stock
which to provide load the prediction data (the n last days)

.. _params-2:

Params:
-------

timestep : the prediction periode nlast_prediction_days : the n last day
of the prediction

.. _usage-3:

Usage:
------

         obj_extra_data_stock = Extra_data_stock(“AAPL”) df =
         obj_extra_data_stock.load_ndata_prediction(90,9) df.head()

““”

““” Vector_stock : the class to provide the methodes to manipulate the
list of the stock tickers

.. _params-3:

Params:
-------

list_data : the list containing the values of the stock ticker on the
market step : the periode which considerate as the memory of the time
series

.. _usage-4:

Usage:
------

         values_list = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12, 24]
         objet_vector_stock = Vector_stock(values_list, 4)

““”

““” Vector_stock : the class that treates the list of the data (stock
ticker of the market)

.. _params-4:

Params:
-------

list_data: the list of the data step: the len of the periode

.. _usage-5:

Usage:
------

         lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 ,
         24] obj = Vector_stock(lst_vector_data, 4) len(obj) obj[0]
         obj[3] = [11, 22, 44, 33] print(obj) for uu in obj: print(uu)

““”

“““Transform_stock : the class which transforms the data stock as matrix
of the aviriables

.. _params-5:

Params:
-------

list_data: list contains the value of the stock ticker step: the
timestep or the memory of the time series

.. _usage-6:

Usage:
------

         lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 ,
         24]

““”

““” get_y_X_stock: method of the class Transform_stock which extracts
the matrix X and the outcom y of data

.. _params-6:

Params:
-------

self: the object of the class Transform_stock i: the rank of the to
extract the y

.. _usage-7:

Usage:
------

         obj1 = Transform_stock(lst_vector_data,4) obj2 =
         Transform_stock(lst_vector_data,4) new_obj = obj1 + obj2
         new_obj = new_obj.Xmatrix_3D y_train, X_train =
         new_obj.get_y_X_stock()

““”

“““Stock_processing : class which provides transformation of the stock
ticker variable

.. _params-7:

Params:
-------

tiker : symbol of the tiker on the market start : the date to starting
the load the historical data of a stock ticker end_date : the date of
the end of the data hystory

.. _usage-8:

Usage:
------

         obj_stock = Stock_processing(‘AAPL’, start=“2023-01-01”,
         end_date=“2023-03-01”)

““”

“““stock_market_data: the method of the class Stock_processing to
loading the historical data

.. _params-8:

Params:
-------

self: object of the Stock_processing

.. _usage-9:

Usage:
------

         dico_obj_stock = obj_stock.stock_market_data()

““”

““” graph_stock: the method that represente graphicaly the differente
indicators associate to stock tickers

.. _params-9:

Params:
-------

indicators: 1: open, 2: high, 3: low, 4: close, 5 : volume

.. _usage-10:

Usage:
------

         obj_stock.graph_stock(1)

““”

““” feature_scaling: the static method of the class Stock_processing

.. _params-10:

Params:
-------

df: dataframe of the stock tickers name: name of the indicator or
variable type: to indicate the mthod 1:MinMaxScaler or 2:StandardScaler

.. _usage-11:

Usage:
------

None

““”

“““transf_featur_scaling: method of the class Stock_processing that
transforms data

.. _params-11:

Params:
-------

type: indicate 1:MinMaxScaler or 2:StandardScaler by the default is 1

.. _usage-12:

Usage:
------

         len(dico_obj_stock) data_scaler, fct_scaler =
         obj_stock.tranf_featur_scaling() new_scaler_byobj =
         data_scaler[‘datLow’]

““”

Contribution
~~~~~~~~~~~~

Contributions are welcon Notice a bug let us know. Thanks!

Author
~~~~~~

-  Main Maintainer: Molière Nguile-makao
-  moliere.nguile@gmail.com
