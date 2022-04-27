#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:41:02 2022

@author: shasha_pogon
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
# Read the patent csv file 

us_filers = pd.read_csv("U.S._filers_2014.csv")


indivi_patents = us_filers[(us_filers['assignee_name'] == '~INDIVIDUALLY OWNED PATENT')]
print(indivi_patents)
print(len(indivi_patents))

indivi_patents.to_csv("individually_owned_patent.csv")

#%% 
# Pick out individually owned patents in the US
# Do some calculation of the percentage
#

us_indivi_patents = indivi_patents[(indivi_patents['us_or_foreign'] == '(U.S.)')]
print(us_indivi_patents)

us_indivi_patents = us_indivi_patents.drop(us_indivi_patents.index[-1])
print(us_indivi_patents)

tot_us_indivi_patents = us_indivi_patents["CY_ALL"].sum()
print(tot_us_indivi_patents)

rank = us_indivi_patents.sort_values("CY_ALL", ascending = False)
rank.reset_index()
print(rank)
rank_ten = rank.iloc[0:10]
print(rank_ten)

rank_ten = rank_ten.copy()

rank_ten["pct_rank_ten"] = rank_ten["CY_ALL"]/tot_us_indivi_patents*100
print(rank_ten["pct_rank_ten"])

#%%
# Construct a graph showing the top ten individually owned patents in the US 
# 
fig,ax1 = plt.subplots(dpi=300)
sns.barplot(data=rank_ten,y="pct_rank_ten",x="st_country_cd",ax=ax1)
fig.suptitle("Top Ten Individually Owned Patents in the US")
ax1.set_xlabel("States")
ax1.set_ylabel("Percentage")

fig.tight_layout()
fig.savefig("top_ten_indivi_patents.png")

#%%
# Pick out individually owned patents in foreign countries
# Do some calculation of the percentage

assignees_patents = pd.read_csv("Assignees2014_5yr.csv")

foreign_patents = assignees_patents[(assignees_patents['us_or_foreign'] == '(Foreign)')]
print(foreign_patents)
print(len(foreign_patents))

foreign_indivi_patents = foreign_patents[(foreign_patents['assignee_name'] == '~INDIVIDUALLY OWNED PATENT')]
print(foreign_indivi_patents)
print(len(foreign_indivi_patents))

foreign_indivi_patents = foreign_indivi_patents.drop(foreign_indivi_patents.index[-1])
print(foreign_indivi_patents)

tot_fore_indivi_patents = foreign_indivi_patents["CY_ALL"].sum()
print(tot_fore_indivi_patents)

foreign_rank = foreign_indivi_patents.sort_values("CY_ALL", ascending = False)
foreign_rank.reset_index()
print(foreign_rank)
foreign_rank_ten = foreign_rank.iloc[0:10]
print(foreign_rank_ten)

foreign_rank_ten = foreign_rank_ten.copy()

foreign_rank_ten["pct_foreign_rank_ten"] = foreign_rank_ten["CY_ALL"]/tot_fore_indivi_patents*100
print(foreign_rank_ten["pct_foreign_rank_ten"])

#%%
# Construct a graph showing the top ten individually owned patents in foreign countries 
# 

fig,ax1 = plt.subplots(dpi=300)
sns.barplot(data=foreign_rank_ten,x="pct_foreign_rank_ten",y="state_country_of_origin",ax=ax1)
fig.suptitle("Top Ten Individually Owned Patents in the World")
ax1.set_xlabel("Percentage")
ax1.set_ylabel("countries")

fig.tight_layout()
fig.savefig("top_foreign_indivi_patents.png")



