# تشغيل النظام وتجربته
# حدد الدولة ونوع الحل المطلوب البحث عنهما بين علامات التنصيص

country, sol = "US", "MRS"
c_top, s_top, b_top, rec_top = get_recommendations(country, sol)

print(f"Results for {country} & {sol}")
print(f"Top 4 by Country: {c_top}")
print(f"Top 4 by Solution: {s_top}")
print(f"Top 4 Combined: {b_top}")
print(f"Recalculated Top 4 (Next Steps): {rec_top}")