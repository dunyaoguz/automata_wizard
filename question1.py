from PySimpleAutomata import automata_IO


def get_user_input():
    """ Welcomes user to the program and obtain the necessary inputs """

    print('\nWelcome, human. (￣(oo)￣)ﾉ')
    print('Answer these questions to create a pretty transition diagram.')
    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')

    # converts a given user input into a set
    def converter(x): return set([s.strip() for s in x.split(',')])

    type = input('Do you want to create a diagram for a dfa or an nfa? ')
    states = converter(input('Enter the states of your automaton: '))

    initial = converter(input('Specify the initial state(s): '))
    while len([i for i in initial if i not in states]) > 0:
        print('\nERROR: State not found. Try again. ¯\\_(ツ)_/¯\n')
        initial = converter(input('Specify the initial state(s): '))

    while type == 'dfa' and len(initial) != 1:
        print('\nERROR: Only one initial state can be entered for a dfa. Try again. >_>\n')
        initial = converter(input('Specify the initial state(s): '))

    final = converter(input('Specify the final state(s): '))
    while len([f for f in final if f not in states]) > 0:
        print('\nERROR: State not found. Try again. ¯\\_(ツ)_/¯\n')
        final = converter(input('Specify the final state(s): '))

    alphabet = converter(input('Enter the alphabet of your automaton: '))
    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')

    with open('table1.csv', 'w') as file:
        file.writelines('𝛿,' + ','.join(alphabet) + '\n')
        for s in states:
            file.writelines(s + '\n')

    print('Now, open the file called table1.csv and fill in the transition table.')
    print('For nfas, separate multiple states with the `|` character.')
    is_complete = False
    while not is_complete:
        is_complete = input('When you\'re done, hit any key + enter to continue: ')
    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')

    return type, states, initial, alphabet, final


def read_transitions(type, states):
    """ Reads the transition table filled by the user """

    print('Reading transitions...')
    with open('table1.csv', 'r') as file:
        lines = file.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip('\n').split(','))

    transitions = {}
    if type == 'dfa':
        for row in rows[1:]:
            for i, cell in enumerate(row[1:]):
                if cell != '':
                    try:
                        transitions[(row[0], rows[0][i+1])] = cell
                        if cell not in states:
                            print(f'Detected unknown state {cell}. ಠ_ಠ')
                    except IndexError:
                        print('\nFATAL ERROR: You gave multiple states for a dfa. (¬_¬)')
                        print('Exiting. ╚(ಠ_ಠ)=┐\n')
                        raise SystemExit
    else:
        for row in rows[1:]:
            for i, cell in enumerate(row[1:]):
                key = (row[0], rows[0][i+1])
                for c in cell.split('|'):
                    if c != '':
                        transitions.setdefault(key, set()).add(c)
                        if c not in states:
                            print(f'Detected unknown state {c}. ಠ_ಠ')
    print('Done!')
    return transitions


def create_graph(type, states, initial, alphabet, final, transitions):
    """ Creates an svg file displaying the transition diagram """

    automata = {'alphabet': alphabet,
                'states': states,
                'accepting_states': final,
                'transitions': transitions}

    if type == 'dfa':
        automata['initial_state'] = ''.join(initial)
        automata_IO.dfa_to_dot(automata, 'graph.png')
    else:
        automata['initial_states'] = initial
        automata_IO.nfa_to_dot(automata, 'graph.png')

    print('\nYour transition diagram is created! ~(˘▾˘~)')
    print('Check it out in the file called graph.png.\n')


if __name__ == '__main__':
    type, states, initial, alphabet, final = get_user_input()
    transitions = read_transitions(type, states)
    create_graph(type, states, initial, alphabet, final, transitions)
