# 2- تجميع المسارات 
df = df.sort_values(['account_id', 'activity_date'])

# بناء المسارات لكل عميل
paths_df = df.groupby(['account_id', 'Country', 'solution']).agg({
    'types': lambda x: ' -> '.join(x),
    'target': 'max'
}).reset_index()

# حساب أعلى 5 مسارات تكراراً 
top_paths_summary = paths_df.groupby(['Country', 'solution', 'types']).size().reset_index(name='frequency')
top_paths_summary = top_paths_summary.sort_values(['Country', 'solution', 'frequency'], ascending=[True, True, False])

# =====================================