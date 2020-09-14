import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = {'TID': ['T100', 'T200', 'T300', 'T400', 'T500', 'T600'],
                    'Items Bought': [('E', 'K', 'M', 'N', 'O'), 
                                     ('D', 'E', 'K', 'N', 'O', 'Y'),
                                     ('A', 'E', 'K', 'M'),
                                     ('C', 'K', 'M', 'U', 'Y'),
                                     ('C', 'E', 'I', 'K', 'O'), 
                                     ('B', 'K', 'O')]}
data = pd.DataFrame(data = d)

print(data.head())
