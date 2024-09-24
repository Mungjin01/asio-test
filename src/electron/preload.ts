const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electron", {
  startAsio: () => ipcRenderer.send("start-asio"),
});
