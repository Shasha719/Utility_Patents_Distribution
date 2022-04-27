#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:28:25 2022

@author: shasha_pogon
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
# Read the patent csv file 

raw_patents = pd.read_csv("Stc2015_5yr.csv")
print(raw_patents)

print("\nThe number of records in the dataframe:")
print(len(raw_patents))

tot_patents = raw_patents.drop(raw_patents.index[196:])
tot_patents = tot_patents["CY_ALL"].sum()
print(tot_patents)

#%%
# Sort US patents in different ways
#

us_patents = raw_patents.drop(raw_patents.index[55:])
print(us_patents)

tot_us_patents = us_patents["CY_ALL"].sum()
print(tot_us_patents)

high_to_low = us_patents.sort_values("CY_ALL", ascending = False)
print(high_to_low)

top_ten_uspatents = high_to_low.iloc[0:10]
print(top_ten_uspatents)

top_ten_uspatents = top_ten_uspatents.copy()

top_ten_uspatents["pct_top_ten"] = top_ten_uspatents["CY_ALL"]/tot_us_patents*100
print(top_ten_uspatents["pct_top_ten"])

#%%
# Construct a graph showing the top ten patents in the US 
# 

fig,ax1 = plt.subplots(dpi=300)
sns.barplot(data=top_ten_uspatents,y="pct_top_ten",x="st_country_cd",ax=ax1)
fig.suptitle("Top Ten Patents in the US")
ax1.set_xlabel("States")
ax1.set_ylabel("Percentage")

fig.tight_layout()
fig.savefig("top_ten_patents.png")

#%%
# Calculate US patents percentage of the world patents
#

pct_us_patents = round(tot_us_patents/tot_patents*100,2)
print(pct_us_patents)

#%%
# Drop some rows in the raw data and group it to show the world patents 
# distribution by countries

patents = raw_patents.drop(labels=range(0,55),axis=0)
patents = patents.drop(labels = [197,198], axis = 0)
print(patents)

high_to_low_patents = patents.sort_values("CY_ALL", ascending = False)
print(high_to_low_patents)

top_ten = high_to_low_patents.iloc[0:10]
print(top_ten)

top_ten = top_ten.copy()

top_ten["pct_top_ten"] = top_ten["CY_ALL"]/tot_patents*100
print(top_ten["pct_top_ten"])

#%%
# Construct a graph showing the top ten patents in the world
#

fig,ax1 = plt.subplots(dpi=300)
sns.barplot(data=top_ten,x="pct_top_ten",y="state_country_of_origin",ax=ax1)
fig.suptitle("Top Ten Patents in the World")
ax1.set_xlabel("Percentage")
ax1.set_ylabel("countries")

fig.tight_layout()
fig.savefig("top_ten.png")



