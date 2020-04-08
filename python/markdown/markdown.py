import re


def parse_header(line):

    header = re.match(r"^(#+)", line)
    if header:
        text = line[header.end():].strip()
        h_size = len(header.group())

        return f"<h{h_size}>{text}</h{h_size}>"
    else:
        return ""


def parse_bold_and_italic(line):

    tag = {
        2: "strong",
        1: "em"
    }

    for n in sorted(tag.keys(), reverse=True):
        m = re.match(f"(.*)_{{{n}}}(.*)_{{{n}}}(.*)", line)
        if m:
            line = f"{m.group(1)}<{tag[n]}>{m.group(2)}</{tag[n]}>{m.group(3)}"

    return line


def parse(markdown):
    res = []
    list_data = []
    for line in markdown.splitlines():

        header = parse_header(line)
        if header:
            res.append(header)
            continue

        m = re.match(r'\* (.*)', line)
        if m:
            text = parse_bold_and_italic(m.group(1))
            list_data.append(f"<li>{text}</li>")
            continue

        if list_data:
            res.append(f"<ul>{''.join(list_data)}</ul>")
            list_data = []

        line = parse_bold_and_italic(line)
        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = f"<p>{line}</p>"

        res.append(line)
    else:
        if list_data:
            res.append(f"<ul>{''.join(list_data)}</ul>")
            list_data = []

    return "".join(res)
