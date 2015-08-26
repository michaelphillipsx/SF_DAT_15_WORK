"""
SF_DAT_15 project
"""
# Author: Michael Phillips <michael.phillips@gooddata.com>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the pre-processed CSV from Git repo
accidents2 = pd.read_csv('https://raw.githubusercontent.com/michaelphillipsx/SF_DAT_15_WORK/master/Project/transbaseexport.csv')


accidents2.head()
accidents2.info()
accidents2.describe()
accidents2.shape
# (4228, 14)
accidents2.columns
#Index([u'switrs_col_pkey', u'collision_date', u'accident_year',
#       u'collision_time', u'day_of_week', u'intersection', u'primary_rd',
#       u'secondary_rd', u'collision_severity', u'weather_1', u'road_surface',
#       u'lighting', u'chp_vehtype_at_fault', u'daytype'],
#      dtype='object')



# Check for any null values
accidents2.isnull().sum()




# Usually clear -- agrees with other dataset
accidents2.intersection.value_counts()
accidents2.weather_1.value_counts()

# Even distribution accross days of week
accidents2.day_of_week.value_counts()
accidents2.daytype.value_counts()

# Almost always dry roads
accidents2.road_surface.value_counts()


accidents2.lighting.value_counts()


# Who's at fault?
accidents2.chp_vehtype_at_fault.value_counts()

def Blame(n):
    if ( n == 'Bicycle' ): return "Bicycle"
    elif (n == '(null)' or n == 'Not Stated or Unknown (Hit and Run)'): return "Unknown"    
    elif (n != 'Bicycle'): return "Other"

accidents2['Blame'] = accidents2.chp_vehtype_at_fault.apply(Blame)
accidents2.groupby('Blame').chp_vehtype_at_fault.count().plot(kind='bar')



# What time of day are accidents happening?
accidents2.collision_time.value_counts()

def HoD(n):
    if ( n >= 2300 ): return "23"
    elif (n >= 2200  and n < 2300): return "22"
    elif (n >= 2100  and n < 2200): return "21" 
    elif (n >= 2000  and n < 2100): return "20"
    elif (n >= 1900  and n < 2000): return "19"
    elif (n >= 1800  and n < 1900): return "18"
    elif (n >= 1700  and n < 1800): return "17"
    elif (n >= 1600  and n < 1700): return "16"
    elif (n >= 1500  and n < 1600): return "15"
    elif (n >= 1400  and n < 1500): return "14"
    elif (n >= 1300  and n < 1400): return "13"
    elif (n >= 1200  and n < 1300): return "12"
    elif (n >= 1100  and n < 1200): return "11"
    elif (n >= 1000  and n < 1100): return "10"
    elif (n >= 900  and n < 1000): return "09"
    elif (n >= 800  and n < 900): return "08"
    elif (n >= 700  and n < 800): return "07"
    elif (n >= 600  and n < 700): return "06"
    elif (n >= 500  and n < 600): return "05"
    elif (n >= 400  and n < 500): return "04"
    elif (n >= 300  and n < 400): return "03"
    elif (n >= 200  and n < 300): return "02"
    elif (n >= 100  and n < 200): return "01"
    elif (n >= 0  and n < 100): return "00"

accidents2['HoD'] = accidents2.collision_time.apply(HoD)
accidents2.groupby('HoD').collision_time.count().plot(kind='bar')






