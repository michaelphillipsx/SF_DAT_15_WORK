"""
SF_DAT_15 project
"""
# Author: Michael Phillips <michael.phillips@gooddata.com>

import pandas as pd
import seaborn as sns


# Read the pre-processed CSV from Git repo
accidents = pd.read_csv('https://raw.githubusercontent.com/michaelphillipsx/SF_DAT_15_WORK/master/Project/SFDAT15_Project.csv')


accidents.head()
accidents.info()
accidents.describe()
accidents.shape
# (307, 16)
accidents.columns
#Index([u'lat', u'severity', u'street1', u'street2', u'image_id', u'year',
#      u'date', u'lng', u'coord', u'intersection', u'day', u'desc', u'precip',
#      u'high', u'low', u'month'],
#      dtype='object')



# Check for any null values
accidents.isnull().sum()

# Check for dates with the most reported accidents
accidents.date.value_counts()

# Check for locations with the most reported accidents
locations = accidents.coord.value_counts()
locations.head()
# 4/307 = 1.3%
intsxn = accidents.intersection.value_counts(sort=True)
intsxn.head()
# 4/307 = 1.3%


#check all features to see if anything looks interesting
sns.pairplot(accidents)


# Lots of boring data in pairplots
sns.pairplot(accidents, x_vars='image_id', y_vars='day')

sns.pairplot(accidents, x_vars='image_id', y_vars='precip')
accidents.groupby('precip').precip.count().plot(kind='bar')


accidents.groupby('month').month.count().plot(kind='line')



# On to something here!
accidents.groupby('desc').desc.count().plot(kind='bar')


def weather_groups(n):
    if ( n == "Clear" or n == "Partly Cloudy" or n == "Scattered Clouds"): 
        return "Sunny"
    elif (n == "Fog" or n == "Mostly Cloudy" or n == "Overcast"):
        return "Cloudy"
    elif (n == "Rain" or n == "Thunderstorm"):
        return "Rainy"

accidents['weather_groups'] = accidents.desc.apply(weather_groups)
accidents.groupby('weather_groups').desc.count().plot(kind='bar')

accidents.groupby('weather_groups').desc.describe()
# 64/307 = 20.846905537 % Cloudy
# 38/307 = 12.377850163 % Rainy
# 205/307 = 66.7752443 % Sunny
