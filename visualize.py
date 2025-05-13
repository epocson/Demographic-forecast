import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.forecast import PopulationForecaster
import numpy as np
from pathlib import Path

# Set the style
sns.set_theme()
sns.set_palette("husl")

# Read the data
df = pd.read_csv('data/population_2015_2024.csv')

# Initialize and train forecaster
forecaster = PopulationForecaster('data/population_2015_2024.csv')
forecaster.load_data()
forecaster.train_model()
future_predictions = forecaster.forecast_future(years=6)  # 2025-2030

# Create figure with subplots (3 rows now)
fig = plt.figure(figsize=(12, 16))
gs = fig.add_gridspec(3, 1, height_ratios=[2, 2, 1])

# Population trend with forecasts
ax1 = fig.add_subplot(gs[0])
ax1.plot(df['year'], df['population'], marker='o', linewidth=2, label='Historical')
ax1.plot(future_predictions['year'], future_predictions['population'], 
         marker='s', linewidth=2, linestyle='--', label='Forecast')
ax1.set_title('Population Trend and Forecast (2015-2030)', fontsize=14)
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')
ax1.grid(True)
ax1.legend()

# Format y-axis to show millions
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1e6)}M'))

# Add value labels
for x, y in zip(df['year'], df['population']):
    ax1.annotate(f'{int(y/1e6)}M', 
                (x, y), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center')
for x, y in zip(future_predictions['year'], future_predictions['population']):
    ax1.annotate(f'{int(y/1e6)}M', 
                (x, y), 
                textcoords="offset points", 
                xytext=(0,-15), 
                ha='center',
                color='darkred')

# Demographic indicators
ax2 = fig.add_subplot(gs[1])
ax2.plot(df['year'], df['birth_rate'], marker='o', label='Birth Rate')
ax2.plot(df['year'], df['death_rate'], marker='s', label='Death Rate')
ax2.plot(df['year'], df['migration_rate'], marker='^', label='Migration Rate')
ax2.set_title('Demographic Indicators (2015-2024)', fontsize=14)
ax2.set_xlabel('Year')
ax2.set_ylabel('Rate')
ax2.legend()
ax2.grid(True)

# Create statistics table
ax3 = fig.add_subplot(gs[2])
ax3.axis('tight')
ax3.axis('off')

# Prepare table data
table_data = future_predictions[['year', 'population']].copy()
table_data['year_over_year_change'] = table_data['population'].pct_change() * 100
table_data['population_millions'] = table_data['population'] / 1_000_000

table_data = table_data.round({'population': 0, 'year_over_year_change': 2, 'population_millions': 2})
table_data.columns = ['Year', 'Population', 'Change (%)', 'Population (M)']

# Create table
table = ax3.table(cellText=table_data.values,
                  colLabels=table_data.columns,
                  cellLoc='center',
                  loc='center',
                  colColours=['#f2f2f2']*4)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)

# Add table title
ax3.set_title('Population Forecast Statistics (2025-2030)', pad=20, fontsize=14)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('population_analysis_with_forecast.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Create correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Demographic Indicators')
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

# Save forecast statistics to CSV
table_data.to_csv('forecast_statistics_2025_2030.csv', index=False) 