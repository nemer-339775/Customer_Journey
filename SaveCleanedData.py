# حفظ البيانات المنظفة
# حفظ البيانات المنظفة في ملف إكسيل
df.to_excel('cleaned_customer_journey_data.xlsx', index=False)

print(" تم حفظ البيانات المنظفة في ملف إكسيل بنجاح")
df.head()