# MLOps Telco Churn Project

This repo contains a production-oriented ML pipeline for customer churn prediction using Databricks, including dev/prod separation, configuration management, workflow orchestration, and CI/CD deployment.

## Environment-Specific Schema Naming
To ensure a clear separation of development and production data artifacts, this project uses dedicated database schemas:


__telco_dev__
Contains all development tables, views, features, and intermediate results. Used for experimentation, testing, and QA.

__telco_prod__
Holds production-grade tables, features, and model outputs. Only code that has passed all tests and reviews should write here.

Note: All pipeline code and notebooks are designed to be environment-agnostic. The target schema is set dynamically using configuration files (dev.yaml, prod.yaml), making it easy to promote code and artifacts between dev and prod.


