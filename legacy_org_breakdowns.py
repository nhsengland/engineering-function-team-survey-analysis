import pandas as pd
from pathlib import Path

from src.data_imports import data_imports

df_survey = data_imports.import_survey_to_df()

for col in df_survey.columns:
    print("'" + col + "'")

group_column = 'What is your legacy team?\xa0\xa0'
count_column = 'Which platforms have you used in the last 12 months? '

df_survey_with_group_and_count_columns_only = df_survey[[group_column, count_column]]

print(df_survey_with_group_and_count_columns_only)

df_survey_with_group_and_count_columns_only[count_column] = (
    df_survey_with_group_and_count_columns_only[count_column].str.split(";")
)

df_survey_count_column_exploded = (df_survey_with_group_and_count_columns_only
    .explode(count_column)
)

df_platform_by_legacy_org = df_survey_count_column_exploded.groupby([group_column, count_column]).size().reset_index(name='counts')

df_platform_by_legacy_org = df_platform_by_legacy_org.sort_values([group_column, "counts"], ascending = False)

print(df_platform_by_legacy_org)

