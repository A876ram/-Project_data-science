# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error , mean_squared_error
# import seaborn as sns
# import matplotlib.pyplot as plt


# df=pd.read_csv('HighSchoolResult2022.csv')


# df=df.drop(['Percentage_2nd','status_2nd','arabic_2nd'
#               ,'first_foreign_lang_2nd','second_foreign_lang_2nd'
#               ,'pure_mathematics_2nd','history_2nd','geography_2nd'
#               ,'philosophy_2nd','psychology_2nd','chemistry_2nd'
#               ,'biology_2nd','geology_2nd','applied_math_2nd'
#               ,'physics_2nd','total_2nd','religion_2nd'
#               ,'national_education_2nd','economics_statistics_2nd','_merge'],axis=1)


# df.loc[df['branch'] == 'أدبي', ["pure_mathematics","chemistry","biology"
#                             ,"geology","applied_math","physics"]] = df.loc[df['branch'] == 'أدبي'
#                             , ["pure_mathematics","chemistry","biology","geology","applied_math"
#                             ,"physics"]].fillna('غير مقرر')
# df.loc[df['branch'] == 'علمي علوم', ["pure_mathematics","applied_math","history","geography"
#                               ,"philosophy","psychology"]] = df.loc[df['branch'] == 'علمي علوم'
#                               , ["pure_mathematics","applied_math","history","geography"
#                               ,"philosophy","psychology"]].fillna('غير مقرر')
# df.loc[df['branch'] == 'علمي رياضة', ["biology","geology","history","geography","philosophy"
#                               ,"psychology"]] = df.loc[df['branch'] == 'علمي رياضة'
#                               , ["biology","geology","history","geography","philosophy"
#                               ,"psychology"]].fillna('غير مقرر')
                                                       
# df['status']=df['status'].replace('دور ثاني','راسب')


# """
# df.loc[df['status'].isna(),['economics_statistics','national_education','religion','physics'
#                             ,'applied_math','geology','biology','chemistry','psychology','philosophy'
#                             ,'geography','history','pure_mathematics','second_foreign_lang'
#                             ,'first_foreign_lang','arabic'
#                             ,'Percentage']] = df.loc [df['status'].isna() ,['economics_statistics'
#                             ,'national_education','religion','physics','applied_math'
#                             ,'geology','biology','chemistry','psychology','philosophy','geography'
#                             ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
#                             ,'arabic','Percentage']].fillna(0)
# """


# # drop desk_ no that didn't have student
# df = df.dropna(subset=['status'])                   
                                                                                                           
# nan_rows = df[df['status'].isna()]


# df.loc[df['Percentage'] == 0,['economics_statistics','national_education','religion','physics'
#                             ,'applied_math','geology','biology','chemistry','psychology','philosophy'
#                             ,'geography','history','pure_mathematics','second_foreign_lang'
#                             ,'first_foreign_lang','arabic'
#                             ,'Percentage']] = df.loc [df['Percentage'] == 0 ,['economics_statistics'
#                             ,'national_education','religion','physics','applied_math'
#                             ,'geology','biology','chemistry','psychology','philosophy','geography'
#                             ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
#                             ,'arabic','Percentage']].fillna(0)
                                                                              
                                                                              
# df.loc[df['status'] == 'راسب',['economics_statistics','national_education','religion','physics'
#                             ,'applied_math','geology','biology','chemistry','psychology','philosophy'
#                             ,'geography','history','pure_mathematics','second_foreign_lang'
#                             ,'first_foreign_lang','arabic'
#                             ,'Percentage']] = df.loc [df['status'] == 'راسب' ,['economics_statistics'
#                             ,'national_education','religion','physics','applied_math'
#                             ,'geology','biology','chemistry','psychology','philosophy','geography'
#                             ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
#                             ,'arabic','Percentage']].fillna(0)
                                                            

