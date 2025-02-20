# Service Endpoints Overview

This document provides an overview of service endpoints analyzed as part of the interoperability gap analysis.  
[[source file](https://icos-ri.atlassian.net/wiki/spaces/GEOR/pages/372801570/Your+input+contribution+to+GEORGE+WP4+Task+1.+i+roadmap)]

## Endpoints Overview

| Research Infrastructure | Service Type | Endpoint | Data Topic | Data Format | Contact |
|-------------------------|----------|----------|------|------------|---------|
| **Euro-Argo** | HTTPS Server | https://data-argo.ifremer.fr/ | Argo floats data and metadata | NetCDF | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | S3 server | https://registry.opendata.aws/argo-gdac-marinedata/ | Argo floats data and metadata | NetCDF | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | Open Search | https://opensearch.ifremer.fr/html | Argo floats metadata | Opensearch Atom granules | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | ERDDAP Server | https://erddap.ifremer.fr/erddap/tabledap/ArgoFloats-synthetic-BGC.graph | Argo floats data and metadata | OpenDAP on top of NetCDF | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | SPARQL endpoint | https://sparql.ifremer.fr/argo/query | Argo floats metadata | RDF triples | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | JSON API | https://sextant.ifremer.fr/examind/WS/sts/coriolis/v1.1 | Argo floats data and metadata | JSON | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | JSON API | https://fleetmonitoring.euro-argo.eu/swagger-ui.html | Argo floats metadata | JSON | Delphine Dobler, Thierry Carval |
| **Euro-Argo** | JSON API | https://dataselection.euro-argo.eu/swagger-ui.html#/ | Argo floats data | JSON | Delphine Dobler, Thierry Carval |
| **IFREMER** | ERDDAP Server | https://erddap.ifremer.fr/erddap/tabledap/OceanGlidersGDACTrajectories.html | Glider data and metadata | OpenDAP on top of NetCDF | Delphine Dobler, Thierry Carval |
| **IFREMER** | FTP Server |ftp://ftp.ifremer.fr/ifremer/glider/v2 | Glider data and metadata | OceanGliders NetCDF | Delphine Dobler, Thierry Carval |
| **ICOS** | SPARQL endpoint | https://meta.icos-cp.eu/sparqlclient/?type=CSV | Data from ships & moorings in the ICOS network | Various (JSON, CSV, XML, TSV, Turlte) | Steve Jones |
| **ICOS** | Data portal | https://data.icos-cp.eu/portal/ | Data from ships & moorings in the ICOS network | Various (JSON, RDF/XML, Turtle, XML) | Steve Jones |
| **EMSO ERIC** | ERDDAP Server | https://erddap.emso.eu/erddap | EMSO regional facilities data and metadata | CSV, NetCDF, JSON, HTML, etc. | Aljaz Maslo |
