#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""关于窗口"""

from tkinter import Tk, Label, Message, Toplevel

# import lib.global_variable as glv
# from lib.functions import set_window_center


class Init(Tk):
    """
    """

    def __init__(self):
        Tk.__init__(self)
        self.title("")
        # set_window_center(self, 400, 400)
        self.app_name = "Python Tkinter Application" # glv.get_variable("APP_NAME")
        self.app_version = "0.1.1"
        self.app_desc = "Brief"
        self.app_url = "https://hsbc.com"
        self.app_ = "Copyright © 2022 Ankit Mishra. All rights reserved."
        self.init_page()

    def init_page(self):
        """
        """
        Label(self, text="LOGO").pack(fill="both")
        Label(self, text=self.app_name).pack()
        Label(self, text=self.app_version).pack()
        Label(self, text=self.app_url).pack()
        Label(self, text=self.app_).pack()
        Message(self, text=self.app_desc).pack()

if __name__ == "__main__":
    APP_ABOUT = Init()
    APP_ABOUT.mainloop()