# df.loc[df['status'] == 'ناجح',['economics_statistics','national_education','religion','physics'
#                             ,'applied_math','geology','biology','chemistry','psychology','philosophy'
#                             ,'geography','history','pure_mathematics','second_foreign_lang'
#                             ,'first_foreign_lang','arabic'
#                             ,'Percentage']] = df.loc [df['status'] == 'ناجح' ,['economics_statistics'
#                             ,'national_education','religion','physics','applied_math'
#                             ,'geology','biology','chemistry','psychology','philosophy','geography'
#                             ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
#                             ,'arabic','Percentage']].fillna('غير مدرج')
                                                                               
# df.loc[df['gender'].isna()] = df.loc[df['gender'].isna()].fillna('F')
                                                                                                
                                                                               
# # data that we work
# dw = df
# for column in df.columns:
#     dw[column] = df[column].replace('غير مدرج', 0)
                                                                    
# for column in df.columns:
#     dw[column] = df[column].replace('غير مقرر',0)
# #this part return number of rows have missing value    

# x1 = df[df['gender'].isna()]
# x2 = df[df['school_name'].isna()]
# x3 = df[df['administration'].isna()]
# x4 = df[df['city'].isna()]
# x5 = df[df['branch'].isna()]
# x6 = df[df['Percentage'].isna()]
# x7 = df[df['status'].isna()]
# x8 = df[df['arabic'].isna()]
# x9 = df[df['first_foreign_lang'].isna()]
# x10 = df[df['second_foreign_lang'].isna()]
# x11 = df[df['pure_mathematics'].isna()]
# x12 = df[df['history'].isna()]
# x13 = df[df['geography'].isna()]
# x14 = df[df['philosophy'].isna()]
# x15 = df[df['psychology'].isna()]
# x16 = df[df['chemistry'].isna()]
# x17 = df[df['biology'].isna()]
# x18 = df[df['geology'].isna()]
# x19 = df[df['applied_math'].isna()]
# x20 = df[df['physics'].isna()]
# x21 = df[df['total'].isna()]
# x22 = df[df['religion'].isna()]
# x23 = df[df['national_education'].isna()]
# x24 = df[df['economics_statistics'].isna()]
# x25 = df[df['gender'].isna()]

# desx = df.describe()

# df.to_csv('HighSchoolResult2022_modified.csv', index=False)


# ''' Analysis '''

# # Count of student in each City
# city_column = 'city'
# city_student_num = dw['city'].value_counts().reset_index(name='city_student_num')
# city_student_num = city_student_num.sort_values('city_student_num', ascending=False)
# city_student_num = city_student_num.rename(columns={'index': 'city'})

# # Rate of student in each City
# city_student_rate = dw['city'].value_counts() / dw['city'].count() * 100
# city_student_rate = city_student_rate.reset_index(name='city_student_rate')
# city_student_rate = city_student_rate.sort_values('city_student_rate', ascending=False)

# # Count of student in each Administration
# admin_student_num = dw['administration'].value_counts().reset_index(name='admin_student_num')
# admin_student_num = admin_student_num.sort_values('admin_student_num', ascending=False)
# admin_student_num = admin_student_num.rename(columns={'index': 'administration'})

# # Rate of student in each Administration
# admin_student_rate = dw['administration'].value_counts() / dw['administration'].count() * 100
# admin_student_rate = admin_student_rate.reset_index(name='admin_student_rate')
# admin_student_rate = admin_student_rate.sort_values('admin_student_rate', ascending=False)

# # Count of student M or F
# gender_student_num = dw['gender'].value_counts().reset_index(name='gender_student_num')
# gender_student_num = gender_student_num.sort_values('gender_student_num', ascending=False)

# # Rate of student M or F
# gender_student_rate = dw['gender'].value_counts()/ dw['gender'].count() * 100
# gender_student_rate = gender_student_rate.reset_index(name='gender_student_rate')
# gender_student_rate = gender_student_rate.sort_values('gender_student_rate', ascending=False)

