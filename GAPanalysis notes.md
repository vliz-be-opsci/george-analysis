notes on ODIS-alignment:
(1) ARGO floats & gliders

	ARGO floats Metadata --> should be modeled as Vessels (following https://book.odis.org/thematics/vessels/index.html) in the RDF representation 

looking at SPARQL endpoint (~ only Argo floats metadata, the representation of ARGO metadata that is closed to ODIS framework since it is already RDF) 
- some use of dcat
- no use of schema.org... (not a prefix in sparql endpoint)
- use of nerc vocabs... ? 
    --> not a prefix in SPARQL endpoint
    --> but included in the data  
    (e.g. <https://fleetmonitoring.euro-argo.eu/float/1900045> foaf:maker <http://vocab.nerc.ac.uk/collection/R24/current/WRC> )
    (e.g. )
- use of own defined vocab (argo-vocab), but e.g. institutes from standardized nerc vocab (https://vocab.nerc.ac.uk/collection/R24/current/)
- data interoperable; but there are errors: 
    (e.g. triple <https://fleetmonitoring.euro-argo.eu/float/1900045#group3> <https://co.ifremer.fr/co/argo-linked-data/doc/argo-floats.ttl#dataState> <http://vocab.nerc.ac.uk/collection/R06/current/2> --> object url doesn't exist..)
- no license information (not retrievable from SPARSL endpoint - but data is openly avaiable through endpoint)
- partial adherence to thematic patterns of ODIS --> similar concepts present (e.g. data, vessels, etc.) but modeled differently (~ e.g. floats are modeled as datasets; data files are modeled as distributions of datasets)


in context to getting to 5 star data
--> ARGO vocab server shows many standardised lists (e.g. all principal investigators have a unique identifier: https://vocab.nerc.ac.uk/search_nvs/R40/)
~ these need to be used in the RDF representation of the data 
(currently not so... 
e.g. principalinvestigators in SPARQL endpoint: 
	- url structure is <https://co.ifremer.fr/co/argo-linked-data/doc/argo-floats.ttl#{PI-name}> 
	- are objects with rdf:type and foaf:name
	- https://vocab.nerc.ac.uk/search_nvs/R40/
	
	ARGO floats data --> should be modeled as Datasets (following https://book.odis.org/thematics/dataset/index.html#) in the RDF representation

no RDF representation available yet... only sensorthings API (which already follows a stadnard - OK in itself) and swagger-ui API docs 


	Gliders
	


(2) ICOS 

looking at SPARQL endpoint ( ~ the representation of ICOS (meta)data that is closed to ODIS framework since it is already RDF) 
- schema.org not included in data model, but not classes from ODIS (Dataset, Vehicle, ...)
- ontology available as xml/rdf ( http://meta.icos-cp.eu/ontologies/cpmeta/ ) 
	- only mention of http://schema.org/image (no other schema.org mentions)
	- no mention of dcat 
- dcat is included in data model (use of various predicates, classes --> analysed with queries + predefined sparql query with dcat available 'DCAT METADATA DEMO')
- partial adherence to thematic patterns of ODIS --> similar concepts present (e.g. data, vessels, etc.) but modeled differently (through use of internal vocabs: 
    <http://meta.icos-cp.eu/ontologies/cpmeta/>,
    <http://meta.icos-cp.eu/ontologies/stationentry/>, 
    <http://meta.icos-cp.eu/ontologies/otcmeta/>)


in context of getting to 5 start data 
use of self defined ontologies ... ~ 4stars 
hasDOI has string as value -> DOI could be provided as link/anyURI
anyURI is available for some properties: DataTheme, Station, image of an Agent, fundingInfoProp of a Funding, 



(3) EMSO ERIC
only ERDDAPP server 
docs available on github ~ attributes and codes described there / no identifiers 
--> docs do mention that several controlled vocabs of NERC Vocabulary SErvice are used in the metadata standard 


in context of getting to 5 start data
3 stars 
no rdf available 


EMSO (meta)data --> should be modeled as RDF making use of both schema.org (following the ODIS framework) and dcat ontologies

looking at description of attributes a match with ODIS framework seems possible ~ mention of dataset, institutes, ... (no mention of vessels)
also indicates that alignment with dcat ontogy is possible

(before conversion to RDF even, use of url in description of datasets is also improvement -- though conversion to RDF likely to offer higher pay-off given amount of input work )

############################################
Indicators for compliance to ODIS framework:
############################################
1. Use of RDF for structured data (0.2)
2. adherence to thematic patterns (0.2)
3. implementation of schema.org vocab (0.2)
4. incorporation of json-ld snippets within html pages (0.2) 
5. availability of xml sitemaps listing resoruces intended for indexing (0.2)

--> weighted score calculated based on combination of indicators  

To determine scores for compliance with the ODIS Framework, you can develop a scoring methodology that assesses how well a dataset or service aligns with its key principles. This involves evaluating structured data practices, adherence to metadata standards, interoperability, and alignment with ODIS thematic patterns.
Step 1: Identify Key ODIS Criteria

Based on the ODIS framework and its documentation, the evaluation criteria can include:

    Metadata Standards
    Use of Schema.org Vocabulary
    Structured Data with JSON-LD
    Thematic Patterns Compliance
    Data Accessibility
    Interoperability
    Participation in ODIS Network
    Validation and Quality Assurance

Step 2: Develop Indicators and Scoring Rubric

Each criterion can be scored on a consistent scale (e.g., 0-5), where higher scores indicate better compliance. Here’s an example rubric:
1. Metadata Standards

    Indicators:
        Adherence to recognized metadata standards (e.g., ISO 19115, Dublin Core).
        Completeness of metadata (e.g., title, description, license, keywords).
    Scoring:
        0: No metadata available.
        1: Metadata exists but lacks structure or completeness.
        3: Metadata follows partial standards but is incomplete.
        5: Metadata is complete and compliant with recognized standards.

2. Use of Schema.org Vocabulary

    Indicators:
        Incorporation of schema.org terms in metadata.
        Alignment with ODIS thematic patterns using schema.org properties.
    Scoring:
        0: No schema.org vocabulary used.
        1: Minimal use of schema.org properties.
        3: Schema.org properties partially used and thematic alignment present.
        5: Full implementation of schema.org with thematic alignment.

3. Structured Data with JSON-LD

    Indicators:
        Presence of JSON-LD in web pages.
        Correct and complete implementation of structured data.
    Scoring:
        0: No structured data present.
        1: Structured data exists but lacks accuracy or completeness.
        3: JSON-LD is used and mostly correct.
        5: JSON-LD is complete, validated, and accurate.

4. Thematic Patterns Compliance

    Indicators:
        Adherence to ODIS thematic patterns for specific resource types (e.g., datasets, institutions, projects).
    Scoring:
        0: No thematic compliance.
        1: Limited alignment with patterns.
        3: Partial adherence to thematic patterns.
        5: Full compliance with thematic patterns.

5. Data Accessibility

    Indicators:
        Data availability through standard web protocols (e.g., HTTP, APIs).
        Open licensing and minimal restrictions on access.
    Scoring:
        0: Data not accessible.
        1: Restricted access with limited protocols.
        3: Data accessible with partial open licensing.
        5: Fully accessible data with open licensing.

6. Interoperability

    Indicators:
        Use of controlled vocabularies (e.g., SeaDataNet, GCMD keywords).
        Interoperable formats (e.g., NetCDF, XML, RDF).
    Scoring:
        0: No interoperability features.
        1: Minimal use of controlled vocabularies or formats.
        3: Partial interoperability through vocabularies and formats.
        5: Fully interoperable data with extensive use of vocabularies and formats.

7. Participation in ODIS Network 									?????

    Indicators:
        Contribution of datasets or services to the ODIS network.
        Integration with ODIS Catalog of Sources (ODISCat).
    Scoring:
        0: No participation.
        1: Minimal integration with ODIS.
        3: Partial integration with some datasets/services in ODISCat.
        5: Full participation with all relevant datasets/services in ODISCat.

8. Validation and Quality Assurance									?????

    Indicators:
        Validation of structured data using ODIS-recommended tools.
        Consistency and quality of data/metadata.
    Scoring:
        0: No validation performed.
        1: Limited validation with errors present.
        3: Partial validation with minor issues.
        5: Fully validated data with no errors.

#############################################
Indicators for compliance to inclusion in ENVRI catalogue
#############################################

TODO


#############################################
Indicators for compliance to 5 star open data
#############################################

Criteria		Weight	Score (0-5)	Weighted Score
Machine-readable Data	0.2	4		0.8
Structured Data		0.2	3		0.6
Open Formats		0.2	2		0.4
Use of URIs		0.2	1		0.2
Linked Data		0.2	1		0.2

--> Determining scores for the 5-Star Open Data Criteria involves evaluating data services or datasets against the specific characteristics of each star level. Here's how to assess and score each criterion:
1-Star: Available on the Web (Machine-Readable)

    Description: The data is available online in any format.
    Indicators:
        Presence of downloadable files on a public website.
        Files are in machine-readable formats like TXT, CSV, or XLS.
    Scoring:
        0: Data is not available online.
        1: Data is available but in non-machine-readable formats (e.g., PDF, images).
        2: Data is available in machine-readable formats.

2-Star: Structured Data

    Description: The data is structured and provided in an open format.
    Indicators:
        Data is organized in tables or structured formats (e.g., CSV, JSON).
        Use of non-proprietary formats.
    Scoring:
        0: Data is unstructured (e.g., plain text).
        1: Data is structured but in proprietary formats (e.g., XLS, DOC).
        2: Data is structured and in open formats like CSV or JSON.

3-Star: Open Formats

    Description: The data is in a format that is non-proprietary and platform-independent.
    Indicators:
        Use of truly open formats (e.g., CSV, JSON, XML, RDF).
        Avoidance of proprietary formats (e.g., XLS, DOC).
    Scoring:
        0: Data is in proprietary formats.
        1: Data is in partially open formats or has dependencies.
        2: Data is in fully open formats.

4-Star: Use of URIs

    Description: Data is linked and uses Uniform Resource Identifiers (URIs) to uniquely identify resources.
    Indicators:
        Resources are described with unique URIs that can be resolved over the web.
        Links to other datasets or related resources are provided.
    Scoring:
        0: No use of URIs.
        1: Limited use of URIs, not resolvable.
        2: Widespread use of resolvable URIs.

5-Star: Linked Data

    Description: The data is linked to other datasets, enabling integration and contextualization.
    Indicators:
        Use of semantic web technologies (e.g., RDF, SPARQL).
        Links to other datasets through shared URIs or vocabularies.
    Scoring:
        0: No linked data.
        1: Limited use of linked data concepts (e.g., URIs for some elements).
        2: Full implementation of linked data principles (interoperable, queryable).




No use of FAIR assessment tools
--> scoring data serives, platforms, data models
--> could have look at dataset level 
    --> https://www.f-uji.net/ 
    --> https://worldfair-project.eu/cross-domain-interoperability-framework/ 
    --> https://www.sitemaps.org/protocol.html

https://book.odis.org/