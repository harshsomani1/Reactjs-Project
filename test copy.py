import requests
import json
import pandas as pd



# import json
# with open("/Users/harsh/Desktop/backend/stitch.tsv", "r") as p:
#     df=pd.read_csv(p)
# df2=df.loc[df["uniprot"]=="['O95140']"]
# f = open('/Users/harsh/Desktop/backend/smilesmap.json')
  

# data = json.load(f)

# df2["smiles"]=df2["chemical"].astype(str).map(data)

# for smiles_id in df2["smiles"]:

  
#   if type(smiles_id[0])==str:
#     if "#" in smiles_id[0]:
#       print("Cant run API")
#       continue
#     base_url = f'https://www.ebi.ac.uk/chembl/api/data/similarity/{smiles_id[0]}/80?format=json'
#     r = requests.get(base_url)

#     json_data=json.loads(r.text)

#     #Toxicity fetching
#     if json_data["molecules"]:
#       gene_id=json_data["molecules"][0]["molecule_chembl_id"]
#       print(gene_id, end=" ")
gene_id="CHEMBL2096800"
query_string = """
  query drugannotation($chemblId: String!){
    drug(chemblId: $chemblId) {
    id
    
    drugWarnings {
      
      
      toxicityClass
      
      
      
    }
  }
}"""

# Setting variables object of arguments to be passed to endpoint
variables = {"chemblId": gene_id}

# Setting base URL of GraphQL API endpoint
base_url = "https://api.platform.opentargets.org/api/v4/graphql"

# Performing POST request and check status code of response
r = requests.post(base_url, json={"query": query_string, "variables": variables})

api_response=json.loads(r.text)
if not api_response["data"]["drug"]["drugWarnings"]:
  print("Toxicity data not found")
else:
  print(api_response["data"]["drug"])
# else:
#   print("No chemblID found")
# else:
#   print("No smilesID found")








