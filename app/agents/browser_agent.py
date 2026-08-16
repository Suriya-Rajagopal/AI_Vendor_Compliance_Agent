from app.tools.browser_tool import BrowserTool


class BrowserAgent:

    def __init__(self):

        self.browser = BrowserTool()

    def run(self, url):

        return self.browser.browse(url)