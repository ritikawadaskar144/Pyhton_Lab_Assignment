import matplotlib.pyplot as plt

# Example process data
processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [5, 3, 8, 6]
priority = [2, 1, 4, 3]


# ---------------- FCFS ----------------
def fcfs(processes, burst_time):
    waiting_time = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    turnaround_time = [burst_time[i] + waiting_time[i] for i in range(len(processes))]

    print("FCFS Waiting Time:", waiting_time)
    print("FCFS Turnaround Time:", turnaround_time)

    gantt_chart(processes, burst_time, "FCFS")


# ---------------- SJF ----------------
def sjf(processes, burst_time):
    data = list(zip(processes, burst_time))
    data.sort(key=lambda x: x[1])

    processes_sorted = [x[0] for x in data]
    burst_sorted = [x[1] for x in data]

    waiting_time = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting_time[i] = burst_sorted[i - 1] + waiting_time[i - 1]

    turnaround_time = [burst_sorted[i] + waiting_time[i] for i in range(len(processes))]

    print("SJF Waiting Time:", waiting_time)
    print("SJF Turnaround Time:", turnaround_time)

    gantt_chart(processes_sorted, burst_sorted, "SJF")


# ---------------- PRIORITY ----------------
def priority_scheduling(processes, burst_time, priority):
    data = list(zip(processes, burst_time, priority))
    data.sort(key=lambda x: x[2])

    processes_sorted = [x[0] for x in data]
    burst_sorted = [x[1] for x in data]

    waiting_time = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting_time[i] = burst_sorted[i - 1] + waiting_time[i - 1]

    turnaround_time = [burst_sorted[i] + waiting_time[i] for i in range(len(processes))]

    print("Priority Waiting Time:", waiting_time)
    print("Priority Turnaround Time:", turnaround_time)

    gantt_chart(processes_sorted, burst_sorted, "Priority")


# ---------------- ROUND ROBIN ----------------
def round_robin(processes, burst_time, quantum):
    remaining = burst_time.copy()
    time = 0
    sequence = []

    while True:
        done = True

        for i in range(len(processes)):
            if remaining[i] > 0:
                done = False

                if remaining[i] > quantum:
                    time += quantum
                    remaining[i] -= quantum
                    sequence.append((processes[i], quantum))
                else:
                    time += remaining[i]
                    sequence.append((processes[i], remaining[i]))
                    remaining[i] = 0

        if done:
            break

    p = []
    b = []
    for i in sequence:
        p.append(i[0])
        b.append(i[1])

    gantt_chart(p, b, "Round Robin")


# ---------------- Gantt Chart ----------------
def gantt_chart(processes, burst, title):
    start = 0

    for i in range(len(processes)):
        plt.barh(0, burst[i], left=start)
        plt.text(start + burst[i] / 2, 0, processes[i], ha='center', va='center')
        start += burst[i]

    plt.title(title + " Gantt Chart")
    plt.yticks([])
    plt.xlabel("Time")
    plt.show()


# Run Algorithms
fcfs(processes, burst_time)
sjf(processes, burst_time)
priority_scheduling(processes, burst_time, priority)
round_robin(processes, burst_time, quantum=2)