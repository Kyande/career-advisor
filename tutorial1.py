from pyknow import *


class MyFact(Fact):
    pass


@Rule(MyFact())
def match_with_every_myfact():
    pass


@Rule(Fact('animal', family='felinae'))
def match_with_cats():
    """
        Match with every `Fact` which:

          * f[0] == 'animal'
          * f['family'] == 'felinae'

        """
    print("Meow!")