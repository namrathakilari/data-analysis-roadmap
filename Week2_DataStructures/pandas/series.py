import pandas as pd
fruit_protein = {
    "Avocado": 2.0,       
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}
s2=pd.Series(fruit_protein,name='Protein')
print(s2)

#conditional selection
print(s2>1) #boolean
print(s2[s2>1.5]) # fruits names with their values greater than 1.5
print(s2[(s2>0.5)& (s2<2)]) # and operation
print(s2[~(s2>1)]) #not operation
s2['Mango']=2.8 #modifying
