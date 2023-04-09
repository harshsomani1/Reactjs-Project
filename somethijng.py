import requests
import json
import pandas as pd



import json
with open("/Users/harsh/Desktop/backend/stitch.tsv", "r") as p:
    df=pd.read_csv(p)
df2=df.loc[df["uniprot"]=="['O95140']"]
f = open('/Users/harsh/Desktop/backend/smilesmap.json')
  

data = json.load(f)

df2["smiles"]=df2["chemical"].astype(str).map(data)
for smiles_id,score in zip(df2.smiles, df2.combined_score):
    print(smiles_id,score)
    #print(df2.loc[df2["smiles"].astype(str)=="['C1COCCC1NC2=NC=C(C(=N2)NC3=CC=CC=C3NC(=O)CCS)Cl']"])