# # Count of student Pass or Fall
# status_student_num = dw['status'].value_counts().reset_index(name='status_student_num')
# status_student_num = status_student_num.sort_values('status_student_num', ascending=False)

# # Rate of student Pass or Fall
# status_student_rate = dw['status'].value_counts() / dw['status'].count() * 100
# status_student_rate = status_student_rate.reset_index(name='status_student_rate')
# status_student_rate = status_student_rate.sort_values('status_student_rate', ascending=False)

# # list of top 10 Student
# grades_column = 'Percentage'
# branch_column = 'branch'

# # list of top 10 Student in Adaby
# target_branch_a = 'أدبي'
# num_top_students_a = 14
# top_students_in_branch_a = dw.loc[df[branch_column] == target_branch_a].nlargest(num_top_students_a, grades_column)

# # list of top 10 Student in Math
# target_branch_m = 'علمي رياضة'
# num_top_students_m = 191
# top_students_in_branch_m = dw.loc[df[branch_column] == target_branch_m].nlargest(num_top_students_m, grades_column)

# # list of top 10 Student in Science
# target_branch_s = 'علمي علوم'
# num_top_students_s = 356
# top_students_in_branch_s = dw.loc[dw[branch_column] == target_branch_s].nlargest(num_top_students_s, grades_column)

# # Number of Student in Adaby
# num_students_in_branch_a = dw.loc[dw[branch_column] == target_branch_a].count()[branch_column]

# # Number of Student in Math
# num_students_in_branch_m = dw.loc[dw[branch_column] == target_branch_m].count()[branch_column]

# # Number of Student in Science
# num_students_in_branch_s = dw.loc[dw[branch_column] == target_branch_s].count()[branch_column]


# # Count of passing student in each City
# city_column = 'city'
# status_column = 'status'

# city_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(city_column)[status_column].count().reset_index(name='city_passing_students_num')
# city_passing_students_num = city_passing_students_num.sort_values('city_passing_students_num', ascending=False)

# # Rate of passing student in each City
# city_passing_students_rate = pd.merge(city_student_num, city_passing_students_num, on='city')
# city_passing_students_rate['rate_passing_students'] = city_passing_students_rate['city_passing_students_num'] / city_passing_students_rate['city_student_num'] * 100

# # Count of falling student in each City
# city_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(city_column)[status_column].count().reset_index(name='city_falling_students_num')
# city_falling_students_num = city_falling_students_num.sort_values('city_falling_students_num', ascending=False)

# # Rate of falling student in each City
# city_falling_students_rate = pd.merge(city_student_num, city_falling_students_num, on='city')
# city_falling_students_rate['rate_falling_students'] = city_falling_students_rate['city_falling_students_num'] / city_falling_students_rate['city_student_num'] * 100


# # Count of passing student in each administration
# admin_column = 'administration'
# admin_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(admin_column)[status_column].count().reset_index(name='admin_passing_students_num')
# admin_passing_students_num = admin_passing_students_num.sort_values('admin_passing_students_num', ascending=False)

# # Rate of passing student in each City
# admin_passing_students_rate = pd.merge(admin_student_num, admin_passing_students_num, on='administration')
# admin_passing_students_rate['rate_passing_students'] = admin_passing_students_rate['admin_passing_students_num'] / admin_passing_students_rate['admin_student_num'] * 100

# # Count of falling student in each administration
# admin_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(admin_column)[status_column].count().reset_index(name='admin_falling_students_num')
# admin_falling_students_num = admin_falling_students_num.sort_values('admin_falling_students_num', ascending=False)

# # Rate of falling student in each City
# admin_falling_students_rate = pd.merge(admin_student_num, admin_falling_students_num, on='administration')
# admin_falling_students_rate['rate_falling_students'] = admin_falling_students_rate['admin_falling_students_num'] / admin_falling_students_rate['admin_student_num'] * 100


