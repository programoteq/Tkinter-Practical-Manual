# -*- coding: utf8 -*-
'''
      ========== Tkinter Practical Manual, Python GUI Framework ==========

    Simple application illustrating how to build Python desktop graphical user
    interfaces with tkinter, tkinter.ttk and tkinter.messagebox.

    You will find here information about standard options and methods
    supported by tkinter widgets together with guidelines how to use them.
'''

import tkinter as tk
import tkinter.ttk as ttk  
import tkinter.messagebox


def main():
        
    root = tk.Tk()
    ''' Instance of the Tkinter main window class: Tk()'''

    Tkinter_GUI(root)
    Tkinter_ttw_GUI(root)

    root.mainloop()
    ''' This function calls the endless loop of the window, so the window will
     wait for any user event till it will be closed.
    '''

class Tkinter_GUI:

    def __init__(self, master):
        self.master = master

        window_width = 600
        half_screen_width = master.winfo_screenwidth()/2
        x_coordinate = half_screen_width - window_width/2
        '''
        half_screen_width = winfo_screenwidth()/2
        half_screen_height = winfo_screenheight()/2        

        '''
        master.geometry(f'{window_width}x710+{int(x_coordinate)}+50')
        '''
        window.geometry("width x height + XPOS + YPOS") in pixels
        '''

        master.resizable(0,1)
        '''
        .resizable(x,y) - If you want to restrict users from changing the
                        size of your screen in x and/or y direction you
                        should enter 0 in the suitable locations.
        .resizable(width=False, height=True) - same as above
        '''

##        master.config(bg='grey85')
##        ''' Background colour changed to show location of widgets '''

        self.img_icon = tk.PhotoImage(file="img/Other-python-icon-48.png")
        master.iconphoto(True, self.img_icon)


        # ----- Widgets section -----

        # Title
        master.title("Tkinter window .title")

        # Label
        self.label = tk.Label(master, text="Tkinter Practical Manual",
                           font=("Arial 12 bold italic"))                

        # Entry widget
        self.txt_entry = tk.Entry(master, width=30) 
        self.txt_entry.focus()
        ''' .focus() - set focus to entry widget '''

        # Button for Entry widget activation
        self.entry_button = tk.Button(master,
                                      text="Entry.Button",
                                      padx=20,
                                      command=self.entry_func)   
##  
        ## LabelFrame to organize 3 different types of Entry input display
        self.labelframe_entry = tk.LabelFrame(master,
                                              text="Entry Display",
                                              fg='purple',
                                              padx=10,
                                              pady=5)

        # Label as a display
        ''' Lable used to to display text from Entry widget '''
        self.label_display = tk.Label(self.labelframe_entry,
                                      width=26,
                                      bg='grey90')
        '''
        wraplength=170 - Label can wrap text, default is 0. This is given
                        in screen units
        '''

        # Entry as a display
        self.entry_display = tk.Entry(self.labelframe_entry,
                                      width=26,
                                      justify='left')
        ''' No variable defined in entry_display '''
      
        # Read only Entry as a display
        self.ro_entry_display_var = tk.StringVar()
        self.ro_entry_display = tk.Entry(self.labelframe_entry,
                                       width=26,
                                       fg='white',
                                       textvariable = self.ro_entry_display_var,
                                       justify="right")       # or tk.RIGHT
        self.ro_entry_display.config(state='readonly',
                                     readonlybackground='#0b486b',
                                     font = ("Segoe UI", 10))

        # LabelFrame placements
        self.label_display.grid(column=0, row=0, padx=5, pady=2, sticky='nswe')
        self.entry_display.grid(column=1, row=0, padx=5, pady=2, sticky='nswe')
        self.ro_entry_display.grid(column=2, row=0, padx=5, pady=2,
                                   sticky='nswe')
