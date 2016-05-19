# Practice Journal - by Johnathon Kwisses (Kwistech)
from os import path
from tkinter import *
import webbrowser
from files.sqlite3_functions import *
from files.html_functions import *


class App:
    """Represents the GUI and its function interaction.

    Only call this class once as it creates and displays the interface. """

    def __init__(self, conn):
        """Initialize all data to create interface.

        Args:
            conn (sqlite3.Connection): Connection to journal.db.
        """
        self.conn = conn
        self.ratings = list(range(1, 11))
        self.summary = self.get_summary()
        self.html_file = "./files/practice_journal.html"
        self.interface()

    def interface(self):
        """Create GUI (tkinter) for App.

        If you want to change some of the kwargs, just note that all tkinter
        objects (except frame) are set in a grid (row/column pairs).
        """
        frame = Frame()
        frame.pack()

        main_label = Label(frame, text="Welcome to Your Practice Journal")
        main_label.grid(row=0, columnspan=3, pady=5)

        sub_label = Label(frame, text=self.summary)
        sub_label.grid(row=2, rowspan=2, column=1, columnspan=2)

        copyright_label = Label(frame, text="© 2016 Kwistech")
        copyright_label.grid(row=4, column=1, columnspan=2, sticky="SE")

        p_label = Label(frame, text="What did you practice?")
        p_label.grid(row=1, column=0, padx=3, pady=3, sticky="W")

        n_label = Label(frame, text="Additional Notes:")
        n_label.grid(row=3, column=0, padx=3, pady=3, sticky="W")

        r_label = Label(frame, text="Rating for today:")
        r_label.grid(row=1, column=1)

        p_text = Text(frame, width=30, height=8)
        p_text.grid(row=2, column=0, padx=3, pady=3)

        n_text = Text(frame, width=30, height=8)
        n_text.grid(row=4, column=0, padx=3, pady=3)

        r_spinbox = Spinbox(frame, width=3, justify="center",
                            values=self.ratings)
        r_spinbox.grid(row=1, column=2)

        info = (p_text, n_text, r_spinbox)  # Retrieves all info from user

        o_button = Button(frame, text="Open", width=8, height=1,
                          command=lambda: self.open_html())
        o_button.grid(row=4, column=1, columnspan=2, pady=5, sticky="N")

        s_button = Button(frame, text="Submit", width=8, height=2,
                          command=lambda: self.get_info(info))
        s_button.grid(row=4, column=1, columnspan=2, pady=5)

    @staticmethod
    def get_summary():
        """Retrieve lines from summary.txt

        Returns:
            list: Contains lines from summary.txt.
        """
        with open("./files/summary.txt", "r") as f:
            f = f.readlines()
            f = ' '.join(f)
        return f

    def open_html(self):
        """Open html_file in web browser."""
        webbrowser.open(path.realpath(self.html_file))

    def get_info(self, info):
        """Clean info, send it to insert_db, get html_file, write entries.

        Gets user input from info, cleans it up, and sends it to insert_db.
        Retrieves lines in the self.html_file and gets all entries in
        database (journal.db). Finally, writes each entry to self.html_file.
        """
        p_text, n_text, r_spinbox = info

        p_text = p_text.get(1.0, 9.0)
        p_text = p_text.replace("\n", " ")
        n_text = n_text.get(1.0, 9.0)
        n_text = n_text.replace("\n", " ")
        r_spinbox = r_spinbox.get()

        key = get_key(self.conn)  # Number of entries in database

        insert_db(self.conn, key, p_text, n_text, r_spinbox)
        html_format = get_html_file(self.html_file)
        entries = get_db(self.conn, key)

        for entry in entries:
            write_html(self.html_file, html_format, entry)


def main():
    """Create connection to database and run main program loop."""
    root = Tk()
    root.title("Practice Journal")

    conn = create_conn()
    create_db(conn)

    App(conn)
    root.mainloop()

if __name__ == "__main__":
    main()
