# ======================================
# 5. تشغيل النظام وتحليل النتائج
# ======================================
run_advanced_journey_system(country="US", solution="MRS", last_action="Email")
# ======================================

# إظهار الدول والحلول والأنشطة المتوفرة في ملف البيانات وذلك لاستخدامها عند تشغيل النظام
print(f"\n" + "-"*30)
print(f" AVAILABLE DATA SUMMARY:")
print(f"------------------------------")
print(f"  THE COUNTRIES LIST:  {df['Country'].unique().tolist()}")
print(f"------------------------------")
print(f"  THE SOLUTIONS LIST:  {df['solution'].unique().tolist()}")
print(f"------------------------------")
# إضافة قائمة الأنشطة المتوفرة
print(f"  AVAILABLE ACTIONS:   {df['types'].unique().tolist()}")
print(f"------------------------------")