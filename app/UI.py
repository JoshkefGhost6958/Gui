from tkinter import *
from main import *


root = Tk()

canv = Canvas(root, width=500, height=420, bg='gray')


open_file_btn = Button(root, text="open file",
                       command=open_file, font=("Helvetica", 16), bg='gray')
open_file_btn.grid(row=1, column=2)


cp_btn = Button(root, text="Copy a File", command=copy_file)
cp_btn.grid(row=2, column=2)

del_file_btn = Button(root, text="Delete a File", command=delete_file)
del_file_btn.grid(row=3, column=2)

rename_btn = Button(root, text="Rename a File", command=rename_file)
rename_btn.grid(row=4, column=2)

mv_btn = Button(root, text="Move a File", command=move_file)
mv_btn.grid(row=5, column=2)

mkdir_btn = Button(root, text="Make a Folder", command=make_folder)
mkdir_btn.grid(row=6, column=2)

del_folder_btn = Button(root, text="Remove a Folder",
                        command=delete_folder)
del_folder_btn.grid(row=65, column=2)

all_files_btn = Button(root, text="List all Files in Directory",
                       command=list_files)
all_files_btn.grid(row=85, column=2)


root.mainloop()
