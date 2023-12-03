# Clear profiles folder
rm -rf "./_profiles"/*
for scale in 1 2 3 4 5 6 7 8
do
    rm -rf "./_profiles"/*
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
rm -rf "./_profiles"/*