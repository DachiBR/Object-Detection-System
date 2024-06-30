import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from camera import Camera
from item_detection import detect_items
import cv2

class ScrewCounterApp:
    def __init__(self, root, camera_index=1):  # Default to the first USB camera
        self.root = root
        self.root.title("Screw Counter Application")

        self.camera = Camera(camera_index)

        self.video_frame = ttk.Label(self.root)
        self.video_frame.grid(row=0, column=0, columnspan=3)

        self.capture_button = ttk.Button(self.root, text="Capture", command=self.capture_image)
        self.capture_button.grid(row=1, column=0)

        self.count_button = ttk.Button(self.root, text="Count", command=self.count_items, state=tk.DISABLED)
        self.count_button.grid(row=1, column=1)

        self.refresh_button = ttk.Button(self.root, text="Refresh", command=self.refresh, state=tk.DISABLED)
        self.refresh_button.grid(row=1, column=2)

        self.count_label = ttk.Label(self.root, text="Items Count: 0")
        self.count_label.grid(row=2, column=0, columnspan=3)

        self.current_frame = None  # Initialize current_frame attribute

        self.update_video_frame()

    def update_video_frame(self):
        ret, frame = self.camera.get_frame()
        if ret:
            self.current_frame = frame  # Update current_frame
            cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2_image)
            imgtk = ImageTk.PhotoImage(image=pil_image)
            self.video_frame.imgtk = imgtk
            self.video_frame.config(image=imgtk)
        self.root.after(10, self.update_video_frame)

    def capture_image(self):
        if self.current_frame is not None:
            self.count_button.config(state=tk.NORMAL)
            self.refresh_button.config(state=tk.NORMAL)
        else:
            # Handle case where current_frame is None
            print("No frame captured yet.")

    def count_items(self):
        if self.current_frame is not None:
            items_count, contours = detect_items(self.current_frame)
            self.count_label.config(text=f"Items Count: {items_count}")
            self.display_detected_items(contours)
        else:
            # Handle case where current_frame is None
            print("No frame captured yet.")

    def display_detected_items(self, contours):
        if self.current_frame is not None:
            output_image = self.current_frame.copy()
            cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)
            cv2_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2_image)
            imgtk = ImageTk.PhotoImage(image=pil_image)
            self.video_frame.imgtk = imgtk
            self.video_frame.config(image=imgtk)

    def refresh(self):
        self.count_label.config(text="Items Count: 0")
        self.count_button.config(state=tk.DISABLED)
        self.refresh_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrewCounterApp(root, camera_index=1)  # Adjust the index as needed
    root.mainloop()
