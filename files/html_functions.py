def get_html_file(html_file):
    """Open html_file and get lines in file.

    Args:
        html_file (str): Path to html_file.

    Returns:
        list: Lines in html_file.

    Raises:
        IOError: html_file could not be opened and/or read; raise.
    """
    try:
        with open(html_file, "r") as f:
            f = f.readlines()
    except IOError:
        raise
    else:
        return f


def write_html(html_file, html_format, entries):
    """Write entries to html_file.

    Opens html_file to be written to, wiping all existing contents. This is
    good as the existing contents are saved in html_format before this
    function call.

    entry_str is a string literal which keeps its format when it is written
    to html_file.

    Args:
        html_file (str): Path to html_file.
        html_format (list): Lines in html_file before writing.
        entries (list): Entries in database table journal.

    Raises:
        IOError: html_file could not be opened; raise.
    """
    try:
        file = open(html_file, "w")
    except IOError:
        raise

    key = int(entries[0]) + 1  # Accounts for zero-based numbering
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
    html_format.insert(-3, entry_str)  # Inserts a table row in html table

    for line in html_format:
        file.writelines(line)

    file.close()
