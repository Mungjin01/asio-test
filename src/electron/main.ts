const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const asioAddon = require("./build/Release/asioaddon.node"); // 네이티브 모듈 가져오기

let mainWindow;

app.on("ready", () => {
  mainWindow = new BrowserWindow({
    webPreferences: {
      preload: path.join(__dirname, "preload.js"), // preload 스크립트 로드
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  mainWindow.loadURL("http://localhost:3000"); // React 앱 로드

  ipcMain.on("start-asio", () => {
    asioAddon.startAsioStream(); // ASIO 스트림 시작
  });
});
