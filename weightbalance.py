
# استخدام class_weight='balanced' لموازنة البيانات وتحسين الدقة
dt_model = DecisionTreeClassifier(max_depth=7, class_weight='balanced', random_state=42)
dt_model.fit(X, y)
