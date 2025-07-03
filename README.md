# EdgeGuard

## 🔍 소개
**EdgeGuard**는 CPU 사용률을 측정하고 실시간 시각화하는 경량 Linux 기반 시스템 모니터링 툴입니다.  
C++로 작성된 CPU 모니터링 프로그램과 Python 기반 시각화 도구를 통합하여, 시스템 자원 감시에 도움을 줍니다.

---

## 📁 프로젝트 구조
EdgeGuard/
├── cpp_monitor/                    # C++ 모듈 디렉토리
│   └── monitor.cpp                # CPU 사용률 측정 로직
├── logs/                          
│   └── data.txt                   # CPU 로그 저장 파일
├── python_analyzer/               # Python 시각화 디렉토리
│   ├── live_plot_cpu.py          # 실시간 시각화 (matplotlib)
│   ├── plot_cpu_usage.py         # 정적 분석용 시각화 (옵션)
│   └── venv/                     # Python 가상환경 (matplotlib 포함)
├── run_all.sh                     # 전체 자동 실행 스크립트
└── README.md                      # 프로젝트 설명서

## 🚀 실행 방법

### 1. 가상환경 준비

```bash
cd EdgeGuard
python3 -m venv python_analyzer/venv
source python_analyzer/venv/bin/activate
pip install matplotlib

## 🧩 전체 섹션에 이어 붙이면 이렇게 됩니다

```markdown
### 2. 전체 실행

```bash
./run_all.sh

