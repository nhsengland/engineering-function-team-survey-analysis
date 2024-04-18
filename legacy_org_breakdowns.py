import pandas as pd
from pathlib import Path

from src.data_imports import data_imports
from src.processing import aggregations

df_survey = data_imports.import_survey_to_df()

# for col in df_survey.columns:
#     print("'" + col + "'")

group_column = 'What is your legacy team?\xa0\xa0'
count_column = 'Which platforms have you used in the last 12 months? '





print(
    aggregations.group_and_count_cols(df_survey, [group_column, count_column])
)