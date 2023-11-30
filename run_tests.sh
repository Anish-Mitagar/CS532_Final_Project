#!/bin/bash

# for scale in 2
# do
#   echo "Running with $scale workers"
#   export SCALE=$scale
#   docker-compose up --scale spark-worker=$scale
#   docker-compose down
# done

for scale in 1 2 4 8
do
    echo "Running experiment with scale = $scale"

    # Export the scale environment variable
    export SCALE=$scale

    # Start the Docker containers with the specified scale
    docker-compose up --scale spark-worker=$scale -d

    echo "Running Spark Job..."

    # Submit the Spark job to the cluster
    docker exec spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./opt/application/pipeline.py > /dev/null 2>&1

    # Shut down the Docker containers
    docker-compose down

    echo "Spark Job Finished."

    echo "Completed experiment for scale = $scale"
done
