import pandas as pd
import numpy as np

print("A. HIERARCHICAL INDEXING")
print()

index = [
    ['Engineering', 'Engineering', 'Science', 'Science'],
    ['CSE', 'ECE', 'Physics', 'Chemistry']
]

multi_index = pd.MultiIndex.from_arrays(
    index,
    names=['Department', 'Branch']
)

marks = pd.Series(
    [85, 78, 92, 88],
    index=multi_index
)

print("Original Series:")
print(marks)

print("\nData for Engineering:")
print(marks.loc['Engineering'])

print("\nData for CSE:")
print(marks.loc[('Engineering', 'CSE')])

print("\nData for Science:")
print(marks.loc['Science'])


print("\nB. STACK AND UNSTACK")
print()

index = pd.MultiIndex.from_tuples(
    [
        ('Engineering', 'CSE'),
        ('Engineering', 'ECE'),
        ('Science', 'Physics'),
        ('Science', 'Chemistry')
    ],
    names=['Department', 'Branch']
)

data = pd.DataFrame(
    {
        '2025': [85, 78, 92, 88],
        '2026': [90, 82, 95, 91]
    },
    index=index
)

print("Original Tabular Data:")
print(data)

unstacked_data = data.unstack()

print("\nData after Unstack():")
print(unstacked_data)

stacked_data = unstacked_data.stack()

print("\nData after Stack():")
print(stacked_data)


print("\nC. MERGE AND COMBINE")
print()

df1 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Sita', 'Arun'],
        'Marks': [85, None, 78],
        'Grade': ['A', 'B', None]
    },
    index=[101, 102, 103]
)

df2 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Sita', 'Kiran'],
        'Marks': [90, 88, 82],
        'Grade': [None, 'A', 'B']
    },
    index=[101, 102, 104]
)

print("First DataFrame:")
print(df1)

print("\nSecond DataFrame:")
print(df2)

merged = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_DF1', '_DF2')
)

print("\nMerged DataFrame:")
print(merged)

combined = df1.combine_first(df2)

print("\nDataFrame after combine_first():")
print(combined)