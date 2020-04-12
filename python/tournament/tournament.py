def add_entry(name, result, storage):
    if name not in storage:
        storage[name] = {
            "matches": 0,
            "win": 0,
            "draw": 0,
            "loss": 0,
            "points": 0
        }

    storage[name]["matches"] += 1

    if result == "win":
        storage[name]["win"] += 1
        storage[name]["points"] += 3
    elif result == "draw":
        storage[name]["draw"] += 1
        storage[name]["points"] += 1
    else:
        storage[name]["loss"] += 1


def build_table(teams):
    res = []

    res.append("Team                           | MP |  W |  D |  L |  P")

    names = sorted([key for key in teams.keys()])

    for team in sorted(
        names, key=lambda k: teams[k]["points"], reverse=True
    ):

        matches = teams[team]["matches"]
        win = teams[team]["win"]
        draw = teams[team]["draw"]
        loss = teams[team]["loss"]
        points = teams[team]["points"]

        res.append(
            f"{team:31}|{matches:>3} |{win:>3} |{draw:>3} |{loss:>3} |{points:>3}"
        )

    return res


def tally(rows):

    tournament = {}
    for row in rows:

        team1, team2, result = row.split(";")

        if result == "win":
            add_entry(team1, "win", tournament)
            add_entry(team2, "loss", tournament)
        elif result == "loss":
            add_entry(team1, "loss", tournament)
            add_entry(team2, "win", tournament)
        else:
            add_entry(team1, "draw", tournament)
            add_entry(team2, "draw", tournament)

    return build_table(tournament)
