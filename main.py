# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class A:

    def __init__(self ,arnold, anna):
        self.arnold = arnold
        self._anna = anna
        self.list = ["A", "B"]
        self.dict = {"A": 1}

    def get_arnold(self):
        return self.arnold

    def _get_anna(self):
        return self._anna

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = A("arnold", "anna")
    print(a.get_arnold())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
