from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    max_salary = int(0)
    for item in file:
        if item["max_salary"] and item["max_salary"] != 'invalid'\
                        and int(item["max_salary"]) > max_salary:
            # print(int((item["max_salary"])))
            max_salary = int(item["max_salary"])
    return int(max_salary)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    file = read(path)
    min_salary = int(100000)
    # print(min_salary)
    for item in file:
        if item["min_salary"] and item["min_salary"] != 0 and\
                        item["min_salary"] != 'invalid'\
                        and int(item["min_salary"]) < min_salary:
            # print(int((item["min_salary"])))
            min_salary = int(item["min_salary"])
    # print(min_salary)
    return int(min_salary)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if type(job.get("min_salary")) not in [str, int] or\
         type(job.get("max_salary")) not in [str, int]:
        raise ValueError
    if int(job["min_salary"]) > int(job["max_salary"]) or\
            type(salary) not in [str, int]:
        raise ValueError
    # if salary in range(job["min_salary"], job["max_salary"]):
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_in_salary_range = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_in_salary_range.append(job)
        except ValueError:
            continue
    return jobs_in_salary_range
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
