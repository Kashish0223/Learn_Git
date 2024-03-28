import pandas as pd

#Series 

fruits = ['kiwi','grapes','mango','cheery']
s = pd.Series(fruits)
print(s)

#DataFrame

data = {"calories":[100,200,300],"weight":[55,45,30]}
df = pd.DataFrame(data)
print(df)
