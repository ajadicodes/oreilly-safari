import os

import pandas as pd


def _format_string(s):
    """
    Converts string to lowercase and replace space
    in between sentenses with '_'.
    """
    return s.lower().replace(' ', '_')


def read_csv(filepath):
    """
    Read a comma-separated values (csv) file into Highlights

    Raises:
        FileNotFoundError: if filepath does not exist.

    Returns:
        DataFrame -- A comma-separated values (csv) file is returned as
        two-dimensional data structure with labeled axes.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'"{filepath}" does not exist.')

    df = pd.read_csv(filepath)
    columns = map(_format_string, df.columns)
    df.columns = list(columns)

    # format authors column
    author_series = df['authors'].apply(_format_string)
    df['authors'] = author_series

    # format book_title column
    book_title_series = df['book_title'].apply(_format_string)
    df['book_title'] = book_title_series

    return Highlights(df)


class Highlights(object):

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    @property
    def nrows(self):
        return self.data.shape[0]

    @property
    def ncols(self):
        return self.data.shape[1]

    def where_author(self, author):
        """
        Given a dataframe, return rows that match a given author.

        Returns:
            DataFrame -- A comma-separated values (csv) file is returned as
            two-dimensional data structure with labeled axes.
        """
        df = self.data.query(f'authors == "{author}"')
        df = df.iloc[::-1]
        return Highlights(df)

    def where_book_title(self, book_title):
        """
        Given a dataframe, return reversed rows that match a given book title.

        Returns:
            DataFrame -- A comma-separated values (csv) file is returned as
            two-dimensional data structure with labeled axes.
        """
        df = self.data.query(f'book_title == "{book_title}"')
        df = df.iloc[::-1]
        return Highlights(df)

    def to_txt(self, filepath):
        last_chapter_title = ''

        with open(filepath, 'w') as f:
            f.write(self.data['book_title'].iloc[0] + '\n')
            for chpt_title, h_light, p_note in zip(self.data['chapter_title'],
                                                   self.data['highlight'],
                                                   self.data['personal_note']):
                if chpt_title != last_chapter_title:
                    f.write('\n')
                    f.write(chpt_title + '\n')
                    last_chapter_title = chpt_title
                f.write('\n')
                f.write(h_light + '\n')

                if isinstance(p_note, str):
                    f.write('\n')
                    f.write(f'Note: {p_note} + \n')

                f.write('\n')
