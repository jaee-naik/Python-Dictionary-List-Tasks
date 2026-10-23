
# Task 3: Cricket Players
players = {
    "virat kholi": 100,
    "rohit sharma": 87,
    "shubnam gill": 76,
    "hardik pandya": 56,
    "abhishek sharma": 67,
    "shreyas iyer": 45,
    "kl rahul": 67,
    "jaspreet": 23,
    "vaishav suryavanshi": 44,
    "akshar patel": 12
}


# Task 4: IPL Player Statistics
ipl_players = {
    "virat kohli": {"runs": 650, "matches": 13},
    "rohit sharma": {"runs": 480, "matches": 14},
    "shubmsn gill": {"runs": 720, "matches": 14},
    "hardik pandey": {"runs": 290, "matches": 12}
}


# Cricket analysis function
def analyze_cricket():
    print("\n--- Cricket Analysis ---")

    print("Player scores:")
    for name, runs in players.items():
        print(name, ":", runs)

    print("\nIPL Player Statistics:")
    for name, details in ipl_players.items():
        print(name, ":", details)
