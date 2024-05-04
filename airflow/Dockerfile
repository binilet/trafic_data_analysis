# Use the official Airflow image as the base
FROM apache/airflow:latest

# Set the working directory to /app
WORKDIR /app

# Install dbt and its dependencies
RUN pip install dbt-postgres dbt-redshift

# Copy the dbt project into the Docker image
COPY dbt/ /app/dbt/

# Change ownership to airflow user
RUN sudo chown -R airflow /app/dbt

# Copy the Airflow requirements into the Docker image
COPY requirements.txt /app/requirements.txt

# Install the Airflow dependencies
RUN pip install -r /app/requirements.txt

# Copy the Airflow DAGs into the Docker image
COPY dags/ /opt/airflow/dags/

# Expose the port Airflow web server listens on
EXPOSE 8080

# Initialize the Airflow database
RUN airflow db init

# Start the Airflow webserver in daemon mode
CMD ["bash", "-c", "airflow webserver -D -p 8080 && airflow scheduler"]
