def get_recommendations(country_name, solution_name):
    # التوصيات الإحصائية 
    by_country = df[df['Country'] == country_name]['types'].value_counts().head(4).index.tolist()
    by_solution = df[df['solution'] == solution_name]['types'].value_counts().head(4).index.tolist()
    by_both = df[(df['Country'] == country_name) & (df['solution'] == solution_name)]['types'].value_counts().head(4).index.tolist()
    
    #  إعادة الحساب (Recalculated) باستخدام أوزان شجرة القرار
    all_types = df['types'].unique()
    c_code = le_country.transform([country_name])[0]
    s_code = le_solution.transform([solution_name])[0]
    
    probs = []
    for t in all_types:
        t_code = le_types.transform([t])[0]
        query_data = pd.DataFrame([[c_code, s_code, t_code, 1]], columns=features)
        
        # التنبؤ باحتمالية الفوز 
        p = dt_model.predict_proba(query_data)[0][1]
        probs.append((t, p))
    
    # ترتيب الأنشطة حسب الأوزان الأعلى من النموذج
    recalculated = [a[0] for a in sorted(probs, key=lambda x: x[1], reverse=True)[:4]]
    
    return by_country, by_solution, by_both, recalculated