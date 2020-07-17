# COVID19-models
Linear regression models are studied for maximum mortality and confirmed cases rates normalized on total population in considered county, rate_max=max(cases_per_day/population), 
as outcome and incoming feature is population density in the area, rate(population_density). Maximum rate is maximum slope of number of cases growth. Both outcomes have some 
disadvantages in how they are defined. In both cases model shows similar result. The model is done for China provinces where process was almost complete. 
Only Hubei was excluded that was outlier which showed couple orders of magnitude difference. This shows that conditions were really different there. In the model with mortality 
rate, few provinces which showed zero rate, were excluded, for most of them, excluding Tibet, zero was unexpected. The regression slope can vary if we consider model for 
the other countries. To do normalization over all population is necessary in such model, despite of assumption that everything is distributed homogeneously in given area. 
The absolute number of cases may not have much sense if areas with different population are compared. 

libraries: requests, BeautifulSoup, seaborn, matplotlib, scikitlearn, pandas, numpy

Author: Inga Kuznetsova

Files: virus_model.ipynb, get_data_bs.py, plot_states_cases.py, time_series_covid_19_confirmed.csv, time_series_covid_19_deaths.csv
