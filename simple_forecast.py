import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Load the data
data = pd.read_csv('data/population_2015_2024.csv')
print("Data loaded successfully!")
print(f"Years in data: {data['year'].min()} to {data['year'].max()}")

# Simple linear regression for forecasting
def forecast_population(data, forecast_years=6):
    # Linear regression on population
    years = data['year'].values
    population = data['population'].values
    
    # Calculate the trend using polyfit
    trend = np.polyfit(years, population, 1)
    print(f"Population trend: {trend[0]:,.0f} people per year")
    
    # Generate future years
    future_years = np.arange(data['year'].max() + 1, data['year'].max() + forecast_years + 1)
    
    # Predict future population
    future_population = np.polyval(trend, future_years)
    
    # Create a DataFrame with the results
    forecast_df = pd.DataFrame({
        'year': future_years,
        'population': future_population,
        'year_over_year_change': 0.0,
        'population_millions': future_population / 1_000_000
    })
    
    # Calculate year-over-year change
    last_historical_pop = data['population'].iloc[-1]
    for i, row in forecast_df.iterrows():
        if i == 0:
            forecast_df.loc[i, 'year_over_year_change'] = (row['population'] - last_historical_pop) / last_historical_pop * 100
        else:
            forecast_df.loc[i, 'year_over_year_change'] = (row['population'] - forecast_df.loc[i-1, 'population']) / forecast_df.loc[i-1, 'population'] * 100
    
    return forecast_df

# Generate forecast
print("\nGenerating forecast for 2025-2030...")
forecast = forecast_population(data)

# Round the values for display
forecast = forecast.round({'population': 0, 'year_over_year_change': 2, 'population_millions': 2})

# Display the forecast
print("\nPopulation Forecast (2025-2030):")
print(forecast[['year', 'population', 'year_over_year_change', 'population_millions']].to_string(index=False))

# Save forecast to CSV
forecast.to_csv('forecast_statistics_2025_2030.csv', index=False)
print("\nForecast statistics saved to forecast_statistics_2025_2030.csv")

# Create a simple visualization
plt.figure(figsize=(12, 8))

# Create subplot for population trend
plt.subplot(2, 1, 1)
plt.plot(data['year'], data['population'], 'o-', label='Historical')
plt.plot(forecast['year'], forecast['population'], 's--', label='Forecast')
plt.title('Population Trend and Forecast (2015-2030)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.legend()

# Format y-axis to show millions
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1e6)}M'))

# Create subplot for table
plt.subplot(2, 1, 2)
plt.axis('off')
table_data = forecast.copy()
table_data.columns = ['Year', 'Population', 'Change (%)', 'Population (M)']
table = plt.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    loc='center',
    cellLoc='center',
    colColours=['#f2f2f2']*4
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)
plt.title('Population Forecast Statistics (2025-2030)', pad=20)

plt.tight_layout()
plt.savefig('simple_forecast.png', dpi=300, bbox_inches='tight')
print("Visualization saved to simple_forecast.png")

try:
    plt.show()
except Exception as e:
    print(f"Could not display plot: {e}")
    print("But the plot was saved successfully to simple_forecast.png") 