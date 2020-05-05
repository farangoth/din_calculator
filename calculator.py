#! /usr/bin/env python3

import gi

from data import Rider

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: E402


class Din_window(Gtk.Window):

    def on_main_window_destroy(self, *args):
        """Link the close button and the end of the Gtk process."""
        print("quit from button")
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem):
        print("Quit from the menu")
        Gtk.main_quit()

    def on_gtk_about_activate(self, menuitem):
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def on_button_yes_clicked(self, button):
        self.rider = Rider()
        self.din_set_label = self.builder.get_object("din_result")

        self.rider.weight = int(self.builder.get_object("weight").get_text())
        self.rider.height = int(self.builder.get_object("height").get_text())
        self.rider.level = int(self.builder.get_object("level").get_text())
        self.rider.age = int(self.builder.get_object("age").get_text())
        self.rider.sole_length = int(self.builder.get_object(
                                     "sole_length").get_text())

        self.rider.din_set = self.rider.get_din_set()

        print(self.rider)

        self.din_set_label.set_text(str(self.rider.din_set))

    def __init__(self):
        Gtk.Window.__init__(self, title="DIN Calc")
        self.gladefile = "din_calc.glade"
        self.builder = Gtk.Builder()

        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("main_window")
        self.aboutdialog = self.builder.get_object("aboutdialog")

        self.window.show()


if __name__ == "__main__":
    main = Din_window()
    Gtk.main()
