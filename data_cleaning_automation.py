import pandas as pd
import os

def clean_data(file_path, output_folder="cleaned_data"):
    try:
        # Read the file
        df = pd.read_csv(file_path)
        print("Original Shape:", df.shape)

        # Step 1: Remove duplicates
        df.drop_duplicates(inplace=True)

        # Step 2: Clean column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Step 3: Fill missing values
        for col in df.columns:
            if df[col].dtype == 'object':
                mode_val = df[col].mode()
                if not mode_val.empty:
                    df[col].fillna(mode_val[0], inplace=True)
            else:
                if df[col].isnull().sum() > 0:
                    if df[col].skew() < 1:  # Less skewed: use mean
                        df[col].fillna(df[col].mean(), inplace=True)
                    else:  # More skewed: use median
                        df[col].fillna(df[col].median(), inplace=True)

        # Step 4: Remove remaining missing rows (if any)
        df.dropna(inplace=True)

        # Step 5: Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        # Save cleaned file
        output_path = os.path.join(output_folder, "cleaned_" + os.path.basename(file_path))
        df.to_csv(output_path, index=False)

        print("Cleaned Data Saved to:", output_path)
        print("Final Shape:", df.shape)

    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    file_to_clean = "D:\Internship\Data Cleaning Automation Script\academic.csv"  # Change path as needed
    clean_data(file_to_clean)
