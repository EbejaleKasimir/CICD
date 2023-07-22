from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:P%4055w076@localhost:5432/cohort_4_')
engine.connect()

import pandas as pd

data = [
    {"Country": "USA", "Population": 328200000, "GDP": 21439400, "Unemployment": 3.8},
    {"Country": "China", "Population": 1393000000, "GDP": 14342920, "Unemployment": 3.6},
    {"Country": "Japan", "Population": 126500000, "GDP": 5082465, "Unemployment": 2.4},
    {"Country": "Germany", "Population": 82790000, "GDP": 3845481, "Unemployment": 3.4},
    {"Country": "India", "Population": 1354000000, "GDP": 2956756, "Unemployment": 6.1},
    {"Country": "France", "Population": 66990000, "GDP": 2930535, "Unemployment": 8.0},
    {"Country": "United Kingdom", "Population": 66440000, "GDP": 2825208, "Unemployment": 4.1},
    {"Country": "Italy", "Population": 60480000, "GDP": 2086911, "Unemployment": 9.9},
    {"Country": "Brazil", "Population": 209300000, "GDP": 1868626, "Unemployment": 11.6},
    {"Country": "Canada", "Population": 37590000, "GDP": 1673625, "Unemployment": 5.6},
    {"Country": "South Korea", "Population": 51310000, "GDP": 1660119, "Unemployment": 3.9},
    {"Country": "Australia", "Population": 25200000, "GDP": 1403313, "Unemployment": 5.2},
    {"Country": "Russia", "Population": 144500000, "GDP": 1402081, "Unemployment": 4.8},
    {"Country": "Spain", "Population": 46560000, "GDP": 1394215, "Unemployment": 14.1},
    {"Country": "Mexico", "Population": 126200000, "GDP": 1212294, "Unemployment": 3.3},
    {"Country": "Indonesia", "Population": 267700000, "GDP": 1075216, "Unemployment": 5.3},
    {"Country": "Netherlands", "Population": 17430000, "GDP": 909887, "Unemployment": 3.6},
    {"Country": "Saudi Arabia", "Population": 33699947, "GDP": 793697, "Unemployment": 12.9},
    {"Country": "Turkey", "Population": 82003882, "GDP": 754605, "Unemployment": 11.1},
    {"Country": "Switzerland", "Population": 8541000, "GDP": 703080, "Unemployment": 2.6},
    {"Country": "Nigeria", "Population": 214000000, "GDP": 448120, "Unemployment": 23.1},
]


df = pd.DataFrame(data)

My_Name = "Ebejale Kasimir Ikuenobe"
max_pop_country = df[df['Population'] == df['Population'].max()]['Country'].values[0]
print(f'My name is {My_Name}, and here are my answers:\n\t 1. Country with the highest population: {max_pop_country}.')

avg_gdp = round(df['GDP'].mean(),3)
print(f'\t 2. Average GDP across all countries: {avg_gdp}.')

min_unemployment_country = df[df['Unemployment'] == df['Unemployment'].min()]['Country'].values[0]
print(f'\t 3. Country with the lowest unemployment rate: {min_unemployment_country}.')

top_5_gdp_countries_population = df.nlargest(5, 'GDP')['Population'].sum()
print(f'\t 4. Total population of the top 5 countries by GDP: {top_5_gdp_countries_population}.')

countries_above_5_trillion = df[df['GDP'] > 5000000].shape[0]
print(f'\t 5. There are {countries_above_5_trillion} countries with a GDP higher than 5 trillion.')

df['GDP_per_capita'] = df['GDP'] / df['Population']
min_gdp_per_capita_country = df[df['GDP_per_capita'] == df['GDP_per_capita'].min()]['Country'].values[0]
print(f'\t 6. The country with the lowest GDP per capita: {min_gdp_per_capita_country}.')

# Convert to DataFrame and save to SQL
df.to_sql('world_data', engine, if_exists='replace')

query_check_table = 'SELECT * FROM world_data'
df_from_sql = pd.read_sql(query_check_table, engine)
print(df_from_sql)

# SQL queries
query_max_pop = 'SELECT "Country" FROM world_data ORDER BY "Population" DESC LIMIT 1'
query_avg_gdp = 'SELECT AVG("GDP") average FROM world_data'
query_min_unemployment = 'SELECT * FROM world_data ORDER BY "Unemployment" LIMIT 1'
query_top5_gdp_pop = 'SELECT SUM("Population") summation FROM world_data WHERE "Population" IN (SELECT "Population" FROM world_data ORDER BY "GDP" DESC LIMIT 5)'
query_countries_above_5_trillion = 'SELECT COUNT(*) FROM world_data WHERE "GDP" > 5000000'
query_min_gdp_per_capita = 'SELECT "Country" FROM world_data ORDER BY CAST("GDP" AS FLOAT) / CAST("Population" AS FLOAT) ASC LIMIT 1'

# Execute queries and print results
My_Name = "Ebejale Kasimir Ikuenobe"
print(f'My name is {My_Name}, and here are my answers:')
print(f'\t 1. Country with the highest population: {pd.read_sql(query_max_pop, engine)["Country"].values[0]}.')
print(f'\t 2. Average GDP across all countries: {round(pd.read_sql(query_avg_gdp, engine)["average"].values[0],3)}.')
print(f'\t 3. Country with the lowest unemployment rate: {pd.read_sql(query_min_unemployment, engine)["Country"].values[0]}.')
print(f'\t 4. Total population of the top 5 countries by GDP: {pd.read_sql(query_top5_gdp_pop, engine)["summation"].values[0]}.')
print(f'\t 5. There are {pd.read_sql(query_countries_above_5_trillion, engine).values[0][0]} countries with a GDP higher than 5 trillion.')
print(f'\t 6. The country with the lowest GDP per capita: {pd.read_sql(query_min_gdp_per_capita, engine)["Country"].values[0]}.')