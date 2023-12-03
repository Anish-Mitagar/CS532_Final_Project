import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import re

def plot_and_save_distributions(directory_path):
    # Loop through each CSV file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            # Read the CSV file
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)
            num_trails, _ = df.shape
            num_workers = int(re.findall('[0-9]+', file_path)[0])

            # Plot normal distribution curves for each column
            plt.figure(figsize=(15, 10))

            for i, column in enumerate(df.columns):
                plt.subplot(3, 3, i+1)
                plt.hist(df[column], bins=10, density=True, alpha=0.6, color='g')
                mn, mx = plt.xlim()
                plt.xlim(mn, mx)
                kde_xs = np.linspace(mn, mx, 301)
                kde = st.gaussian_kde(df[column])
                plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
                plt.title(column)
                plt.xlabel('Seconds')
                plt.ylabel('Density')

            plt.suptitle(f"Execution time distributions for {num_workers} workers over {num_trails} trails",fontsize=30)
            plt.tight_layout()

            # Save the plot to a file
            plot_filename = f"plot_{filename[:-4]}.png" 
            plt.savefig(os.path.join(directory_path, plot_filename))
            plt.close() 

plot_and_save_distributions("./data") 