# # Count of passing student in each Branch
# status_column = 'status'

# branch_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(branch_column)[status_column].count().reset_index(name='branch_passing_students_num')
# branch_passing_students_num = branch_passing_students_num.sort_values('branch_passing_students_num', ascending=False)

# # Rate of passing student in each Branch
# branch_passing_students_num['branch_students_num']=[325599, 259147, 97602]
# branch_passing_students_num['rate_passing_students'] = branch_passing_students_num ['branch_passing_students_num'] / branch_passing_students_num ['branch_students_num'] * 100

# # Count of falling student in each Branch
# branch_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(branch_column)[status_column].count().reset_index(name='branch_falling_students_num')
# branch_falling_students_num = branch_falling_students_num.sort_values('branch_falling_students_num', ascending=False)

# # Rate of passing student in each Branch
# branch_falling_students_num['branch_students_num']=[259147, 325599, 97602]
# branch_falling_students_num['rate_falling_students'] = branch_falling_students_num ['branch_falling_students_num'] / branch_falling_students_num ['branch_students_num'] * 100


# # Number of student that have Up to 90%
# student_up_90_num = dw.loc[dw['Percentage'] >= 90]
# student_up_90_rate = student_up_90_num['Percentage'].count() / dw['Percentage'].count() * 100

# # Number of student that have Up to 80% to 90%
# student_up_80_to_90_num = dw.loc[(dw['Percentage'] >= 80) & (dw['Percentage'] < 90)]
# student_up_80_to_90_rate = student_up_80_to_90_num['Percentage'].count() / dw['Percentage'].count() * 100

# # Number of student that have Up to 70% to 80%
# student_up_70_to_80_num = dw.loc[(dw['Percentage'] >= 70) & (dw['Percentage'] < 80)]
# student_up_70_to_80_rate = student_up_70_to_80_num['Percentage'].count() / dw['Percentage'].count() * 100

# # Number of student that have Up to 60% to 70%
# student_up_60_to_70_num = dw.loc[(dw['Percentage'] >= 60) & (dw['Percentage'] < 70)]
# student_up_60_to_70_rate = student_up_60_to_70_num['Percentage'].count() / dw['Percentage'].count() * 100

# # Number of student that have Up to 50% to 60%
# student_up_50_to_60_num = dw.loc[(dw['Percentage'] >= 50) & (dw['Percentage'] < 60)]
# student_up_50_to_60_rate = student_up_50_to_60_num['Percentage'].count() / dw['Percentage'].count() * 100

# # Number of student that have less to 50%
# student_less_50_num = dw.loc[dw['Percentage'] < 50]
# student_less_50_rate = student_less_50_num['Percentage'].count() / dw['Percentage'].count() * 100



# # count of abroad student
# abroad_student_num = dw.loc[dw['school_name'].str.contains('ابناؤنا فى الخارج')]

# ''' Visualisation '''

# correlation=dw.corr()
# sns.heatmap(correlation, linewidths=4,linecolor='k', annot=True)
# plt.hist(dw['gender'])
# plt.hist(dw['city'])
# plt.hist(dw['Percentage'])
# plt.hist(dw['total'])


# z = ['arabic', 'first_foreign_lang',
# 'second_foreign_lang', 'pure_mathematics', 'history', 'geography',
# 'philosophy', 'psychology', 'chemistry', 'biology', 'geology',
# 'applied_math', 'physics', 'total', 'religion', 'national_education',
# 'economics_statistics']

# #sns.violinplot(df=df[z])
# #plt.title("coll between city and subjects")
# #plt.xlabel("city")
# #plt.ylabel("z")

# data = ['desk_no',
#        'Percentage',  'arabic', 'first_foreign_lang',
#        'second_foreign_lang', 'pure_mathematics', 'history', 'geography',
#        'philosophy', 'psychology', 'chemistry', 'biology', 'geology',
#        'applied_math', 'physics', 'total', 'religion', 'national_education',
#        'economics_statistics']


