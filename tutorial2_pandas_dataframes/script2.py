import pandas as pd
import numpy as np


if False:
	data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
               
	the_values = data[1:,1:]
	print("the_values data type is: " + str(type(the_values)))
	
	#the_row_labels = data[1:,0]
	the_row_labels = ['Fred', 'Barney']
	print("the_row_labels data type is: " + str(type(the_row_labels)))
	
	#the_column_labels = data[0,1:]
	the_column_labels = ['JCol1', 'JCol2']
	print("the_column_labels data type is: " + str(type(the_column_labels)))
	
	#my_panda_dataframe = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])
	my_panda_dataframe = pd.DataFrame(the_values, the_row_labels, the_column_labels)
	print(my_panda_dataframe)
	print()
	
	#np.concatenate(the_values, [[10,20]])
	#np.concatenate(the_values, [10,20])
	#np.concatenate(the_values, np.array([10,20]))
	#np.concatenate(the_values, np.array([[10,20]]))
	
	
	# Take a 2D array as input to your DataFrame 
	my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
	df1 = pd.DataFrame(my_2darray)
	print(df1)
	print()
	
	# Take a dictionary as input to your DataFrame 
	my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
	df2= pd.DataFrame(my_dict)
	print(df2)
	print()
	
	# Take a DataFrame as input to your DataFrame 
	my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
	df3 = pd.DataFrame(my_df)
	print(df3)
	print()
	
	# Take a Series as input to your DataFrame
	my_series = pd.Series({"Belgium":"Brussels", "India":"New Delhi", "United Kingdom":"London", "United States":"Washington"})
	df4 = pd.DataFrame(my_series)
	print(df4)
	print()
	
	print("df4 is a: " + str(type(df4)))
	cols = my_panda_dataframe.columns
	print("cols is a: " + str(type(cols)))
	vals = cols.values
	print("vals is a: " + str(type(vals)))
	print(vals)
	print(list(vals))
	
		
	df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'], index=['foo', 'bar', 'baz'])
	print("-- df with ugly index values --")
	print(df)
	print()
	
	df.reset_index(level=0, drop=True, inplace=True)
	print("-- df after reset_index --")
	print(df)
	print()
	
	df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'], index=['foo', 'bar', 'baz'])
	print("-- df with ugly index values --")
	print(df)
	print()
	
	anotherdf = df.reset_index(level=0, drop=True, inplace=False)
	print("-- df after reset_index with inplace False --")
	print(df)
	print()
	
	print("-- anotherdf, which is the output of reset_index --")
	print(anotherdf)
	print()
	

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), 
                  index= [2.5, 12.6, 4.8, 4.8, 2.5], 
                  columns=[48, 49, 50])
       
print("before")
print(df)
print()
anotherdf = df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')

print("after")
print(anotherdf)
print()
