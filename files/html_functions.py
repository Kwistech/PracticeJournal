def get_html_file(html_file):
    try:
        with open(html_file, "r") as f:
            f = f.readlines()
    except IOError:
        raise
    else:
        return f


def write_html(html_file, html_format, entries):
    try:
        file = open(html_file, "w")
    except IOError:
        raise

    key = int(entries[0]) + 1
    date = entries[1]
    practiced = entries[2]
    notes = entries[3]
    rating = entries[4]

    entry_str = """
            <tr>
                <td>{key}</td>
                <td>{date}</td>
                <td>{practiced}</td>
                <td>{notes}</td>
                <td>{rating}</td>
            </tr>\n"""
    entry_str = entry_str.format(key=key, date=date, practiced=practiced,
                                 notes=notes, rating=rating)
    html_format.insert(-3, entry_str)

    for line in html_format:
        file.writelines(line)

    file.close()
