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

nfa = {
  "alphabet": {"5c", "10c", "gum"},
  "states": {"s0", "s1", "s2", "s3", "s4"},
  "initial_states": {"s0"},
  "accepting_states": {"s0", "s2"},
  "transitions": {
    ("s0", "5c"): {"s1, s4"},
    ("s0", "10c"): {"s4"},
    ("s1", "5c"): {"s2", "s3", "s1"},
    ("s1", "10c"): {"s3"},
    ("s2", "5c"): {"s3"},
    ("s2", "10c"): {"s3"},
    ("s4", "5c"): {"s3"},
    ("s4", "10c"): {"s3"},
    ("s3", "gum"): {"s0"}
  }
}
