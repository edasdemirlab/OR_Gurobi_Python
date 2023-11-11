# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:03:34 2023

@author: Huawei
"""
import gurobipy as gp
from gurobipy import GRB   
import pandas as pd
import os

# Model orman_tahsis

# Specify the directory where your CSV file is located
directory = 'C:\\Users\\Huawei\\.spyder-py3\\model_girdileri'  

# Specify the CSV file name
filename = 'orman_veri.csv'

# Use os.path.join() to create the full file path
file_path = os.path.join(directory, filename)

# Read the CSV file into a Pandas DataFrame
orman_veri_df = pd.read_csv(file_path)

# Sabit veriler
analiz_alani = orman_veri_df["Analiz Alani"].tolist()
analiz_alani = set(orman_veri_df["Analiz Alani"])
analiz_alani = list(analiz_alani)
recete = orman_veri_df["Recete"].tolist()
recete = set(orman_veri_df["Recete"])
recete = list(recete)

p = {}
for i in range(len(orman_veri_df)):
    row = orman_veri_df.loc[i, :]
    p[row["Analiz Alani"], row["Recete"]] = row["Net Deger"]
    
s = {}
for i in range(len(orman_veri_df)):
    row = orman_veri_df.loc[i, :]
    s[row["Analiz Alani"]] = row["Donum"]

t = {}
for i in range(len(orman_veri_df)):
    row = orman_veri_df.loc[i, :]
    t[row["Analiz Alani"], row["Recete"]] = row["Kereste"]
    
g = {}
for i in range(len(orman_veri_df)):
    row = orman_veri_df.loc[i, :]
    g[row["Analiz Alani"], row["Recete"]] = row["Otlatma"]
    
w = {}
for i in range(len(orman_veri_df)):
    row = orman_veri_df.loc[i, :]
    w[row["Analiz Alani"], row["Recete"]] = row["Yaban Endeksi"]

m = gp.Model("dagitim")
# Değişkenleri modele ekleyelim
alan = m.addVars(analiz_alani, recete, name="x")

m.update()

# tahsis kısıtı
a = m.addConstrs(
    (alan.sum('*', j) == s[i] for i in analiz_alani for j in recete), "tahsis_kısıtı")

#kereste_kısıt = gp.LinExpr()
#otlatma_kısıt = gp.LinExpr()
#yaban_kısıt = gp.LinExpr()
#amac_fonk = gp.LinExpr()
#for i in analiz_alani_set:
    #for j in recete_set:
       # kereste_kısıt = kereste_kısıt + alan[i,j]*kereste[i,j]
       # otlatma_kısıt = otlatma_kısıt + alan[i,j]*otlatma[i,j]
       # yaban_kısıt = yaban_kısıt + (1/788)*alan[i,j]*yaban[i,j]
       # amac_fonk = amac_fonk + net_deger[i,j] * alan[i,j]
# kereste kısıtı
#m.addConstrs(
    #((gp.quicksum(kereste[i,j]* alan[i,j] for i in analiz_alani_set for j in recete_set) >= 40000) for i in analiz_alani_set for j in recete_set ),name="t")
b = m.addConstr(
    (alan.prod(t) >= 40000), "kereste_kısıtı")

# otlatma kısıtı
#m.addConstrs(
    #((gp.quicksum(otlatma[i,j]* alan[i,j] for i in analiz_alani_set for j in recete_set) >= 5) for i in analiz_alani_set for j in recete_set ),name="g")
c = m.addConstr(
    (alan.prod(g) >= 5), "otlatma_kısıtı")
# yaban endeksi kısıtı
#m.addConstrs(
    #(((1/788)*gp.quicksum(yaban[i,j]* alan[i,j] for i in analiz_alani_set for j in recete_set) >= 70) for i in analiz_alani_set for j in recete_set ),name="w")
m.addConstr(
    ((1/788)*(alan.prod(w)) >= 70), "yaban_kısıtı")
# Compute optimal solution
amac_fonk = gp.quicksum(p[i,j]*alan[i,j] for i in analiz_alani for j in recete)
m.setObjective(amac_fonk, GRB.MAXIMIZE)
m.optimize()

# Print solution
if m.Status == GRB.OPTIMAL:
    solution = m.getAttr('x', alan)
    for i in analiz_alani:
        for j in recete:
            print('%s -> %s: %g' % (i, j, solution[i, j]))












