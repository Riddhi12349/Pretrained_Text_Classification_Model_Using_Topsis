# Pretrained_Model_Comparison_Using_Topsis

Pretrained Text Classification Model using Topsis

## Overview

"Text Classification" refers to task in natural language processing (NLP) where text documents or pieces of text are assigned to predefined categories or classes based on their content or characteristics. The goal of text classification is to automatically classify text data into one or more categories or classes, enabling automated organization, analysis, and retrieval of textual information

Here , We are comparing different Pre-trained Models based on their Topsis Score and analyzing them using BarChart

# Data.csv file:

| Model      | Accuracy | Precision | Recall | F1 Score | Training Time\(hrs\) | Inference Time\(ms/sentence\) | Model Robustness | Interpretability |
| ---------- | -------- | --------- | ------ | -------- | -------------------- | ----------------------------- | ---------------- | ---------------- |
| BERT       | 0\.85    | 0\.86     | 0\.84  | 0\.85    | 24                   | 2                             | High             | Medium           |
| RoBERTa    | 0\.87    | 0\.88     | 0\.86  | 0\.87    | 28                   | 2\.5                          | High             | Medium           |
| XLNet      | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 36                   | 3                             | High             | Medium           |
| ALBERT     | 0\.84    | 0\.85     | 0\.83  | 0\.84    | 20                   | 1\.5                          | High             | Medium           |
| DistilBERT | 0\.82    | 0\.83     | 0\.81  | 0\.82    | 12                   | 1                             | Medium           | Medium           |
| Electra    | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 30                   | 3                             | High             | Medium           |
| T5         | 0\.88    | 0\.89     | 0\.87  | 0\.88    | 40                   | 4                             | High             | Medium           |

## Key Features:

1. **Metrics Considered:**

   - The comparison is based on essential metrics, including Accuracy,F1 Score,Precision,Recall , Training Time and Inference Time.

2. **Methodology - TOPSIS:**

   - The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method is employed for the comparison. This method considers both the similarity to the ideal solution and the dissimilarity to the negative ideal solution, providing a comprehensive ranking.

3. **Models Evaluated:**
   - Real-world pretrained models like BERT, RoBERTa, XLNet, ALBERT, DistilBERT, Electra, and T5 are included in the comparison. These models are widely used in text classification tasks.

## Project Structure:

- **`data.csv`**: CSV file containing evaluation metrics for each model.
- **`result.csv`**: CSV file with ranked results in tabular format and data used for creating a bar chart.
- **`BarChart.png`**: Bar chart visualizing the model comparison.

## Results and Analysis:

1. **Ranked Table:**

- Explore detailed ranked results in conversational result.csv:

| Model      | Accuracy | Precision | Recall | F1 Score | Training Time\(hrs\) | Inference Time\(ms/sentence\) | TOPSIS_Score        | Rank |
| ---------- | -------- | --------- | ------ | -------- | -------------------- | ----------------------------- | ------------------- | ---- |
| BERT       | 0\.85    | 0\.86     | 0\.84  | 0\.85    | 24                   | 2\.0                          | 0\.3938956920180145 | 5\.0 |
| RoBERTa    | 0\.87    | 0\.88     | 0\.86  | 0\.87    | 28                   | 2\.5                          | 0\.5473714258730631 | 4\.0 |
| XLNet      | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 36                   | 3\.0                          | 0\.767313481373997  | 2\.0 |
| ALBERT     | 0\.84    | 0\.85     | 0\.83  | 0\.84    | 20                   | 1\.5                          | 0\.2452443153106506 | 6\.0 |
| DistilBERT | 0\.82    | 0\.83     | 0\.81  | 0\.82    | 12                   | 1\.0                          | 0\.0                | 7\.0 |
| Electra    | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 30                   | 3\.0                          | 0\.6523292486386351 | 3\.0 |
| T5         | 0\.88    | 0\.89     | 0\.87  | 0\.88    | 40                   | 4\.0                          | 1\.0                | 1\.0 |

2. **Bar Chart:**

The bar chart visually represents the performance metrics of each model, providing an easy-to-understand comparison. Accuracy,F1_Score,Precision,Recall and normalized ranks are included for comprehensive evaluation.

## Analysis:

**Model Performance:**

The best model we got on the given dataset is T5 with accuracy 88%. <br>

Given Table for Model Performance:<br>

| Model      | Accuracy | Precision | Recall | F1 Score | Training Time\(hrs\) | Inference Time\(ms/sentence\) | Rank |
| ---------- | -------- | --------- | ------ | -------- | -------------------- | ----------------------------- | ---- |
| T5         | 0\.88    | 0\.89     | 0\.87  | 0\.88    | 40                   | 4\.0                          | 1\.0 |
| XLNet      | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 36                   | 3\.0                          | 2\.0 |
| Electra    | 0\.86    | 0\.87     | 0\.85  | 0\.86    | 30                   | 3\.0                          | 3\.0 |
| RoBERTa    | 0\.87    | 0\.88     | 0\.86  | 0\.87    | 28                   | 2\.5                          | 4\.0 |
| BERT       | 0\.85    | 0\.86     | 0\.84  | 0\.85    | 24                   | 2\.0                          | 5\.0 |
| ALBERT     | 0\.84    | 0\.85     | 0\.83  | 0\.84    | 20                   | 1\.5                          | 6\.0 |
| DistilBERT | 0\.82    | 0\.83     | 0\.81  | 0\.82    | 12                   | 1\.0                          | 7\.0 |

Next Steps:<br>
Feel free to analyze the provided CSV files for more insights.
Consider adjusting the evaluation metrics or adding new models based on your specific use case.
Use the project as a foundation for ongoing research and development in text conversational.
