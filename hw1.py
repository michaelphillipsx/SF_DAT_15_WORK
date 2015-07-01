'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)

# 2. Show the count of missing values in each column

killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"

killings.fillna('Unknown', inplace=True)

# 4. How many killings were there so far in 2015?

killings[killings['year'] == 2015].name.count()

# 5. Of all killings, how many were male and how many female?

killings.gender.value_counts()

# 6. How many killings were of unarmed people?

killings[killings.armed == 'No'].armed.count()

# 7. What percentage of all killings were unarmed?

killings[killings.armed == 'No'].armed.count() / float(killings.shape[0]) *100

# 8. What are the 5 states with the most killings?

killings.state.value_counts().head()

# 9. Show a value counts of deaths for each race

killings.race.value_counts()

# 10. Display a histogram of ages of all killings

killings.age.hist()

# 11. Show 6 histograms of ages by race

killings.age.hist(by=killings.race)

# 12. What is the average age of death by race?

killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month

killings.month.value_counts().plot(kind='bar')


###################
### Less Morbid ###
###################

majors = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

del majors['Employed_full_time_year_round']
del majors['Major_code']

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

majors[['Major', 'Median']].sort_index(by='Median', ascending = False).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!

top_10_majors_by_median = majors.sort_index(by='Median', ascending=False).head(10)[['Major', 'Median']]
graph = top_10_majors_by_median.plot(kind='bar', x='Major', y='Median', title='Highest Paying Majors', color = 'g')
graph.set_xlabel('Major')
graph.set_ylabel('Median')


# 5. What is the average median salary for each major category?

majors.groupby('Major_category').Median.mean()

# 6. Show only the top 5 paying major categories

test = majors.groupby('Major_category').Median.mean()
test.sort(inplace=True)
test.tail()

# 7. Plot a histogram of the distribution of median salaries

majors.Median.hist(bins=20, color='g')

# 8. Plot a histogram of the distribution of median salaries by major category

majors.groupby('Major_category').Median.mean().plot(kind='bar',by='Major_category', color='b')

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?

majors.groupby('Major')['Unemployment_rate'].mean().order(ascending=False).head(10) * 100
  
# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
  
majors.groupby('Major_category')['Unemployment_rate'].mean().order(ascending=False).head(10) * 100

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = majors['Employed'] / majors['Total']

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"

majors['sample_unemployment_rate'] = 1 - majors['sample_employment_rate']
