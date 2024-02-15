import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import result
dataset = pd.read_csv("result.csv")


# Display the table
print("Model Ranking Table:")
print(dataset[["Model","Accuracy","Precision","Recall","F1 Score","Training Time(hrs)","Inference Time(ms/sentence)","Rank"]].sort_values(by="Rank"))
# Bar chart
labels = dataset["Model"]
num_models = len(labels)

# Parameters for bar chart
accuracy = dataset["Accuracy"]
f1_score = dataset["F1 Score"]
precision = dataset["Precision"]
recall = dataset["Recall"]
training_time = dataset["Training Time(hrs)"]
inference_time = dataset["Inference Time(ms/sentence)"]
ranks = dataset["Rank"]

# Normalize ranks to a scale of 0 to 1 for better comparison
normalized_ranks = ranks / np.max(ranks)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(num_models)

ax.bar(index, accuracy, width=bar_width, label="Accuracy")
ax.bar(
    index,
    f1_score,
    width=bar_width,
    label="f1_score",
    bottom=accuracy,
)
ax.bar(
    index,
    recall,
    width=bar_width,
    label="Recall",
    bottom=accuracy + f1_score + precision,
)
ax.bar(
    index,
    precision,
    width=bar_width,
    label="Training Time",
    bottom=accuracy + f1_score,
)
ax.bar(
    index,
    recall,
    width=bar_width,
    label="Inference Time",
    bottom=accuracy + f1_score + precision,
)
ax.bar(
    index,
    normalized_ranks,
    width=bar_width,
    label="Normalized Rank",
    color="black",
    alpha=0.5,
)

ax.set_xticks(index)
ax.set_xticklabels(labels)
ax.set_ylabel("Metrics")
ax.set_title("Text Conversational Model Comparison")

ax.legend(loc = 'upper right')
plt.savefig("BarChart.png")
plt.show()
