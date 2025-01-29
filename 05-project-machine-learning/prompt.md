# Prompt

Hey Chat GPT, act as an application developer expert in python using streamlit, and build a machine learning application using scikit learn with the following workflow

1. Greet the user with a welcome message and a brief description of the application

2. Ask the user if he wants to upload the data or use the example data

3. If the user select to upload the dataset , show the uploader section on the sidebar, upload the dataset in CSV, xlxs, tsv or any possible data format

4.  If the user do not want to upload the data then provide a default dataset selection box on the sidebar. this selection box should download the data from sns.load_dataset() function. The data set should include titanic, tips and iris.

5. Print the basic data information such as data head, data shape, data description, data info and column_names

6. Ask from the user to select the column as features and also the column as target.

7. Identify the problem if the target column is a continuous numeric column the print the message that this is a regression problem, otherwise print the message this is a classification problem

8. Pre-process the data, if the data contains any missing values then fill the missing values with the iterative input function of scikit-learn, if the features are not in the same scale then scale the featues using the standard scaler function of scikit-learn, if the features are categorical variables then encode the categorical variables using the label encoder function of scikit-learn. Please keep in mind to keep the encoder separate for each column as we need to inverse transform the data at the end.

9. Ask the user to provide the train test split size via slider or user input function.

10. Ask the user to select the model from the sidebar, the model should include linear regression, decision tree, random forest and support vector machines and same classes of models for the classification problem.

11. Train the models on the training data and evaluate on the test data

12. If the problem is a regression problem, use the mean squared error, RMSE, MAE, AUROC curve and r2 score for evaluation, if the problem is classification problem, use the accuracy score, precision, reacall, f1 score and draw confusion matrix for evaluation.

13. Print the evaluation matrix for each model

14. Highlight the best model based on the evaluation matrix.

15. Ask the user if he wants to download the model, if yes then download the model in the pickle format.

16. Ask the user if he wants to make the prediction, if yes then ask the user to provide the input data using slider or uploaded file and make the prediction using the best model.

17. Show the prediction to the user.