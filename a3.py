from PySimpleAutomata import automata_IO
import pandas as pd

dfa = {
  "alphabet": {"5c", "10c", "gum"},
  "states": {"s0", "s1", "s2", "s3", "s4"},
  "initial_state": "s0",
  "accepting_states": {"s0", "s2"},
  "transitions": {
    ("s0", "5c"): "s1",
    ("s0", "10c"): "s4",
    ("s1", "5c"): "s2",
    ("s1", "10c"): "s3",
    ("s2", "5c"): "s3",
    ("s2", "10c"): "s3",
    ("s4", "5c"): "s3",
    ("s4", "10c"): "s3",
    ("s3", "gum"): "s0"
  }
}


def get_user_input():
    '''Welcome the user to the program and prompt for necessary inputs'''

    print('\nWelcome, human (￣(oo)￣)ﾉ')
    print('Answer these questions to create a pretty transition diagram')
    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')

    # generalized function that converts user input into set
    def converter(x): return set([s.strip() for s in x.split(',')])

    states = converter(input('Enter the states of your automaton: '))

    initial = input('Specify the initial state: ')
    while initial not in states:
        print('\nERR.. State not found ¯\\_(ツ)_/¯\n')
        initial = input('Specify the initial state: ')

    final = converter(input('Specify the final state(s): '))
    for f in final:
        if f not in states:
            print('\nERR.. State not found ¯\\_(ツ)_/¯\n')
            final = converter(input('Specify the final state(s): '))

    alphabet = converter(input('Enter the alphabet of your automaton: '))

    print('\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *\n')
    df = pd.DataFrame(columns=['𝛿'] + list(alphabet))
    df['𝛿'] = list(states)
    df.to_csv('t.csv', index=False)
    print('Now, open t.csv and fill in the transition table')

    is_complete = False
    while not is_complete:
        is_complete = input('Enter \'Y\' here when you\'re done: ')

    return states, initial, alphabet, final


def read_transitions():

    return transitions


if __name__ == '__main__':
    states, initial, alphabet, final = get_user_input()
    automata_IO.dfa_to_dot(dfa, 'graph.png')
