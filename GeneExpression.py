import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
df = pd.read_csv("mmp7_expression.csv")

# Step 2: Calculate average MMP-7 expression
df["Average"] = df[["Mouse1", "Mouse2", "Mouse3"]].mean(axis=1)

# Step 3: Create dictionary to easily access groups
positive_avg = df[df["Group"] == "Positive"]["Average"].values[0]

# Step 4: Calculate fold change compared to Positive group
df["Fold_Change_vs_Positive"] = df["Average"] / positive_avg

# Step 5: Label expression status
def classify(fc):
    if fc <= 0.5:
        return "Strong Downregulation"
    elif fc <= 0.8:
        return "Mild Downregulation"
    elif fc >= 1.2:
        return "Upregulated"
    else:
        return "No Significant Change"

df["Status"] = df["Fold_Change_vs_Positive"].apply(classify)

# Step 6: Print summary
print(df[["Group", "Average", "Fold_Change_vs_Positive", "Status"]])

# Step 7: Bar plot
plt.figure(figsize=(10,6))
sns.barplot(data=df, x="Group", y="Fold_Change_vs_Positive", hue="Status", dodge=False)
plt.axhline(1, color="gray", linestyle="--")
plt.title("Fold Change of MMP-7 vs Positive Control")
plt.ylabel("Fold Change (Treated / Positive)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 8: Heatmap of expression levels
expression_values = df.set_index("Group")[["Mouse1", "Mouse2", "Mouse3"]]
plt.figure(figsize=(8, 6))
sns.heatmap(expression_values, annot=True, cmap="magma", fmt=".1f")
plt.title("MMP-7 Expression Levels in Each Mouse")
plt.tight_layout()
plt.show()


