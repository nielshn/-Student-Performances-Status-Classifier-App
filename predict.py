import argparse
import pandas as pd
import joblib


def manual_input_to_df(args):
    # Buat dict dari input CLI untuk fitur utama
    input_dict = {
        "Application_mode": [args.application_mode],
        "Application_order": [args.application_order],
        "Course": [args.course],
        "Daytime_evening_attendance": [args.attendance],
        "Admission_grade": [args.admission_grade],
        "Mothers_qualification": [args.mother_edu],
        "Fathers_qualification": [args.father_edu],
        "Mothers_occupation": [args.mother_job],
        "Fathers_occupation": [args.father_job],
        "Scholarship_holder": [args.scholarship],
        "Gender": [args.gender],
        "Age_at_enrollment": [args.age],
        "Curricular_units_1st_sem_evaluations": [args.eval1],
        "Curricular_units_1st_sem_approved": [args.pass1],
        "Curricular_units_1st_sem_grade": [args.grade1],
        "Curricular_units_2nd_sem_evaluations": [args.eval2],
        "Curricular_units_2nd_sem_approved": [args.pass2],
        "Curricular_units_2nd_sem_grade": [args.grade2],
        "Unemployment_rate": [args.unemployment],
        "Inflation_rate": [args.inflation],
        "GDP": [args.gdp]
    }

    df = pd.DataFrame(input_dict)
    return df


def preprocess_and_predict(input_path=None, output_path=None, args=None):
    # Load model dan preprocessor
    preprocessor = joblib.load("./model/preprocessor.pkl")
    model = joblib.load("./model/randomforestmodel.pkl")

    if input_path:
        df = pd.read_csv(input_path)
    else:
        df = manual_input_to_df(args)

    X_transformed = preprocessor.transform(df)
    preds = model.predict(X_transformed)

    df['Prediction'] = preds
    status_map = {0: "Dropout", 1: "Graduate", 2: "Enrolled"}
    df['Prediction_Label'] = df['Prediction'].map(status_map)

    if output_path:
        df.to_csv(output_path, index=False)
        print(f"✅ Prediksi selesai. Hasil disimpan di {output_path}")
    else:
        print("✅ Hasil Prediksi:")
        print(df[['Prediction', 'Prediction_Label']])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Student Status Prediction")

    parser.add_argument("--input", help="Path ke file CSV input")
    parser.add_argument("--output", help="Path ke file hasil output")

    # Argumen manual untuk prediksi tunggal
    parser.add_argument("--application_mode", type=int)
    parser.add_argument("--application_order", type=int)
    parser.add_argument("--course", type=int)
    parser.add_argument("--attendance", type=int)
    parser.add_argument("--admission_grade", type=float)
    parser.add_argument("--mother_edu", type=int)
    parser.add_argument("--father_edu", type=int)
    parser.add_argument("--mother_job", type=int)
    parser.add_argument("--father_job", type=int)
    parser.add_argument("--scholarship", type=int)
    parser.add_argument("--gender", type=int)
    parser.add_argument("--age", type=int)
    parser.add_argument("--eval1", type=int)
    parser.add_argument("--pass1", type=int)
    parser.add_argument("--grade1", type=float)
    parser.add_argument("--eval2", type=int)
    parser.add_argument("--pass2", type=int)
    parser.add_argument("--grade2", type=float)
    parser.add_argument("--unemployment", type=float)
    parser.add_argument("--inflation", type=float)
    parser.add_argument("--gdp", type=float)

    args = parser.parse_args()

    if args.input:
        preprocess_and_predict(input_path=args.input, output_path=args.output)
    else:
        preprocess_and_predict(args=args)
