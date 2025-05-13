# Population Forecasting

This project analyzes historical population data from 2015 to 2024 and forecasts population trends for 2025-2030 using statistical modeling.

You can freely edit this code to extend the features and use other data to forecast.

## Project Structure

```
population_forecasting/
├── data/
│   └── population_2015_2024.csv  # Historical population data
├── model/
│   └── catboost_model.cbm        # Trained forecasting model
├── notebooks/
│   └── analysis.ipynb            # Jupyter notebook for data analysis
├── src/
│   └── forecast.py               # Main forecasting algorithm
├── simple_forecast.py            # Simple visualization script
├── text_forecast.py              # Text-based forecast output
└── requirements.txt              # Required Python packages
```

## Features

- Historical population data analysis from 2015-2024
- Linear trend forecasting for 2025-2030
- Data visualization with population trends
- Demographic indicator analysis (birth rate, death rate, migration)
- Table visualization of forecast statistics

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- catboost (for advanced modeling)
- scikit-learn

## Usage

For a simple text-based forecast:

```bash
python text_forecast.py
```

For visualization with charts and tables:

```bash
python simple_forecast.py
```

## Sample Output

```
Population Forecast (2025-2030):
============================================================
Year      Population          Change (%)     Population (M)
------------------------------------------------------------
2025      146,279,091          0.16%          146.28M
2026      146,237,164          -0.03%          146.24M
2027      146,195,237          -0.03%          146.20M
2028      146,153,309          -0.03%          146.15M
2029      146,111,382          -0.03%          146.11M
2030      146,069,455          -0.03%          146.07M
============================================================
``` 
