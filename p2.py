
import pandas as pd

df = pd.read_csv('cleaned_data.csv')

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.columns)

print(df.describe())


#Total Pending Cases State-wise
state_cases = df.groupby('srcStateName')['Pending cases'].sum().reset_index()
print(state_cases)

#Total Pending Cases District-wise
district_cases = df.groupby('srcDistrictName')['Pending cases'].sum().reset_index()
print(district_cases)

#Analyze Pending Cases by Year Range
year_range_cols = [
    'Pending cases for a period of 0 to 1 Years',
    'Pending cases for a period of 1 to 3 Years',
    'Pending cases for a period of 3 to 5 Years',
    'Pending cases for a period of 5 to 10 Years',
    'Pending cases for a period of 10 to 20 Years',
    'Pending cases for a period of 20 to 30 Years',
    'Pending cases over 30 Years'
]

pending_by_years = df[year_range_cols].sum()
print(pending_by_years)

#Analyze Cases by Stage
stage_cols = [
    'Cases pending at Appearance or Service-Related stage',
    'Cases pending at Compliance or Steps or stay stage',
    'Cases pending at Evidence or Argument or Judgement stage',
    'Cases pending at Pleadings or Issues or Charge stage'
]

cases_by_stage = df[stage_cols].sum()
print(cases_by_stage)

#Total Cases Filed vs Disposed in Last Month
filed_vs_disposed = df[['Cases instituted in last month', 'Cases disposed in last month']].sum()
print(filed_vs_disposed)

#Total Cases Filed by Senior Citizens and Women
special_cases = df[['Cases filed by Senior Citizens', 'Cases filed by women']].sum()
print(special_cases)







import matplotlib.pyplot as plt
import seaborn as sns


#Pending Cases Across States & Districts

# State-wise Pending Cases - Bar Plot
plt.figure(figsize=(12,6))
state_cases = df.groupby('srcStateName')['Pending cases'].sum().sort_values(ascending=False)
state_cases.plot(kind='bar', color='teal')
plt.title('State-wise Pending Court Cases')
plt.xlabel('State')
plt.ylabel('Total Pending Cases')
plt.xticks(rotation=90)
plt.show()

# Heatmap: State vs Court case Type Pending Cases
#state_district_cases = df.pivot_table(values='Pending cases', index='srcStateName', columns='District and Taluk Court Case type', fill_value=0)
#plt.figure(figsize=(16,8))
#sns.heatmap(state_district_cases, cmap='Reds')
#plt.title('Heatmap: Pending Cases Across States & Districts')
#plt.show()

# -----------------------------------------------
# Objective 2: Duration-wise Pending Cases Analysis

duration_cols = [
    'Pending cases for a period of 0 to 1 Years',
    'Pending cases for a period of 1 to 3 Years',
    'Pending cases for a period of 3 to 5 Years',
    'Pending cases for a period of 5 to 10 Years',
    'Pending cases for a period of 10 to 20 Years',
    'Pending cases for a period of 20 to 30 Years',
    'Pending cases over 30 Years'
]


#Boxplot for Cases Pending Duration
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[duration_cols])
plt.title('Boxplot for Cases Pending Duration')
plt.xlabel('Duration Categories')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Stacked Bar Chart
df_duration_sum = df[duration_cols].sum()
df_duration_sum.plot(kind='bar', stacked=True, color=sns.color_palette("Blues", 7))
plt.title('Pending Cases by Duration Range')
plt.xlabel('Duration Range')
plt.ylabel('Number of Pending Cases')
plt.xticks(rotation=45)
plt.show()

# Histogram
df[duration_cols].plot.hist(bins=20, figsize=(10,6))
plt.title('Histogram of Pending Cases Duration')
plt.xlabel('Pending Cases Count')
plt.show()

# Boxplot
#plt.figure(figsize=(10,6))
#sns.boxplot(data=df[duration_cols])
#plt.title('Boxplot of Pending Cases Duration')
#plt.xticks(rotation=45)
#plt.show()

