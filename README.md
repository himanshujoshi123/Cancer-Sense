# Breast Cancer Prediction 🔬💻

This repository contains a machine learning model for predicting the presence of breast cancer using the `sklearn` dataset `load_breast_cancer`. The model is trained using Random Forest, SVM, and XGBoost algorithms. The data preprocessing, exploratory data analysis (EDA), feature selection, and oversampling using SMOTE are also included. 📊📈

## Data Features 📊

The data consists of 569 samples with 30 features each. The features are real-valued and represent characteristics of the breast cancer cells. The target variable is binary, indicating the Malignant (1 : presence) or Benign (0 : absence) of breast cancer.

### The features include:

- Radius (mean of distances from center to points on the perimeter)
- Texture (standard deviation of gray-scale values)
- Perimeter
- Area
- Smoothness (local variation in radius lengths)
- Compactness (perimeter^2 / area - 1.0)
- Concavity (severity of concave portions of the contour)
- Concave points (number of concave portions of the contour)
- Symmetry
- Fractal dimension ("coastline approximation" - 1)
- Radius error (mean absolute error in radius lengths)
- Texture error (mean absolute error in gray-scale values)
- ... (and more)

## Data Preprocessing 🧪

Before training the model, the data was preprocessed using the following steps:

- Data cleaning: Missing values were checked and handled appropriately.
- Feature selection: The top 10 features were selected based on their importance score from the Random Forest algorithm.
- Feature scaling: The features were scaled using standard scaling to ensure comparability.
- Data splitting: The data was split into a training set and a testing set using a 70:30 ratio.

## Exploratory Data Analysis (EDA) 📈

EDA was performed using the following techniques:

- Correlation matrix
- Visualization: Histograms and box plots

## Model Training 📊

The model was trained using the following algorithms:

- Random Forest
- SVM
- XGBoost

## Oversampling ⚙️

To handle the class imbalance in the dataset, the SMOTE (Synthetic Minority Over-sampling Technique) algorithm was used.

## User App 📱

A user-friendly app was created to use the model for prediction. The app takes the values of the 10 selected features as input and predicts the probability of breast cancer for the given input.

To use the app:

1. Download the repository.
2. Set the command prompt path to the downloaded folder.
3. Run `pip install -r requirements.txt` to install the necessary packages.
4. Run `python application.py` to start the app.

The app will prompt you to enter the values of the 10 selected features. After submitting the values, the app will display the result.
