#!/bin/bash

for scale in 8
do
  echo "Running with $scale workers"
  export SCALE=$scale
  docker-compose up --scale spark-worker=$scale
  docker-compose down
done
