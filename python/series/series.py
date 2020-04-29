def slices(series, length):

    if len(series) < length or length < 1:
        raise ValueError("Input not allowed")

    return [
        series[i:i+length] for i in range(len(series)-(length-1))
    ]
