# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:41:36 2020

@author: kuzn137
"""
import requests
import pandas as pd
from datetime import datetime
import seaborn as sns
from bs4 import BeautifulSoup as bs
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"
def get_soup(url):
    """Constructs and returns a soup using the HTML content of `url` passed"""
    # initialize a session
    session = requests.Session()
    # set the User-Agent as a regular browser
    session.headers['User-Agent'] = USER_AGENT
    # request for english content (optional)
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    # make the request
    html = session.get(url)
    # return the soup
    return bs(html.content, "html.parser")
def get_all_tables(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("table")
def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers
def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows
def save_as_csv(table_name, headers, rows):
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")
def main(url, state):
    # get the soup
    soup = get_soup(url)
    # extract all the tables from the web page
    tables = get_all_tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    # iterate over all tables
    for i, table in enumerate(tables, start=0):
        # get the table headers
        headers = get_table_headers(table)
        # get all the rows of the table
        rows = get_table_rows(table)
        # save table as csv file
        table_name = state
        print(f"[+] Saving {table_name}")
        save_as_csv(table_name, headers, rows)
   
stab=[('Alabama', 'AL'), ('Alaska', 'AK'), ('Arizona', 'AZ'), ('Arkansas', 'AR'), ('California', 'CA'), ('Colorado', 'CO'), ('Connecticut', 'CT'), ('Delaware', 'DE'), ('Florida', 'FL'), 
('Georgia', 'GA'), ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Iowa', 'IA'), ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Maine', 'ME'), 
('Maryland', 'MD'), ('Massachusetts', 'MA'), ('Michigan', 'MI'), ('Minnesota', 'MN'), ('Mississippi', 'MS'), ('Missouri', 'MO'), ('Montana', 'MT'), ('Nebraska', 'NE'), ('Nevada', 'NV'),
('New-Hampshire', 'NH'), ('New-Jersey', 'NJ'), ('New-Mexico', 'NM'), ('New-York', 'NY'), ('North-Carolina', 'NC'), ('North-Dakota', 'ND'), ('Ohio', 'OH'),
('Oklahoma','OK'), ('Oregon', 'OR'), ('Pennsylvania', 'PA'), ('Rhode-Island', 'RI'), ('South-Carolina', 'SC'), ('South-Dakota', 'SD'), ('Tennessee', 'TN'), ('Texas', 'TX'), ('Utah', 'UT'),
('Vermont','VT'), ('Virginia', 'VA'), ('Washington', 'WA'), ('West-Virginia', 'WV'), ('Wisconsin', 'WI'), ('Wyoming', 'WY')] 
#connection does not allow to read all at the same time
#for j in range(0, 4):
states=[i[0].lower() for i in stab]#['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'florida', 'connecticut', 'new-york', 'oregon']
df=pd.DataFrame()
for i in states:
    url='https://covidtracking.com/data/state/'+i+'/#history'
    main(url, i) 
    dfs=pd.read_csv(i +'.csv', thousands=',')
    dfs = dfs[['Date', 'Positive', 'Negative', 'Total test resultsPositive + Negative', 'Deaths']]
    dfs['state'] = i
    dfs=dfs.fillna(0)
    dfs.to_csv(i+'.csv', index=False)
    df=df.append(dfs, ignore_index=True)
#df=df.dropna()
#df=pd.read_csv('new-york.csv', thousands=',')
print(df.columns)
df=df.drop([0])
df = df[['state', 'Date', 'Positive', 'Negative', 'Total test resultsPositive + Negative', 'Deaths']]
df=df.fillna(0)
print(df)
print(df['Positive'].astype(str))
print (df[['state', 'Positive', 'Negative']])
#sns.scatterplot(df['day'].astype(int), df['ratio_positive_to_negative'])
df.to_csv('states_covid_cases.csv', index=False)
