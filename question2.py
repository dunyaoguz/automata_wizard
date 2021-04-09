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
    rows = [[r.strip('->').strip('*') for r in row] for row in rows]

    return rows, alphabet, states, initial, final


def find_new_states(transitions, new_states):
    """ Recursively finds the new states generated during the nfa-to-dfa conversion"""
    # base case
    if not new_states:
        return transitions

    new = {}
    for k, v in transitions.items():
        if len(v) > 1:
            for letter in rows[0][1:]:
                r = []
                for _ in v:
                    if (_, letter) in transitions.keys():
                        r.extend(list(transitions[(_, letter)]))
                new[(str(v), letter)] = set(r)

    current_states = [k[0] for k in transitions.keys()]
    new_states = [v for v in new.values() if len(v) > 1
                  and str(v) not in current_states]
    return find_new_states(transitions | new, new_states)


def convert_nfa(rows):
    """ Converts the nfa in the transition table to a dfa """

    transitions = {}
    for row in rows[1:]:
        for i, cell in enumerate(row[1:]):
            key = (row[0], rows[0][i+1])
            for c in cell.split('|'):
                if c != '':
                    transitions.setdefault(key, set()).add(c)

    new_states = [v for v in transitions.values() if len(v) > 1]
    return find_new_states(transitions, new_states)


def create_output(alphabet, states, initial, final, transitions):
    """ Creates a transition table and diagram for the new dfa """

    # Q: How to determine the initial state of the new dfa?
    # Q: How to determine the final state of the new dfa?
    # Q: Is it ok to not include those additional rows in the table?

    nfa = {'alphabet': alphabet,
           'states': states,
           'accepting_states': final,
           'transitions': transitions}


if __name__ == '__main__':
    rows, alphabet, states, initial, final = read_nfa()
    transitions = convert_nfa(rows)
