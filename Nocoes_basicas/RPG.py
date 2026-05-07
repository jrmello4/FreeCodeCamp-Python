full_dot = '●'
empty_dot = '○'

def create_character(name, strong, smart, carisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    
    if type(strong)!= int or type(smart) != int or type(carisma) != int:
        return 'All stats should be integers'
    if strong < 1 or smart < 1 or carisma < 1:
        return 'All stats should be no less than 1'
    if strong > 4 or smart > 4 or carisma > 4:
        return 'All stats should be no more than 4'
    if strong + smart + carisma != 7:
        return 'The character should start with 7 points'
    
    return f'{name}\nSTR {strong * full_dot + (10 - strong) * empty_dot}\nINT {smart * full_dot + (10 - smart) * empty_dot}\nCHA {carisma * full_dot + (10 - carisma) * empty_dot}'
