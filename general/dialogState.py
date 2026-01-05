"""
Do we need to include Dialog from both the system and user?
"""


class DialogState:
    def __init__(self):
        self.history = [[]]

    def updateUser(self, result):
        self.history[-1] = result

    def getHistory(self):
        return self.history

    def newTurn(self):
        self.history.append([])
