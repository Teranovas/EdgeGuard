import matplotlib
matplotlib.use("TkAgg")  # macOS GUI용 백엔드 설정
import matplotlib.pyplot as plt
from matplotlib import animation
import os

log_path = "/Users/apple/EdgeGuard/logs/data.txt"

print("🔍 파일 존재 여부:", os.path.exists(log_path))
print("📂 경로 확인:", log_path)

# 파일 내용 출력
try:
    with open(log_path, "r") as f:
        print("📄 파일 내용:")
        print(f.read())
except Exception as e:
    print("❌ 파일 열기 실패:", e)


usage_values = []

def read_cpu_usage():
    global usage_values
    usage_values.clear()  # ✅ 기존 전역 리스트를 비움
    try:
        with open(log_path, "r") as file:
            for line in file:
                if "CPU Usage" in line:
                    percent = float(line.strip().split(":")[1].replace("%", ""))
                    usage_values.append(percent)
    except FileNotFoundError:
        print("Log file not found.")
    return usage_values[-20:]



def animate(i):
    plt.cla()
    data = read_cpu_usage()
    plt.plot(data, marker='o', linestyle='-', color='green')
    plt.title("Live CPU Usage")
    plt.xlabel("Measurement Index")
    plt.ylabel("CPU Usage (%)")
    plt.grid(True)
    plt.tight_layout()

fig = plt.figure(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