# x = dw[data]
# y = dw['Percentage']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, random_state=42)
# clf = LinearRegression()
# clf.fit(x_train,y_train)
# prediction = clf.predict(x_test)
# mse = mean_squared_error(y_test , prediction)
# mae = mean_absolute_error(y_test , prediction)
# r_squared = clf.score(x_test, y_test)

# print('Mean Squared Error :', mse)
# print('Mead Absolute Eroor :', mae)
# print('R_squared :', r_squared)


###########################################################

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('HighSchoolResult2022.csv')


df.loc[df['branch'] == 'أدبي', ["pure_mathematics","chemistry","biology"
                           ,"geology","applied_math","physics"]] = df.loc[df['branch'] == 'أدبي'
                           , ["pure_mathematics","chemistry","biology","geology","applied_math"
                           ,"physics"]].fillna('غير مقرر')
df.loc[df['branch'] == 'علمي علوم', ["pure_mathematics","applied_math","history","geography"
                             ,"philosophy","psychology"]] = df.loc[df['branch'] == 'علمي علوم'
                             , ["pure_mathematics","applied_math","history","geography"
                             ,"philosophy","psychology"]].fillna('غير مقرر')
df.loc[df['branch'] == 'علمي رياضة', ["biology","geology","history","geography","philosophy"
                              ,"psychology"]] = df.loc[df['branch'] == 'علمي رياضة'
                              , ["biology","geology","history","geography","philosophy"
                              ,"psychology"]].fillna('غير مقرر')
                                                       
df['status']=df['status'].replace('دور ثاني','راسب')


"""
df.loc[df['status'].isna(),['economics_statistics','national_education','religion','physics'
                            ,'applied_math','geology','biology','chemistry','psychology','philosophy'
                            ,'geography','history','pure_mathematics','second_foreign_lang'
                            ,'first_foreign_lang','arabic'
                            ,'Percentage']] = df.loc [df['status'].isna() ,['economics_statistics'
                            ,'national_education','religion','physics','applied_math'
                            ,'geology','biology','chemistry','psychology','philosophy','geography'
                            ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
                            ,'arabic','Percentage']].fillna(0)
"""


# drop desk_ no that didn't have student
df = df.dropna(subset=['status'])                   
                                                                                                           
nan_rows = df[df['status'].isna()]


df.loc[df['Percentage'] == 0,['economics_statistics','national_education','religion','physics'
                            ,'applied_math','geology','biology','chemistry','psychology','philosophy'
                            ,'geography','history','pure_mathematics','second_foreign_lang'
                            ,'first_foreign_lang','arabic'
                            ,'Percentage']] = df.loc [df['Percentage'] == 0 ,['economics_statistics'
                            ,'national_education','religion','physics','applied_math'
                            ,'geology','biology','chemistry','psychology','philosophy','geography'
                            ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
                            ,'arabic','Percentage']].fillna(0)
                                                                              
                                                                              
df.loc[df['status'] == 'راسب',['economics_statistics','national_education','religion','physics'
                            ,'applied_math','geology','biology','chemistry','psychology','philosophy'
                            ,'geography','history','pure_mathematics','second_foreign_lang'
                            ,'first_foreign_lang','arabic'
                            ,'Percentage']] = df.loc [df['status'] == 'راسب' ,['economics_statistics'
                            ,'national_education','religion','physics','applied_math'
                            ,'geology','biology','chemistry','psychology','philosophy','geography'
                            ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
                            ,'arabic','Percentage']].fillna(0)
                                                            

