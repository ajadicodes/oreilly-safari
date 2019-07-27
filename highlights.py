import os

import pandas as pd


def load_csv(filepath):
    """
    Reads a CSV file, formats column names, authors and book titles columns.

    Raises:
        FileNotFoundError: if filepath does not exist.

    Returns:
        DataFrame -- A comma-separated values (csv) file is returned as
        two-dimensional data structure with labeled axes.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'"{filepath}" not found.')
    df = pd.read_csv(filepath)
    columns = map(format_string, df.columns)
    df.columns = list(columns)

    # format authors column
    author_series = df['authors'].apply(format_string)
    df['authors'] = author_series

    # format book_title column
    book_title_series = df['book_title'].apply(format_string)
    df['book_title'] = book_title_series

    return df


def where_author(dataframe, author):
    """
    Given a dataframe, return rows that match a given author.

    Returns:
        DataFrame -- A comma-separated values (csv) file is returned as
        two-dimensional data structure with labeled axes.
    """
    return dataframe.query(f'authors == "{author}"')


def where_book_title(dataframe, book_title):
    """
    Given a dataframe, return reversed rows that match a given book title.

    Returns:
        DataFrame -- A comma-separated values (csv) file is returned as
        two-dimensional data structure with labeled axes.
    """
    df = dataframe.query(f'book_title == "{book_title}"')
    df = df.iloc[::-1]
    return df


def format_string(s):
    """
    Converts string to lowercase and replace space
    in between sentenses with '_'.
    """
    return s.lower().replace(' ', '_')


def write_highlights_to_file(filepath, dataframe):
    last_chapter_title = ''

    with open(filepath, 'w') as f:
        f.write(dataframe['book_title'].iloc[0] + '\n')
        for chpt_title, highlight, p_note in zip(dataframe['chapter_title'],
                                                 dataframe['highlight'],
                                                 dataframe['personal_note']):
            if chpt_title != last_chapter_title:
                f.write('\n')
                f.write(chpt_title + '\n')
                last_chapter_title = chpt_title
            f.write('\n')
            f.write(highlight + '\n')

            if isinstance(p_note, str):
                f.write('\n')
                f.write(f'Note: {p_note} + \n')

            f.write('\n')
