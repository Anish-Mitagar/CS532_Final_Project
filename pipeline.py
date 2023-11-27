import time

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer, OneHotEncoder
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import pandas as pd
import os

results = {}
scale = os.getenv('SCALE', "local")

os.chdir("/opt/application") #docker only

for iter in range (1):

    print(f"Running iter {iter + 1}")

   

    # Initialize Spark Session
    spark = SparkSession.builder.appName("DiabetesPredictionPipeline").getOrCreate()

    # Load the dataset
    data_path = "file:///opt/application/diabetes_prediction_dataset.csv" #docker only
    #data_path = "diabetes_prediction_dataset.csv" #local only
    df = spark.read.csv(data_path, header=True, inferSchema=True)

    # Columns for features and label
    numerical_features = ['age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    categorical_features = ['gender', 'smoking_history']
    label_col = 'diabetes'

    # Stages
    stages = []
    stage_times = []

    # Data Preprocessing for Numerical Features
    num_assembler = VectorAssembler(inputCols=numerical_features, outputCol="num_features")
    scaler = StandardScaler(inputCol="num_features", outputCol="scaled_num_features")

    # Data Preprocessing for Categorical Features
    for categoricalCol in categorical_features:
        stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + 'Index')
        encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
        stages += [stringIndexer, encoder]

    # Combine all processed numerical and categorical features into a single feature vector
    assembler_inputs = [c + "classVec" for c in categorical_features] + ["scaled_num_features"]
    assembler = VectorAssembler(inputCols=assembler_inputs, outputCol="features")
    stages += [num_assembler, scaler, assembler]


    total_time = 0
    i = 1
    # Apply each stage manually and time them
    for stage in stages:
        start_time = time.perf_counter()
        
        # For estimators (like StringIndexer, OneHotEncoder, and StandardScaler), fit and then transform
        if isinstance(stage, StringIndexer) or isinstance(stage, OneHotEncoder) or isinstance(stage, StandardScaler):
            model = stage.fit(df)
            df = model.transform(df)
        else:  # For transformers (like VectorAssembler), just transform
            df = stage.transform(df)

        end_time = time.perf_counter()
        stage_times.append((f"Preprocessing Stage {i}: " + stage.__class__.__name__, end_time - start_time))
        total_time += (end_time - start_time)
        if f"Preprocessing Stage {i}: " + stage.__class__.__name__ not in results:
            results[f"Preprocessing Stage {i}: " + stage.__class__.__name__] = list()
        print(f"Finished the following stage: {stage.__class__.__name__}")
        i +=1

    # Random Forest Classifier
    rf = RandomForestClassifier(labelCol=label_col, featuresCol="features")

    # Now apply CrossValidator
    paramGrid = ParamGridBuilder() \
        .addGrid(rf.numTrees, [10]) \
        .addGrid(rf.maxDepth, [5]) \
        .build()

    crossval = CrossValidator(estimator=rf,
                            estimatorParamMaps=paramGrid,
                            evaluator=MulticlassClassificationEvaluator(labelCol=label_col, predictionCol="prediction"),
                            numFolds=10)

    start_time = time.perf_counter()
    cvModel = crossval.fit(df)
    end_time = time.perf_counter()
    stage_times.append(("CrossValidator", end_time - start_time))
    total_time += (end_time - start_time)
    if "CrossValidator" not in results:
            results["CrossValidator"] = list()
    print(f"Finished the following stage: CrossValidator")

    stage_times.append(("Total Time", total_time))
    if "Total Time" not in results:
            results["Total Time"] = list()

    # Print out the stage times
    for stage_name, timing in stage_times:
        print(f"{stage_name} took {timing:.8f} seconds")
        results[stage_name].append(timing)

    # Model Evaluation (this is part of CrossValidator timing)
    predictions = cvModel.transform(df)
    evaluator = MulticlassClassificationEvaluator(labelCol=label_col, predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test set accuracy = " + str(accuracy))

    # Stop the session
    spark.stop()

df = pd.DataFrame(results)

# Save to a CSV file

df.to_csv(f"./spark-data/results_num_node_{scale}.csv", index=False) #docker only 

# df.to_csv(f"results_num_node_{scale}.csv", index=False) #local only