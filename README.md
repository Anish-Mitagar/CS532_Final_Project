# CS532 Final Project

### Team Members: Anish Mitagar, Scott Fortune, Karishma Manchanda, Sugun Yadla

## ML Pipeline Execution Time versus Horizontal Scaling

This project demostrates the effect Horizontal Scaling in the Distributed Computing Set Up has on the execution time of several stages of the ML Pipeline. Every stage of the ML Pipeline ulilizes a Spark Job/Function from the PySpark library.

![Alt text](https://www.matridtech.net/wp-content/uploads/2020/07/Horizontal-Scaling.png)

## The ML Pipeline Stage

### Data Preprocessing

### Model Training

#### The Dataset: Diabetes Diagnosis
The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. We chose this dataset from Kaggle as the data for each parameter is varied enough for it to be preprocessed.
![Alt text](https://scitechdaily.com/images/Diabetes-Treatments.jpg)

#### The Model Family: Random Forests (Classification)
The Random Forest machine learning model is an ensemble learning method widely used for both classification and regression tasks. This model operates by constructing a multitude of decision trees during training, which are used to make predictions. Each tree in the 'forest' is built from a random sample of the data, and at each decision point within the tree, a random subset of features is considered. This randomness not only helps in creating a diverse set of trees but also significantly reduces the risk of overfitting, a common issue where a model performs well on training data but poorly on unseen data. In practice, for classification tasks, each tree 'votes' for a class, and the class with the most votes is chosen as the model's prediction. For regression tasks, the model averages the outputs of different trees.

![Alt text](https://miro.medium.com/v2/resize:fit:1200/1*hmtbIgxoflflJqMJ_UHwXw.jpeg)

One of the key strengths of Random Forest is its versatility and robustness across various types of data, be it categorical or numerical. It generally requires less preprocessing of data and is easier to tune compared to many other algorithms. Additionally, Random Forest models provide valuable insights into the importance of different features in predicting the outcome, which can be crucial in understanding and interpreting the results. Due to these attributes, Random Forests are highly regarded for their strong performance and are a popular choice for a wide range of machine learning applications.
#### Hyperparameter Grid Search + K-Fold Cross Validation

![Alt text](https://knowledge.dataiku.com/latest/_images/hyperparameter-search.png)

![Alt text](https://i1.wp.com/sqlrelease.com/wp-content/uploads/2021/07/K-fold-cross-validation-1.jpg?fit=2290%2C928&ssl=1)
#### Evaluation and Selection

## Experiment Setup

## Instructions for Running 

```
./run_tests.sh
```

```
python3 generate_visuals.py
```
