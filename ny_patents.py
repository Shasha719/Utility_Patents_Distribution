#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 00:19:25 2022

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

ny_patents = assignees_patents[(assignees_patents['state_country_of_origin'] == 'NEW YORK')]
print(ny_patents)
print(len(ny_patents))

top_ten_nypatents = ny_patents.iloc[0:10]
print(top_ten_nypatents)

tot_ny_patents = ny_patents["CY_ALL"].sum()
print(tot_ny_patents)

#%%
# Construct a graph showing the top ten patents in NY state
#

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle("Top Patents Candidates in NY")
sns.barplot(data = top_ten_nypatents, y="assignee_name",x="CY_ALL",ax=ax1)
ax1.set_ylabel("")
ax1.set_xlabel("Patents")

fig.tight_layout()
fig.savefig("ny_patents.png")








