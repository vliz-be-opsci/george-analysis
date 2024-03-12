from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON

# Define the SPARQL endpoint URL
sparql_endpoint = "https://sparql.ifremer.fr/argo/query"

# Create an RDF graph
g = Graph()

# Query the SPARQL endpoint
sparql = SPARQLWrapper(sparql_endpoint)
sparql.setQuery("""
    prefix geo: <https://www.w3.org/2003/01/geo/wgs84_pos#>
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    prefix ssn: <http://www.w3.org/ns/ssn/> 
    prefix xml: <http://www.w3.org/XML/1998/namespace> 
    prefix xsd: <http://www.w3.org/2001/XMLSchema#> 
    prefix argo: <http://www.argodatamgt.org/argo-ontology#> 
    prefix foaf: <http://xmlns.com/foaf/0.1/> 
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    prefix sosa: <http://www.w3.org/ns/sosa/>
    prefix nerc: <http://vocab.nerc.ac.uk/collection/>
    prefix dct: <http://purl.org/dc/terms/>
    prefix prov: <https://www.w3.org/TR/prov-o/>
    SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object } LIMIT 25
""")
sparql.setReturnFormat(JSON)

# Execute the query and parse the results
results = sparql.query().convert()

# Process the results and add them to the RDF graph
for result in results["results"]["bindings"]:
    subject = result["subject"]["value"]
    predicate = result["predicate"]["value"]
    object = result["object"]["value"]
    g.add((subject, predicate, object))  # You may need to specify the subject and predicate here

# Now you can work with the RDF graph
for s, p, o in g:
    print(s, p, o)