import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

d = {'TID': ['T100', 'T200', 'T300', 'T400', 'T500', 'T600'],
                    'Items Bought': [['E', 'K', 'M', 'N', 'O'], 
                                     ['D', 'E', 'K', 'N', 'O', 'Y'],
                                     ['A', 'E', 'K', 'M'],
                                     ['C', 'K', 'M', 'U', 'Y'],
                                     ['C', 'E', 'I', 'K', 'O'], 
                                     ['B', 'K', 'O']]}

data = pd.DataFrame(data = d)
rowCount = (len(data.index) / 2)
data = data.explode('Items Bought') # Turns list into individual items
counts = data.groupby('Items Bought').count()
counts = counts.rename(columns = {'Items Bought': 'Item', 'TID': 'Count'})

filtered = counts[counts['Count'] > rowCount]
print(filtered)
print(rowCount)

