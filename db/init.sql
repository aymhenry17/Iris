CREATE DATABASE irisdb;

\connect irisdb;

CREATE TABLE iris_data (
    id SERIAL PRIMARY KEY,
    feature1 FLOAT,
    feature2 FLOAT,
    feature3 FLOAT,
    feature4 FLOAT,
    target FLOAT
);