df.loc[df['status'] == 'ناجح',['economics_statistics','national_education','religion','physics'
                            ,'applied_math','geology','biology','chemistry','psychology','philosophy'
                            ,'geography','history','pure_mathematics','second_foreign_lang'
                            ,'first_foreign_lang','arabic'
                            ,'Percentage']] = df.loc [df['status'] == 'ناجح' ,['economics_statistics'
                            ,'national_education','religion','physics','applied_math'
                            ,'geology','biology','chemistry','psychology','philosophy','geography'
                            ,'history','pure_mathematics','second_foreign_lang','first_foreign_lang'
                            ,'arabic','Percentage']].fillna('غير مدرج')
                                                                               
df.loc[df['gender'].isna()] = df.loc[df['gender'].isna()].fillna('F')
                                                                               
                  
                                                                               
# data that we work
dw = df
for column in df.columns:
    dw[column] = df[column].replace('غير مدرج', 0)
                                                                    
for column in df.columns:
    dw[column] = df[column].replace('غير مقرر',0)
#this part return number of rows have missing value    

x1 = df[df['gender'].isna()]
x2 = df[df['school_name'].isna()]
x3 = df[df['administration'].isna()]
x4 = df[df['city'].isna()]
x5 = df[df['branch'].isna()]
x6 = df[df['Percentage'].isna()]
x7 = df[df['status'].isna()]
x8 = df[df['arabic'].isna()]
x9 = df[df['first_foreign_lang'].isna()]
x10 = df[df['second_foreign_lang'].isna()]
x11 = df[df['pure_mathematics'].isna()]
x12 = df[df['history'].isna()]
x13 = df[df['geography'].isna()]
x14 = df[df['philosophy'].isna()]
x15 = df[df['psychology'].isna()]
x16 = df[df['chemistry'].isna()]
x17 = df[df['biology'].isna()]
x18 = df[df['geology'].isna()]
x19 = df[df['applied_math'].isna()]
x20 = df[df['physics'].isna()]
x21 = df[df['total'].isna()]
x22 = df[df['religion'].isna()]
x23 = df[df['national_education'].isna()]
x24 = df[df['economics_statistics'].isna()]
x25 = df[df['gender'].isna()]

desx = df.describe()



''' Analysis '''

# Count of student in each City
city_column = 'city'
city_student_num = dw['city'].value_counts().reset_index(name='city_student_num')
city_student_num = city_student_num.sort_values('city_student_num', ascending=False)
city_student_num = city_student_num.rename(columns={'index': 'city'})

# Rate of student in each City
city_student_rate = dw['city'].value_counts() / dw['city'].count() * 100
city_student_rate = city_student_rate.reset_index(name='city_student_rate')
city_student_rate = city_student_rate.sort_values('city_student_rate', ascending=False)

# Count of student in each Administration
admin_student_num = dw['administration'].value_counts().reset_index(name='admin_student_num')
admin_student_num = admin_student_num.sort_values('admin_student_num', ascending=False)
admin_student_num = admin_student_num.rename(columns={'index': 'administration'})

# Rate of student in each Administration
admin_student_rate = dw['administration'].value_counts() / dw['administration'].count() * 100
admin_student_rate = admin_student_rate.reset_index(name='admin_student_rate')
admin_student_rate = admin_student_rate.sort_values('admin_student_rate', ascending=False)

# Count of student M or F
gender_student_num = dw['gender'].value_counts().reset_index(name='gender_student_num')
gender_student_num = gender_student_num.sort_values('gender_student_num', ascending=False)

# Rate of student M or F
gender_student_rate = dw['gender'].value_counts()/ dw['gender'].count() * 100
gender_student_rate = gender_student_rate.reset_index(name='gender_student_rate')
gender_student_rate = gender_student_rate.sort_values('gender_student_rate', ascending=False)

# Count of student Pass or Fall
status_student_num = dw['status'].value_counts().reset_index(name='status_student_num')
status_student_num = status_student_num.sort_values('status_student_num', ascending=False)

# Rate of student Pass or Fall
status_student_rate = dw['status'].value_counts() / dw['status'].count() * 100
status_student_rate = status_student_rate.reset_index(name='status_student_rate')
status_student_rate = status_student_rate.sort_values('status_student_rate', ascending=False)

