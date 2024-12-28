import scipy.stats as stats

# Example data
group1 = [23, 45, 67, 89, 12]
group2 = [34, 56, 78, 90, 23]
group3 = [45, 67, 89, 12, 34]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")