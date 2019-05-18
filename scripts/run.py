import pandas as pd
from pandas.io.json import json_normalize

from SPARQLWrapper import SPARQLWrapper, JSON

sparql_service = "https://query.wikidata.org/sparql"
sparql_query = """
SELECT ?drug ?drugLabel ?gene ?geneLabel ?entrez_id ?disease ?diseaseLabel WHERE {
      ?drug wdt:P129 ?gene_product .   # drug interacts with a gene_product 
      ?gene_product wdt:P702 ?gene .  # gene_product is encoded by a gene
      ?gene wdt:P2293 ?disease .    # gene is genetically associated with a disease 
      ?gene wdt:P351 ?entrez_id .  # get the entrez gene id for the gene 
      # add labels
      SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en" .
      }
    }
    limit 1000
"""

def get_sparql_dataframe(service, query):
    """
    Query the endpoint with the given query string and return the results as a pandas Dataframe.
    """
    # create the connection to the endpoint
    sparql = SPARQLWrapper(service)
    
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # ask for the result
    result = sparql.query().convert()
    return json_normalize(result["results"]["bindings"])

df = get_sparql_dataframe(sparql_service, sparql_query)
simple_table = df[["drugLabel.value", "diseaseLabel.value", "geneLabel.value"]]
print(simple_table.head())