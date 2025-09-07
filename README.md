# Python Programming Assignment
### This repository contains the following Programming Assignments:

## Problem 1
### In this section, we are tasked to do the following:
### a) Load the corresponding .csv file into a data frame named cars using pandas
### b) Display the first five and last five rows of the resulting cars.

### Link: https://github.com/gabriel-marygraceclare/EXPERIMENT-3---PYTHON-DATA-ANALYSIS-PANDAS-/blob/main/Gabriel_Pandas-P1.py.ipynb

### 1. I started with importing the pandas library as pd.
```python
import pandas as pd
```
### 2. Then load the file "cars.csv" into a pandas data frame named cars. Then it displayed the datas in tabular.
```python
cars = pd.read_csv('cars.csv')
```
### 3. Then display the output of cars' entire data frame to view all the loaded data from the CSV file.
```python
cars
```
### 4. Then used .head() to display the first 5 rows of the data frame.
```python
cars.head() 
```
### 5. And .tail() to display the last 5 rows of the data frame.
```python
cars.tail() 
```

## Problem 2
### In this section, we are tasked to do the following:
### a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
### b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
### c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
### d)  Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Link: 

### 1. I started with importing the pandas library as pd.
```python
import pandas as pd
```
### 2. Then load the file "cars.csv" into a pandas data frame named cars. Then it displayed the datas in tabular.
```python
cars = pd.read_csv('cars.csv')
```
### 3. Then display the output of cars' entire data frame to view all the loaded data from the CSV file.
```python
cars
```
### 4. Then used .iloc to get the first 5 rows and the odd-numbered columns.
```python
cars_oddnumbers = cars.iloc[:5, [1, 3, 5, 7, 9, 11]]
cars_oddnumbers
```
### 5. Then used .loc to display the specified row at index 0 and selected all the key columns to show the complete details of the car.
```python
cars_oddnumbers = cars.iloc[:5, [1, 3, 5, 7, 9, 11]]
cars_oddnumbers
```
### 6. Right after, we then filtered the data to select the row where the model is "Camaro Z28" and take the value of the cyl for that specific model. And then display the result.
```python
camaro = cars[cars['Model'] == 'Camaro Z28']
cylinders = camaro['cyl'].values[0]
print(f"The car model Camaro Z28 has {cylinders} cylinders.")
```
### 7. Lastly, used .loc to access the specific row indicated by indexes and selected columns. After that, we print the result.
```python
specific_cars = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
specific_cars

```
