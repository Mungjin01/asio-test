// 전역 window 객체에 electron 속성을 추가
interface ElectronAPI {
  startAsio: () => void; // Electron의 startAsio 메소드 타입 정의
}

declare global {
  interface Window {
    electron: ElectronAPI;
  }
}

export {};
