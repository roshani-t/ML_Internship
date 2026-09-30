import pandas as pd
import sys


def clean_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    print("Original dataset shape:", df.shape)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicate rows removed:", duplicates)

    # Fill missing numerical values with median
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    # Fill missing text values with the most common value
    text_columns = df.select_dtypes(include="str").columns

    for column in text_columns:
        df[column] = df[column].fillna(df[column].mode()[0])

    # Save cleaned dataset
    df.to_csv(output_file, index=False)

    print("Cleaned dataset shape:", df.shape)
    print("Missing values after cleaning:")
    print(df.isnull().sum())
    print("Cleaned file saved to:", output_file)
    print("Cleaning completed successfully!")


# CLI section
if len(sys.argv) != 3:
    print("Usage:")
    print("python src\\clean_data.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

clean_data(input_file, output_file)