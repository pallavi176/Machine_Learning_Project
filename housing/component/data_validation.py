import os
import sys
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.logger import logging
from housing.exception import HousingException

class DataValidation:

    def __init__(self, data_validation_config: DataValidationConfig, data_ingestion_artifact: DataIngestionArtifact) -> None:
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e

    

    def is_train_test_file_exists(self):
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exists = False
            is_test_file_exists = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)

            is_available =  is_train_file_exists and is_test_file_exists

            logging.info(f"Is train and test file exists?-> {is_available}")

            if not is_available:
                message = f'Training file: {train_file_path} or Testing file: {test_file_path} is not presnt'
                logging.info(message)
                raise Exception(message)

            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e

    def validate_dataset_schema(self):
        try:
            validation_status = False

            #Validate training and testing dataset using schema file
            #1. Number of Column
            #2. Check the value of ocean proximity 
            # acceptable values     <1H OCEAN
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN
            #3. Check column names

            validation_status = True

            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self):
        try:
            is_available = self.is_train_test_file_exists()
            validation_status = self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e, sys) from e