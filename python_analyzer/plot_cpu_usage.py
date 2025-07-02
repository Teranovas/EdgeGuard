import matplotlib.pyplot as plt

# 데이터 파일 경로
log_path = "../logs/data.txt"

# 사용률 데이터를 읽기
usage_values = []

with open(log_path, "r") as file:
    for line in file:
        if "CPU Usage" in line:
            # 예: "CPU Usage: 17.5%" → 17.5만 추출
            percent = float(line.strip().split(":")[1].replace("%", ""))
            usage_values.append(percent)

# 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(usage_values, marker='o', linestyle='-', color='blue')
plt.title("CPU Usage Over Time")
plt.xlabel("Measurement Index")
plt.ylabel("CPU Usage (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
