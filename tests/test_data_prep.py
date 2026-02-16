import yaml
from pyspark.sql import SparkSession

def test_config_load(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    assert config["schema"] == "telco_dev"
    assert "bronze_table" in config
    assert "silver_table" in config
    assert "fs_table" in config
    print("Config load test passed")

def test_bronze_table_load():
    spark = SparkSession.builder.getOrCreate()
    df = spark.table("telco_dev.bronze_customer_churn")
    assert df.count() > 0
    required_columns = ["customerID", "gender", "SeniorCitizen", "tenure", "TotalCharges", "Churn"]
    assert all(col in df.columns for col in required_columns)
    print("Bronze table load test passed")

def test_total_charges_transformation():
    spark = SparkSession.builder.getOrCreate()
    df = spark.table("telco_dev.silver_customer_churn")
    blanks = df.filter(df.TotalCharges.isNull()).count()
    assert blanks >= 0
    assert dict(df.dtypes)["TotalCharges"] in ("float", "double")
    print("TotalCharges transformation test passed")