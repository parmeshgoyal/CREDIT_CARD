# Credit Card Fraud Detection System

A machine learning project that uses a Random Forest classifier to classify credit card transactions as fraudulent or legitimate.

## Project Overview

This project uses Python and machine learning to identify potentially fraudulent credit card transactions.

The current model performs the following steps:

1. Loads transaction data from `creditcard.csv` using Pandas.
2. Separates input features and the target column `Class`.
3. Splits the dataset into training and testing sets (80:20).
4. Trains a Random Forest classifier with 100 estimators.
5. Evaluates the model using accuracy, a confusion matrix, and a classification report.

## Features

- Credit card transaction classification
- Random Forest machine learning model
- Training and testing data split
- Model performance evaluation
- Precision, recall, and F1-score reporting

## Tech Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn
- **Algorithm:** Random Forest Classifier

## Project Structure

```text
CREDIT_CARD/
├── ML.py
├── creditcard.csv
├── README.md
└── CREDIT CARD FRAUD DETECTION .pptx
```

*Note: The structure above shows the main files required for the project. The dataset must be downloaded separately if it is not already available.*

## Installation

Make sure Python 3 is installed.

Install the required libraries:

```bash
python -m pip install pandas scikit-learn
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/parmeshgoyal/CREDIT_CARD.git
```

### 2. Open the project directory

```bash
cd CREDIT_CARD
```

### 3. Prepare the dataset

Place `creditcard.csv` in the project directory. Ensure that the dataset contains a target column named `Class`.

### 4. Run the project

Rename `ML.txt` to `ML.py` if you have not already done so, then run:

```bash
python ML.py
```

## Model Evaluation

The model reports the following evaluation metrics:

- **Accuracy:** Overall proportion of correctly classified transactions.
- **Confusion Matrix:** Shows correct and incorrect predictions for each class.
- **Precision:** Measures how many transactions predicted as fraudulent were actually fraudulent.
- **Recall:** Measures how many actual fraudulent transactions were detected.
- **F1-Score:** Combines precision and recall into a single metric.

For fraud detection, precision and recall are particularly important because fraudulent transactions may be much less common than legitimate ones.

## Future Improvements

- Add visualizations for the confusion matrix.
- Evaluate class imbalance and apply suitable balancing techniques if required.
- Add precision-recall curves for better model comparison.
- Include a requirements file for reproducible installation.
- Improve the project interface for easier use.

## Author

**Parmesh Goyal**

- GitHub: [parmeshgoyal](https://github.com/parmeshgoyal)
- Project Repository: [CREDIT_CARD](https://github.com/parmeshgoyal/CREDIT_CARD)
