import pandas as pd

# Read ESS Poland round 9
# .dta is a Stata file
df = pd.read_stata('ESS9PL.stata/ESS9PL.dta', convert_categoricals=False)

print(df.head())
print(df.columns)
print(df.netustm)

print(df.netustm.value_counts().sort_index())