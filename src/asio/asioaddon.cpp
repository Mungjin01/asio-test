#include "asio_driver.h"
#include <iostream> 

bool asioRunning = false;


void StartASIO() {
    if (asioRunning) {
        std::cout << "ASIO already running." << std::endl;
        return;
    }

    // 여기서 ASIO 드라이버를 초기화 & 스트림 시작
    std::cout << "Initializing ASIO driver..." << std::endl;

    // ASIO 드라이버가 성공적으로 시작되면 asioRunning을 true로 설정
    asioRunning = true;
    std::cout << "ASIO driver started successfully." << std::endl;
}

// ASIO 드라이버 정지 함수 
void StopASIO() {
    if (!asioRunning) {
        std::cout << "ASIO is not running." << std::endl;
        return;
    }

    // 여기서 실제 ASIO 드라이버를 종료 & 자원 해제
    std::cout << "Stopping ASIO driver..." << std::endl;

    // ASIO 드라이버가 성공적으로 종료되면 asioRunning을 false로 설정
    asioRunning = false;
    std::cout << "ASIO driver stopped successfully." << std::endl;
}

// ASIO 드라이버가 실행 중인지 확인하는 함수 
bool IsASIORunning() {
    return asioRunning;
}
