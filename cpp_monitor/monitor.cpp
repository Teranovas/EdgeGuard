#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>

double get_cpu_usage() {
    std::ifstream stat_file("/proc/stat");
    std::string cpu;
    long user, nice, system, idle;
    stat_file >> cpu >> user >> nice >> system >> idle;
    stat_file.close();

    long total = user + nice + system + idle;
    long usage = user + nice + system;
    return (double)usage / total * 100.0;
}

int main() {
    for (int i = 0; i < 10; ++i) {  // 10번 반복 (원하면 while(true)로 바꿀 수도 있음)
        double usage = get_cpu_usage();

        std::ofstream out("../../logs/data.txt", std::ios::app); // 기존 내용 뒤에 추가
        out << "CPU Usage: " << usage << "%" << std::endl;
        out.close();

        std::cout << "Saved CPU usage: " << usage << "%" << std::endl;
        sleep(5); // 5초 대기
    }

    return 0;
}
