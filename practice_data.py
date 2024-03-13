#!/usr/bin/env python

import pandas as pd

# Constants
HEALTH_BOARD = 'S08000029'
PRACTICE = 21261

practices_in_scotland = pd.read_csv('practice.csv')
number_of_practices_in_scotland = practices_in_scotland.shape[0]
practices_in_fife = practices_in_scotland.loc[(practices_in_scotland['HB'] == HEALTH_BOARD)]
number_of_practices_in_fife = practices_in_fife.shape[0]
scoonie = practices_in_scotland.loc[(practices_in_scotland['PracticeCode'] == PRACTICE)]

# calculate average practice list size and std (number of patients registered with the practice)
print("Mean number of patients per practice")
print(int(round(practices_in_scotland.loc[:, 'PracticeListSize'].mean())))
print("Std for number of patients per practice")
print(int(round(practices_in_scotland.loc[:, 'PracticeListSize'].std())))
print("Number all patients in Scotland")
print(int(round(practices_in_scotland.loc[:, 'PracticeListSize'].sum())))
print("Number all patients in Fife")
print(int(round(practices_in_fife.loc[:, 'PracticeListSize'].sum())))
print("Median number of patients per practice")
print(int(round(practices_in_scotland.loc[:, 'PracticeListSize'].median())))


# check Scoonie practice size
print("Number of patients in Scoonie Practice")
print(scoonie.PracticeListSize.to_string(index=False))

# print data
print("number of practices in Scotland " + str(number_of_practices_in_scotland))
print("number of practices in Fife " + str(number_of_practices_in_fife))
