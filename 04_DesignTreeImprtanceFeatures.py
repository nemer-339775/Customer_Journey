# 3- تدريب شجرة القرار 
le_country, le_solution, le_types = LabelEncoder(), LabelEncoder(), LabelEncoder()

df['c_enc'] = le_country.fit_transform(df['Country'])
df['s_enc'] = le_solution.fit_transform(df['solution'])
df['t_enc'] = le_types.fit_transform(df['types'])

features = ['c_enc', 's_enc', 't_enc', 'is_lead']
X, y = df[features], df['target']

dt_model = DecisionTreeClassifier(max_depth=7, class_weight='balanced', random_state=42)
dt_model.fit(X, y)

# استخراج أهمية السمات 
importances = dt_model.feature_importances_
feature_importance_dict = dict(zip(['Country', 'Solution', 'Action Type', 'Is Lead'], importances))

def plot_feature_importance(importance_dict):
    features_names = list(importance_dict.keys())
    values = list(importance_dict.values())
    
    plt.figure(figsize=(10, 6))
    colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(features_names)))
    
    plt.barh(features_names, values, color=colors)
    plt.xlabel('Importance Score (0 to 1)')
    plt.title('Decision Tree: Feature Importance Analysis')
    plt.gca().invert_yaxis() 
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.show()

# مشاهدة النتائج البيانية
plot_feature_importance(feature_importance_dict)
