import pandas as pd

def convert_targets(input_csv_path):
    # Read the input CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Ensure the columns are correctly named and available
    if 'id' in df.columns and 'target' in df.columns:
        # Convert the target column to binary
        df['target'] = (df['target'] >= 0.5).astype(int)
        
        # Output the DataFrame to a new CSV file
        df.to_csv('submission.csv', index=False)
        print("Conversion complete. Saved to 'submission.csv'.")
    else:
        print("Input CSV must contain 'id' and 'target' columns.")


convert_targets('submission_raw.csv')

