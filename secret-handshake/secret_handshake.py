def commands(binary_str: str):
    '''
    binary_str is already 5 chars long, and always will be
    '''
    code = ['wink', 'double blink', 'close your eyes', 'jump']
    actions = []

    for i, do_action in enumerate(binary_str[::-1][:-1]):

        if int(do_action) :
            actions.append(code[i])
        

    return actions if not int(binary_str[0]) else actions[::-1]