
# حفظ المسارات في ملف CSV 
top_5_paths.to_csv('top_customer_paths.csv', index=False, encoding='utf-8-sig')

print(" تم استخراج المسارات وحفظها في ملف: top_customer_paths.csv")
display(top_5_paths.head(10))