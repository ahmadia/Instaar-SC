def get_data_column(header_line, file_delimiter, data_match_string):
    """ Given a header line and delimiter, find column in line that contains a match
    for the data string

    Assumes: data_match_string is not case-sensitive
    """
    fields = header_line.split(file_delimiter)
    matches = [data_match_string.lower() in field.lower() for field in fields]
    if sum(matches) < 1:
        raise ValueError("Unable to find a %s column in %s" % (
                         data_match_string, fields))
    elif sum(matches) > 1:
        raise ValueError("%s column is ambiguous in %s" % (
                         data_match_string, fields))
    return matches.index(True)

def test_get_data_column_end():
    assert 2 == get_data_column('Apples, Bananas, Cheerios', ',', 'Cheerios')

def test_get_data_column_beg():
    assert 0 == get_data_column('Apples, Bananas, Cheerios', ',', 'Apples')


