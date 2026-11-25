# GEORGE Interoperability Gap Analysis

Interoperability and FAIRness gap analysis of marine research infrastructure data services conducted within the Horizon Europe **GEORGE** project (*Next generation multiplatform Ocean observing technologies for research infrastructures*, Grant Agreement No. 101094716).

## Analysis & Findings

The interoperability assessment of data services and web services across Euro-Argo, ICOS, EMSO ERIC, and IFREMER is documented in the `notebooks/` directory:

### Synthesis & Framework Assessments
- [Use Cases & Selected Datasets](UseCases.md)
- [Overview of Service Endpoints](notebooks/service_overview.ipynb)
- [ODIS Compliance Assessment](notebooks/ODIScompliance.ipynb)
- [5-Star Open Data Assessment](notebooks/5StarOpenData.ipynb)
- [Interoperability Assessment by Service Type](notebooks/service_type_interop_assessment.ipynb)
- [Comparison of ERDDAP Services](notebooks/comparison_erddap_services.ipynb)
- [Comparison of SPARQL Endpoints](notebooks/comparison_sparql_endpoints.ipynb)

### Individual Service Assessments
- **Euro-Argo**:
  - [HTTPS Server](notebooks/interop_euroargo_https_server.ipynb)
  - [AWS S3 Bucket](notebooks/interop_euroargo_awsS3bucket.ipynb)
  - [OpenSearch](notebooks/interop_euroargo_opensearch.ipynb)
  - [ERDDAP Service](notebooks/interop_euroargo_erddap_service.ipynb)
  - [SPARQL Endpoint](notebooks/interop_euroargo_sparqlendpoint.ipynb)
  - [OGC SensorThings API](notebooks/interop_euroargo_ogcsensorthings_jsonapi.ipynb)
  - [Floats Metadata JSON API](notebooks/interop_euroargo_floatsmetadata_jsonapi.ipynb)
  - [Floats Data JSON API](notebooks/interop_euroargo_floatsdata_jsonapi.ipynb)
- **IFREMER**:
  - [ERDDAP Service](notebooks/interop_ifremer_erddap_service.ipynb)
  - [Glider FTP Server](notebooks/interop_euroargo_ftp_server.ipynb)
- **ICOS**:
  - [SPARQL Endpoint](notebooks/interop_icos_sparqlendpoint.ipynb)
  - [Data Portal](notebooks/interop_icos_dataportal.ipynb)
- **EMSO ERIC**:
  - [ERDDAP Service](notebooks/interop_emso_erddap_service.ipynb)

## Repository Structure

- `notebooks/`: Jupyter notebooks containing endpoint explorations, framework scoring, cross-service comparisons, SPARQL queries (`queries/`), helper modules (`accessibility.py`, `summarize.py`, `connec_functions.py`), Python dependencies (`requirements.txt`), and captured reference outputs/files.
- `data/`: RDF project metadata (`project.ttl`) and exported JSON API CSV tables (`json_api_data/`).
- `src/py/data_retrieve/`: Standalone Python scripts for retrieving and inspecting Argo endpoint, HTTPS, JSON API, and NetCDF data.
- `docker/` & `docker-compose.yml`: Local GraphDB, Jupyter, `lwua-ingest`, `lwua-dereferencer`, and `lwua-sembench` services used during analysis.
- `config/` & `templates/`: Configuration (`sembench.json`) and template files for semantic benchmarking.

## Using This Project

### Docker Environment

1. Retrieve the source code from GitHub:

```bash
git clone https://github.com/vliz-be-opsci/george-analysis.git
cd george-analysis
```

2. Configure the environment and build the services:

```bash
cp dotenv-example .env
docker compose build
```

3. Start up the services:

```bash
docker compose up
```

4. Open JupyterLab / Jupyter Notebook:

```bash
xdg-open $(docker/jupyter_url.sh)
```

5. Open the GraphDB browser UI:

```bash
xdg-open http://localhost:7200
```

6. Run a test ingest (introduces `data/project.ttl` into the triple store if automatic ingestion has not run):

```bash
docker exec -it george_ingest /bin/bash
python -m lwua.ingest
```

### Python Environment (Notebooks Only)

To inspect or re-run the analysis notebooks outside Docker, install the Python dependencies listed in [notebooks/requirements.txt](notebooks/requirements.txt).

## Authors

- **Laurian Van Maldeghem** — Flanders Marine Institute (VLIZ), ORCID: [0000-0003-0663-5907](https://orcid.org/0000-0003-0663-5907)
- **Marc Portier** — Flanders Marine Institute (VLIZ), ORCID: [0000-0002-9648-6484](https://orcid.org/0000-0002-9648-6484)
- **Thanos Gkritzalis** — Flanders Marine Institute (VLIZ), ORCID: [0000-0002-7897-4230](https://orcid.org/0000-0002-7897-4230)

## Citation

If you use this repository, please refer to [CITATION.cff](CITATION.cff) (also accessible via GitHub's *Cite this repository* menu) and the archived Zenodo record once published.

## Funding

This work was supported by the European Union's Horizon Europe research and innovation programme under Grant Agreement No. **101094716** (**GEORGE** — *Next generation multiplatform Ocean observing technologies for research infrastructures*).

## License

This repository is dedicated to the public domain under **CC0 1.0 Universal (CC0 1.0)**. See [LICENSE](LICENSE) for details.
