from pyknow import *

@Rule(
    AND(
        OR(User('admin'),
           User('root')),
        NOT(Fact('drop-priviledges'))
    )
)
def the_user_has_powers():
    'user has powers'
    pass