import pandas as pd
import os

def calculate_statistics_for_directory(directory_path, output_file_path):
    # Initialize a DataFrame to store the results
    combined_stats_df = pd.DataFrame()

    # Iterate over each CSV file in the directory
    for file in os.listdir(directory_path):
        if file.endswith(".csv"):
            file_path = os.path.join(directory_path, file)
            df = pd.read_csv(file_path)

            # Extracting a prefix from the file name
            prefix = os.path.splitext(file)[0].capitalize()

            # Initialize a DataFrame for the current file's statistics
            stats_df = pd.DataFrame()

            # Calculate statistics for each column
            for column in df.columns:
                stats_df.at[prefix + '_Mean', column] = df[column].mean()
                stats_df.at[prefix + '_Median', column] = df[column].median()
                stats_df.at[prefix + '_Standard Deviation', column] = df[column].std()

            # Append the stats from the current file to the combined DataFrame
            combined_stats_df = pd.concat([combined_stats_df, stats_df])

    # Sort the rows alphabetically by their index (row names)
    combined_stats_df.sort_index(inplace=True)

    # Save the combined statistics to a new CSV file
    combined_stats_df.to_csv(output_file_path)

    return combined_stats_df

directory_path = "./data"  
output_file_path = './data/output_statistics.csv'   

# Calculate and print the statistics
stats_data = calculate_statistics_for_directory(directory_path, output_file_path)