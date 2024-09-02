const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('resizeEvent', {
    resizeWindow: () => ipcRenderer.invoke('resize-window'),
})