# Copyright (C) 2024, SIESTA project (WP15 and WP10)

import numpy as np
import pandas as pd
from pydp.algorithms.laplacian import BoundedMean

inputfile = pd.read_csv("participants.tsv", sep="\t")
inputfile = inputfile.dropna()
print(inputfile.head())

# use the column names and capitalization from the original dataset
# ignore missing values
averaged_age = np.mean(inputfile['age'].values)
averaged_height = np.mean(inputfile['Height'].values)
averaged_weight = np.mean(inputfile['Weight'].values)

# construct table with results
result = pd.DataFrame({
    'averagedage': [averaged_age],
    'averagedHeight': [averaged_height],
    'averagedWeight': [averaged_weight]
})
print(result)

epsilon = 1
age = BoundedMean(
    epsilon=epsilon,
    lower_bound=min(inputfile['age'].values),
    upper_bound=max(inputfile['age'].values)
)
dp_mean_age = age.quick_result(inputfile['age'].values)
print(f'AGE: \n \t Real mean:{averaged_age} \n \t Mean with DP: {dp_mean_age}')

height = BoundedMean(
    epsilon=epsilon,
    lower_bound=min(inputfile['Height'].values),
    upper_bound=max(inputfile['Height'].values),
    dtype="float"
)
dp_height_age = height.quick_result(inputfile['Height'].values)
print(f'Height: \n \t Real mean:{averaged_height} \n \t Mean with DP: {dp_height_age}')

weight = BoundedMean(
    epsilon=epsilon,
    lower_bound=min(inputfile['Weight'].values),
    upper_bound=max(inputfile['Weight'].values),
    dtype="float"
)
dp_weight_age = height.quick_result(inputfile['Weight'].values)
print(f'Weight: \n \t Real mean:{averaged_weight} \n \t Mean with DP: {dp_weight_age}')

# AGE:
#         Real mean:19.897959183673468
#         Mean with DP: 19.75
# Height:
#         Real mean:164.8704081632653
#         Mean with DP: 159.41681926793166
# Weight:
#         Real mean:60.26938775510204
#         Mean with DP: 56.96018377382619

