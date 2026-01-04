# ترميز وتحويل البيانات النصية إلى أرقام
le_country = LabelEncoder()
le_solution = LabelEncoder()
le_types = LabelEncoder()

df['c_enc'] = le_country.fit_transform(df['Country'])
df['s_enc'] = le_solution.fit_transform(df['solution'])
df['t_enc'] = le_types.fit_transform(df['types'])