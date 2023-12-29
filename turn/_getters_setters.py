from turn.exception import InvalidNumberOfDice, InvalidDieValue
@property
def current_role(self):
    return self.__current_role


@current_role.setter
def current_role(self, value):
    '''makes unit testing easier'''
    if len(value) <= 0 or len(value) > 6:
        raise InvalidNumberOfDice("Failed to set roll either too many (>6) or too few (0) ")
    for x in value:
        if x <= 0 or x >= 7:
            raise InvalidDieValue
    self.__current_role = sorted(value)


@property
def scoring_opportunities(self):
    return self.__scoring_opportunities


@scoring_opportunities.setter
def scoring_opportunities(self, args):
    '''used for testing only '''
    key, value = args
    self.__scoring_opportunities[key] = value