import pandas as pd
iris = pd.read_csv('iris.csv')
##Task1
missing_data = iris.isnull().sum()
print(missing_data)

##TASK2
duplicates = iris.duplicated()
duplicate_rows = iris[duplicates]
print(duplicate_rows)

iris['SepalArea'] = iris['SepalLengthCm'] * iris['SepalWidthCm']
iris['PetalArea'] = iris['PetalLengthCm'] * iris['PetalWidthCm']
iris['TotalArea'] = iris['SepalArea'] + iris['PetalArea']
print(iris['TotalArea'])

missing_data = iris.isnull().sum()
print(missing_data)

##TASK3
speciesMapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
iris['SpeciesNumerical'] = iris['Species'].map(speciesMapping)
print(iris['SpeciesNumerical'])

aggregatedData = iris.groupby('Species')[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].sum()
print(aggregatedData)

##Task4

longFormat = iris.melt(id_vars=['Species', 'SpeciesNumerical'], 
                        value_vars=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
                        var_name='attribute', value_name='value')

print(longFormat.head())