##

        # Checkbutton widget
        self.check_state = tk.StringVar()
        self.check_state.set('chk_on')
        '''
        Checkbutton state by default:  .set(1) - checked, 0 - unchecked,
        or take values specified in keys:  onvalue/offvalue.
        '''
        self.check = tk.Checkbutton(master,
                                    text='Checkbutton',
                                    variable = self.check_state,
                                    onvalue='chk_on',
                                    offvalue='chk_off')
        # Checkbutton Button
        self.check_button = tk.Button(master,
                                      text="Checkbutton.Button",
                                      bd=4,
                                      relief= tk.RAISED,
                                      padx=2,
                                      command=self.check_func)
        """ relief =[RAISED = default, SUNKEN, FLAT, RIDGE, GROOVE, SOLID],
            borderwidth: bd = [1 up to eg. 6]
            Examples of all values of relief option 
        """

        # Combobox widget
        combo_data=(1, 2, 3, 4, 5, "ComboText6")
        self.txt_combo = ttk.Combobox(master,
                                      width=27,
                                      state='readonly',
                                      values=combo_data)
        ''' NB: Widget from ttk module'''
        self.txt_combo.current(0)
        ''' .current(0) - set the selected item '''

        # Combo Button
        self.combo_button = tk.Button(master,
                                      text="Combobox.Button",
                                      bd=4,
                                      relief= tk.SUNKEN,
                                      padx=17,
                                      command=self.combo_func)

        # Frame as separator
        frame_separator1 = tk.Frame(height=3, bd=1, relief=tk.SUNKEN) 
        frame_separator2 = tk.Frame(height=3, bd=1, relief=tk.RIDGE) 
        ''' Separator with defined height & relif.
            Height of the separator defineby by 'pady' in geometry manager.
        '''

        # Listbox widget  
        listb_data=(1, 'two', 3, 'four')
        self.listb = tk.Listbox(master,
                                height=len(listb_data),
                                selectmode=tk.MULTIPLE)
        """
        selectmode:
            SINGLE (just a single choice),
            BROWSE (same, but the selection can be moved using the mouse),
            MULTIPLE (multiple item can be choosen, by clicking at them one 
                at a time), or
            EXTENDED (multiple ranges of items can be chosen, using the Shift
                and Control keyboard modifiers).
        """
        for el in listb_data:
            self.listb.insert(tk.END, el)
            """
            Insert(index, element) - ins new elements in the list just
                before the element given by index. If index is specified
                as END then the new elements are added to the end of the
                list.
            """
        self.listb.configure(exportselection=False)
        '''
        exportselection=False   - not to affect other Listbox selections
                                on the screen
        '''

        # Listbox Button
        self.listb_button = tk.Button(master,
                                      text="Listbox.Button",
                                      bd=4,
                                      relief=tk.RIDGE,
                                      padx=18,
                                      command=self.listbox_func)

        # Label as separator
        label_separator = tk.Label(master, text='tk.Label as a simple separator')
        '''
        Adding line breaks in Tk has no effect without adding any widget
        like eg. Label(). Empty rows and columns are ignored when using 
        - .grid() and
        - .pack()
        '''

        # OptionMenu
        self.optionmenu_var = tk.StringVar(master)
        self.optionmenu_var.set("one")                  # initial value
        self.optionmenu = tk.OptionMenu(master,
                                        self.optionmenu_var,
                                        "one", "two", "three", "four")

        # OptionMenu Button
        self.optionmenu_button = tk.Button(master,
                                           text="OptionMenu.Button",
                                           bd=2,
                                           relief=tk.SOLID,
                                           padx=18,
                                           command=self.optionmenu_func)

        # Radiobutton widget  
        self.radio_var = tk.StringVar()
        self.radio_var.set('male')
        self.radio1 = tk.Radiobutton(master,
                                     text="male",
                                     variable=self.radio_var,
                                     value='male')
        self.radio2 = tk.Radiobutton(master,
                                     text="female",
                                     variable=self.radio_var,
                                     value='female')

        # Radiobutton Button
        self.radio_button = tk.Button(master,
                                      text="Radiobutton.Button",
                                      bd=4,
                                      relief= tk.FLAT,
                                      padx=4,
                                      command=self.radio_func)

        # Spinbox widget
        self.txt_spin = tk.Spinbox(master, from_=1, to= 100, width=30)
        ''' Spinbox kwarg: values=(2, 5, 10), lub from_=1, to= 100
            NB: 'from_' !!!
        '''

        # Spinbox Button
        self.spin_button = tk.Button(master,
                                     text="Spinbox.Button",
                                     bd=4,
                                     relief=tk.GROOVE,
                                     padx=28,
                                     command=self.spin_func)

        # Text widget
        self.txt_text = tk.Text(master, wrap=tk.WORD, width=50, height=5)          

