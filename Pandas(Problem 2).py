import pandas as pd
cars=pd.read_csv('cars.csv.mdlp')
carsa=cars.iloc[0:5,[0,2,4,6,8,10]]
carsb=cars.iloc[0]
carsc=cars.loc[23,'cyl']
carsd=cars.loc[[1,28,18],['Model','cyl','gear']]