from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_types.add(job["job_type"])
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")
        filtered_jobs = []
        for job in jobs:
            if all(
                key in job and job[key] == value for key,
                value in filter_criteria.items()
            ):
                filtered_jobs.append(job)
        return filtered_jobs
