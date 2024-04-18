import pandas as pd
from pathlib import Path

def import_survey_to_df():

    xlsx_survey = pd.xlsx_file = pd.ExcelFile(Path("data_in/Tech & Engineering Survey(1-34).xlsx"))

    df_survey = pd.read_excel(xlsx_survey)

    return df_survey