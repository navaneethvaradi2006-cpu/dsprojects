# DATA SCIENCE - 22DS102006

# Experiment 5 - Data Wrangling

## Aim

To perform data wrangling operations using Pandas, including hierarchical indexing, stack and unstack operations, index-based merging, and combining overlapping data using combine_first().

## Topics Covered

1. Hierarchical Indexing
2. Partial Indexing
3. Stack and Unstack
4. Index-Based Merge
5. combine_first()

---

## A. Hierarchical Indexing

### Aim

To create a Pandas Series with hierarchical multi-level indexing and select subsets of data using partial indexing.

### Program

```python
import pandas as pd

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

print(marks)
print(marks.loc['Engineering'])
print(marks.loc[('Engineering', 'CSE')])
print(marks.loc['Science'])