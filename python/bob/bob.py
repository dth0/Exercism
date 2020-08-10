def response(hey_bob):
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"

    upper = hey_bob.isupper()

    if hey_bob[-1] == "?":
        if upper:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif upper:
        return "Whoa, chill out!"
    else:
        return "Whatever."
