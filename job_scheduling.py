num_jobs = int(input("Enter number of jobs : "))
jobs=[]
for i in range(num_jobs):
    name=input(f"Enter job name : ")
    priority=int(input("Enter priority : "))
    duration=int(input("Enter duration : "))
    job={"name":name,"priority":priority,"duration":duration}
    jobs.append(job)
sorted_jobs = sorted(jobs,key=lambda x:(x["priority"],x["duration"]))
for job in sorted_jobs:
    print(f"Job:{job['name']}, Priority:{job['priority']}, Duration:{job['duration']}")