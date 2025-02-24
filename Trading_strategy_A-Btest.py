### **2. `ab_test_analysis.py` (A/B Testing Script FOR TESTING OUT TRADING STRATGIES)**
```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind

# Load dataset
data = pd.read_csv("trade_data.csv")

# Check dataset structure
print(data.head())

# Group A and B data
group_A = data[data["group"] == "A"]["converted"]
group_B = data[data["group"] == "B"]["converted"]

# Perform Chi-Square Test
contingency_table = pd.crosstab(data["group"], data["converted"])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-Square Test Results:\nChi2 Statistic: {chi2:.4f}, p-value: {p:.4f}")

# Perform t-Test
t_stat, p_value = ttest_ind(group_A, group_B, equal_var=False)

print(f"t-Test Results:\nt-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p < alpha:
    print("Reject the null hypothesis: There is a significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates.")
