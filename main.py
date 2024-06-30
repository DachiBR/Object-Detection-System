from gui import ScrewCounterApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrewCounterApp(root, camera_index=1)  # Adjust the index as needed
    root.mainloop()
