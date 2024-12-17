import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RBFInterpolator

categories = [
    "Gedung lt 1 Bu Eti", "Gedung lt 1 Bu Is Widi", "Gedung lt 2 ruang Pak Asep", "Gedung lt 2 ruang Bu Enung", "Gedung lt 3 ruang Bu Elvi",
    "Gedung lt 3 ruang Bu Vira", "BTQ sampai Bu Ranti", "Bu Farah", "Bu Lia sampai Bu Irna",
    "Bu Muti", "Bu Sabila", "Bu Septi sampai Bu Astri", "Bu Shinta", 
    "Bu Titin", "Kelas 6 Bu Novi", "Pak Irfan", "Ruangan UKS", "SD Lab 1 Ruangan Pak Irwan"]

def create_heatmap(dataframe, title="Heatmap", grid_size=100):
   
    # Remove duplicate points
    dataframe = dataframe.drop_duplicates(subset=['Longitude', 'Latitude'])

    # Create grid for interpolation
    x = np.linspace(dataframe['Longitude'].min(), dataframe['Longitude'].max(), grid_size)
    y = np.linspace(dataframe['Latitude'].min(), dataframe['Latitude'].max(), grid_size)
    X, Y = np.meshgrid(x, y)

    # Data for interpolation
    points = dataframe[['Longitude', 'Latitude']].values
    values = dataframe['LTERSSI'].values

    # Perform RBF interpolation
    rbf = RBFInterpolator(points, values, kernel='linear')
    Z = rbf(np.column_stack([X.ravel(), Y.ravel()])).reshape(grid_size, grid_size)

    # Create the heatmap plot
    fig, ax = plt.subplots(figsize=(10, 8))
    c = ax.contourf(X, Y, Z, levels=100, cmap='coolwarm')
    plt.colorbar(c, ax=ax, label='LTERSSI (dBm)')
    ax.scatter(dataframe['Longitude'], dataframe['Latitude'], color='black', s=5, label='Data Points')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(title)
    ax.legend()
    return fig

def plot_average_column(dfs, column_name):
    
    average_values = [df[column_name].mean() for df in dfs.values() if column_name in df.columns]

    average_df = pd.DataFrame({
    'Category': categories,
    'Average_' + column_name : average_values})
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(average_df['Category'], average_df['Average_' + column_name], color='skyblue')
    ax.set_title(f'Average {column_name}')
    ax.set_xlabel('Tempat')
    ax.set_ylabel(f'Average {column_name}')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    ax.set_xticklabels(average_df['Category'], rotation=45, ha='right')

    return fig



