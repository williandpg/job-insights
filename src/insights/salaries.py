from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            if job["max_salary"].isdigit():
                if int(job["max_salary"]) > max_salary:
                    max_salary = int(job["max_salary"])
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                if int(job["min_salary"]) < min_salary:
                    min_salary = int(job["min_salary"])
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if not isinstance(salary, int) and not salary.isdigit():
            raise TypeError("salary must be an integer or a string of digits")
        if job["min_salary"].isdigit() and job["max_salary"].isdigit():
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                return True
        return False

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
