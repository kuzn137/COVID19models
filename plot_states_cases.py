# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:27:46 2020

@author: kuzn137
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class plot_ratio_state(object):
      def __init__(self, cut_off_pos):
          self.cut_off_pos =cut_off_pos
          self.state=None
      def read_data(self, state):
          """
          input: state is state name written as in link
          read table with Date and deaths number from .csv file starting from number of death >0 for given state
          return: Init Date is initial date and data is vector with death numbers starting from this date
          """
          self.state=state
          df=pd.read_csv('states_covid_cases.csv')
          df=df.loc[(df['state']==self.state) & (df['Positive']>self.cut_off_pos)][::-1][:-2]
          data_deaths= df[['Deaths']].to_numpy().reshape(1, len(df))[0]
          data_positive= df[['Positive']].to_numpy().reshape(1, len(df))[0]
          data_negative= df[['Negative']].to_numpy().reshape(1, len(df))[0]
          ratio_positive_to_negative=np.divide(data_positive, data_negative) 
          InitDate = df[['Date']].to_numpy()[0][0]
          return InitDate, data_deaths, data_positive, data_negative, ratio_positive_to_negative
      def plot_ratio(self, state):
          self.state=state
          InitDate, data_deaths, data_positive, data_negative, ratio_positive_to_negative = self.read_data(self.state)
          plt.figure()
          sns.boxplot().set_title(self.state)
          sns.scatterplot(range(1, len(ratio_positive_to_negative)+1), ratio_positive_to_negative)   

      def plot_ratio_all(self):
          states=[('Alabama', 'AL'), ('Alaska', 'AK'), ('Arizona', 'AZ'), ('Arkansas', 'AR'), ('California', 'CA'), ('Colorado', 'CO'), ('Connecticut', 'CT'), ('Delaware', 'DE'), ('Florida', 'FL'), 
('Georgia', 'GA'), ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Iowa', 'IA'), ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Maine', 'ME'), 
('Maryland', 'MD'), ('Massachusetts', 'MA'), ('Michigan', 'MI'), ('Minnesota', 'MN'), ('Mississippi', 'MS'), ('Missouri', 'MO'), ('Montana', 'MT'), ('Nebraska', 'NE'), ('Nevada', 'NV'),
('New-Hampshire', 'NH'), ('New-Jersey', 'NJ'), ('New-Mexico', 'NM'), ('New-York', 'NY'), ('North-Carolina', 'NC'), ('North-Dakota', 'ND'), ('Ohio', 'OH'),
('Oklahoma','OK'), ('Oregon', 'OR'), ('Pennsylvania', 'PA'), ('Rhode-Island', 'RI'), ('South-Carolina', 'SC'), ('South-Dakota', 'SD'), ('Tennessee', 'TN'), ('Texas', 'TX'), ('Utah', 'UT'),
('Vermont','VT'), ('Virginia', 'VA'), ('Washington', 'WA'), ('West-Virginia', 'WV'), ('Wisconsin', 'WI'), ('Wyoming', 'WY')] 
          for i in states:
              self.state=i[0].lower()
              self.plot_ratio(self.state)
    
    
plot_ratio_state(10).plot_ratio_all()
