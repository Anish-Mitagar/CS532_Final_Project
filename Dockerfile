FROM openjdk:8-jdk

# Install Spark
RUN apt-get update && apt-get install -y wget
RUN wget https://downloads.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
RUN tar xvf spark-3.5.0-bin-hadoop3.tgz && \
    mv spark-3.5.0-bin-hadoop3 /spark && \
    rm spark-3.5.0-bin-hadoop3.tgz

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin