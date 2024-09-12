from OlympicsDataAnalysis import logger
from OlympicsDataAnalysis.pipeline.Stage_01_data_ingestion import DataIngestionPipeline
from OlympicsDataAnalysis.pipeline.Stage_02_data_preprocessing import DataPreprocessPipeline

STAGE_NAME = "Data Ingestion stage"
STAGE_NAME_02 = "Data Preprocess Stage"

# try:
#     logger.info(f"==== stage {STAGE_NAME} started =======")
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logger.info(f"======== stage {STAGE_NAME} completed ============")
# except Exception as e:
#     raise logger.exception(e)

try:
    logger.info(f"==== stage {STAGE_NAME_02} started =======")
    data_preprocessing = DataPreprocessPipeline()
    data_preprocessing.main()
    logger.info(f"======== stage {STAGE_NAME_02} completed ============")
except Exception as e:
    raise logger.exception(e)