from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import *
import time

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.urlChanged.connect(self.handle_url_changed)
        self.page().quotaRequested.connect(lambda request: request.accept())
        self.page().setInspectedPage(QWebEnginePage(self))
        
    def handle_url_changed(self, url):
        changed_url = url.toString()
        if changed_url == "https://app.mirada.ai" or changed_url == "https://app.mirada.ai/home":
            time.sleep(5)
            self.get_local_storage_value('userID')

    def get_local_storage_value(self, key):
        script = f"""
        (function() {{
            windows.localStorage.getItem('{key}');
        }})();
        """
        print("localStorage==========>", self.page().profile().persistentStoragePath())
        print("localStorage==========>", self.page().runJavaScript(script))
        return self.page().runJavaScript(script)

