import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

st.title("Data Analyst Excercise📊📈")
st.write("Ini adalah web sederhana untuk menghandle missing value dan anomaly.")

st.subheader("📂Upload File")
file = st.file_uploader("Upload file di sini, pastikan filenya dengan tipe excel.", type=['xlsx'])

if file is not None:
    df = pd.read_excel(file)
    st.subheader('🫵This is your data')
    st.write(f"Data yang kamu upload terdiri dari ***{df.shape[0]}*** baris, dan ***2*** kolom yaitu ***{df.columns[0]}*** dan ***{df.columns[1]}***")
    st.write(df)

    # Let users choose which column represents date and total sales
    date_column = st.selectbox("Pilih kolom tanggal:", df.columns)
    sales_column = st.selectbox("Pilih kolom total sales:", df.columns)

    if date_column and sales_column and date_column != sales_column:
        st.subheader("📪Handle Missing Values")
        st.write("Missing value atau nilai yang hilang akan diisi dengan methode **ffill** atau mengisi nilai kosong dengan nilai sebelumnya.")
        null = df.isnull().sum()
        st.write(null)

        df[sales_column].fillna(method='ffill', inplace=True)
        df[sales_column].fillna(0, inplace=True)

        if null[sales_column] > 0:
            st.success('Hasil data yang telah bebas dari missing value✅')
            st.write(df)
        else:
            st.success('Tidak ada missing value 😊')


        st.subheader("😶‍🌫️Handle Anomaly")
        st.write("Anomaly data adalah data yang tidak sesuai atau berbeda secara signifikan dari pola umum atau tren dalam suatu kumpulan data. Handle anomaly menggunakan metode Z-Score dengan threshold = 3")

        # anomaly
        mean = df[sales_column].mean()
        std = df[sales_column].std()

        # Step 1: Deteksi Outlier dengan Z-score
        df["z_score"] = (df[sales_column] - mean) / std
        df["is_anomaly"] = df["z_score"].abs() > 3
        outliers = df[df["z_score"].abs() > 3]  # Outlier = lebih dari 3 std deviasi

        fig = plt.figure(figsize=(12, 5))
        plt.plot(df[date_column], df[sales_column], marker="o", linestyle="-", label="Data Asli")
        plt.scatter(outliers[date_column], outliers[sales_column], color="red", label="Outlier", zorder=3)
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.legend()
        plt.title("Visualisasi Outlier dalam Tren Data")
        plt.xticks(rotation=45)
        plt.show()

        st.write('**Detect Anomaly📌**')
        st.pyplot(fig)

        # Jika tidak ada outlier
        if outliers.empty:
            st.success("✅ Tidak ada outlier yang signifikan.")
            outlier_fixed = True
        else:
            st.warning("⚠️ Terdapat outlier pada data.")
            st.write(outliers)
            outlier_fixed = False

            if st.button("Handle with Median", type="primary"):
                # Replace anomalies with the median sales value
                #median_sales = df["Total Sales"].median()
                #df.loc[df["is_anomaly"], "Total Sales"] = median_sales
                # Calculate median sales (used to replace anomalies)
                median_sales = df[sales_column].median()

                # Create a new column where anomalies are replaced with the median
                df["New Total Sales"] = df[sales_column].copy()  # Duplicate the column first
                df.loc[df["is_anomaly"], "New Total Sales"] = median_sales  # Replace anomalies only in the new column

                # Drop the Z-score column (not needed anymore)
                df.drop(columns=["z_score", "is_anomaly"], inplace=True)
                st.success("✅Anomaly sukses dihandle menggunakan median.")
                st.write(df)
                outlier_fixed = True
                
        st.subheader("🗓️Daily Delta")
        st.write('Perbedaan nilai harian, kolom pertama diganti dengan nilai 0. Daily Delta = Total Sales - Total Sales (hari sebelumnya)')

        if outliers.empty:
            df["daily_delta"] = df[sales_column].diff().fillna(0)
            st.write(df)
        # Jika ada outlier dan sudah di-handle, hitung dengan New Total Sales
        elif outlier_fixed:
            df["daily_delta"] = df["New Total Sales"].diff().fillna(0)
            st.write(df)
        else:
            st.warning("⚠️ Harap handle outlier terlebih dahulu untuk menghitung daily delta.")

            





