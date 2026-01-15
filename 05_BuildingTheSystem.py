# 4- النظام  
def run_advanced_journey_system(country, solution, last_action=None, last_touch_weight=0.3):
    # توحيد المدخلات مع البيانات المنظفة
    country = country.strip().upper()
    solution = solution.strip().upper()
    
    print(f"\n" + "="*70)
    print(f" CUSTOMER JOURNEY SYSTEM: {country} | {solution}")
    print("="*70)

    try:
        c_code = le_country.transform([country])[0]
        s_code = le_solution.transform([solution])[0]
    except ValueError:
        print(f" ERROR: The input '{country}' or '{solution}' was not found.")
        return

    # عرض الأهمية النسبية داخل النظام
    print(f"\n FEATURE IMPORTANCE (Model Weights):")
    for feat, val in sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"   - {feat:15}: {val*100:.1f}% ")

    # المخرجات الإحصائية (Top 4)
    c_df = df[df['Country'] == country]
    s_df = df[df['solution'] == solution]
    b_df = df[(df['Country'] == country) & (df['solution'] == solution)]

    c_top = c_df['types'].value_counts().head(4).index.tolist() if not c_df.empty else ["No Data"]
    s_top = s_df['types'].value_counts().head(4).index.tolist() if not s_df.empty else ["No Data"]
    b_top = b_df['types'].value_counts().head(4).index.tolist() if not b_df.empty else ["No Data"]

    # تاريخ المسارات المسجلة 
    print(f"\n TOP 5 PATHS :")
    segment_paths = top_paths_summary[(top_paths_summary['Country'] == country) & 
                                     (top_paths_summary['solution'] == solution)].head(5)
    if not segment_paths.empty:
        for i, row in segment_paths.iterrows():
            print(f"   [{row['frequency']} times]: {row['types']}")

    # التوصيات وإعادة الحساب الديناميكي
    all_actions = df['types'].unique()
    recalc_results = []
    
    for action in all_actions:
        try:
            a_code = le_types.transform([action])[0]
            query = pd.DataFrame([[c_code, s_code, a_code, 1]], columns=features)
            base_w = dt_model.predict_proba(query)[0][1]
            
            # خفض الوزن إذا كان هو نفس النشاط الأخير (تجنب التكرار الممل)
            final_w = base_w * (1 - last_touch_weight) if (last_action and action == last_action) else base_w
            recalc_results.append((action, final_w))
        except ValueError:
            continue
    
    sorted_recommendations = sorted(recalc_results, key=lambda x: x[1], reverse=True)[:4]

    # استخراج أقصر رحلة فوز 
    won_paths = paths_df[(paths_df['Country'] == country) & 
                         (paths_df['solution'] == solution) & 
                         (paths_df['target'] == 1)].copy()
    
    if not won_paths.empty:
        won_paths['journey_len'] = won_paths['types'].apply(lambda x: len(x.split(' -> ')))
        best_trip = won_paths.sort_values('journey_len').iloc[0]['types']
    else:
        best_trip = "No successful (WON) journeys recorded yet."

    print(f"\n RECOMMENDATIONS:")
    print(f"• Top 4 by Country:            {c_top}")
    print(f"• Top 4 by Solution:           {s_top}")
    print(f"• Top 4 by Country & Solution: {b_top}")
    
    print(f"\n RECALCULATED NEXT STEPS :")
    for act, score in sorted_recommendations:
        print(f"   - {act:15} | Prob: {score*100:.1f}%")
    
    print(f"\n BEST SHORTER JOURNEY TO WIN:")
    print(f"   {best_trip}")
    print("="*70)
