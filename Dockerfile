FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pandas
RUN pip3 install pyspark

RUN apt-get update && apt-get install -y wget
RUN wget https://downloads.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
RUN tar xvf spark-3.5.0-bin-hadoop3.tgz && \
    mv spark-3.5.0-bin-hadoop3 /spark && \
    rm spark-3.5.0-bin-hadoop3.tgz

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

COPY ./pipeline.py /opt/application/pipeline.py
COPY ./diabetes_prediction_dataset.csv /opt/application/diabetes_prediction_dataset.csv
COPY ./pipeline_w_prof.py /opt/application/pipeline_w_prof.py
COPY ./pipeline_w_prof2.py /opt/application/pipeline_w_prof2.py
COPY ./profilerdeck.py /opt/application/profilerdeck.py
RUN mkdir /opt/application/spark-data
RUN mkdir /opt/application/_profiles

