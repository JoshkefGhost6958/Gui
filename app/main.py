from tkinter import *
import shutil  # offers high level operations on files
import os
import easygui
from tkinter import filedialog  # folder selection lib
from tkinter import messagebox as mb
import time
from sys import exit
# imageio

# open filebox window to select file


def open_window():
    read = easygui.fileopenbox()
    return read

# open file


def open_file():
    string = open_window()
    if string is None:
        mb.showinfo("Error", "No file was selected")
    elif (os.path.isfile):
        try:
            os.open(string, os.O_RDWR)
        finally:
            os.close(string)
    else:
        mb.showinfo('confirmation', "File was not found!!")


def copy_file():
    source = open_window()
    if (source is None):
        exit()
    try:
        destination = filedialog.askdirectory()
        shutil.copy(source, destination)
        mb.showinfo("Confirmation", "File was copied succesfully")
    except:
        mb.showinfo("ERROR", "An error occured while coppying file")


def delete_file():
    targ_file = open_window()
    if targ_file is None:
        exit()
    else:
        if os.path.exists(targ_file):
            os.remove(targ_file)
            path = []
            path = targ_file.split("/")
            mb.showinfo("confirmation", f"{path[-1]} has been deleted")
        else:
            mb.showinfo("", "File does not exist")


def rename_file():
    chosen_file = open_window()
    prev_path = os.path.dirname(chosen_file)

    # Gets the extension of the file

    extension = os.path.splitext(chosen_file)[1]
    newName = input("Enter the name for chosen file: ")
    path = os.join(prev_path, newName+extension)
    os.rename(chosen_file, path)
    mb.showinfo("", "File Renamed")


def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if (source == destination):
        mb.showerror("", "source and destination are the same")
    else:
        shutil.move(source, destination)
        mb.showinfo("", "File moved!")


def make_folder():
    folder_path = filedialog.askdirectory()
    folder = input("Enter name of folder")
    path = os.join(folder_path, folder)
    os.mkdir(path)
    mb.showinfo("", "Folder Created")


def delete_folder():
    delFolder = filedialog.askdirectory()
    print(delFolder)

    try:
        if os.removedirs(delFolder):
            exit("file deleted succesfully")
        else:
            mb.showwarning("", "you are trying to delete a populated folder")
            shutil.rmtree(delFolder, ignore_errors=True)
            # fails on read only files,pass in an extra parameter
            mb.showinfo("", "File deleteted succesfully")
    except NotADirectoryError:
        print("specified path is not a directory")

    except PermissionError:
        print("permission denied")

    except OSError as e:
        print("Directory cannot be removed", e)

    finally:
        if os.path.isdir(delFolder) is True:
            mb.showinfo("", "Folder was not deleted")


def list_files():
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))
    print("File in folder list are: ")
    val = len(sort_list)
    i = 0
    while (i < int(val)):
        print(sort_list[i] + '\n')
        i += 1
