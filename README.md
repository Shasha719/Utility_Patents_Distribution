# patent_dev

## Summary

This project intends to demonstrate the utility patents distribution in the world, as well as in the United States. I will also conduct an analysis of the utility patents particularly in New York State, both quantitatively and qualitatively.  

## Input data

There are two input files.

They can be obtained through below API endpoint:
https://uspto.data.commerce.gov/resource/5yb9-mbg7.json
https://uspto.data.commerce.gov/resource/jwx5-kdx6.json

**Stc2015_5yr.csv**, prepared from the U.S. Patent and Trademark Office (USPTO), Technology Assessment and Forecast (TAF) database, displays a listing of geographic regions from which utility patents (i.e., patents for invention) originated during the indicated 5 year time period and a corresponding count of patents for each of the years of the period. Each displayed annual count corresponds to the count of patents received in a calendar year (January 1 to December 31).

**Assignees2014_5yr.csv**, prepared from the U.S. Patent and Trademark Office (USPTO), Technology Assessment and Forecast (TAF) database, displays a listing of organizations receiving the most utility patents (i.e., patents for invention) during the indicated 5 year time period. Each displayed annual count corresponds to the count of patents received in a calendar year (January 1 to December 31). This file generally contains the contents of the PTMT report, DRILL-DOWN Utility Patent Report, Patenting by Geographic Origin (State and Country) - Breakout By Organization. 

## Deliverables

There are six deliverables: three scripts, **patents.py**, **ny_patents.py** and **patents_dist**; Three figures, **top_ten_patents.png**, **top_ten.png** and **ny_patents.png**.

## Instructions

### A. Downloading files from USPTO government website

Using below API endpoints, or download csv files directly:
https://uspto.data.commerce.gov/resource/5yb9-mbg7.json
https://uspto.data.commerce.gov/resource/jwx5-kdx6.json

### B. Scrpit patents.py

1. Read the patents csv file.
2. Sort out the foreign and US utility patents in different ways to get a better sense of the geographic distribution. As well as, US patents percentage of the world patents, the percentage of US patents in different states.
3. Do some data cleaning and grouping
4. Construct figures showing the top ten patents in the world and in the US.

### C. Script ny_patents.py

1. Read the assignees patents csv file.
2. Trim down the data frame to show NY patents distribution.
3. Construct a figure showing the top ten patents in NY state. 