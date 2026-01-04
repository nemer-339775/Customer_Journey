# ترتيب البيانات زمنياً لكل حساب
df = df.sort_values(['account_id', 'activity_date'])

# تجميع المسارات (Paths)
paths_df = df.groupby(['account_id', 'Country', 'solution'])['types'].apply(lambda x: ' -> '.join(x)).reset_index()
