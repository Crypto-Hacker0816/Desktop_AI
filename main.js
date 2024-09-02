const { app, BrowserWindow, Tray, Menu, screen, ipcMain } = require('electron')
const path = require('node:path')


const createWindow = () => {
    const primaryDisplay = screen.getPrimaryDisplay()
    const { width, height } = primaryDisplay.workAreaSize
    const win = new BrowserWindow({
      width: 570,
      height: 800,
      x : width - 540,
      y : 0,
      frame : false,
      skipTaskbar : false,
      transparent : true,
      webPreferences : {
        preload : path.join(__dirname, 'preload.js')
      },
      icon : path.join(__dirname, 'head.png')
    })

    
    ipcMain.handle('resize-window', function() {  
        win.loadFile('pages/fullscreen.html')      
        win.setSize(width, height)
        win.setPosition(0, 0)
        
    })

    win.loadFile('pages/index.html')

    win.on('minimize', (event) => {
        event.preventDefault();
        win.minimize();
    });
}



app.whenReady().then(() => {
    appIcon = new Tray('resources/tray.png')
    const contextMenu = Menu.buildFromTemplate([
        { 
            label: 'Open', 
            type: 'normal',
            click : createWindow
         },
        { 
            label: 'Exit', 
            type: 'normal',
            click: () =>  app.exit()
        }
    ])

    contextMenu.items[1].checked = false
    appIcon.setContextMenu(contextMenu)  
})