# list of top 10 Student
grades_column = 'Percentage'
branch_column = 'branch'

# list of top 10 Student in Adaby
target_branch_a = 'أدبي'
num_top_students_a = 14
top_students_in_branch_a = dw.loc[df[branch_column] == target_branch_a].nlargest(num_top_students_a, grades_column)

# list of top 10 Student in Math
target_branch_m = 'علمي رياضة'
num_top_students_m = 191
top_students_in_branch_m = dw.loc[df[branch_column] == target_branch_m].nlargest(num_top_students_m, grades_column)

# list of top 10 Student in Science
target_branch_s = 'علمي علوم'
num_top_students_s = 356
top_students_in_branch_s = dw.loc[dw[branch_column] == target_branch_s].nlargest(num_top_students_s, grades_column)

# Number of Student in Adaby
num_students_in_branch_a = dw.loc[dw[branch_column] == target_branch_a].count()[branch_column]

# Number of Student in Math
num_students_in_branch_m = dw.loc[dw[branch_column] == target_branch_m].count()[branch_column]

# Number of Student in Science
num_students_in_branch_s = dw.loc[dw[branch_column] == target_branch_s].count()[branch_column]


# Count of passing student in each City
city_column = 'city'
status_column = 'status'

city_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(city_column)[status_column].count().reset_index(name='city_passing_students_num')
city_passing_students_num = city_passing_students_num.sort_values('city_passing_students_num', ascending=False)

# Rate of passing student in each City
city_passing_students_rate = pd.merge(city_student_num, city_passing_students_num, on='city')
city_passing_students_rate['rate_passing_students'] = city_passing_students_rate['city_passing_students_num'] / city_passing_students_rate['city_student_num'] * 100

# Count of falling student in each City
city_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(city_column)[status_column].count().reset_index(name='city_falling_students_num')
city_falling_students_num = city_falling_students_num.sort_values('city_falling_students_num', ascending=False)

# Rate of falling student in each City
city_falling_students_rate = pd.merge(city_student_num, city_falling_students_num, on='city')
city_falling_students_rate['rate_falling_students'] = city_falling_students_rate['city_falling_students_num'] / city_falling_students_rate['city_student_num'] * 100


# Count of passing student in each administration
admin_column = 'administration'
admin_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(admin_column)[status_column].count().reset_index(name='admin_passing_students_num')
admin_passing_students_num = admin_passing_students_num.sort_values('admin_passing_students_num', ascending=False)

# Rate of passing student in each City
admin_passing_students_rate = pd.merge(admin_student_num, admin_passing_students_num, on='administration')
admin_passing_students_rate['rate_passing_students'] = admin_passing_students_rate['admin_passing_students_num'] / admin_passing_students_rate['admin_student_num'] * 100

# Count of falling student in each administration
admin_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(admin_column)[status_column].count().reset_index(name='admin_falling_students_num')
admin_falling_students_num = admin_falling_students_num.sort_values('admin_falling_students_num', ascending=False)

# Rate of falling student in each City
admin_falling_students_rate = pd.merge(admin_student_num, admin_falling_students_num, on='administration')
admin_falling_students_rate['rate_falling_students'] = admin_falling_students_rate['admin_falling_students_num'] / admin_falling_students_rate['admin_student_num'] * 100


# Count of passing student in each Branch
status_column = 'status'

branch_passing_students_num = dw[dw[status_column] == 'ناجح'].groupby(branch_column)[status_column].count().reset_index(name='branch_passing_students_num')
branch_passing_students_num = branch_passing_students_num.sort_values('branch_passing_students_num', ascending=False)

# Rate of passing student in each Branch
branch_passing_students_num['branch_students_num']=[325599, 259147, 97602]
branch_passing_students_num['rate_passing_students'] = branch_passing_students_num ['branch_passing_students_num'] / branch_passing_students_num ['branch_students_num'] * 100

