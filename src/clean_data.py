import pandas as pd
import sys
import os


def clean_data(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return False

    try:
        # Load the dataset
        df = pd.read_csv(input_file)

        print("Original dataset shape:", df.shape)

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Remove duplicate rows
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()

        print("Duplicate rows removed:", duplicates)

        # -------------------------------------------------
        # Handle missing target values
        # -------------------------------------------------

        target_column = "Life expectancy"

        if target_column in df.columns:
            missing_target = df[target_column].isna().sum()

            if missing_target > 0:
                print(
                    f"Rows removed because '{target_column}' was missing: "
                    f"{missing_target}"
                )

                # Life expectancy is the main analysis/target column,
                # so missing target values are removed instead of imputed.
                df = df.dropna(subset=[target_column])

        # -------------------------------------------------
        # Fill missing numerical values
        # -------------------------------------------------

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            # Do not include the target column because
            # missing target values have already been removed.
            if column == target_column:
                continue

            # Calculate median for each country
            country_median = df.groupby("Country")[column].transform("median")

            # Fill using country median first
            df[column] = df[column].fillna(country_median)

            # If a country has no value at all for this column,
            # fall back to the overall dataset median.
            overall_median = df[column].median()

            df[column] = df[column].fillna(overall_median)

        # -------------------------------------------------
        # Fill missing text values
        # -------------------------------------------------

        # Works with both pandas 2.x and pandas 3.x
        text_columns = df.select_dtypes(
            include=["object", "string"]
        ).columns

        for column in text_columns:
            if df[column].isna().any():

                mode_values = df[column].mode()

                if not mode_values.empty:
                    df[column] = df[column].fillna(mode_values.iloc[0])
                else:
                    df[column] = df[column].fillna("Unknown")

        # -------------------------------------------------
        # Save cleaned dataset
        # -------------------------------------------------

        df.to_csv(output_file, index=False)

        print("Cleaned dataset shape:", df.shape)

        print("\nMissing values after cleaning:")
        print(df.isnull().sum())

        print("\nCleaned file saved to:", output_file)
        print("Cleaning completed successfully!")

        return True

    except Exception as error:
        print(f"Error while cleaning dataset: {error}")
        return False


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print(
            "python src\\clean_data.py "
            "<input_file> <output_file>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    success = clean_data(input_file, output_file)

    if not success:
        sys.exit(1)