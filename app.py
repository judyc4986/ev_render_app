from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# =========================================================
# Load statewide supercharger count
# =========================================================
def load_statewide_supercharger_count():
    excel_path = "supercharger_by_county_summary.xlsx"  # Must be in project root

    if not os.path.exists(excel_path):
        print("⚠ Missing supercharger_by_county_summary.xlsx")
        return None

    try:
        df = pd.read_excel(excel_path)

        # Normalize column names
        df.columns = [str(c).strip().lower() for c in df.columns]

        # County column
        if "county" not in df.columns:
            print("⚠ 'County' column missing")
            return None

        # Find the row where County == "Total"
        row = df[df["county"].str.lower() == "total"]

        if row.empty:
            print("⚠ No 'Total' row found")
            return None

        # Try to find the supercharger count column
        sc_col = None
        for name in df.columns:
            if "super" in name or "charger" in name:
                sc_col = name
                break

        if not sc_col:
            print("⚠ No supercharger count column found")
            return None

        return int(row[sc_col].iloc[0])

    except Exception as e:
        print("⚠ Error loading statewide count:", e)
        return None


STATEWIDE_SC = load_statewide_supercharger_count()


# =========================================================
# Statewide forecast model
# =========================================================
def statewide_forecast(x):
    ev_reg = (
        0.0026120043 * (x ** 3)
        - 4.7343743373 * (x ** 2)
        + 4547.3532407731 * x
        - 140511.0057756579
    )

    adopt = (
        0.0000000007 * (x ** 3)
        - 0.0000012533 * (x ** 2)
        + 0.0012038019 * x
        - 0.0371968938
    )

    return ev_reg, adopt


# =========================================================
# UI Route
# =========================================================
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            x_raw = request.form.get("superchargers", "").strip()
            x = float(x_raw)

            ev_reg, adopt = statewide_forecast(x)

            result = {
                "x": x,
                "ev_reg_str": f"{ev_reg:,.0f}",
                "adopt_pct_str": f"{adopt * 100:.2f}",
            }
        except ValueError:
            error = "Please enter a valid numeric value."

    return render_template(
        "index.html",
        result=result,
        error=error,
        statewide_sc=STATEWIDE_SC,
    )


if __name__ == "__main__":
    app.run(debug=True)
