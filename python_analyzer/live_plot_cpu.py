import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import datetime  # ✅ 그래프 저장용

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

    # 점별 색상
    cpu_colors = ['red' if val >= 90 else 'blue' for val in cpu_data]
    mem_colors = ['orange' if val >= 90 else 'green' for val in mem_data]

    # 선: 색상 조건별로 나눠서 따로 그림
    def plot_colored_line(data, colors, label_prefix):
        for color in set(colors):
            indices = [j for j, c in enumerate(colors) if c == color]
            if len(indices) >= 2:
                x_vals = [x[k] for k in indices]
                y_vals = [data[k] for k in indices]
                plt.plot(x_vals, y_vals, color=color, alpha=0.4, label=f"{label_prefix} {color.title()} Line")

    plot_colored_line(cpu_data, cpu_colors, "CPU")
    plot_colored_line(mem_data, mem_colors, "MEM")

    # 점: 색상 그대로
    plt.scatter(x, cpu_data, label="CPU Usage (%)", c=cpu_colors)
    plt.scatter(x, mem_data, label="Memory Usage (%)", c=mem_colors)

    plt.title("Live CPU & Memory Usage")
    plt.xlabel("Measurement Index")
    plt.ylabel("Usage (%)")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()

    # 실시간 경고
    if any(val >= 90 for val in cpu_data):
        print("⚠️ CPU ALERT: Usage exceeded 90%!")
    if any(val >= 90 for val in mem_data):
        print("⚠️ MEMORY ALERT: Usage exceeded 90%!")

    # ✅ 요약 통계 및 그래프 저장 (1회만)
    if i == 1 and cpu_data and mem_data:
        avg_cpu = sum(cpu_data) / len(cpu_data)
        max_cpu = max(cpu_data)
        min_cpu = min(cpu_data)

        avg_mem = sum(mem_data) / len(mem_data)
        max_mem = max(mem_data)
        min_mem = min(mem_data)

        print("\n🔍 리소스 사용 요약 (최근 20회 기준)")
        print(f"🟦 CPU 평균: {avg_cpu:.1f}%, 최대: {max_cpu:.1f}%, 최소: {min_cpu:.1f}%")
        print(f"🟩 MEM 평균: {avg_mem:.1f}%, 최대: {max_mem:.1f}%, 최소: {min_mem:.1f}%\n")

        # ✅ 그래프 저장
        filename = f"resource_usage_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(filename)
        print(f"📸 그래프 저장됨: {filename}")

fig = plt.figure(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
