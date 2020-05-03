#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter, os, shutil

from tkinter import messagebox

from tkinter import *

class My_Cleaning_Program:
    
    def __init__(self, parent):

        self.main_frame = parent 
        self.main_frame = Frame(parent) ###
        self.main_frame.pack(
        padx = '5m',
        pady = '5m')

        def make_message(name, parent, caption, form, row_num, col_num, **options):
            
            name = Message(parent, text = caption, relief = form, **options)
            name.grid(row = row_num, column = col_num)
       
        ## Messages that go in the Main Frame ##
        
        #title of program#
        make_message('title', self.main_frame, "Tomato's going to clean this PC up", 'ridge', 2, 1, borderwidth = '2m',
                    aspect = 900, padx = '5m', pady= '1m')

        #program explanation#
        make_message('about', self.main_frame, 'The program so far:\n\n    In the beginning computers were created.'+
                     'This has made a lot of people very angry and been widley regarded as a bad move.\n'+
                     '\n    T-omato\'s PC cleaner intends on cleaning these buggers up with a swift hit on the Return Key,'+
                     'or even by hitting the left mouse button. \n Firstly, you\'ll want to type in your main directory'+
                     ' which usualy looks like \'Users/\'name\'. This will display the subfolders and the loosefiles in there.\n'+
                     ' You\'ll be able to choose to "Remove" or "Move" files and say you\'re not particularly happy with the'+
                     ' directory you\'ve chosen, simply type "b" to return\n to the options.'+
                     ' This is a prototype and as such there are a few bugs:\n \na) When moving files, if a file with the same name'+
                     ' exists in the specified directory, it will not be moved.\n \nb) After moving or deleting a file'+
                     ' it will persist in the list adjacent to where you first typed your main directory. Be careful not to '+
                     'delete a moved file,\n    by clicking on the file in this list while in "Delete" mode.\n'+
                     '\nSo long, and thanks for all of the bytes', 'flat', 3, 1, aspect = 600, pady = '5m')
        
        ## Frames that will be used in this program ##
        
        #Entry frame
        self.entry_frame = Frame(self.main_frame, padx = '2m')
        self.entry_frame.grid(row = 4, column = 0)
        
        
        #Listbox frame
        self.listbox_frame = Frame(self.main_frame, padx = '1m')
        self.listbox_frame.grid(row = 4, column = 1)
        
        self.deleted_listbox_frame = Frame(self.main_frame, padx = '1m')
        self.deleted_listbox_frame.grid(row = 3, column = 0)
        
        #button constants
        button_width = 10
        button_padx = '2m'
        button_pady = '1m'
         
        ## This program is read "Bottom-up", starting from: Main_directory_navigation() ##
        
        def remove_file(directory_location, listbox, yesOrno_entry):
            #this function a priori will create another listbox where items that are double clicked in the first listbox
            #will be transported to. Afterwards, the users may choose to cancel his Deletion plans, or continue and press
            #Delete. If the User deletes the selected files, then a listbox will appear that shows the deleted files. 
            using_remove_buttons = Message(self.entry_frame, relief = 'flat', aspect = 1200)
            using_remove_buttons.configure(text = 'Press cancel to clean the list and return to'+
                                                              'option selection. Press "Delete" to permenantly delete'+
                                                              'files in the list')
            using_remove_buttons.grid(row = 6, columnspan = 2)
                                
            # Cancel Button #                   
            cancel_remove = Button(self.entry_frame)
            cancel_remove.configure(text = 'Cancel', width = button_width, padx = button_padx,
                                    pady= button_pady)
            cancel_remove.grid(row = 7, column = 0)
                                
            def cancel_remove_button(event):
                yesOrno_entry.configure(state = 'normal')
                using_remove_buttons.grid_remove()
                cancel_remove.grid_remove()
                delete_remove.grid_remove()
                listbox_loosefile.grid_remove()
                scrollbar2.grid_remove()
                                    
            cancel_remove.bind('<Button-1>', cancel_remove_button)
                                
            # End of Cancel Button definitions #
            
            # Delete Button #
            
            delete_remove = Button(self.entry_frame)
            delete_remove.configure(text = 'Delete', width = button_width, padx = button_padx,
                                    pady = button_pady)
            delete_remove.grid(row = 7, column = 1)
                                
            def delete_remove_button(event):
                                   
                listbox.configure(state = 'disabled')
                listbox_loosefile.configure(state = 'disabled')
                
                #works on listbox_loosefile to move files from listbox and then shows deleted
                #files in deleted_files listbox.
                
                def select_all():
                                        
                    listbox_loosefile.select_set(0, END)
                    
                    #deleted_files listbox + Scrollbar
                    scrollbar3 = Scrollbar(self.deleted_listbox_frame, orient = 'vertical')
                    deleted_files = Listbox(self.deleted_listbox_frame, yscrollcommand = scrollbar3.set)
                    scrollbar3.config(command = deleted_files.yview)
                    scrollbar3.grid(row = 2, column = 0, sticky = 'NS')
                    deleted_files.configure(width = 30, height = 8)
                    deleted_files.grid(row = 2, column = 1, pady = '2m')
                    
                    delete_message = Message(self.deleted_listbox_frame, text = 'These files have been deleted', aspect = 800)
                    delete_message.grid(row = 1, columnspan = 2, pady = '3m')
                    #End of deleted_files parametrs
                    
                    #Inserts files to deleted_files listbox and deletes files while also cleaning loose_file listbox.
                    for items in listbox_loosefile.get(0, END):
                        deleted_files.insert(0, items)
                                        
                    for item in listbox_loosefile.get(0, END):
                        if os.path.exists(directory_location + item):
                            os.remove(directory_location + item)
                                        
                    listbox_loosefile.delete(0, END)
                    #End of select_all()
                
                #After clicking 'delete' this pop-up will make sure that the user is sure of deleting the files
                self.make_sure = Toplevel(parent)
                self.make_sure.wm_title('Delete these files?')
                pop_up_label = Label(self.make_sure, text = 'This will delete the files permenantly')
                pop_up_label.grid(row = 0, columnspan = 2)
                                    
                pop_up_button = Button(self.make_sure, text = "DON'T PANIC", foreground = 'red')
                pop_up_button2 = Button(self.make_sure, text = "CANCEL", foreground = 'green')
                                    
                pop_up_button.grid(row=1, column = 0)
                pop_up_button2.grid(row = 1, column = 1)
                
                #cancel button destroys pop_up and brings user back to main_frame
                def cancel_pop_up(event):
                    self.make_sure.destroy()
                    listbox.configure(state = 'normal')
                    listbox_loosefile.configure(state = 'normal')
                #End of cancel_pop_up()
                
                #dont_panic button will do what cancel button does but will execute select_all()
                def dont_panic(event):
                    self.make_sure.destroy()
                    listbox.configure(state = 'normal')
                    listbox_loosefile.configure(state = 'normal')
                    select_all()
                #end of dont_panic
                
                pop_up_button.bind('<Button-1>', dont_panic)    
                pop_up_button2.bind('<Button-1>', cancel_pop_up)
                
            delete_remove.bind('<Button-1>', delete_remove_button)   
            #End of Delete_button
            
            #Creates new listbox where items that are double-clicked in listbox will be seen in this listbox
            scrollbar2 = Scrollbar(self.listbox_frame, orient=VERTICAL)
            listbox_loosefile = Listbox(self.listbox_frame, yscrollcommand= scrollbar2.set)
            scrollbar2.config(command=listbox_loosefile.yview)
            scrollbar2.grid(row = 2, column = 1, sticky='NSW')
            listbox_loosefile.configure(width = 70)
            listbox_loosefile.grid(row = 2, column = 0, pady = '4m')
            
            #function for copying items in listbox to loose_file listbox
            def select_file(event):
                selection = listbox.curselection()
                selection_text = listbox.get(selection)
                listbox_loosefile.insert(END, selection_text)
                                
            listbox.bind('<Double-Button>', select_file)
            #End of listbox_frame parameters
        
        def move_file_to(directory_location, listbox, yesOrno_entry, no_answer):
            #Move file will move files to the selected directory (moving_entry) and if files are moved will create
            #a listbox on the top area of the main_frame showing moved items and where the were moved to.
            moving_label = Label(self.entry_frame, relief = 'flat')
            moving_label.configure(text = 'Move files inside main directory? (yes | no)')
            moving_label.grid(row = 6, column = 0)
                                
            move_var = StringVar()
            moving_entry = Entry(self.entry_frame, relief = 'flat', textvariable = move_var)
            moving_entry.grid(row = 6, column = 1)
            moving_entry_content = ''
            
            def main_function_for_moving():
                move_file = StringVar()
                moving_entry.configure(textvariable = move_file)
                move_file_content = ''
                                            
                def move_file_string(event):
                    move_file_content = move_file.get()
                    moving_entry.configure(state = 'disabled')
                                                
                    # Cancel Button #                   
                    cancel_remove = Button(self.entry_frame)
                    cancel_remove.configure(text = 'Cancel', width = button_width, padx = button_padx,
                                            pady= button_pady)
                    cancel_remove.grid(row = 7, column = 0)
                                
                    def cancel_remove_button(event):
                        yesOrno_entry.configure(state = 'normal')
                        moving_entry.grid_remove()
                        moving_label.grid_remove()
                        cancel_remove.grid_remove()
                        move_away.grid_remove()
                        listbox_loosefile.grid_remove()
                        scrollbar2.grid_remove()
                                    
                    cancel_remove.bind('<Button-1>', cancel_remove_button)
                                
                    # End of Cancel Button definitions #
            
                    # move button #
            
                    move_away = Button(self.entry_frame)
                    move_away.configure(text = 'Move', width = button_width, padx = button_padx,
                                        pady = button_pady)
                    move_away.grid(row = 7, column = 1)
                                
                    def move_away_button(event):
                                                    
                        if not os.path.exists(directory_location + move_file_content + '/'):
                            os.makedirs(directory_location + move_file_content + '/')
                                                   
                        #deleted_files listbox + Scrollbar
                        scrollbar4 = Scrollbar(self.deleted_listbox_frame, orient = 'vertical')
                        moved_files = Listbox(self.deleted_listbox_frame, yscrollcommand = scrollbar4.set)
                        scrollbar4.config(command = moved_files.yview)
                        scrollbar4.grid(row = 4, column = 0, sticky = 'NS')
                        moved_files.configure(width = 30, height = 8)
                        moved_files.grid(row = 4, column = 1, pady = '2m')
                
                        Moved_message = Message(self.deleted_listbox_frame, text = 'These files have been moved', aspect = 800)
                        Moved_message.grid(row = 3, columnspan = 2, pady = '1m')
                                                                       
                        for items in listbox_loosefile.get(0, END):
                            moved_files.insert(0, items)
                                                                       
                        for item in listbox_loosefile.get(0, END):
                            if os.path.exists(directory_location + move_file_content + '/' + item):
                                moved_files.insert(0, item + ' exists at location')
                            else:
                                shutil.move(directory_location + item, directory_location + move_file_content + '/')
                                                   
                        listbox_loosefile.delete(0, END)
                        #End of deleted_files parametrs
                                                    
                                            
                    move_away.bind('<Button-1>', move_away_button)
                                        
                    #Creates new listbox where items that are double-clicked in listbox will be seen in this listbox
                    scrollbar2 = Scrollbar(self.listbox_frame, orient=VERTICAL)
                    listbox_loosefile = Listbox(self.listbox_frame, yscrollcommand= scrollbar2.set)
                    scrollbar2.config(command=listbox_loosefile.yview)
                    scrollbar2.grid(row = 2, column = 1, sticky='NSW')
                    listbox_loosefile.configure(width = 70)
                    listbox_loosefile.grid(row = 2, column = 0, pady = '4m')
            
                    #function for copying items in listbox to loose_file listbox
                    def select_file(event):
                        selection = listbox.curselection()
                        selection_text = listbox.get(selection)
                        listbox_loosefile.insert(END, selection_text)
                                
                    listbox.bind('<Double-Button>', select_file)
    
                                            
                moving_entry.bind('<Return>', move_file_string)
                    
            
            def move_var_string(event):
                moving_entry_content = move_var.get().lower()
                move_answer = ['yes', 'y', 'no', 'n']
                if moving_entry_content not in move_answer:
                    no_answer.grid(row = 6, column = 0)
                else:
                    no_answer.grid_remove()
                    moving_entry.delete(0, END)
                                        
                    if moving_entry_content == "yes" or moving_entry_content == 'y':
                        moving_label.configure(text = "Write the file's destination")
                        
                        main_function_for_moving()
                        
                    else:
                        moving_label.configure(text = "write the new destination i.e. (Downloads/Mind-boggingly). Do not re-type the Main Directory")
                        
                        main_function_for_moving()
                        
            moving_entry.bind('<Return>', move_var_string)    
                              
        #After defining a main_directory, this function will be the program's battle-horse. It will esentially call on 
        #either of two functions: remove_file for deleting files or move_file for moving them. 
        def loose_file(directory_location, entry, directory_format, listbox):
                    
            what_to_do = Message(self.entry_frame, text = 'You can choose a new directory if you want', aspect = 800)
            #After accesing a main_directory succesfully the entry input is disabled to avoid accidents.
            entry.configure(state = 'disabled')
            #A new entry is created and asks if the user wants to do something with the files. If yes, the program
            #procedes. But the main reason for this step, is if the Users finds that he doesn't want to do anything
            #in the directory they chose, in which case the "main_directory" entry is enabled once again.
            yesOrno_label = Label(self.entry_frame, text = 'Would you like to do something with these files? (yes | no)', pady = '5m')
            yesOrno_label.grid(row = 5, column = 0)
            yesOrno_var = StringVar()
            yesOrno_entry = Entry(self.entry_frame, textvariable = yesOrno_var)
            yesOrno_entry.grid(row = 5, column = 1)
            yesOrno_content = ''
            
            no_answer = Message(self.entry_frame, text = 'Please answer "Yes/y" | "No/n"', aspect = 800)
            
            def yesOrno_string(event):
                yesOrno_content = yesOrno_var.get().lower()
                yesOrno_answer = ['yes', 'y', 'no', 'n']
                if yesOrno_content not in yesOrno_answer:
                    no_answer.grid(row = 6, column = 0)
                else:
                    no_answer.grid_remove()
                    #yesOrno_entry will be cleaned and recycled for further use
                    yesOrno_entry.delete(0, END)
                    
                    if yesOrno_content == "yes" or yesOrno_content == 'y':
                        
                        yesOrno_label.configure(text = 'Would you like to remove or move files? Answer "r" or "m" ')
                        
                        ans = ['r', 'm', 'b']
                        #The variables that catches the recycled yesOrno_entry is defined as remove (r)Or(m) move (rOrm) 
                        rOrm = StringVar()
                        yesOrno_entry.configure(textvariable = rOrm)
                        rOrm_content = ''
                        
                        rOrm_no_answer = Message(self.entry_frame)
                        
                        def rOrm_string(event):
                            rOrm_content = rOrm.get().lower()
                        
                            if rOrm_content not in ans:
                                rOrm_no_answer.configure(text = 'Anser Remove: "r" or Move: "m" or "b" to go back to main options ', aspect = 800)
                                rOrm_no_answer.grid(row = 6, column = 0)
                                
                            elif rOrm_content == 'b' or rOrm_content == 'back':
                                rOrm_no_answer.grid_remove()
                                #pretty straight forward, but if rOrm ==b then go back to main options so as to go back
                                #to the main_directory input
                                yesOrno_label.configure(text = 'Would you like to do something with these files? (yes | no)')
                                yesOrno_entry.configure(textvariable = yesOrno_var)
                                yesOrno_entry.bind('<Return>', yesOrno_string)
                                
                            
                            elif rOrm_content == 'r' or rOrm_content == 'remove':
                                rOrm_no_answer.grid_remove()
                                yesOrno_entry.configure(state = 'disabled')
                                #remove_file function takes in 3 arguments, the directory location, which is defined
                                #in main_directory_navigation as the main_directory entry input. the listbox that was
                                #created in main_directory_navigation, and the recycled yesOrno_entry
                                remove_file(directory_location, listbox, yesOrno_entry)
                            
                            else:
                                rOrm_no_answer.grid_remove()
                                yesOrno_entry.configure(state = 'disabled')
                                #as will be seen later, move_file is a modified remove_file and uses the same arguments 
                                #with an added argument "no_answer" which is a "global" message of loose_file() that will
                                #be recycled
                                move_file_to(directory_location, listbox, yesOrno_entry, no_answer)
                                
                        yesOrno_entry.bind('<Return>', rOrm_string)
                    
                    else:
                        entry.configure(state = 'normal')
                        yesOrno_entry.configure(state = 'disabled')
                        directory_format.grid_remove()
                        what_to_do.grid(row = 2, column = 0)
                        
                
            yesOrno_entry.bind('<Return>', yesOrno_string)
            
        ## The whole program is instantiated when this function is called.     
            
        def main_directory_navigation(parent, caption, form, row_num, col_num, **options):
            
            ## This label and Entry will are defined by the arguments given when function is called
            
            Label(parent, text = caption, relief = form, **options).grid(row = row_num, column = col_num)
            content = ''
            entry_string = StringVar()
            
            entry = Entry(parent, textvariable = entry_string, **options, state = 'normal')
            entry.grid(row = row_num, column = (col_num + 1))
            
            
            directory_format = Message(self.entry_frame, text = 'Directories on a Windows usually looks like: Users/name',
                                       relief = 'flat', pady = '1m', aspect = 1100)
            directory_format.grid(row = 1, column = 0)
            
            ## created two Messages as local variables in main_directory_navigation, but will be considered "global"
            ## when processed by "return_string" function.
            
            fail_message = Message(self.main_frame)        
            success_message = Message(self.listbox_frame)
            
            def return_string(event):
                ## We retrieve what the user has defined as their main_directory and pass it on as a string named
                ## actual_directory which will be evaluated by the os.path.exists from the os module.
                content = entry_string.get()
                actual_directory = 'C:/' + content + '/'
                
                #I call the listbox_frame that was created and give it its dimensions in the main_frame
                self.listbox_frame.grid()
                
                if not os.path.exists(actual_directory):
                
                    fail_message.configure(text="Almost, but not quite, entirely unlike a directory", relief = 'flat', aspect = 1000,
                                          pady = '1m') 
                    fail_message.grid(row = 4, columnspan = 2)
                    ## this line has to do with a "looping" effect, so if the user accidentally changes the directory
                    ## the listbox_frame created if os.path.exists == True (else statement) will be removed.
                    self.listbox_frame.grid_remove()
                    

                else:
                    fail_message.grid_remove()
                    success_message.configure(text = "This is what's going on here", relief = 'flat', aspect = 600)
                    success_message.grid(row = 0, column = 0)
                    
                    
                    scrollbar1 = Scrollbar(self.listbox_frame, orient=VERTICAL)
                    listbox = Listbox(self.listbox_frame, yscrollcommand= scrollbar1.set)
                    scrollbar1.config(command=listbox.yview)
                    scrollbar1.grid(row = 1, column = 1, sticky='NSW')
                    listbox.configure(width = 70)
                    listbox.grid(row = 1, column = 0)     
                    
                    #Create a scrollbar and Listbox where subfolders and filenames will be displayed
                    for foldername, subfolders, filenames in os.walk(actual_directory):
                        listbox.insert(END, 'These are the subfolders')
                        listbox.insert(END, '')
                        
                        for subfolder in subfolders:
                            listbox.insert(END, subfolder)
                        
                        listbox.insert(END, '')
                        listbox.insert(END, 'These are the loose files')
                        listbox.insert(END, '')
                        
                        for files in filenames:
                            listbox.insert(END, files)
                        break
                    #The next part of the program uses the function "loose_file" and takes in 4 arguments
                    # directory_location = actual_directory, the entry box for typing the main_directory,
                    # the message "directory_format" and the lastly created lisbox
                    loose_file(actual_directory, entry, directory_format, listbox)
                
            entry.bind('<Return>', return_string)
            
        main_directory_navigation(self.entry_frame, 'Insert Main Directory', 'flat', 3, 0, borderwidth = 3)
        
        

root = Tk()
myapp = My_Cleaning_Program(root)
root.mainloop()

