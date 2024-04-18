import pandas as pd

MULTIPLE_CHOICE_COLS = [
    'Which platforms have you used in the last 12 months? ',
    'Which cloud computing services do you have access to?',
    'Which programming languages have you used in the last 12 months? ',
    'Which organisational cloud repositories do you have access to?',
    'Which dashboarding tools do you have access to?',
    'Where do you store your project files?',
    'What do you use as team knowledge store? ',
    'Which tools do you use for project management?',
    'What do you typically use for project team communication',
    'What tools do you use for stakeholder engagement?',
    'Which of the following do you use for work? (select multiple if it applies)',
]

def split_and_explode_column(df : pd.DataFrame, col : str, sep : str = ";"):

    df = df.copy()

    df[col] = (
        df[col].str.split(sep)
    )

    df = df.explode(col)

    return df


def group_and_count_cols(df : pd.DataFrame, col_list : list):

    count_col_name = "counts"

    df = df[col_list].copy()

    for col in col_list:
        if col in MULTIPLE_CHOICE_COLS:
            df = split_and_explode_column(df, col)
            
    df = df.groupby(col_list).size().reset_index(name=count_col_name)

    df = df.sort_values(col_list[:-1] + [count_col_name], ascending = False)

    return df