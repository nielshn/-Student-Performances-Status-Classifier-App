# predict.py
import argparse
import pandas as pd
import joblib


def preprocess_and_predict(input_path, output_path):
    # Load model dan preprocessor
    preprocessor = joblib.load("./model/preprocessor.pkl")
    model = joblib.load("./model/xgboost_model.pkl")

    # Load data
    df = pd.read_csv(input_path)

    # Preprocessing
    X_transformed = preprocessor.transform(df)

    # Prediksi
    preds = model.predict(X_transformed)
    df['Prediction'] = preds

    # Simpan hasil
    df.to_csv(output_path, index=False)
    print(f"✅ Prediksi selesai. Hasil disimpan di {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Student Status Prediction")
    parser.add_argument("--input", required=True,
                        help="Path ke file CSV input")
    parser.add_argument("--output", required=True,
                        help="Path ke file hasil output")
    args = parser.parse_args()

    preprocess_and_predict(args.input, args.output)
