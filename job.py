jobs = []

def take_jobs(n):
    for _ in range(n):
        jobname = input("Enter Job name: ")
        priority = int(input("Enter priority: "))
        duration = int(input("Enter duration: "))
        profit = int(input("Enter profit: "))

        job = {
            "name": jobname,
            "priority": priority,
            "duration": duration,
            "profit": profit
        }
        jobs.append(job)

def schedule(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: ( -x['profit'],x['priority'], x['duration']))
    for job in sorted_jobs:
        print(f"name: {job['name']}, priority: {job['priority']}, duration: {job['duration']}, profit: {job['profit']}")

n = int(input("Enter number of jobs: "))
take_jobs(n)
schedule(jobs)
