
data <- read.csv("rentals.csv")

data <- data[(data$rentPeriodId=="MON") & data$latitude> -28 & data$latitude < -27 & data$longitude > -49 
             & data$longitude < -48 & data$bathrooms > 0 & data$rooms > 0 & data$rentPrice < 4000 & 
               !is.na(data$area),  ]

train_indexes <- runif(nrow(data)) < 0.7

train_data <- data[train_indexes,]
l <- lm(data = train_data, formula = rentPrice ~  rooms + bathrooms + latitude + longitude + garages + area)

test_data <- data[!train_indexes,]

test_data <- data[!train_indexes,]
predicted <- predict(l, test_data)

source('visualization.R')









