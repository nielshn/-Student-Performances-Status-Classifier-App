# app.py (redesain versi)
import streamlit as st
import pandas as pd
import joblib
import csv

# Load model dan preprocessor
preprocessor = joblib.load("model/preprocessor.pkl")
model = joblib.load("model/randomforest_model.pkl")
status_map = {0: "Dropout", 1: "Graduate", 2: "Enrolled"}

# Helper function: auto delimiter detection


def load_csv(file):
    try:
        return pd.read_csv(file, sep=";")
    except Exception:
        file.seek(0)
        try:
            return pd.read_csv(file, sep=",")
        except Exception as e:
            raise ValueError(
                "Gagal membaca CSV. Pastikan file menggunakan delimiter ';' atau ',' dan formatnya benar.")


# UI setup
st.set_page_config(page_title="🎓 Student Status Classifier", layout="wide")
st.title("🎓 Student Status Classifier App")
st.markdown("Prototype untuk klasifikasi status mahasiswa: **Dropout**, **Graduate**, atau **Enrolled** berdasarkan data akademik.")

uploaded_file = st.file_uploader(
    "📁 Upload file CSV data mahasiswa", type=["csv"])

if uploaded_file is not None:
    df = load_csv(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📄 Preview Data")
        st.dataframe(df.head(), use_container_width=True)

    with col2:
        st.subheader("📊 Info Dataset")
        st.write(f"- Jumlah baris: `{df.shape[0]}`")
        st.write(f"- Jumlah fitur: `{df.shape[1]}`")
        st.write(f"- Kolom: `{', '.join(df.columns[:5])}...`")

    st.markdown("---")
    if st.button("🔍 Jalankan Prediksi"):
        try:
            X_transformed = preprocessor.transform(df)
            preds = model.predict(X_transformed)
            df["Prediction"] = preds
            df["Prediction_Label"] = df["Prediction"].map(status_map)

            st.subheader("✅ Hasil Prediksi")
            pred_counts = df["Prediction_Label"].value_counts()
            st.write("Distribusi Prediksi:")
            st.bar_chart(pred_counts)

            styled_df = df[["Prediction", "Prediction_Label"]].copy()
            styled_df["Prediction_Label"] = styled_df["Prediction_Label"].apply(
                lambda x: f"🟥 Dropout" if x == "Dropout" else (
                    f"🟩 Graduate" if x == "Graduate" else "🟦 Enrolled")
            )

            st.dataframe(styled_df, use_container_width=True)

            # Download result
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="💾 Download Hasil Prediksi",
                data=csv,
                file_name="hasil_prediksi.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"❌ Gagal memproses data: {e}")
else:
    st.info("Silakan unggah file CSV untuk memulai prediksi.")
