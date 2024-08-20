import pandas as pd
import requests
from collections import defaultdict
import json

def json_keys(data, summary=None, parent_key=""):
    """
    Recursively summarizes all keys in a JSON object.

    :param data: The JSON data (as a Python dictionary or list).
    :param summary: A dictionary to store the summary of keys (default: None).
    :param parent_key: A string representing the parent key (for nested keys).
    :return: A dictionary summarizing the occurrence and types of all keys.
    """
    if summary is None:
        summary = defaultdict(lambda: {"count": 0, "types": set(), "example": "", "wmo": set()})

    if isinstance(data, dict):
        for key, value in data.items():
            # Create a full key path for nested keys
            full_key = f"{parent_key}.{key}" if parent_key else key
            summary[full_key]["count"] += 1
            summary[full_key]["types"].add(type(value).__name__)
            summary[full_key]["example"] = value
            if key == "wmo":
                summary[full_key]["wmo"].add(value)
            json_keys(value, summary, full_key)

    elif isinstance(data, list):
        for item in data:
            json_keys(item, summary, parent_key)

    return summary

def data_frame(df, datasetID):
    """
    Summarizes all columns in a DataFrame.

    :param df: The DataFrame to summarize.
    :return: A dictionary summarizing the occurrence, types, examples, and unique values in each column.
    """
    summary = defaultdict(lambda: {"count": 0, "types": set(), "example": "", "unique_values": set()})
    
    for col in df.columns:
        summary[col]["count"] = df[col].notnull().sum()
        summary[col]["types"].add(df[col].dtype.name)
        if summary[col]["count"] > 0:  # Only set example and unique values if there is data
            summary[col]["example"] = df[col].dropna().iloc[0]
            if len(df[col].unique()) <= 10:  # Add unique values if there are 10 or fewer unique values
                summary[col]["unique_values"].update(df[col].dropna().unique())
    
    #turn dict into dataframe
    df_summary = pd.DataFrame([
            {
                "DatasetID": datasetID,
                "Property": col,
                "Count": info["count"],
                "Types": ', '.join(info["types"]),
                "Example": info["example"],
                "UniqueValues": info["unique_values"]
            }
            for col, info in summary.items()
        ])
                
    return df_summary