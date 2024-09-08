from OlympicsDataAnalysis import logger
from OlympicsDataAnalysis.pipeline.Stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"==== stage {STAGE_NAME} started =======")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"======== stage {STAGE_NAME} completed ============")
except Exception as e:
    raise logger.exception(e)
