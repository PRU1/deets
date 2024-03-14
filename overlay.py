import tkinter as tk
import win32gui
import win32con
import win32api

class TransparentOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-alpha", 0.0)  # Set window transparency (0 is fully transparent, 255 is fully opaque)
        self.root.overrideredirect(True)  # Remove window decorations (title bar, borders)
        self.root.geometry("%dx%d+%d+%d" % (
        win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1), 0, 0))  # Set window size to cover entire screen
        self.root.attributes("-topmost", True)  # Keep window on top of others

        # Set window click-through using Win32 API
        hwnd = self.root.winfo_id()
        extended_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extended_style | win32con.WS_EX_LAYERED)

        # Set the alpha transparency of the entire window
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

        # Place widgets or add content to the overlay window
        label = tk.Label(self.root, text="Test", fg="white", bg="blue", font=("Arial", 24))
        label.pack(pady=50)
        button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        button.pack(pady=10)

        # Bind the F9 key to toggle window visibility
        self.root.bind("<KeyPress-F10>", self.toggle_visibility)
        self.root.bind("<KeyRelease-F10>", self.toggle_visibility)

        self.hidden = True  # Variable to track window visibility
        self.root.mainloop()




    def on_button_click(self):
        """Function to handle button click event"""
        print("Button clicked!")

    def toggle_visibility(self, event):
        """Function to toggle window visibility when F9 key is pressed or released"""
        if event.type == tk.EventType.KeyPress:
            self.hidden = not self.hidden
            if self.hidden:
                self.root.attributes("-alpha", 0.0)  # Hide the window
            else:
                self.root.attributes("-alpha", 0.5)  # Show the window

if __name__ == "__main__":
    TransparentOverlay()

