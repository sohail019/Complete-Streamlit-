import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer

st.set_page_config(page_title="Machine learning App", layout="wide")


# Function to preprocess data
def preprocess_data(X, y, problem):
    # Identify categorical columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    
    # Encode categorical columns
    for col in categorical_cols:
        X[col] = LabelEncoder().fit_transform(X[col])
    
    # Encode target variable if it is categorical
    if y.dtype == 'object' or y.dtype.name == 'category':
        y = LabelEncoder().fit_transform(y)
    
    # Fill missing values
    imp = IterativeImputer()
    X_imputed = pd.DataFrame(imp.fit_transform(X), columns=X.columns)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    return X_scaled, y


# Function to train and evaluate models
def train_and_evaluate(X_train, X_test, y_train, y_test, model, problem_type):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    if problem_type == 'Regression':
        mse = mean_squared_error(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return predictions, mse, mae, r2
    else:
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions, average='weighted')
        recall = recall_score(y_test, predictions, average='weighted')
        f1 = f1_score(y_test, predictions, average='weighted')
        return predictions, accuracy, precision, recall, f1

# Main application function
def main():
    st.title("Machine Learning Application")
    st.write("Welcome to the machine learning application. This app allows you to train and evaluate different machine learning models on your dataset.")
    
    # Initialize data variable
    data = pd.DataFrame()
    
    # Data upload or example data selection
    data_source = st.sidebar.selectbox("Do you want to upload data or use example data?", ["Upload", "Example"])
    
    if data_source == "Upload":
        uploaded_file = st.sidebar.file_uploader("Choose a file", type=['csv', 'xlsx', 'tsv'])
        if uploaded_file is not None:
            if uploaded_file.type == "text/csv":
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                data = pd.read_excel(uploaded_file)
            elif uploaded_file.type == "text/tab-separated-values":
                data = pd.read_csv(uploaded_file, sep='\t')
    else:
        dataset_name = st.sidebar.selectbox("Select a dataset", ["titanic", "tips", "iris"])
        data = sns.load_dataset(dataset_name)
    
    if not data.empty:
        st.write("Data Head:", data.head())
        st.write("Data Shape:", data.shape)
        st.write("Data Description:", data.describe())
        st.write("Data Info:", data.info())
        st.write("Column Names:", data.columns.tolist())
        
        # Select features and target
        features = st.multiselect("Select features columns", data.columns.tolist())
        target = st.selectbox("Select target column", data.columns.tolist())
        problem_type = st.selectbox("Problem Type", ["Classification", "Regression"])
        
        if features and target and problem_type:
            X = data[features]
            y = data[target]
            
            st.write(f"You have selected a {problem_type} problem.")
            
            # Button to start analysis
            if st.button("Run Analysis"):
                # Pre-process data
                X_processed, y_processed = preprocess_data(X, y, problem_type)
                
                # Train-test split
                test_size = st.slider("Select test split size", 0.1, 0.5, value=0.2)
                X_train, X_test, y_train, y_test = train_test_split(X_processed, y_processed, test_size=test_size, random_state=42)
                
                # Model selection based on problem type
                model_options = ['Linear Regression', 'Decision Tree', 'Random Forest', 'SVM'] if problem_type == 'Regression' else ['Decision Tree', 'Random Forest', 'SVM']
                selected_model = st.sidebar.selectbox("Select model", model_options)
                
                # Initialize model
                if selected_model == 'Linear Regression':
                    model = LinearRegression()
                elif selected_model == 'Decision Tree':
                    model = DecisionTreeRegressor() if problem_type == 'Regression' else DecisionTreeClassifier()
                elif selected_model == 'Random Forest':
                    model = RandomForestRegressor() if problem_type == 'Regression' else RandomForestClassifier()
                elif selected_model == 'SVM':
                    model = SVR() if problem_type == 'Regression' else SVC()
                    
                # Train and evaluate model
                predictions, *metrics = train_and_evaluate(X_train, X_test, y_train, y_test, model, problem_type)
                
                # Evaluation metrics and results presentation
                if problem_type == 'Regression':
                    mse, mae, r2 = metrics
                    st.write(f"Mean Squared Error: {mse}")
                    st.write(f"Mean Absolute Error: {mae}")
                    st.write(f"R^2 Score: {r2}")
                else:
                    accuracy, precision, recall, f1 = metrics
                    st.write(f"Accuracy: {accuracy}")
                    st.write(f"Precision: {precision}")
                    st.write(f"Recall: {recall}")
                    st.write(f"F1 Score: {f1}")
                
                st.write("Model training and evaluation complete.")
                
                # Save the trained model
                model_filename = f"{selected_model.replace(' ', '_').lower()}_model.pkl"
                with open(model_filename, 'wb') as file:
                    pickle.dump(model, file)
                st.write(f"Model saved as {model_filename}")
                
                # Allow user to download the model
                with open(model_filename, 'rb') as file:
                    st.download_button(label="Download Model", data=file, file_name=model_filename, mime='application/octet-stream')
                
                # Allow user to make predictions with new data
                st.write("Make Predictions with New Data")
                new_data = st.text_area("Enter new data (comma-separated values)", "")
                if new_data:
                    new_data = np.array(new_data.split(',')).reshape(1, -1)
                    scaler = StandardScaler().fit(X_train)  # Define and fit scaler
                    new_data = scaler.transform(new_data)  # Scale new data
                    new_predictions = model.predict(new_data)
                    st.write(f"Predictions: {new_predictions}")
if __name__ == "__main__":
    main()