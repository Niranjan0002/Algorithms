def maxProfit(jobs):
    jobs.sort(key = lambda t: (t[1], -t[2]))
    order = []
    time = 1
    for job in jobs:
        if job[1] >= time:
            order.append(job)
            time+=1
    return order

n = int(input("No. of Jobs : "))
jobs = [tuple(map(int,input("ID, Deadline, Profit of Job " + str(i+1) + " : ").split()))  for i in range(n)]
order = maxProfit(jobs)
print("\nJob\tDeadline\tProfit")
profit = 0
for job in order:
    print(f" {job[0]}\t   {job[1]}\t           {job[2]}")
    profit+=job[2]
print(f"Total Profit : \t\t  {profit}")