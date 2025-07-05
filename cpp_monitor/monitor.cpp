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

double get_memory_usage() {
    std::ifstream mem_file("/proc/meminfo");
    std::string line;
    long mem_total = 0, mem_available = 0;

    while (std::getline(mem_file, line)) {
        if (line.find("MemTotal:") == 0) {
            sscanf(line.c_str(), "MemTotal: %ld kB", &mem_total);
        } else if (line.find("MemAvailable:") == 0) {
            sscanf(line.c_str(), "MemAvailable: %ld kB", &mem_available);
            break;
        }
    }

    mem_file.close();

    if (mem_total == 0) return 0.0;

    long mem_used = mem_total - mem_available;
    return (double)mem_used / mem_total * 100.0;
}

int main() {
    for (int i = 0; i < 10; ++i) {
        double cpu_usage = get_cpu_usage();
        double mem_usage = get_memory_usage();

        std::ofstream out("/Users/apple/EdgeGuard/logs/data.txt", std::ios::app);
        out << "CPU Usage: " << cpu_usage << "%, "
            << "Memory Usage: " << mem_usage << "%" << std::endl;
        out.close();

        std::cout << "Saved: CPU " << cpu_usage << "%, Memory " << mem_usage << "%" << std::endl;
        sleep(5); // 5초 대기
    }

    return 0;
}
