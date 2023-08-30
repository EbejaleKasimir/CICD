    SELECT SUM("Confirmed") AS Total_Confirmed, 
           SUM("Deaths") AS Total_Deaths, 
           SUM("Recovered") AS Total_Recoveries
    FROM covid_19_data;
    
    -- There are four 4 quarters in a year. To capture the first quarter, we would have to look at the first three months.
    SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
           SUM("Confirmed") AS Total_Confirmed, 
           SUM("Deaths") AS Total_Deaths, 
           SUM("Recovered") AS Total_Recoveries
    FROM covid_19_data
    WHERE EXTRACT(MONTH FROM "ObservationDate") BETWEEN 1 AND 3
    GROUP BY Year;
    
    -- Comprehensive summary for each country captured in the table available in covid_19_data.csv file.
    SELECT "Country", 
           SUM("Confirmed") AS Total_Confirmed, 
           SUM("Deaths") AS Total_Deaths, 
           SUM("Recovered") AS Total_Recoveries
    FROM covid_19_data
    GROUP BY "Country";
    
-- Percentage death increase from the year 2019 and 2020
    WITH "Deaths" AS (
      SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
             SUM("Deaths") AS Total_Deaths
      FROM covid_19_data
      GROUP BY Year
    )

    SELECT (d2.Total_Deaths - d1.Total_Deaths) / d1.Total_Deaths * 100 AS Percentage_Increase
    FROM "Deaths" d1, "Deaths" d2
    WHERE d1.Year = 2019 AND d2.Year = 2020;
    

-- Top Five 5 countries with the highest confirmed cases    
    SELECT "Country", SUM("Confirmed") AS Total_Confirmed
    FROM covid_19_data
    GROUP BY "Country"
    ORDER BY Total_Confirmed DESC
    LIMIT 5;
    
-- Net Change in confirmed cases per month over two-year period
    SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
           EXTRACT(MONTH FROM "ObservationDate") AS Month, 
           SUM("Confirmed") - LAG(SUM("Confirmed")) OVER (ORDER BY EXTRACT(YEAR FROM "ObservationDate"), EXTRACT(MONTH FROM "ObservationDate")) AS Net_Change
    FROM covid_19_data
    GROUP BY Year, Month;
