import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import animation
import os

log_path = "/Users/apple/EdgeGuard/logs/data.txt"

usage_cpu = []
usage_mem = []

def read_usage_data():
    global usage_cpu, usage_mem
    usage_cpu.clear()
    usage_mem.clear()

    try:
        with open(log_path, "r") as file:
            for line in file:
                if "CPU Usage" in line and "Memory Usage" in line:
                    try:
                        cpu_part = line.split("CPU Usage:")[1].split("%")[0].strip()
                        mem_part = line.split("Memory Usage:")[1].split("%")[0].strip()
                        usage_cpu.append(float(cpu_part))
                        usage_mem.append(float(mem_part))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("data.txt not found.")
    return usage_cpu[-20:], usage_mem[-20:]

def animate(i):
    plt.cla()
    cpu_data, mem_data = read_usage_data()
    x = list(range(len(cpu_data)))

    # ✅ [추가] 경고 색상 조건
    cpu_colors = ['red' if val >= 90 else 'blue' for val in cpu_data]
    mem_colors = ['orange' if val >= 90 else 'green' for val in mem_data]

    # ✅ [변경] scatter로 개별 마커 시각화
    plt.scatter(x, cpu_data, label="CPU Usage (%)", c=cpu_colors)
    plt.scatter(x, mem_data, label="Memory Usage (%)", c=mem_colors)

    plt.title("Live CPU & Memory Usage")
    plt.xlabel("Measurement Index")
    plt.ylabel("Usage (%)")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()

    # ✅ [추가] 콘솔 경고
    if any(val >= 90 for val in cpu_data):
        print("⚠️ CPU ALERT: Usage exceeded 90%!")
    if any(val >= 90 for val in mem_data):
        print("⚠️ MEMORY ALERT: Usage exceeded 90%!")

fig = plt.figure(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