# -----------------------------------------------
# Objective 3: Stage-wise Pending Cases Analysis

stage_cols = [
    'Cases pending at Appearance or Service-Related stage',
    'Cases pending at Compliance or Steps or stay stage',
    'Cases pending at Evidence or Argument or Judgement stage',
    'Cases pending at Pleadings or Issues or Charge stage'
]

# Bar Plot
df_stage_sum = df[stage_cols].sum()
df_stage_sum.plot(kind='bar', color='coral')
plt.title('Stage-wise Pending Court Cases')
plt.xticks(rotation=45)
plt.ylabel('Number of Cases')
plt.show()

# Pie Chart
df_stage_sum.plot(kind='pie', autopct='%1.1f%%', figsize=(7,7))
plt.title('Stage-wise Pending Cases Distribution')
plt.ylabel('')
plt.show()

# Heatmap: Stage vs District
#plt.figure(figsize=(14,8))
#sns.heatmap(df.pivot_table(values='Pending cases', index='srcDistrictName', columns='srcStateName', aggfunc='sum', fill_value=0), cmap='YlGnBu')
#plt.title('Heatmap of Pending Cases Across Stages & Districts')
#plt.show()

# -----------------------------------------------
# Objective 4: Cases Instituted vs Disposed Last Month

plt.figure(figsize=(12,6))
df.groupby('srcStateName')[['Cases instituted in last month', 'Cases disposed in last month']].sum().plot(kind='bar')
plt.title('Cases Instituted vs Disposed Last Month (State-wise)')
plt.ylabel('Number of Cases')
plt.xticks(rotation=90)
plt.show()

# Scatter Plot: Correlation
plt.figure(figsize=(8,6))
sns.scatterplot(x='Cases instituted in last month', y='Cases disposed in last month', data=df)
plt.title('Correlation: Cases Instituted vs Disposed')
plt.xlabel('Cases Instituted')
plt.ylabel('Cases Disposed')
plt.show()

# -----------------------------------------------
# Objective 5: Special Case Categories (Senior Citizens, Women, Delayed)

# Bar Plot: Senior Citizens vs Women Cases
plt.figure(figsize=(10,6))
df[['Cases filed by Senior Citizens', 'Cases filed by women']].sum().plot(kind='bar', color=['orange', 'purple'])
plt.title('Cases Filed by Senior Citizens vs Women')
plt.ylabel('Total Cases')
plt.xticks(rotation=0)
plt.show()

# Heatmap: District-wise Delayed Cases
#plt.figure(figsize=(14,8))
#sns.heatmap(df.pivot_table(values='Cases delayed in disposal', index='srcDistrictName', columns='srcStateName', aggfunc='sum', fill_value=0), cmap='coolwarm')
#plt.title('Heatmap of Delayed Case Disposal (District-wise)')
#plt.show()

# Boxplot: Delayed Cases Distribution
#plt.figure(figsize=(10,6))
#sns.boxplot(x='srcStateName', y='Cases delayed in disposal', data=df)
#plt.title('Distribution of Delayed Cases Across States')
#plt.xticks(rotation=90)
#plt.show()






# Duration Columns
duration_cols = [
    'Pending cases for a period of 0 to 1 Years',
    'Pending cases for a period of 1 to 3 Years',
    'Pending cases for a period of 3 to 5 Years',
    'Pending cases for a period of 5 to 10 Years',
    'Pending cases for a period of 10 to 20 Years',
    'Pending cases for a period of 20 to 30 Years',
    'Pending cases over 30 Years'
]

# Group by State and Sum Duration-wise Pending Cases
state_duration = df.groupby('srcStateName')[duration_cols].sum()

# Plot Heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(state_duration, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=0.5)
plt.title('Heatmap: State vs Duration-wise Pending Cases')
plt.xlabel('Case Pending Duration')
plt.ylabel('State')
plt.show()



