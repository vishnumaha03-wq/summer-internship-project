import pandas as pd
from pathlib import Path

INPUT_FILE = "data/glerrors.xlsx"

OUTPUT_FILE = "cleaned_data/cleaned_GL.csv"


def preprocess():

    df = pd.read_excel(
        INPUT_FILE
    )

    print(
        "\nOriginal Shape:",
        df.shape
    )

    df.columns = (
        df.columns
        .str.strip()
    )

    df.drop_duplicates(
        inplace=True
    )

    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].fillna(
                "Missing"
            )

        else:

            df[col] = df[col].fillna(
                0
            )

    Path(
        "cleaned_data"
    ).mkdir(
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nClean data saved to {OUTPUT_FILE}"
    )

    print(
        "Preprocessing complete."
    )


if __name__ == "__main__":

    preprocess()