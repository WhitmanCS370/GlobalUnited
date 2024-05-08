import customtkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import shutil
import os

class Tools:
    def __init__(self):
        pass
    
    def on_play_sound(self, object):
        pass

    def on_stop_sound(self, object):
        pass

    def on_pause_sound(self, object):
        pass

    def on_resume_sound(self, object):
        pass

    def on_sort_playlist(self, object):
        pass

    def on_edit_sound(self, object):
        pass

    def on_record_sound(self, object):
        pass


    def on_add_sound_to_playlist(self, playlist_path, soundplaye):
        sound_files = filedialog.askopenfilenames(
        title="Add Sounds to Playlist",
        initialdir="sounds",  # Optionally start in the sounds folder
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]  # Add more audio filetypes as needed
        )

        if sound_files: 
            for file in sound_files:
                try: 
                    shutil.copy(file, playlist_path)
                    # Add the filename to your playlist data structure if needed  
                except shutil.Error as err:
                    tkinter.messagebox.showerror("Error", f"Failed to copy {file}: {err}") 


    def create_playlist_folder(self, soundplayer):

        playlist_name = tk.simpledialog.askstring("Create Playlist", "Enter a name for your playlist:")

        if playlist_name:  # Check if a name was provided
            button = customtkinter.CTkButton(master=soundplayer.playlist_frame, 
                                            text=playlist_name,
                                            command= lambda: soundplayer.update_sounds(playlist_name))
            button.grid(row=soundplayer.playlist_frame.grid_size()[1], column=0, padx=5, pady=5)
            
            playlist_path = os.path.join("sounds", playlist_name)

            try:
                os.mkdir(playlist_path)
                return playlist_path
            except FileExistsError:
                tkinter.messagebox.showerror("Error", f"Playlist '{playlist_name}' already exists.")

        return None 

    def on_create_playlist(self, soundplayer):
        playlist_path = self.create_playlist_folder(soundplayer)
        if playlist_path:
            self.on_add_sound_to_playlist(playlist_path, soundplayer)
            
        

    def update_sounds(self, soundplayer, playlist):

        pass

    def on_delete_playlist(self, soundplayer):
        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist to delete: ", title="Delete Playlist")
        playlist_name = dialog.get_input()
        if playlist_name in soundplayer.playlists:
            shutil.rmtree(os.path.join("sounds", playlist_name))
            del soundplayer.playlists[playlist_name]
            for widget in soundplayer.playlist_frame.winfo_children():
                if widget.cget("text") == playlist_name:
                    widget.destroy()
        


        

    def on_delete_sounds(self):
        pass