#
        self.txt_text.tag_add("h1", "1.0", "1.0")
        '''
        New Hedline Tag added as .tag_add(name, beginning, end) where
        '1.0' means: row 1, char in row 0
        '''
        self.txt_text.tag_config("h1",
                                 foreground='purple',
                                 font=("Arial 11 bold italic"))
        ''' Note: 'fg' - does not work with tabs '''
        self.txt_text.tag_add("p", "1.0", "1.0")
        self.txt_text.tag_config("p", foreground='cyan4')


        # Text.delete Button
        self.text_del_button = tk.Button(master,
                                         text="Text.delete Button",
                                         fg='red',
                                         command=self.text_del_func)

        # Scrollbar widget
        self.scroll = tk.Scrollbar(master)
        # attach Scrollbar to Text
        self.txt_text.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.txt_text.yview)
 
        # Message Button
        self.message1_button = tk.Button(master,
                                         text="Message.Button",
                                         fg='green',
                                         command=self.message_func)

        # Message Text
        self.txt_message1 = tk.Message(master,
                                       width=200,
                                       text="",
                                       font=("Tahoma 8"))

        # Message.delete Button
        self.message_del_button = tk.Button(master,
                                            text="Message.delete Button",
                                            fg='white',
                                            bg='blue',
                                            command=self.message_del_func)

        # Frame as separator for Message text
        frame_separator3 = tk.Frame(height=90) 


        # Image
        self.img_author = tk.PhotoImage(file="img/programoteq.100.png")
        self.img_Label = tk.Label(master, image=self.img_author)

        # Close Button
        self.close_button = tk.Button(master, text="Close", padx=50, pady=2,
                                      fg='red', bg='yellow',
                                      command=self.close_func)

        # ----- Layout section -----

        self.label.grid(column=1, row=0, pady=5)

        self.txt_entry.grid(column=0, row=1)
        self.entry_button.grid(column=2, row=1)

        self.labelframe_entry.grid(columnspan=3, row=2, padx=7, pady=5,
                             sticky='nswe') 

        self.check.grid(column=0, row=3)
        self.check_button.grid(column=2, row=3, pady=5)

        self.txt_combo.grid(column=0, row=4)
        self.combo_button.grid(column=2, row=4)

        frame_separator1.grid(columnspan=3, row=5, sticky='we', padx=10, pady=5)
        frame_separator2.grid(columnspan=3, row=6, sticky='we', padx=10, pady=5)

        self.listb.grid(column=0, row=7)
        self.listb_button.grid(column=2, row=7)

        label_separator.grid(columnspan=3, row=8)

        self.optionmenu.grid(column=0, row=9)
        self.optionmenu_button.grid(column=2, row=9, pady=5)

        self.radio1.grid(column=0, row=10)
        self.radio2.grid(column=1, row=10)
        self.radio_button.grid(column=2, row=10)

        self.txt_spin.grid(column=0, row=11, padx=5, pady=2)
        self.spin_button.grid(column=2, row=11, padx=5, pady=5)

        self.txt_text.grid(columnspan=2, row=15)
        self.text_del_button.grid(column=2, row=15)
        self.scroll.grid(columnspan=2, row=15, stick = 'nse')    # ScrollBar

        self.message1_button.grid(column=0, row=17, sticky='nswe', padx=5,
                                  pady=5)
        self.txt_message1.grid(column=1, row=17, rowspan=2, sticky='nswe',
                               padx=5, pady=5)
        self.message_del_button.grid(column=2, row=17, sticky='nswe', padx=5,
                               pady=5)
        frame_separator3.grid(column=0, row=18, pady=5)

        
        self.close_button.grid(column=2, row=20, pady=5)

        self.img_Label.grid(columnspan=3, row=21, sticky='s', pady=2)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        '''
        There are 3 geometry managers available in tkinter:
        
            .pack(side='top')
                side=TOP or BOTTOM or LEFT or RIGHT,
                fill=BOTH, X, Y
                expand=1    - widget expands when window resized
                
            .grid(column=1, row=0)
                column=1, row=0
                columnspan=2, rowspan=2,    - spans across # of col/row
                sticky=NS+E, (N, NE, E, SE, S, SW, W, NW, or CENTER)
        
            .place(x=60, y=50)
                x=60, y=50

        Sequence of 'TAB' - 'Shift-Tab' keys selection depends on the widgets'
        definition order, not on the placement manager.
        '''

    # ----- Functions section -----

    def entry_func(self):
        entry_value = self.txt_entry.get()
        # Text box Display
        self.txt_text.insert(tk.END, "Entry widget 1 text: ", ("h1"))
        self.txt_text.insert(tk.END, " %s. \n" % entry_value, ("p"))
