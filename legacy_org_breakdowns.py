import pandas as pd
from pathlib import Path

from src.data_imports import data_imports
from src.processing import aggregations

df_survey = data_imports.import_survey_to_df()

group_column = 'What is your legacy team?\xa0\xa0'

print(
    aggregations.group_and_count_cols(df_survey, [group_column, 'Which platforms have you used in the last 12 months? '])
)

print(
    aggregations.group_and_count_cols(df_survey, [group_column, 'I can do my job with the tools available to me '])
)

print(
    aggregations.group_and_count_cols(df_survey, [group_column, 'Which of the following do you use for work? (select multiple if it applies)'])
)
