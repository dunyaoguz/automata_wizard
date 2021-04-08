from PySimpleAutomata import automata_IO

def read_nfa():
    """ Reads the transition table given by the user for an nfa """

    print('\nWelcome, human. (￣(oo)￣)ﾉ')
    print('Find the empty transition table inside the file called table2.csv.')
    print('Fill it in with the nfa that you want to convert to a dfa.')
    print('Append a `->` at the start of initial states and a `*` at the start of final states.')

    is_complete = False
    while not is_complete:
        is_complete = input('When you\'re done, hit any key + enter to continue: ')
    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')

    with open('table2.csv', 'r') as file:
        lines = file.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip('\n').split(','))

    # read the given csv to find the characteristics of the automata
    alphabet = rows[0][1:]
    states = [row[0] for row in rows[1:]]
    initial = [state.strip('->') for state in states if '->' in state]
    final = [state.strip('*') for state in states if '*' in state]
    states = [state.strip('->').strip('*') for state in states]

    return rows, alphabet, states, initial, final

def convert_nfa(nfa):
    """ Converts the nfa in the transition table to a dfa """

    return None

if __name__ == '__main__':
    rows, alphabet, states, initial, final = read_nfa()
