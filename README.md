# EdgeGuard

**EdgeGuard**는 CPU 및 메모리 사용률을 실시간으로 시각화하고, 경고 알림과 그래프 저장 기능을 제공하는 경량 시스템 모니터링 툴입니다.  
C++ 기반의 모니터링 도구와 Python 시각화 도구를 통합하여 시스템 자원 감시에 도움을 줍니다.

---

## 🔍 소개

- **실시간 모니터링**: CPU 및 메모리 사용률을 색상 기반으로 시각화
- **경고 감지**: 일정 사용률 이상일 경우 텍스트 경고 출력
- **그래프 자동 저장**: 특정 시점 또는 조건에서 이미지 파일로 저장
- **C++ + Python 통합**: C++로 수집, Python으로 시각화

---

## 🚀 실행 방법

### 1. 가상환경 준비

```bash
cd EdgeGuard
python3 -m venv python_analyzer/venv
source python_analyzer/venv/bin/activate
pip install matplotlib
```

### 2. 전체 실행

```bash
./run_all.sh
```

---

## 🧰 프로젝트 구조

```
EdgeGuard/
├── cpp_monitor/            # C++ 기반 CPU/메모리 사용량 측정
├── python_analyzer/        # Python 시각화 및 애니메이션
├── run_all.sh              # 전체 실행 스크립트
├── resource_usage_*.png    # 저장된 시각화 그래프
├── logs/data.txt           # 로그 데이터 파일
└── README.md
```

---

## 💡 주요 기능 요약

- 실시간 CPU/Memory 시각화
- 고사용률 시 색상별 경고 및 콘솔 알림
- 평균/최댓값/최솟값 통계 자동 출력
- 1회 그래프 저장 기능 (`savefig` 활용)

---

## 🛠 개발 환경

| 구성 요소     | 버전/환경                         |
|--------------|----------------------------------|
| OS           | Linux 기반 (Ubuntu 등) 추천       |
| Python       | 3.x (Matplotlib, psutil 사용)     |
| C++          | C++11 이상, `/proc` 파싱 기반     |
| 시각화 방식   | `matplotlib.animation.FuncAnimation` 활용 |

---

## 📸 결과 예시

| 실시간 그래프 (예시) |
|-----------------------|
| ![result](resource_usage_20250705_225335.png) |

---

## 📎 기타

- 추후 기능 아이디어: 음성 경고, CSV 기록 등
