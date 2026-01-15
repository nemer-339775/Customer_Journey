import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# 1- تجهيز البيانات من ملف القالب (xltx)
try:
    # استخدام engine='openpyxl'  لقراءة ملفات xltx  
    df = pd.read_excel('data_all.xltx', engine='openpyxl')
    print(" Template file loaded successfully")
except Exception as e:
    print(f" Failed to load file: {e}")
    

# تنظيف المسافات وتوحيد حالة الأحرف 
df['Country'] = df['Country'].astype(str).str.strip().str.upper()
df['solution'] = df['solution'].astype(str).str.strip().str.upper()

# تنظيف البيانات ومعالجة التواريخ والقيم المفقودة
df['activity_date'] = pd.to_datetime(df['activity_date'])
df['opportunity_stage'] = df['opportunity_stage'].fillna('no_opp')
df['is_lead'] = df['is_lead'].fillna(0)
df = df.dropna(subset=['types'])

# تحديد الهدف  WON = 1, Others = 0
df['target'] = df['opportunity_stage'].apply(lambda x: 1 if 'WON' in str(x).upper() else 0)

# =====================================
