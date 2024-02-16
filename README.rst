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

Use class Extra_data_stock: to provide the method to loading the data
from the yahoo finance

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_extra_data_stock = stp.Extra_data_stock("AAPL")

Use class load_data_stock: the method of the class Extra_data_stock
which to provide load the data of the stock market

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_extra_data_stock = stp.Extra_data_stock("AAPL")
   >>> df = obj_extra_data_stock.load_data_stock()
   >>> df.head()

Use the method load_ndata_prediction: the method of the class
Extra_data_stock which to provide load the prediction data (the n last
days)

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_extra_data_stock = stp.Extra_data_stock("AAPL")
   >>> df = obj_extra_data_stock.load_ndata_prediction(90,9)
   >>> df.head()

Use class Vector_stock : the class to provide the methodes to manipulate
the list of the stock tickers

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> values_list = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12, 24]
   >>> objet_vector_stock = stp.Vector_stock(values_list, 4)

Use Vector_stock: the class that treates the list of the data (stock
ticker of the market)

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 , 24]
   >>> obj = stp.Vector_stock(lst_vector_data, 4)
   >>> len(obj) 
   >>> obj[0]
   >>> obj[3] = [11, 22, 44, 33]
   >>> print(obj)
   >>> for uu in obj:
            print(uu)

Use Transform_stock: the class which transforms the data stock as matrix
of the aviriables

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12 , 24]
   >>> objet_vector_stock = stp.Vector_stock(lst_vector_data, 4)

Use get_y_X_stock: method of the class Transform_stock which extracts
the matrix X and the outcom y of data

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj1 = stp.Transform_stock(lst_vector_data,4)
   >>> obj2 = stp.Transform_stock(lst_vector_data,4)
   >>> new_obj = obj1 + obj2
   >>> new_obj = new_obj.Xmatrix_3D
   >>> y_train, X_train = new_obj.get_y_X_stock() 

Use Stock_processing: class which provides transformation of the stock
ticker variable

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_stock = stp.Stock_processing('AAPL', start="2023-01-01", end_date="2023-03-01")

Use stock_market_data: the method of the class Stock_processing to
loading the historical data

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_stock = stp.Stock_processing('AAPL', start="2023-01-01", end_date="2023-03-01")
   >>> dico_obj_stock = obj_stock.stock_market_data()

Use graph_stock: the method that represente graphicaly the differente
indicators associate to stock tickers

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_stock = stp.Stock_processing('AAPL', start="2023-01-01", end_date="2023-03-01")
   >>> obj_stock.graph_stock(1)

Use transf_featur_scaling: method of the class Stock_processing that
transforms data

.. code:: python

   >>> from stock_transform import stock_preprocess as stp
   >>> obj_stock = stp.Stock_processing('AAPL', start="2023-01-01", end_date="2023-03-01")
   >>> len(obj_stock)
   >>> data_scaler, fct_scaler = obj_stock.tranf_featur_scaling()
   >>> new_scaler_byobj = data_scaler['datLow']

Contribution\`
--------------

Contributions are welcon Notice a bug let us know. Thanks!

Author
------

-  Main Maintainer: Molière Nguile-makao
-  moliere.nguile@gmail.com
