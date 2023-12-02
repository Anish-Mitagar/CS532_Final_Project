import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import glob
import os
import sys

# List of CSV file paths
csv_files = glob.glob(os.getcwd() + "/data" + '/*.csv')  # Modify this path to your CSV files directory

if __name__ == "__main__":
    if len(sys.argv) == 3:

        # Columns to be compared
        columns = [
            "Preprocessing Stage 1: StringIndexer",
            "Preprocessing Stage 2: OneHotEncoder",
            "Preprocessing Stage 3: StringIndexer",
            "Preprocessing Stage 4: OneHotEncoder",
            "Preprocessing Stage 5: VectorAssembler",
            "Preprocessing Stage 6: StandardScaler",
            "Preprocessing Stage 7: VectorAssembler",
            "CrossValidator",
            "Total Time"
        ]

        # Read each CSV file and store data for each column
        data_per_column = {column: [] for column in columns}


        num_trails = None

        csv_files = [os.getcwd() + f"/data/results_num_node_{sys.argv[1]}.csv", os.getcwd() + f"/data/results_num_node_{sys.argv[2]}.csv"]
        print(csv_files)
        if not os.path.exists(csv_files[0]):
             raise FileNotFoundError(f"The file {csv_files[0]} does not exist.")
        if not os.path.exists(csv_files[1]):
             raise FileNotFoundError(f"The file {csv_files[1]} does not exist.")
        for file in csv_files:
            df = pd.read_csv(file)
            num_trails, _ = df.shape
            for column in columns:
                if column in df.columns:
                    data_per_column[column].append(df[column])

        # Plotting the data
        plt.figure(figsize=(15, 10))

        for i, column in enumerate(columns):
            plt.subplot(3, 3, i + 1)
            for j, data in enumerate(data_per_column[column]):
                label = f"File {j+1}"  # Label each dataset by file number
                # Plot histogram
                plt.hist(data, bins=10, density=True, alpha=0.6, label=label)
                # Plot KDE
                mn, mx = plt.xlim()
                kde_xs = np.linspace(mn, mx, 301)
                kde = st.gaussian_kde(data)
                plt.plot(kde_xs, kde.pdf(kde_xs), label=f"{label} KDE")
            plt.title(column)
            plt.xlabel('Seconds')
            plt.ylabel('Density')
            plt.legend([f'{sys.argv[1]} workers', f'{sys.argv[1]} workers KDE curve', f'{sys.argv[2]} workers', f'{sys.argv[2]} workers KDE curve'])
        plt.suptitle(f"Execution time distributions for {sys.argv[1]} versus {sys.argv[2]} workers over {num_trails} trails",fontsize=30)

        plt.tight_layout()
        plt.savefig(f"./data/plot_results_num_node_{sys.argv[1]}_vs_{sys.argv[2]}")