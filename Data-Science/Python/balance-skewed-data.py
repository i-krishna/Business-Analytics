# balancing skewed data with imbalanced-learn library is a standard resource for resampling methods

import numpy as np
from sklearn.datasets import make_classification
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Generate a highly imbalanced dataset
X, y = make_classification(n_samples=10000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=3,
                           n_clusters_per_class=1,
                           weights=[0.10, 0.20, 0.70],
                           flip_y=0, random_state=42)

print(f"Original class distribution: {Counter(y)}")

# Apply SMOTE to oversample the minority classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

print(f"Resampled class distribution (SMOTE): {Counter(y_resampled)}")

# Apply a combination of SMOTE and Random Undersampling
oversample = SMOTE(random_state=42)
X_over, y_over = oversample.fit_resample(X, y)

undersample = RandomUnderSampler(random_state=42)
X_combined, y_combined = undersample.fit_resample(X_over, y_over)

print(f"Combined class distribution (SMOTE + Undersampling): {Counter(y_combined)}")
