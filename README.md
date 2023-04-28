# Electricity-Price-Predication-Web Application

Suppose that your business relies on computing services where the power consumed by your machines varies throughout the day. You do not know the actual cost of the electricity consumed by the machines throughout the day, but the organization has provided you with historical data of the price of the electricity consumed by the machines.

A streamlit application is availed to do this for you. This application is trained to predict your electricity prices with high accuracy having been trained on a dataset with just over 38000 entries, hence accuracy is assured in our model.

The user is to feed the model with the following input:

1. Day: Monday, Tuesday, Wednesday,..., Sunday.
2. Month: January, February, March, April,..., December.
3. Wind Forecast: forecasted wind production.
4. System load forecast: forecasted national load.
5. Price forecast
6. Actual temperature 
7. Wind measured: wind speed measured
8. Co2 Intensity: ctual C02 intensity for the electricity produced
9. Actual wind: actual wind energy production
10. System load: actual national system load

A random forest regressor is trained to predict electricity price based on the mentioned inputs.

![image](https://user-images.githubusercontent.com/89415200/235266499-b5ed6a2d-a94b-4775-9e80-7641dee80543.png)
![image](https://user-images.githubusercontent.com/89415200/235266562-f1435386-2a2e-47bb-b022-0fad76fc0ddd.png)
