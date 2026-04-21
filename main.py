import pandas as pd

def main():
    # Load the dataset
    df = pd.read_csv('data.csv')
    
    # Display the first few rows of the dataset
    print(df.head())
    
    # Perform some basic analysis
    print("Summary statistics:")
    print(df.describe())
    
    # Check for missing values
    print("Missing values:")
    print(df.isnull().sum())

    
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

print('-----------------------------')

mydataset2 = [
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Peter", "age": 34, "city": "Berlin"}
]
myvar2 = pd.DataFrame(mydataset2)
print(myvar2[myvar2['age'] > 25])