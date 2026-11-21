# 🛡️ Network Intrusion Detection System (Network IDS)

### Machine Learning-Based Network Traffic Classification & Security Dashboard

A machine learning-based Network Intrusion Detection System that analyzes network traffic features and classifies network activity as **BENIGN** or **ATTACK** using a trained Random Forest classifier.

The project combines data preprocessing, exploratory data analysis, feature selection, machine learning model training and evaluation with an interactive Streamlit dashboard designed to present network security insights.

---

## 📌 Project Overview

Network security is an important part of modern computing. Malicious network activities such as port scanning, denial-of-service attacks and brute-force attempts can compromise systems and sensitive information.

Traditional security methods often depend on predefined rules and signatures. This project explores a machine learning-based approach that identifies suspicious network traffic by learning patterns from network flow data.

The system uses the CIC-IDS2017 dataset to train and evaluate a Random Forest classifier.

## ✨ Key Features

- **Network Traffic Classification:** Classifies network traffic as BENIGN or ATTACK.
- **Machine Learning Model:** Uses a Random Forest classifier trained on network flow features.
- **Interactive Dashboard:** Provides a multi-page cybersecurity dashboard using Streamlit.
- **Traffic Detection:** Supports CSV-based network traffic analysis.
- **Attack Analysis:** Presents attack-related insights and traffic distributions.
- **Model Performance Evaluation:** Displays accuracy, precision, recall, F1-score and confusion matrix.
- **Data Visualization:** Uses interactive and statistical visualizations to understand network traffic.
- **Prediction Export:** Allows users to download prediction results as a CSV file.
- **Sample Dataset:** Includes a small sample CSV for testing the prediction workflow.

## 🧠 Machine Learning Model

**Algorithm:** Random Forest Classifier

**Dataset:** CIC-IDS2017

**Classification Type:** Binary Classification

| Class | Label |
|---|---|
| BENIGN | 0 |
| ATTACK | 1 |

### Model Configuration

- Number of estimators: 100
- Random state: 42
- Class weighting: Balanced
- Train-test split: 80:20
- Stratified sampling: Enabled

### Dataset Information

| Description | Records |
|---|---:|
| Original combined dataset | 2,830,743 |
| Processed dataset | 2,520,798 |
| Training records | 2,016,638 |
| Testing records | 504,160 |
| Selected features | 70 |

The dataset was cleaned by handling missing values, infinite values, duplicate records and constant features before model training.

## 📊 Model Performance

The trained Random Forest model achieved the following results on the held-out test dataset:

| Metric | Result |
|---|---:|
| Accuracy | 99.89% |
| ROC-AUC | 0.9998 |
| BENIGN Precision | 99.96% |
| BENIGN Recall | 99.91% |
| ATTACK Precision | 99.56% |
| ATTACK Recall | 99.80% |
| ATTACK F1-score | 99.68% |

### Confusion Matrix

| Actual / Predicted | BENIGN | ATTACK |
|---|---:|---:|
| BENIGN | 418,634 | 378 |
| ATTACK | 173 | 84,975 |

The model evaluation demonstrates strong classification performance on the selected test split. However, further validation using capture-day-separated data would help assess generalization to previously unseen network traffic.

## 🖥️ Interactive Dashboard

The Streamlit application contains six main sections:

1. **Overview** – Displays key project statistics and network traffic insights.
2. **Live Monitor** – Provides the monitoring and traffic visualization interface.
3. **Traffic Detection** – Supports network traffic classification and CSV-based predictions.
4. **Attack Analysis** – Presents attack-related patterns and analysis.
5. **Model Performance** – Displays model evaluation metrics and visualizations.
6. **About Project** – Explains the system, methodology and project information.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn, Altair |
| Dashboard | Streamlit |
| Model Serialization | Joblib |
| Dataset | CIC-IDS2017 |
| Version Control | Git, GitHub |

## 📁 Project Structure

```text
Network-IDS/
│
├── .streamlit/
│   └── config.toml
│
├── app/
├── dashboard/
│   ├── views/
│   │   ├── overview.py
│   │   ├── live_monitor.py
│   │   ├── traffic_detection.py
│   │   ├── attack_analysis.py
│   │   ├── model_performance.py
│   │   └── about_project.py
│   │
│   ├── data_loader.py
│   └── styles.py
│
├── data/
│   └── processed/
│       ├── random_forest_model.pkl
│       ├── sample_upload.csv
│       ├── model_evaluation_metrics.json
│       ├── confusion_matrix.png
│       ├── confusion_matrix_dark.png
│       └── traffic_distribution.png
│
├── models/
├── replay/
│
├── app.py
├── prepare_dataset.py
├── explore_dataset.py
├── feature_analysis.py
├── feature_selection.py
├── split_dataset.py
├── train_model.py
├── evaluate_model.py
├── predict.py
├── check_labels.py
├── eda.py
│
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/amulypshetty/Network-IDS.git
```

### 2. Navigate to the project directory

```bash
cd Network-IDS
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your browser, usually at:

```text
http://localhost:8501
```

## 📂 Dataset

This project uses the **CIC-IDS2017 dataset**, which contains labeled network traffic and attack scenarios.

The original dataset is not included in this GitHub repository because of its large file size.

Download it from the Canadian Institute for Cybersecurity:

https://www.unb.ca/cic/datasets/ids-2017.html

For the complete training pipeline, place the extracted CSV files in:

```text
data/MachineLearningCVE/
```

The repository already includes a trained model and a small sample CSV for testing the prediction workflow.

## 🚀 Future Enhancements

- Real-time network packet capture and traffic monitoring.
- Integration with additional machine learning algorithms.
- Multi-class attack classification.
- Improved validation using capture-day-separated datasets.
- Alert notifications for suspicious network activities.
- Deployment to a cloud hosting platform.
- Enhanced reporting and security analytics.

## 🎯 Project Objectives

- Understand network traffic patterns and intrusion detection.
- Apply machine learning techniques to cybersecurity.
- Build an interactive dashboard for network traffic analysis.
- Evaluate classification performance using standard ML metrics.
- Explore practical applications of data science in network security.

## 👩‍💻 Author

**Amulya P Shetty**

Information Science and Engineering

Sahyadri College of Engineering and Management

GitHub: https://github.com/amulypshetty

---

⭐ If you find this project interesting, consider giving the repository a star!


