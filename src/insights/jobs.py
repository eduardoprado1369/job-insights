from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(file_path: str) -> List[Dict]:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """


def get_unique_job_types(path: str) -> List[str]:
    file = read(path)
    job_types = set()
    for item in file:
        job_types.add(item["job_type"])
    return job_types
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = list(dict())
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
