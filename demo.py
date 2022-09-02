import os
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration
from housing.exception import HousingException
from housing.logger import logging
from housing.component.data_transformation import DataTransformation

def main():
    try:
        # pipeline = Pipeline()
        # pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # schema_file_path = r"\config\schema.yaml"
        # file_path = r"\housing\artifact\data_ingestion\2022-08-29-16-23-20\ingested_data\train\housing.csv"
        # df = DataTransformation.load_data(file_path = file_path, schema_file_path = schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        config_path = os.path.join("config", "config.yaml")
        pipeline = Pipeline(Configuration(config_file_path = config_path))
        pipeline.start()
        logging.info("main function execution completed.")
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()