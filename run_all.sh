#!/bin/bash

echo "[0/2] 가상환경 활성화"
source python_analyzer/venv/bin/activate

echo "[1/2] CPU 모니터링 실행 중... (백그라운드)"
g++ cpp_monitor/monitor.cpp -o monitor
./monitor &  # 백그라운드 실행
MONITOR_PID=$!  # 백그라운드 PID 저장

echo "[2/2] 실시간 시각화 시작!"
python3 python_analyzer/live_plot_cpu.py

echo "🛑 실시간 시각화 종료됨. 모니터링 중단 중..."
kill $MONITOR_PID
