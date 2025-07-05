import matplotlib
matplotlib.use("TkAgg")  # macOS GUI 백엔드 설정
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

    plt.plot(x, cpu_data, marker='o', label="CPU Usage (%)", color='blue')
    plt.plot(x, mem_data, marker='s', label="Memory Usage (%)", color='green')

    plt.title("Live CPU & Memory Usage")
    plt.xlabel("Measurement Index")
    plt.ylabel("Usage (%)")
    # plt.ylim(0, 100)  # ← 주석 처리: 자동 스케일 조정됨
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()

fig = plt.figure(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
