from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load enthalpy data based on the refrigerant choice
refrigerant_data = {
    "R717": pd.read_excel('enthalpy_data.xlsx'),
    "R134a": pd.read_excel('enthalpy_data2.xlsx')   
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    refrigerant = request.form['refrigerant']
    enthalpy_data = refrigerant_data.get(refrigerant)

    if enthalpy_data is None or enthalpy_data.empty:
        return render_template('error.html', message="Invalid refrigerant choice.")
  
    T1 = float(request.form['T1'])
    T2 = float(request.form['T2'])
    T3 = float(request.form['T3'])
    T4 = float(request.form['T4'])

    # # Interpolate enthalpy values for specified temperatures
    # h1 = enthalpy_data.interpolate().at[T1, "Enthalpy_Vapour"]
    # h2 = enthalpy_data.interpolate().at[T2, "Enthalpy_Liquid"]
    # h3 = enthalpy_data.interpolate().at[T3, "Enthalpy_Vapour"]
    # h4 = h2 #enthalpy_data.interpolate().at[T4, "Enthalpy_Liquid"]

    h1 = enthalpy_data.loc[enthalpy_data["Temp"] == T1, "Enthalpy_Vapour"].values
    h2 = enthalpy_data.loc[enthalpy_data["Temp"] == T2, "Enthalpy_Liquid"].values
    h3 = enthalpy_data.loc[enthalpy_data["Temp"] == T3, "Enthalpy_Vapour"].values
    h4 = h2  # enthalpy_data.loc[enthalpy_data["Temp"] == T4, "Enthalpy_Liquid"].values

    # Check if data is available for the chosen temperature values
    if h1.size == 0 or h2.size == 0 or h3.size == 0 or h4.size == 0:
        return render_template('error.html', message="Invalid temperature values.")
    
    # Extract scalar values from the numpy arrays
    h1, h2, h3, h4 = h1[0], h2[0], h3[0], h4[0]

    Q = round((h3 - h4), 3)
    W = round((h1 - h3), 3)
    cop = round((Q / W), 3)
    ideal_cop = round(((T3 + 273.15) / (T2 - T3)), 3)

    return render_template('result.html', refrigerant=refrigerant, T1=T1, T2=T2, T3=T3, T4=T4, 
    h1=h1, h2=h2,h3=h3,h4=h4, Q=Q, W=W, cop=cop, ideal_cop=ideal_cop)

if __name__ == '__main__':
    app.run(debug=True)
