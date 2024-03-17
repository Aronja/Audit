#!/usr/bin/env python

import pandas as pd

# Constants
HEALTH_BOARD = 'S08000029'
PRACTICE = 21261

june = pd.read_csv('June.csv')
oct = pd.read_csv('October.csv')

# define prescribing data for GP practice
scoonie_june = june.loc[june['GPPractice'] == PRACTICE]
scoonie_oct = oct.loc[oct['GPPractice'] == PRACTICE]

# define prescribing data for Heathboard
hb_june = june.loc[june['HBT'] == HEALTH_BOARD]
hb_oct = oct.loc[oct['HBT'] == HEALTH_BOARD]

def find_relevant_drugs(df):
    '''finds the relevant drugs for a given dataframe'''
    filtered_df = df.loc[
(df['BNFItemCode'] == '1306010Z0BBAAAA') # Epiduo 0.1%
| (df['BNFItemCode'] == '1306010Z0BBABAB') # Epiduo 0.3%
| (df['BNFItemCode'] == '1306010H0AAABAB') # Adapalene Cream
| (df['BNFItemCode'] == '1306010H0AAAAAA') # Adapalene Gel
| (df['BNFItemCode'] == '1306010H0BBABAB') # Differin 0.1% Cream
| (df['BNFItemCode'] == '1306010I0BFAAAF') # Aknemycin plus
| (df['BNFItemCode'] == '1306010ABBBAAAA') # Treclin 1%/0.0.25%
| (df['BNFItemCode'] == '1306010ABAAAAAA')] # Clindamycin 1% /Tretinoin 0.025% Cream

def print_data(df, month, comparison):
    print('prescribed in ' + month + ' in ' + comparison)
    print(calculate_total_number_of_prescribed_items(df))
    #print(df)

def calculate_total_number_of_prescribed_items(df):
    return df.sum(numeric_only = True)

# drugs prescribed in the practice
practice_prescriptions_june = find_relevant_drugs(scoonie_june)
print_data(practice_prescriptions_june, "June", "Scoonie")
practice_prescriptions_oct = find_relevant_drugs(scoonie_oct)
print_data(practice_prescriptions_oct, "October", "Scoonie")

# drugs prescribed in the Healthboard
hb_prescriptions_june = find_relevant_drugs(hb_june)
print_data(hb_prescriptions_june, "June", "Healthboard")
hb_prescriptions_oct = find_relevant_drugs(hb_oct)
print_data(hb_prescriptions_oct, "October", "Healthboard")

# drugs prescribed in Scotland
scot_prescriptions_june = find_relevant_drugs(june)
print_data(scot_prescriptions_june, "June", "Scotland")
scot_prescriptions_oct = find_relevant_drugs(oct)
print_data(scot_prescriptions_oct, "October", "Scotland")
