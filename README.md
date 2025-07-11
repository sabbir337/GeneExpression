# GeneExpression

# 🧬 Gene Expression Analysis of MMP-7 in an IPF Mouse Model

## 🧪 Project Overview

This project investigates the **gene expression levels of MMP-7** in a mouse model of **Idiopathic Pulmonary Fibrosis (IPF)**. The study evaluates the **therapeutic potential of _Tylophora indica_ extract** by analyzing MMP-7 expression across various treatment groups.

## 🎯 Objective

- Analyze MMP-7 gene expression data from experimental mice
- Compare treatment effects relative to the IPF-positive group
- Classify expression changes (e.g., upregulation, downregulation)
- Visualize the findings using plots (bar plot and heatmap)

## 🧾 Dataset Description

The dataset file `mmp7_expression.csv` contains MMP-7 expression levels (arbitrary units) for six experimental groups, with three biological replicates (mice) per group.

### 📋 Sample Data

| Group         | Mouse1 | Mouse2 | Mouse3 |
|---------------|--------|--------|--------|
| Control       | 10     | 12     | 11     |
| Positive      | 80     | 85     | 90     |
| Pre-Treatment | 55     | 52     | 58     |
| Treatment 1   | 20     | 22     | 18     |
| Treatment 2   | 40     | 42     | 38     |
| Drug          | 25     | 27     | 26     |

## 🧰 Tools & Libraries Used

- `pandas` – Data loading and manipulation  
- `matplotlib` – Plotting  
- `seaborn` – Advanced visualizations  

Install the required libraries with:

```bash
pip install pandas matplotlib seaborn
```

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/sabbir337/GeneExpression.git
   ```

2. Ensure the following files are present:
   - `gene_expression_analysis.py`
   - `mmp7_expression.csv`

3. Run the Python script:
   ```bash
   python gene_expression_analysis.py
   ```

## 📊 Output Description

### ✅ Console Output:
- Average MMP-7 expression per group
- Fold change compared to the IPF-positive group
- Regulation status classification

### 📈 Plots:
- **Bar Plot** showing fold change vs Positive group
- **Heatmap** showing expression values for each mouse

## 🧠 Biological Insight

- MMP-7 is a key biomarker in lung fibrosis progression.
- The **Positive** group (80–90 units) shows strong upregulation.
- **Treatment 1 (300 mg/kg)** shows the **greatest downregulation** (~20 units), indicating the strongest therapeutic effect.
- This suggests _Tylophora indica_ may suppress fibrosis-associated gene expression.

## 📌 Expression Status Criteria

| Fold Change vs Positive | Classification          |
|-------------------------|--------------------------|
| ≤ 0.5                   | Strong Downregulation    |
| > 0.5 and ≤ 0.8         | Mild Downregulation      |
| 0.8 < FC < 1.2          | No Significant Change    |
| ≥ 1.2                   | Upregulated              |

## 👨‍🔬 Author

- **Md. Sabbir Khan**  
  Department of Biochemistry and Molecular Biology

## 📄 License

This project is intended for academic and educational purposes only.
