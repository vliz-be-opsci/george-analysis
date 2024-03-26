from pykg2tbl import DefaultSparqlBuilder, KGSource, QueryResult
from pathlib import Path
from pandas import DataFrame
import os

class GDB():
    
    def __init__(self, endpoint:str, queries_folder:str) -> None:
        # SPARQL EndPoint to use - wrapped as Knowledge-Graph 'source'
        self.GDB_BASE: str = os.getenv("GDB_BASE", "http://localhost:7200/")
        self.GDB_REPO: str = os.getenv("GDB_REPO", "kgap")
        #print(f"{os.getenv('GDB_BASE')=}")
        #print(f"{GDB_BASE=}")
        self.GDB_ENDPOINT: str = endpoint if endpoint else f"{self.GDB_BASE}repositories/{self.GDB_REPO}"
        self.GDB: KGSource = KGSource.build(self.GDB_ENDPOINT)
        #print(f"{GDB_ENDPOINT=}")
        self.TEMPLATES_FOLDER = str(Path().absolute() / "queries" / queries_folder) if queries_folder else str(Path().absolute() / "queries")  


    def generate_sparql(self, name: str, **vars) -> str:
        """Simply build the sparql by using the named query and applying the vars"""
        GENERATOR = DefaultSparqlBuilder(templates_folder=self.TEMPLATES_FOLDER)
        return GENERATOR.build_syntax(name, **vars)


    def execute_to_df(self, name: str, **vars) -> DataFrame:
        """Builds the sparql and executes, returning the result as a dataframe."""
        sparql = self.generate_sparql(name, **vars)
        result: QueryResult = self.GDB.query(sparql=sparql)
        return result.to_dataframe()
