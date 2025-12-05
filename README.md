# 🚗⚡ Washington Statewide EV Forecast Tool  
### Part of the *Tesla EV Growth Strategy · Washington EV Hub*

This repository contains the **Statewide Forecast Tool (`ev_render_app`)**, which powers EV forecast modeling for Washington state—integrated into the overall site architecture shown below.

---

## 🧩 Site Flow & Architecture Overview

```
                         +----------------------+
                         |       Home Hub       |
                         +----------+-----------+
                                    |
            +-----------------------+-----------------------+
            |                                               |
    +-------v-----------------------+       +---------------v----------------------+
    |     Statewide Forecast Tool   |       |     County-Level Forecast Tool      |
    |         (ev_render_app)       |       |         (ev_forecast_app)           |
    +---------------+---------------+       +------------------+-------------------+
                    |                                          |
                    +----------------------+-------------------+
                                           |
                                 +---------v----------+
                                 |     Forecast       |
                                 |      Results       |
                                 | (EV Registrations  |
                                 |    & Adoption)     |
                                 +--------------------+
```

---

## 🌐 Access the Full EV Growth Strategy Hub  
👉 **Tesla EV Growth Strategy · Washington EV Hub**  
https://home-page-ev.onrender.com/

---

## 🔥 Why This Tool Is Useful

Washington’s EV ecosystem is expanding rapidly—but not uniformly. This tool helps identify **where charger investment generates the largest EV adoption gains**, revealing:

- High-population counties with insufficient charging  
- Areas at risk of **charging anxiety**  
- Infrastructure imbalance caused by corridor-first planning  
- How EV registrations change per additional charger  
- County-level adoption shifts as infrastructure grows  
- Whether counties meet 2030–2050 climate mandates  
- Charger deployment ROI comparisons  
- Budget allocation guidance based on density & impact  

This transforms raw data into actionable statewide strategy.

---

## 🛠 How the Model Was Developed

The forecasting engine blends **EV registrations**, **population**, **charger counts**, and **state policy goals** using:

1. Demographic + registration review  
2. Infrastructure inventory  
3. County density classification  
4. Monte Carlo simulations  
5. Regression & logistic curve fitting  
6. Flask integration for interactive forecasting  

---

## 📁 Repository Structure

```
ev_render_app/
│
├── app.py                       # Main Flask backend
├── templates/
│     ├── index.html             # Input page
│     └── results.html           # Forecast results page
│
├── static/
│     ├── map.png                # Statewide EV / charger geographic visualization
│     └── chart.png              # Forecast curve visualization (EVs vs SC)
│
├── supercharger_by_county_summary.xlsx   # Required input file
│
└── README.md
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/<yourname>/ev_render_app.git
cd ev_render_app
pip install -r requirements.txt
flask run
```

Local app runs at:  
**http://127.0.0.1:5000**

---

## 🚀 Deploy to Render

**Build Command**
```
pip install -r requirements.txt
```

**Start Command**
```
gunicorn app:app
```

---
