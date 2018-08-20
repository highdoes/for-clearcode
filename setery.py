'''

documentation

'''


class Grades():
    def __init__(self,score=0):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value > 100 or value < 0:
            raise ValueError("invalid")
        self._score = value


ocenka = Grades(50)
print(ocenka.score)


class Readonly():
    @property
    def constant(self):
        return 344