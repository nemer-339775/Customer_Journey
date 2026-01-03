import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# تحميل البيانات
df = pd.read_excel('data_all.xlsx')

# تنظيف البيانات (Data Cleaning)
# معالجة التواريخ والقيم الرقمية
df['activity_date'] = pd.to_datetime(df['activity_date'])
df['opportunity_stage'] = df['opportunity_stage'].fillna('no_opp')
df['is_lead'] = df['is_lead'].fillna(0)

# نقوم بحذف أي صف فيه القيمة فارغة في types 
df = df.dropna(subset=['types']) 
# تحديد الهدف (target)
# الفوز 1 & الخسارة أو عدم وجود فرصة 0
df['target'] = df['opportunity_stage'].apply(lambda x: 1 if 'WON' in str(x).upper() else 0)

print(f" تم تحميل وتنظيف البيانات بنجاح. عدد الصفوف المتبقية {len(df)}")
df.head()