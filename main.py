from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from pygame import mixer
from tkinter import filedialog
import threading
from Modules import Image_resize,Volume


def App():
    # created a tkinter gui window frame
    root = Tk()
    # Define the geometry
    root.geometry('445x420')
    root.resizable(False,False)
    # Set the title of tkinter frame
    root.title('MP3 Player')
    Icon = PhotoImage(file='MP3 Player\\Image\\Icon.png')
    root.iconphoto(False, Icon)
    # is used to initialize the mixer module
    # so that we can use it’s various functions in our application
    mixer.init()


    # widget is used to create a listbox in which we will store our songs 
    song_list = Listbox(root,selectmode=SINGLE,
                    bg="black",fg="white",
                    font=('Calibri',15),
                    height=16,width=45,
                    selectbackground="black",selectforeground="lightblue",)
    song_list.grid(columnspan=9)


    # This function is for adding Songs to our App  
    def AddSongs():
        # choose song 
        song_item=filedialog.askopenfilenames(initialdir="Music/",title="Choose Your Songs", filetypes=(("mp3 Files","*.mp3"),))
        for s in song_item:
            song_list.insert(END,s)

    # This function is for deleting selected Songs 
    def deletesong():
        curr_song=song_list.curselection()
        song_list.delete(curr_song[0])

    # with this function we can play the selected Songs 
    def Play():
        try:
            song=song_list.get(ACTIVE)
            mixer.music.load(song)
            mixer.music.play()
        except :
            messagebox.showerror('Error','At First Select Your Songs')

    def Pause():
        mixer.music.pause()

    def Resume():
        mixer.music.unpause()

    #Function to navigate from the current song
    def Previous():
        try:
            #to get the selected song index
            previous_one=song_list.curselection()
            #to get the previous song index
            previous_one=previous_one[0]-1
            #to get the previous song
            temp2=song_list.get(previous_one)
            mixer.music.load(temp2)
            mixer.music.play()
            song_list.selection_clear(0,END)
            #activate new song
            song_list.activate(previous_one)
            #set the next song
            song_list.selection_set(previous_one)
        except:
            messagebox.showerror('Error','You Did Not Select Any Songs')
    def Next():
        try:
            #to get the selected song index
            next_one=song_list.curselection()
            #to get the next song index
            next_one=next_one[0]+1
            #to get the next song 
            temp=song_list.get(next_one)
            mixer.music.load(temp)
            mixer.music.play()
            song_list.selection_clear(0,END)
            #activate newsong
            song_list.activate(next_one)
             #set the next song
            song_list.selection_set(next_one)
        except:
            messagebox.showerror('Error','You Did Not Select Any Songs')
    

    play_img = Image_resize.resize('MP3 Player/Image/PlayMusic.png')
    # Create a play button and pass the img to it 
    play_button = ttk.Button(root,image=play_img,command=Play)
    # Place the play button to tkinter window 
    play_button.place(x=0,y=350)


    pause_img=Image_resize.resize('MP3 Player/Image/Pause.png')
    # Create a pause button and pass the img to it 
    pause_button = ttk.Button(root,image=pause_img,command=Pause)
    # Place the pause button to tkinter window 
    pause_button.place(x=90,y=350)


    resume_img=Image_resize.resize('MP3 Player/Image/Resume.png')
    # Create a resume button and pass the img to it 
    resume_button = ttk.Button(root,image=resume_img,command=Resume)
    # Place the resume button to tkinter window 
    resume_button.place(x=180,y=350)


    left_img=Image_resize.resize('MP3 Player/Image/Left.png')
    # Create a Previous button and pass the img to it 
    left_button = ttk.Button(root,image=left_img,command=Previous)
    # Place the Previous button to tkinter window 
    left_button.place(x=270,y=350)


    right_img=Image_resize.resize('MP3 Player/Image/Right.png')
    # Create a next button and pass the img to it 
    right_button = ttk.Button(root,image=right_img,command=Next)
    # Place the next button to tkinter window 
    right_button.place(x=360,y=350)


    high_volume_img = Image_resize.volume_resize('MP3 player/Image/volume-up.png')
    # Create a volume up button and pass the img to it 
    high_button = ttk.Button(root,image=high_volume_img,command=Volume.volume_up)
    # Place the volume up button to tkinter window 
    high_button.place(x=404,y=180)


    volume_down_img = Image_resize.volume_resize('MP3 Player/Image/volume-down.png')
    # Create a volume down button and pass the img to it 
    down_button = ttk.Button(root,image=volume_down_img,command=Volume.volume_down)
    # Place the volume down button to tkinter window
    down_button.place(x=404,y=220) 


    # Menu Button 
    my_menu=Menu(root)
    root.config(menu=my_menu)
    add_song_menu=Menu(my_menu)
    my_menu.add_cascade(label="Menu",menu=add_song_menu)
    add_song_menu.add_command(label="Add songs",activebackground='BLACK',activeforeground='YELLOW',command=AddSongs)
    add_song_menu.add_command(label="Delete song",activebackground='BLACK',activeforeground='YELLOW',command=deletesong)

    root.mainloop()

# thread is a separate flow of execution. This means that our program will have two things happening at once
threading.Thread(target=App).start()