# Count of falling student in each Branch
branch_falling_students_num = dw[dw[status_column] == 'راسب'].groupby(branch_column)[status_column].count().reset_index(name='branch_falling_students_num')
branch_falling_students_num = branch_falling_students_num.sort_values('branch_falling_students_num', ascending=False)

# Rate of passing student in each Branch
branch_falling_students_num['branch_students_num']=[259147, 325599, 97602]
branch_falling_students_num['rate_falling_students'] = branch_falling_students_num ['branch_falling_students_num'] / branch_falling_students_num ['branch_students_num'] * 100


# Number of student that have Up to 90%
student_up_90_num = dw.loc[dw['Percentage'] >= 90]
student_up_90_rate = student_up_90_num['Percentage'].count() / dw['Percentage'].count() * 100

# Number of student that have Up to 80% to 90%
student_up_80_to_90_num = dw.loc[(dw['Percentage'] >= 80) & (dw['Percentage'] < 90)]
student_up_80_to_90_rate = student_up_80_to_90_num['Percentage'].count() / dw['Percentage'].count() * 100

# Number of student that have Up to 70% to 80%
student_up_70_to_80_num = dw.loc[(dw['Percentage'] >= 70) & (dw['Percentage'] < 80)]
student_up_70_to_80_rate = student_up_70_to_80_num['Percentage'].count() / dw['Percentage'].count() * 100

# Number of student that have Up to 60% to 70%
student_up_60_to_70_num = dw.loc[(dw['Percentage'] >= 60) & (dw['Percentage'] < 70)]
student_up_60_to_70_rate = student_up_60_to_70_num['Percentage'].count() / dw['Percentage'].count() * 100

# Number of student that have Up to 50% to 60%
student_up_50_to_60_num = dw.loc[(dw['Percentage'] >= 50) & (dw['Percentage'] < 60)]
student_up_50_to_60_rate = student_up_50_to_60_num['Percentage'].count() / dw['Percentage'].count() * 100

# Number of student that have less to 50%
student_less_50_num = dw.loc[dw['Percentage'] < 50]
student_less_50_rate = student_less_50_num['Percentage'].count() / dw['Percentage'].count() * 100



# count of abroad student
abroad_student_num = dw.loc[dw['school_name'].str.contains('ابناؤنا فى الخارج')]

#visolization
correlation=dw.corr()
sns.heatmap(correlation, linewidths=4,linecolor='k', annot=True)
plt.hist(dw['gender'])
plt.hist(dw['city'])
plt.hist(dw['Percentage'])
plt.hist(dw['total'])


z = ['arabic', 'first_foreign_lang',
'second_foreign_lang', 'pure_mathematics', 'history', 'geography',
'philosophy', 'psychology', 'chemistry', 'biology', 'geology',
'applied_math', 'physics', 'total', 'religion', 'national_education',
'economics_statistics']

#sns.violinplot(df=df[z])
#plt.title("coll between city and subjects")
#plt.xlabel("city")
#plt.ylabel("z")

data = ['desk_no',
       'Percentage',  'arabic', 'first_foreign_lang',
       'second_foreign_lang', 'pure_mathematics', 'history', 'geography',
       'philosophy', 'psychology', 'chemistry', 'biology', 'geology',
       'applied_math', 'physics', 'total', 'religion', 'national_education',
       'economics_statistics']


x = dw[data]
y = dw['Percentage']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, random_state=42)
clf = LinearRegression()
clf.fit(x_train,y_train)
prediction = clf.predict(x_test)
mse = mean_squared_error(y_test , prediction)
mae = mean_absolute_error(y_test , prediction)
r_squared = clf.score(x_test, y_test)

print('Mean Squared Error :', mse)
print('Mead Absolute Eroor :', mae)
print('R_squared :', r_squared)
