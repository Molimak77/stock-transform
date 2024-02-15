from stock_transform import __version__
from stock_transform import stock_preprocess as stp
from sklearn.preprocessing import MinMaxScaler, StandardScaler 
import numpy as np
import unittest


def test_version():
    assert __version__ == '0.0.1'

    
class TestExtra_data_stock(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self):
        print("\nRunning setUp method...")
        self.obj = stp.Extra_data_stock("AAPL")
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_load_data_stock(self):
        self.assertEqual(self.obj.load_data_stock().columns[-1], 'Date')
        self.assertIsNotNone(self.obj.load_data_stock())
        
    def test_load_ndata_prediction(self):
        data = self.obj.load_ndata_prediction(90, 9)
        self.assertIsNotNone(data)
        self.assertEqual(data.columns[-1], 'Date')
        self.assertEqual(len(data), 810)
        
    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass method: Run after all test..")  
        
        
class TestVector_stock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    
    def setUp(self):
        print("\nRunning setUp method...")
        lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12, 24]
        self.obj = stp.Vector_stock(lst_vector_data, 4)
        
    def tes_getitem(self):
        self.assertEqual(len(self.obj), 11)
        self.assertEqual(self.obj[0], [1, 4, 8, 0])
        self.assertEqual(self.obj[2], [8, 11, 33, 55])
        
    def test_setitem(self):
        self.obj[3] = [11, 33, 55, 66]
        self.assertEqual(self.obj[3], [11, 33, 55, 66])
        
    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass method: Run after all test..")  
        

class TestTransform_stock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Run beffore all tests...")
        
    def setUp(self):
        print("\nRunning setUp method...")
        lst_vector_data = [1, 4, 8, 0, 7, 5, 23, 45, 7, 99, 66, 8, 12, 24]
        self.obj1 = stp.Transform_stock(lst_vector_data, 4)
        self.obj2 = stp.Transform_stock(lst_vector_data, 4)
        
    def test_add(self):
        def are_matrix_equal(matrix1, matrix2):
            return np.array_equal(matrix1, matrix2)
        
        mat = np.array([[[1.,  1.], [4.,  4.], [8.,  8.], [0.,  0.]],
                        [[4.,  4.], [8.,  8.], [0.,  0.], [7.,  7.]],
                        [[8.,  8.], [0.,  0.], [7.,  7.], [5.,  5.]],
                        [[0.,  0.], [7.,  7.], [5.,  5.], [23., 23.]],
                        [[7.,  7.], [5.,  5.], [23., 23.], [45., 45.]],
                        [[5.,  5.], [23., 23.], [45., 45.], [7.,  7.]],
                        [[23., 23.], [45., 45.], [7.,  7.], [99., 99.]],
                        [[45., 45.], [7.,  7.], [99., 99.], [66., 66.]],
                        [[7.,  7.], [99., 99.], [66., 66.], [8.,  8.]],
                        [[99., 99.], [66., 66.], [8.,  8.], [12., 12.]],
                        [[66., 66.], [8.,  8.], [12., 12.], [24., 24.]]])
        
        new_obj = self.obj1 + self.obj2
        self.assertEqual(new_obj.Xmatrix_3D.shape[0], 11)
        self.assertEqual(new_obj.Xmatrix_3D.shape[1], 4)
        self.assertEqual(new_obj.Xmatrix_3D.shape[2], 2)
        self.assertTrue(are_matrix_equal(new_obj.Xmatrix_3D, mat))
        
    def test_get_y_X_stock(self):
        def are_matrix_equal(matrix1, matrix2):
            return np.array_equal(matrix1, matrix2)
        
        mat_test = np.array([[[4.,  4.], [8.,  8.], [0.,  0.], [7.,  7.]],
                             [[8.,  8.], [0.,  0.], [7.,  7.], [5.,  5.]],
                             [[0.,  0.], [7.,  7.], [5.,  5.], [23., 23.]],
                             [[7.,  7.], [5.,  5.], [23., 23.], [45., 45.]],
                             [[5.,  5.], [23., 23.], [45., 45.], [7.,  7.]],
                             [[23., 23.], [45., 45.], [7.,  7.], [99., 99.]],
                             [[45., 45.], [7.,  7.], [99., 99.], [66., 66.]],
                             [[7.,  7.], [99., 99.], [66., 66.], [8.,  8.]],
                             [[99., 99.], [66., 66.], [8.,  8.], [12., 12.]],
                             [[66., 66.], [8.,  8.], [12., 12.], [24., 24.]]]
                            )
        new_obj = self.obj1 + self.obj2
        y, X = new_obj.get_y_X_stock()
        res = [1.0, 4.0, 8.0, 0.0, 7.0, 5.0, 23.0, 45.0, 7.0, 99.0]
        self.assertEqual(y, res)
        self.assertTrue(are_matrix_equal(X, mat_test))
        
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
      
class TestStock_processing(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
        
    def setUp(self):
        print("\nRunning setUp method...")
        self.obj_stock = stp.Stock_processing('AAPL', start="2023-01-01",
                                              end_date="2023-03-01"
                                              )
        
    def tearDown(self):
        print("Running tearDown method...")
    
    def test_stock_market_data(self):
        name_col = ['data_Open', 'data_Close',
                    'data_High', 'data_Low',
                    'data_Volume'
                    ]
        dico_data = self.obj_stock.stock_market_data()
        self.assertEqual(len(dico_data), 5)
        for uu in dico_data.keys():
            self.assertIsNotNone(dico_data[uu])
            self.assertEqual(dico_data[uu].columns[-1], 'Date')
            self.assertEqual(list(dico_data.keys()), name_col)
            
    def test_tranf_featur_scaling(self):
        dico_obj_stock = self.obj_stock.stock_market_data()
        new_array = np.array(dico_obj_stock['data_Low']["Low"]).reshape(39, 1)
        new_array_scaling = MinMaxScaler().fit_transform(new_array)
        new_list = list(new_array_scaling.flatten())
        data_scaling, fct_scaler = self.obj_stock.transf_featur_scaling()
        new_scaler_byobj = data_scaling['datLow']
        
        new_array_lst = np.array(new_list).reshape(39, 1)
        first_data_low = fct_scaler['fct_scalinLow'].inverse_transform(
            new_array_lst
            )
        anc_array_low = np.array(
            dico_obj_stock['data_Low']['Low']).reshape(39, 1)
        vec1 = list(np.round(first_data_low, 6)[:, 0])
        vec2 = list(np.round(anc_array_low, 6)[:, 0])
        
        self.assertEqual(len(dico_obj_stock), 5)
        self.assertEqual(
            self.obj_stock.transf_featur_scaling()[0]['datLow'], new_list
            )
        self.assertEqual(new_scaler_byobj, new_list)
        self.assertEqual(vec1, vec2)
        