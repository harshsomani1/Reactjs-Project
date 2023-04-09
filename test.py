import requests
import json


# Setting gene_id variable
gene_id = "CHEMBL118"

# Building query string
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

print(r.text)
# Transforming API response into JSON 
api_response_as_json = json.loads(r.text)

# Printing API response to terminal
if api_response_as_json['data']['drug']:
  x=api_response_as_json['data']['drug']['drugWarnings']
  y=api_response_as_json['data']['drug']['id']


  a=[]
  for tox in x:
    a.append(tox['toxicityClass'])
    a.append(" ")
  chemb=dict({"id":y, "toxscore":a})
  p= open("/Users/harsh/Desktop/my-app/src/pages/chembl.json", "w")
  m=[]
  m.append(chemb)
  p.write(json.dumps(m))
  p.close()






