import numpy as np
import pandas as pd
from datetime import datetime

from const import WEEK_IDX_RANGE, DATES_FROM_WEEK_IDX


def load_combined_raw_data():
    """NOTE: Modify if your data storage is different"""
    data = [
        pd.read_csv(f'../data/pulse2020_puf_{n:02d}.csv')
        for n in WEEK_IDX_RANGE
    ]
    return pd.concat(data, ignore_index=True)

def add_dates_start_end_inplace(data):
    data['DATE_START'] = data['WEEK'].apply(lambda idx: DATES_FROM_WEEK_IDX[idx][0])
    data['DATE_END']   = data['WEEK'].apply(lambda idx: DATES_FROM_WEEK_IDX[idx][1])

def add_age_inplace(data):
    data['AGE'] = datetime.now().year - data['TBIRTH_YEAR']

def add_mental_vars_inplace(data):
    """
    Variable are constructed according to
    https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm
    """
    data['ANXIETY_SCORE'] = data['ANXIOUS'] + data['WORRY'] - 2
    data['DEPRESSION_SCORE'] = data['INTEREST'] + data['DOWN'] - 2

    data['ANXIETY_DISORDER']    = data['ANXIETY_SCORE'].apply(lambda x: float(x >= 3) if not np.isnan(x) else np.nan)
    data['DEPRESSION_DISORDER'] = data['DEPRESSION_SCORE'].apply(lambda x: float(x >= 3) if not np.isnan(x) else np.nan)

def replace_codes_with_nan_inplace(data):
    data.replace(-88, np.nan, inplace=True)
    data.replace(-99, np.nan, inplace=True)

    
def get_col_list(col_name, num):
    return [col_name + str(i) for i in range(1, num+1)]

def drop_cols(dta):
    cols_dict = {'WHEREFREE':7, 'FOODSUFRSN':5}
    for c in list(cols_dict.keys()):
        col_lst = get_col_list(c, cols_dict[c])
        if c == 'FOODSUFRSN':
            foodsuf_sum = dta[col_lst].sum(axis = 1).values
            data1[(c+'_SUM')] = foodsuf_sum
        dta.drop(col_lst, 1, inplace = True)
    #return dta    

def get_cleaned_combined_data():
    data = load_combined_raw_data()

    replace_codes_with_nan_inplace(data)

    add_dates_start_end_inplace(data)

    add_age_inplace(data)
    add_mental_vars_inplace(data)
    drop_cols(data)
    return data