#

        # Label Display
        self.label_display.config(text=entry_value)
        # Entry Display
        self.entry_display.delete(0, 'end')
        self.entry_display.insert(0, entry_value)
        ''' Modification of the object value '''

        # Read only Entry Display       
        self.ro_entry_display_var.set(entry_value)
        ''' Text Variable modification '''

    def combo_func(self):
        combo_value = self.txt_combo.get()
        self.txt_text.insert(tk.END, "Combobox text: ", ("h1"))
        self.txt_text.insert(tk.END, " %s. \n" % combo_value)

    def check_func(self):
        check_value = self.check_state.get()
        self.txt_text.insert('end',("Checkbox status: %s. \n" % check_value))

    def radio_func(self):
        self.txt_text.insert('end',("Radiobutton selection: %s. \n"
                                  % self.radio_var.get()))

    def listbox_func(self):
        list_select_indexes = self.listb.curselection()
        '''
        .curselection() - Returns a list containing the numerical indices of
                        all of the elements in the listbox that are currently
                        selected.
        '''
        list_values = [str(self.listb.get(index)) for index
                       in list_select_indexes]
        '''
        .get(first, last) - listbox elements between first and last, inclusive.
                            If last is omitted, returns the contents of the
                            listbox element indicated by first, or an empty string.
        '''
        list_values_joined= ', '.join(list_values)
        self.txt_text.insert(tk.END, ("Listbox selection: %s. \n"
                                   % list_values_joined))

    def spin_func(self):
        spin_value = self.txt_spin.get()
        self.txt_text.insert(tk.END,("Spinbox value: %s. \n" % spin_value))

    def optionmenu_func(self):
        option_value = self.optionmenu_var.get()
        self.txt_text.insert(tk.END,("OptionMenu value: %s. \n" % option_value))


    def message_func(self):
        self.txt_message1.configure(relief=tk.RAISED, text=
'''    Message widget - provides a multiline and noneditable object that displays \
texts, automatically breaking lines and justifying their contents. 
    Its functionality exceeds the one provided by the Label widget (no text wrap, \
no ability to maintain a given width or aspect ratio.)
'''
        )

    def message_del_func(self):
        self.txt_message1.configure(text="", relief=tk.FLAT)

    def text_del_func(self):
        self.txt_text.delete(1.0,tk.END)
        '''
        .delete(beg, end) - from the first index in the text (1.0) - to the
                            last (END).
        '''

    def close_func(self):
        if tkinter.messagebox.askokcancel("tkinter.messagebox.askokcancel",
                                          "Do you really want to Quit?",
                                          icon='warning'):
            self.master.destroy()
            '''
            'messagebox' box functions:
            - showinfo()
            - showwarning()
            - showerror()

            - askquestion()
            - askokcancel()
            - askyesno ()
            - askretrycancel()
            - askyesnocancel() - return True if the answer is yes, None if cancelled

            messagebox questions - you can change default '?' icon:
            - 'info'
            - 'warning'
            - 'error'

            .destroy() - destroys widget/main tkinter window
            '''


class Tkinter_ttw_GUI:

    def __init__(self, master):
        self.master = master

        style = ttk.Style()         
        style.theme_use('xpnative')
        '''
        The default ttw Theme in Win10  is 'vista'. You can use it without style setup.
        To find the available themes write:
            ttk.Style().theme_names()  
        Win10 standard options are:
            ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        From the above, 2 most interesting ones are:
            'xpnative' and 'classic'
        '''

        self.aTop = tk.Toplevel()
        self.aTop.title('tk.Toplevel window .title')
        
        ttk.Label(self.aTop,
                  text="tkinter.ttk - 'xpnative' Theme",
                  font="Consolas 12 bold",
                  padding=(30,10,30,0)).pack(padx=10, pady=1)

        ttkF = ttk.Frame(self.aTop, padding=(40,5,5,5))
        ttkF.pack(fill='both', expand=1)

        ttkLF = ttk.LabelFrame(ttkF, text='ttk.LabelFrame', padding=(5,5,5,5))
        ttkLF.pack(fill='both', expand=1, pady=10)

        ttk.Label(ttkLF, text='ttk.Label').pack(pady=1)

        ttk.Button(ttkLF, text='ttk.Button 1').pack(pady=5)

        ttk.Entry(ttkLF, width=20).pack()

        noteb = ttk.Notebook(ttkF)
        tab1 = ttk.Frame(noteb)   
        tab2 = ttk.Frame(noteb)   
        noteb.add(tab1, text='One')
        noteb.add(tab2, text='Two')
        noteb.pack(fill='both')

        ttk.Label(tab1, text='ttk.Notebook', font='Tahoma 10 bold').pack(pady=1)

        ttk.Button(tab1, text='ttk.Button 2').pack(pady=10)

        ttk.Checkbutton(tab1, text='ttk.Checkbox').pack(padx=10, pady=1)

        # Sizegrip Widget
        ttk.Sizegrip(self.aTop).pack(side='bottom', anchor='se')

        # Image
        self.img_author1 = tk.PhotoImage(file="img/programoteq.100.png")
        self.img_Label1 = tk.Label(self.aTop, image=self.img_author1)
        self.img_Label1.pack()


if __name__ == "__main__":
    main()
