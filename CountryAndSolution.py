# كود لاستخراج أسماء الدول والحلول
unique_countries = df['Country'].unique().tolist()
unique_solutions = df['solution'].unique().tolist()

print("قائمة الدول (Countries) المتاحة")
print(unique_countries)

print("\n قائمة الحلول (Solutions) المتاحة ")
print(unique_solutions)

