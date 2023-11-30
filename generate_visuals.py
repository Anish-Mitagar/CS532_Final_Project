import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# This is a mock-up function to demonstrate the process.
# In practice, you should replace the 'directory_path' with your actual directory path.

def plot_and_save_distributions(directory_path):
    # Loop through each CSV file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            # Read the CSV file
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)

            # Plot normal distribution curves for each column
            plt.figure(figsize=(15, 10))

            for i, column in enumerate(df.columns):
                plt.subplot(3, 3, i+1)
                plt.hist(df[column], bins=20, density=True, alpha=0.6, color='g')
                mn, mx = plt.xlim()
                plt.xlim(mn, mx)
                kde_xs = np.linspace(mn, mx, 301)
                kde = st.gaussian_kde(df[column])
                plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
                plt.title(column)
                plt.ylabel('Density')

            plt.tight_layout()

            # Save the plot to a file
            plot_filename = f"plot_{filename[:-4]}.png"  # Remove '.csv' and add '.png'
            plt.savefig(os.path.join(directory_path, plot_filename))
            plt.close()  # Close the plot to avoid displaying it in the notebook

# Example usage (replace with your directory path)
plot_and_save_distributions("./data") 

"Function ready to use. Replace the directory path with the actual path where your CSV files are located."
