# Load libraries
import matplotlib, matplotlib.pyplot as plt, pandas as pd, numpy as np, statsmodels.formula.api as sm

matplotlib.style.use('ggplot')

# Read data
data = pd.read_csv("rentals.csv")

# -- Simple statistics
data.rentPrice.describe()

(data.iptu / data.area).describe() # Iptu por tamanho do imovel

# Clean data
data =data[(data.rentPeriodId=="MON") & (data.latitude.between(-28, -27)) & (data.longitude.between(-49, -48)) & (data.bathrooms > 0) & (data.rooms > 0) & (data.rentPrice <4000) ]

data = data[[u'propertyId', u'rentPrice', u'latitude', u'longitude',u'garages',u'rooms', u'bathrooms']]
data.describe()

# Split data
np.random.seed(42)
rds = np.random.random(len(data))
train_data, test_data = data[rds < 0.7], data[rds >= 0.7]


# Simple prediction
result = sm.ols(formula="rentPrice ~ rooms + bathrooms", data = train_data).fit()
result.summary()

result = sm.ols(formula="rentPrice ~ rooms + bathrooms + latitude + longitude+garages", data = train_data).fit()
result.summary()

# Plot results
# pd.DataFrame({'pred': result.predict(train_data), 'actual': train_data.rentPrice}).plot(x='actual', y='pred', style='o')