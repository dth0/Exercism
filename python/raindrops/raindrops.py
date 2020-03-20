def convert(number):
    factors = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }

    rval = []
    for factor, msg in factors.items():
        if (number % factor) == 0:
            rval.append(msg)

    return "".join(rval) or str(number)
