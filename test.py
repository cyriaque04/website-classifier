import pandas as pd
import numpy as np

# # a = np.array((1,2,3))
# # b = np.array((1,3,4))

# # c = np.where(a==b)
# # print("\n", c)

# b = np.array([0,1,2])
# c = np.array([0,7,3])
# a = np.where(b != c)[0]
# print(a)


#### iloc ####

# df = pd.DataFrame({"values" : [10,20,30,40]})
# df_test = df.iloc[[1,2]]
# print(df_test)



#### iloc ####

# df = pd.DataFrame({"values" : [10,20,30,40]})
# values_to_keep = [20,30]
# mask = df["values"].isin(values_to_keep)
# print("\nmask: \n\n", mask)
# print("\nresult: \n\n", df[mask])


#### loc ####

# df = pd.DataFrame({
#     'City':    ['Paris', 'Berlin', 'Rome',  'Madrid', 'Lisbon'],
#     'Temp_C':  [25,      22,       28,      30,       26],
#     'Weather': ['sunny', 'cloudy', 'rainy','sunny',  'cloudy']
# }, index=['a','b','g','d','e'])

# print(df.loc["g", "Temp_C"])



