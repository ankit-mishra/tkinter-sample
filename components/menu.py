#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox

class MainMenu:
    """主界面菜单"""

    def __init__(self, master):
        """初始化菜单"""
        self.master = master # 上级
        self.root = master.root # 主窗口
        self.init_menu()

    def init_menu(self):
        """加载菜单"""

        # 创建菜单栏
        self.menubar = Menu(self.root)

        # 将菜单栏添加到窗口
        self.root.config(menu=self.menubar)

        # 文件下拉菜单
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.file_new)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_command(label="Save as", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.root.quit)

        # 用户下拉菜单
        usermenu = Menu(self.menubar, tearoff=0)
        usermenu.add_command(label="List of Users", command=self.master.open_user_list)
        usermenu.add_command(label="User Added", command=self.master.open_user_add)
        usermenu.add_command(label="User Details", command=self.master.open_user_info)

        # 文章下拉菜单
        articlemenu = Menu(self.menubar, tearoff=0)
        articlemenu.add_command(label="Article Query", command=self.master.open_content_list)
        articlemenu.add_command(label="Article Added", command=self.master.open_content_add)
        articlemenu.add_command(label="Article Statistics", command=self.master.open_content_count)

        # 数据下拉菜单
        datamenu = Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="Download", command=self.master.open_download)
        datamenu.add_command(label="Upload", command=self.master.open_upload)
        datamenu.add_command(label="Synchronize", command=self.master.open_synchronize)
        datamenu.add_command(label="Backup", command=self.master.open_backup)

        # 窗口下拉菜单
        window_menu = Menu(self.menubar)
        window_menu.add_command(label="Maximize")
        window_menu.add_command(label="Minimize")
        window_menu.add_separator()
        window_menu.add_command(label="Window To Top", command=self.master.window_to_top)
        window_menu.add_command(label="Window Not Top", command=self.master.window_not_top)
        window_menu.add_separator()
        window_menu.add_command(label="Home", command=self.master.open_home)
        window_menu.add_command(label="Switch to : User")
        window_menu.add_command(label="Switch to : Article List")

        # 帮助下拉菜单
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="欢迎使用", command=self.help_about)
        helpmenu.add_command(label="文档", command=self.help_about)
        helpmenu.add_command(label="版权声明", command=self.help_about)
        helpmenu.add_command(label="隐私声明", command=self.help_about)
        helpmenu.add_separator()
        helpmenu.add_command(label="联系我们", command=self.master.open_ontact)
        helpmenu.add_command(label="关于", command=self.master.open_about)

        # 将下拉菜单加到菜单栏
        self.menubar.add_cascade(label="文件", menu=filemenu)
        self.menubar.add_cascade(label="用户", menu=usermenu)
        self.menubar.add_cascade(label="文章", menu=articlemenu)
        self.menubar.add_cascade(label="数据", menu=datamenu)
        self.menubar.add_cascade(label="窗口", menu=window_menu)
        self.menubar.add_cascade(label="帮助", menu=helpmenu)

    def file_open(self):
        messagebox.showinfo("打开", "文件-打开！")  # 消息提示框

    def file_new(self):
        messagebox.showinfo("新建", "文件-新建！")  # 消息提示框

    def file_save(self):
        messagebox.showinfo("保存", "文件-保存！")  # 消息提示框

    def edit_cut(self):
        messagebox.showinfo("剪切", "编辑-剪切！")  # 消息提示框

    def edit_copy(self):
        messagebox.showinfo("复制", "编辑-复制！")  # 消息提示框

    def edit_paste(self):
        messagebox.showinfo("粘贴", "编辑-粘贴！")  # 消息提示框

    def help_about(self):
        """关于"""
        messagebox.showinfo(
            "关于", "作者: doudoudzj \n verion 1.0 \n 感谢您的使用！ \n doudoudzj@sina.com"
        )
