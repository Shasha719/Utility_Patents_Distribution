# patent_dev

## Summary

This project intends to demonstrate the utility patents distribution in the world, as well as in the United States. I will also conduct an analysis of the utility patents particularly in New York State, Taiwan, both quantitatively and qualitatively.  This analysis is largely exploratory for the general public, however, it might also have certain implications for companies and individuals who are interested in applying for utility patents, analysis generated from this project may help them to decide where to submit its applications with the consideration of competitiveness. 

## Input data

There are two input files.

They can be obtained through below API endpoint:
https://uspto.data.commerce.gov/resource/5yb9-mbg7.json
https://uspto.data.commerce.gov/resource/jwx5-kdx6.json
https://uspto.data.commerce.gov/dataset/U-S-_filers_2014/apaj-dzmw

**U.S._filers_2014**

**Stc2015_5yr.csv**, prepared from the U.S. Patent and Trademark Office (USPTO), Technology Assessment and Forecast (TAF) database, displays a listing of geographic regions from which utility patents (i.e., patents for invention) originated during the indicated 5 year time period and a corresponding count of patents for each of the years of the period. Each displayed annual count corresponds to the count of patents received in a calendar year (January 1 to December 31).

**Assignees2014_5yr.csv**, prepared from the U.S. Patent and Trademark Office (USPTO), Technology Assessment and Forecast (TAF) database, displays a listing of organizations receiving the most utility patents (i.e., patents for invention) during the indicated 5 year time period. Each displayed annual count corresponds to the count of patents received in a calendar year (January 1 to December 31). This file generally contains the contents of the PTMT report, DRILL-DOWN Utility Patent Report, Patenting by Geographic Origin (State and Country) - Breakout By Organization. 


## Deliverables

There are eight deliverables: four scripts, **patents.py**, **ny_patents.py**, **Taiwan_patents.py** and **indiv_patents.py**; six figures, **top_ten_patents.png**, **top_ten.png**, **ny_patents.png**, **Taiwan_patents.png**, **top_ten_indiv_patents.png**, **top_foreign_indivi_patents.png**.

The scripts should be run in the order mentioned below: B-E

## Instructions

### A. Downloading files from USPTO government website

Using below API endpoints, or download csv files directly:
https://uspto.data.commerce.gov/resource/5yb9-mbg7.json
https://uspto.data.commerce.gov/resource/jwx5-kdx6.json

### B. Script patents.py

1. Read the "stc2015_5yr.csv" file to access the patents data from 2010-2014.
2. Sort out the foreign and US utility patents in different ways to get a better sense of the geographic distribution. As well as, US patents percentage of the world patents, the percentage of US patents in different states.
3. Do some data cleaning and grouping
4. Construct figures showing the top ten patents in the world and in the US.

### C. Script ny_patents.py

1. Read the assignees patents csv file.
2. Trim down the data frame to show NY patents distribution.
3. Construct a figure showing the top ten patent candidates in NY state. 


### D. Script Taiwan_patents.py

1. Read the assignees patents csv file.
2. Trim down the data frame to show Taiwan patents distribution.
3. Construct a figure showing the top ten patent candidates in Taiwan, this is to see what industries dominate utility patents in Taiwan. 


### E. Script indiv_patents.py

1. Read the "U.S._FILERS_2014.csv" file to access the individually owned patents in the US. 
2. Do some data cleaning and grouping
3. Construct figures showing the ranking of top ten individually owned patents in the US.
4. Read the "Assignees2014_5yr.csv" file and follow the same steps as above to construct a figure of the ranking of top ten individually owned patents around the world, excluding the US. 

### Key Findings and Moving Forward

The following are the key findings from analyzing the data for this study:

1. In the US, California, Texas and New York seem to dominate utility patents domain in terms of the quantity, California account for more than 25% which is not so surprising due to the existence of Silicon Valley; However, when it comes to individually owned patents, Florida appear to be the number two, it would be interesting to look into the different type of utility patents approved in Florida if the data was available. (See top_ten_patents.png and top_ten_indiv_patents.png)
 
2. Looking at the utility patents' scope around the world, except the US and Germany, Japan, South Korea and Taiwan appear to be on top of the rest of the world when it comes to invention. In Taiwan, it is dominated by semiconductors patents and electronic manufacturing patents

3. In the top ten individual patents distribution in the world, Canada ranks third right after the US and Taiwan. Going forward, it would be interesting to look into the distribution of individually owned patents in Canada in terms of industries.
