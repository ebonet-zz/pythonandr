# Load libraries
import pandas as pd, numpy as np, statsmodels.formula.api as sm

# Read data
data = pd.read_csv("rentals.csv")

# Clean data
data =data[(data.rentPeriodId=="MON") & (data.latitude.between(-28, -27)) & (data.longitude.between(-49, -48))
           & (data.bathrooms > 0) & (data.rooms > 0) & (data.rentPrice <4000) ]

data = data[[u'propertyId', u'rentPrice', u'latitude', u'longitude',u'garages',u'rooms', u'bathrooms']]
data.describe()

# Explore using pandas
# BoxPlot: train_data.rentPrice.plot('box')
# Histogram: train_data.rentPrice.plot('histogram')

# Split data
np.random.seed(42)
rds = np.random.random(len(data))
train_data, test_data = data[rds < 0.7], data[rds >= 0.7]

# Simple prediction
result = sm.ols(formula="rentPrice ~ rooms + bathrooms + latitude + longitude+garages", data = train_data).fit()
result.summary()

# Plot results

from visualization import plot_results, plot_scater_map

plot_scater_map(train_data)
plot_results(test_data.rentPrice, result.predict(test_data))