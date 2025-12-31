import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# تحميل البيانات
df = pd.read_excel('data_all.xlsx')

# 1. تنظيف البيانات (Data Cleaning)
df['activity_date'] = pd.to_datetime(df['activity_date'])
df['opportunity_stage'] = df['opportunity_stage'].fillna('no_opp')
df['types'] = df['types'].fillna('Unknown')

# تحديد الهدف
# للفوز 1
# للخسارة أو عدم وجود فرصة 0

df['target'] = df['opportunity_stage'].apply(lambda x: 1 if 'WON' in str(x).upper() else 0)

print("تم تحميل وتنظيف البيانات بنجاح.")
df.head()