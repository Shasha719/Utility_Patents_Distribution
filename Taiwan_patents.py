#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:18:27 2022

@author: shasha_pogon
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
# Read the patent csv file 

assignees_patents = pd.read_csv("Assignees2014_5yr.csv")

print("\nThe number of records in the dataframe:")
print(len(assignees_patents))

#%%
# Trim the patents data and show the NY patents
#

Taiwan_patents = assignees_patents[(assignees_patents['state_country_of_origin'] == 'TAIWAN')]
print(Taiwan_patents)
print(len(Taiwan_patents))

top_Taiwan_patents = Taiwan_patents.iloc[0:10]
print(top_Taiwan_patents)

tot_Taiwan_patents = Taiwan_patents["CY_ALL"].sum()
print(tot_Taiwan_patents)

#%%
# Construct a graph showing the top ten patents in NY state
#

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Top Patents Candidates in Taiwan")
sns.barplot(data = top_Taiwan_patents, y="assignee_name",x="CY_ALL",ax=ax1)
ax1.set_ylabel("")
ax1.set_xlabel("Patents")

fig.tight_layout()
fig.savefig("Taiwan_patents.png")