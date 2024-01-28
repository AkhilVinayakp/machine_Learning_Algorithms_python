# Feature engineering from raw data
# raw data path: C:\Users\nirva\Documents\GitHub\machine_Learning_Algorithms_python\EtE_projects\house-prices\data\train.csv

import logging
import hydra
from prefect import flow, task
from omegaconf import DictConfig

from utils.initializer import init_spark
from utils.data_loader import file_loader

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

@task
def get_data(spark_session ,file_name):
    @hydra.main(version_base=None, config_path="config", config_name="feat_pipe")
    def data_load_path(cfg:DictConfig):
        """load data from the path
        """
        abs_path = f"{cfg.dev.source_path}\{file_name}"
        logging.info(f"Reading data from path {abs_path}")
        data = file_loader(spark_session, abs_path, schema_info=False)
        return data

    return data_load_path








@flow(name="feat-eng-house-price-dev", log_prints=True)
def feat_pipeline():
    """
    Load the data from the source and create feature dataset.
    """
    session, context = init_spark(app="Test")
    data = get_data(session, file_name="train")()
    logging.info("load data type :", type(data))

if __name__ == "__main__":
    feat_pipeline.serve(name="depl-feat-dev-pipe")