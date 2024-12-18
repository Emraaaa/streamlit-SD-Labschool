import streamlit as st
import pandas as pd
from fungsi import create_heatmaps, plot_average_column

st.set_page_config(layout="wide")

# Streamlit App
st.title("Visualisasi Data SD Labschool")

# Sidebar
menu = st.sidebar.selectbox(
    "Pilih Tampilan:",
    ["Heatmap", "Grafik"]
)

# categories and path file
categories = [
    "Gedung lt 1 Bu Eti", "Gedung lt 1 Bu Is Widi", "Gedung lt 2 ruang Pak Asep", "Gedung lt 2 ruang Bu Enung", "Gedung lt 3 ruang Bu Elvi",
    "Gedung lt 3 ruang Bu Vira", "BTQ sampai Bu Ranti", "Bu Farah", "Bu Lia sampai Bu Irna",
    "Bu Muti", "Bu Sabila", "Bu Septi sampai Bu Astri", "Bu Shinta", 
    "Bu Titin", "Kelas 6 Bu Novi", "Pak Irfan", "Ruangan UKS", "SD Lab 1 Ruangan Pak Irwan"
]

parameter = ["LTERSSI", "Level", "Qual", "DL_bitrate", "UL_bitrate", "SNR"]

file_paths = [
    'Gedung 3 Lantai/Lt 1 Ruang Bu Eti LAB A/XL_2024.12.13_09.34.37.txt',
    'Gedung 3 Lantai/Lt 1 Ruang Bu Is Widi LAB C/XL_2024.12.13_09.42.51.txt',
    'Gedung 3 Lantai/Lt 2 Ruang Asep/XL_2024.12.13_09.59.35.txt',
    'Gedung 3 Lantai/Lt 2 Ruang Enung/XL_2024.12.13_09.50.43.txt',
    'Gedung 3 Lantai/Lt 3 Ruang Ulvi/XL_2024.12.13_10.09.00.txt',
    'Gedung 3 Lantai/Lt 3 Ruang Vira/XL_2024.12.13_10.18.50.txt',
    'BTQ SAMPAI BU RANTI/Smartfren_100%_untuk_Indonesia_2024.12.13_11.16.29.txt',
    'BU FARAH/Smartfren_100%_untuk_Indonesia_2024.12.13_10.11.08.txt',
    'BU LIA SAMPAI BU IRNA/Smartfren_100%_untuk_Indonesia_2024.12.13_10.59.10.txt',
    'BU MUTI/Smartfren_100%_untuk_Indonesia_2024.12.13_09.53.30.txt',
    'BU SABILA/Smartfren_100%_untuk_Indonesia_2024.12.13_10.06.48.txt',
    'BU SEPTI SAMPAI BU ASTRI/Smartfren_100%_untuk_Indonesia_2024.12.13_11.34.34.txt',
    'BU SHINTA/Smartfren_100%_untuk_Indonesia_2024.12.13_09.35.44.txt',
    'BU TITIN/Smartfren_100%_untuk_Indonesia_2024.12.13_09.38.40.txt',
    'KELAS 6 Bu Novi/XL_2024.12.13_11.19.30.txt',
    'PAK IRFAN/Smartfren_100%_untuk_Indonesia_2024.12.13_09.58.04.txt',
    'RUANGAN UKS/Smartfren_100%_untuk_Indonesia_2024.12.13_10.30.15.txt',
    'SD LAB 1 di Ruang Pa Irwin/XL_2024.12.13_10.43.20.txt'
]


if menu == "Heatmap":
    dfs = {}
    for i, path in enumerate(file_paths, start=1):
        try:
            dfs[f"df{i}"] = pd.read_csv(path, sep='\t')
        except FileNotFoundError:
            print(f"File tidak ditemukan: {path}")
        except Exception as e:
            print(f"Error membaca file {path}: {e}")

    selected_parameter = st.selectbox("Pilih Parameter:", parameter)
    st.write(f"### Menampilkan Grafik untuk: **{selected_parameter}**")

    try:
        figures = create_heatmaps(dfs, selected_parameter, grid_size=100)

        cols_per_row = 3 
        num_figures = len(figures)

        for i in range(0, num_figures, cols_per_row):
            cols = st.columns(cols_per_row)  
            for j, col in enumerate(cols):
                idx = i + j  
                if idx < num_figures:  
                    with col:
                        st.write(f"#### {categories[idx]}")  
                        st.pyplot(figures[idx][1])  
    except Exception as e:
        st.error(f"Error: {e}")

elif menu == "Grafik":
    dfs = {}
    for i, path in enumerate(file_paths, start=1):
        try:
            dfs[f"df{i}"] = pd.read_csv(path, sep='\t')
        except FileNotFoundError:
            print(f"File tidak ditemukan: {path}")
        except Exception as e:
            print(f"Error membaca file {path}: {e}")

    selected_parameter = st.selectbox("Pilih Parameter:", parameter)
    st.write(f"### Menampilkan Grafik untuk: **{selected_parameter}**")
    try:
        graph = plot_average_column(dfs, selected_parameter)
        st.pyplot(graph)
    except FileNotFoundError:
        st.error(f"File tidak ditemukan")
    except Exception as e:
        st.error(f"Error: {e}")
