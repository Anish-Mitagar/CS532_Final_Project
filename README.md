# CS532 Final Project

### Team Members: Anish Mitagar, Scott Fortune, Karishma Manchanda, Sugun Yadla

#### Presentation Link: https://www.youtube.com/watch?v=7hOtzbmHNoM

#### Note: The terms nodes and workers are used interchangably in this repo

## ML Pipeline Execution Time versus Horizontal Scaling

This project demostrates the effect Horizontal Scaling in the Distributed Computing Set Up has on the execution time of several stages of a ML Pipeline. Every stage of the ML Pipeline ulilizes a Spark Job/Function from the PySpark library.

## Experiment Setup

Step 1: Have a Unix Based Machine

Step 2: Install Docker

Step 3: Add these packages to your python envionment
```
pip3 install pandas numpy matplotlib scipy snakeviz 
```

Step 4: Start Docker daemon by starting Docker application

Step 5: Build Docker Image
```
docker build -t my-spark-image .     
```

## Instructions for Running 

**Step 1:** To run the experiment, run the following shell script. Outputs to "data" folder.

```
./run_tests.sh
```
**NOTE 1:** to adjust the over which number of workers/node to run the workload on, go to line 3 in run_tests.sh and change the numbers

**NOTE 2:** to adjust number of trials, go to line 30 in pipeline.py and change the number inside ```range(<int>)```

**Step 2:** To generate graphs of the execution time distributions of the pipeline stages per experiment run. Outputs to "data" folder.

```
python3 generate_visuals.py
```

**Step 3:** To generate graphs comparing the execution time distributions of the pipeline stages for two experiments run. Outputs to "data" folder.

```
python3 comparision_visuals.py <int> <int>
```

**EXAMPLE** If want to compare the execution time distrubutions between number workers/nodes equalling 2 versus number workers/nodes equalling 4, then type ```python3 comparision_visuals.py 2 4```


**Step 4:** To generate basic statistics for the execution times of the pipeline stages per experiment run. Outputs to "data" folder.

```
python3 generate_stats.py
```

## Our Results given our hardware setup

**Machine:** 2021 16 inch Macbook Pro with M1 Max and 32GB RAM

Docker Resource Allocation settings:
* CPU limit: 9
* Memory limit: 20 GB
* Swap: 4 GB

Experiment Setups: We ran the workload 50 times each for number of workers/nodes equalling 1, 2, 3, 4, 5, 6, 7, and 8.

Our data and graphs can be found the in the official_results folder.

**NOTE** In the inital implementation of pipeline.py, our time recordings were not "exact" because it took into account the small overhead of the master node starting and stopping the timer before and after running a Pyspark function. We found this out using the profiler code (```profilerdeck.py```) provided by TA Andy Zane. We want to find the pure runtimes of the Pyspark functions (the stages of the pipeline) running in a distributed manner amongst the workers/nodes.

So our official with the time recording including the small amount of master node overhead is placed under the official_results/with_master_timer_overhead directory.

Our official with the time recording excluding master node overhead using the current implementation of pipeline.py is placed under the official_results/without_master_timer_overhead directory. This the most correct/accurate results.

You will see the the results in both subdirectories are hardly different, and the overall trends are the same.

## Playing with the Function Profiler
To see the small time difference in between recording times with account for small master node overhead from starting and stopping timers, look at the csv files in subdirectories official_results/profiler_investigation/method_1 and official_results/profiler_investigation/method_2 where method 2 are the results obtain without the small master node overhead. To see that these results are accurate, compare the second to last value in the csv file to the top value in .prof file. To view the .prof file, run ```snakeviz <path to .prof file>```.

To actually play with the profiler, use ```run_tests_w_prof.sh``` with ```pipeline_w_prof.py``` in a similar manner to the instructions above.

To actually play with the profiler, use ```run_tests_w_prof2.sh``` with ```pipeline_w_prof2.py``` in a similar manner to the instructions above.