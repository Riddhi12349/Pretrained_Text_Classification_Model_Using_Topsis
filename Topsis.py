import pandas as pd
import numpy as np

data = pd.read_csv('dataset.csv')
data.head(5)

# Extract relevant columns
accuracy = data["Accuracy"].values
f1_score = data["F1 Score"].values
precision = data["Precision"].values
recall = data["Recall"].values
training_time = data["Training Time(hrs)"].values
inference_time = data["Inference Time(ms/sentence)"].values

# Weights for each parameter
weights = np.array([0.15 ,0.15, 0.15, 0.2, 0.2, 0.15])

# Normalize the matrix
normalized_matrix = np.column_stack(
    [
        accuracy / np.max(accuracy),
        f1_score / np.max(f1_score),
        precision / np.max(precision),
        recall / np.max(recall),
        training_time / np.max(training_time),
        inference_time / np.max(inference_time)
    ]
)

# Calculate the weighted normalized decision matrix
weighted_normalized_matrix = normalized_matrix * weights

# Ideal and Negative Ideal solutions
ideal_solution = np.max(weighted_normalized_matrix, axis=0)
negative_ideal_solution = np.min(weighted_normalized_matrix, axis=0)

# Calculate the separation measures
distance_to_ideal = np.sqrt(
    np.sum((weighted_normalized_matrix - ideal_solution) ** 2, axis=1)
)
distance_to_negative_ideal = np.sqrt(
    np.sum((weighted_normalized_matrix - negative_ideal_solution) ** 2, axis=1)
)

# Calculate the TOPSIS scores
topsis_scores = distance_to_negative_ideal / (
    distance_to_ideal + distance_to_negative_ideal
)

# Rank the models based on TOPSIS scores
data["TOPSIS_Score"] = topsis_scores
data["Rank"] = data["TOPSIS_Score"].rank(ascending=False)

# Print the results
print("Model Ranking:")
print(data[["Model", "TOPSIS_Score", "Rank"]].sort_values(by="Rank"))

data.to_csv("result.csv", index=False)
