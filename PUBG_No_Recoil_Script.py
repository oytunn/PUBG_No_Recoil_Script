# --------------------------------------------------------------
# PUBG Vertical Recoil Compensation
# --------------------------------------------------------------
# Game Settings:
#   Mouse DPI                : 1000
#   General Sensitivity      : 50
#   Vertical Sens Multiplier : 1.0
#   Aiming Sensitivity       : 50 (Red Dot)
#
# Mathematical Conversion:
#   PUBG Red Dot Sens=50 -> 1 count = 0.022 degrees
#   Vertical Multiplier = 1.0 (linear)
#   Input_Count = Bullet_Angle / 0.022
#
# Smoothing:
#   Each bullet movement is divided into equal sub-parts
#   Remainder fraction is carried over to the next part/bullet
# --------------------------------------------------------------

import os
import sys
import ctypes
import threading
import tkinter as tk
from time import sleep
from pynput.mouse import Listener as MouseListener, Button
from pynput.keyboard import Listener as KeyboardListener, Key

# --------------------------------------------------------------
# Windows Process Configuration for Icons and Taskbar
# --------------------------------------------------------------
def Set_Windows_App_Id():
    """Sets explicit AppUserModelID so Windows taskbar uses the application icon."""
    try:
        My_App_Id = "pubg.recoil.helper.aug.1.0"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(My_App_Id)
    except Exception:
        pass

def Get_Resource_Path(Relative_Path):
    """
    Get absolute path to resource, compatible with both dev mode
    and PyInstaller bundled onefile exe.
    """
    try:
        Base_Path = sys._MEIPASS
    except Exception:
        Base_Path = os.path.abspath(os.path.dirname(__file__)) if "__file__" in globals() else os.path.abspath(".")
    return os.path.join(Base_Path, Relative_Path)

def Get_App_Icon_Path():
    """Finds an existing icon file in the bundle or working directory."""
    Icon_Candidate_Names = ["app.ico", "icon.ico", "aug.ico"]
    for Candidate_Name in Icon_Candidate_Names:
        Candidate_Path = Get_Resource_Path(Candidate_Name)
        if os.path.exists(Candidate_Path):
            return Candidate_Path
        Local_Path = os.path.join(os.path.abspath("."), Candidate_Name)
        if os.path.exists(Local_Path):
            return Local_Path
    return None

# --------------------------------------------------------------
# Game Engine Angular Input Coefficient
# --------------------------------------------------------------
# 1 count = 0.05 degrees (smoother, gentle downward pull)
Count_Per_Degree = 0.050
Part_Count = 5  # Number of sub-steps per bullet

# --------------------------------------------------------------
# Weapon Recoil Pattern Data
# --------------------------------------------------------------
Weapons_Data = {
    "M416": {
        "delay_between_bullets": 0.0857,
        "vertical_angles": [
            0.00, 1.20, 1.15, 1.10, 1.25, 1.30, 1.35, 1.40, 1.40, 1.45,
            1.50, 1.50, 1.50, 1.50, 1.50, 1.45, 1.45, 1.45, 1.45, 1.45,
            1.40, 1.40, 1.40, 1.40, 1.40, 1.35, 1.35, 1.35, 1.35, 1.35,
            1.30, 1.30, 1.30, 1.30, 1.30, 1.25, 1.25, 1.25, 1.25, 1.25
        ]
    },
    "AUG": {
        "delay_between_bullets": 0.080,
        "vertical_angles": [
            0.00, 1.30, 1.25, 1.20, 1.35, 1.40, 1.45, 1.50, 1.50, 1.55,
            1.60, 1.60, 1.60, 1.60, 1.60, 1.55, 1.55, 1.55, 1.55, 1.55,
            1.50, 1.50, 1.50, 1.50, 1.50, 1.45, 1.45, 1.45, 1.45, 1.45,
            1.40, 1.40, 1.40, 1.40, 1.40, 1.35, 1.35, 1.35, 1.35, 1.35
        ]
    },
    "AKM": {
        "delay_between_bullets": 0.100,
        "vertical_angles": [
            0.00, 1.50, 1.45, 1.40, 1.60, 1.65, 1.70, 1.75, 1.75, 1.80,
            1.85, 1.85, 1.85, 1.85, 1.85, 1.80, 1.80, 1.80, 1.80, 1.80,
            1.75, 1.75, 1.75, 1.75, 1.75, 1.70, 1.70, 1.70, 1.70, 1.70,
            1.65, 1.65, 1.65, 1.65, 1.65, 1.60, 1.60, 1.60, 1.60, 1.60
        ]
    },
    "M249": {
        "delay_between_bullets": 0.080,
        "vertical_angles": [
            0.00, 1.25, 1.20, 1.15, 1.35, 1.45, 1.50, 1.60, 1.65, 1.70,
            1.70, 1.75, 1.75, 1.75, 1.80, 1.80, 1.80, 1.80, 1.80, 1.80,
            1.80, 1.80, 1.80, 1.80, 1.80, 1.75, 1.75, 1.75, 1.75, 1.75,
            1.75, 1.75, 1.75, 1.70, 1.70, 1.70, 1.65, 1.65, 1.65, 1.65
        ]
    },
}

# Weapon cycle order: M416 -> AUG -> AKM -> M249 -> OFF -> M416 -> ...
Weapon_Order = list(Weapons_Data.keys()) + ["OFF"]
Active_Order_Index = len(Weapon_Order) - 1  # Initially OFF

# System State Variables
Is_App_Running = True
Is_System_Active = False
Active_Weapon_Name = None
Is_Left_Click_Pressed = False

# Global listener references
Mouse_Listener_Instance = None
Keyboard_Listener_Instance = None

# --------------------------------------------------------------
# Windows API - Mouse Movement
# --------------------------------------------------------------
def Move_Mouse_Down(Count_Amount):
    """Sends vertical mouse movement count using Windows mouse_event API."""
    ctypes.windll.user32.mouse_event(0x0001, 0, int(Count_Amount), 0, 0)

# --------------------------------------------------------------
# On-Screen Information Overlay (Tkinter)
# --------------------------------------------------------------
def Show_Overlay(Display_Text, Text_Color, Display_Duration_Ms=1500):
    """Displays information for specified milliseconds at the top center of the screen."""
    try:
        Overlay_Window = tk.Tk()
        Overlay_Window.overrideredirect(True)
        Overlay_Window.attributes("-topmost", True)
        Overlay_Window.attributes("-alpha", 0.85)
        Overlay_Window.configure(bg="black")

        Icon_Path = Get_App_Icon_Path()
        if Icon_Path:
            try:
                Overlay_Window.iconbitmap(Icon_Path)
            except Exception:
                pass

        Overlay_Label = tk.Label(
            Overlay_Window,
            text=f"  {Display_Text}  ",
            font=("Consolas", 18, "bold"),
            fg=Text_Color,
            bg="black",
            padx=16,
            pady=8
        )
        Overlay_Label.pack()

        Overlay_Window.update_idletasks()
        Window_Width = Overlay_Window.winfo_width()
        Screen_Width = Overlay_Window.winfo_screenwidth()
        Overlay_Window.geometry(f"+{(Screen_Width - Window_Width) // 2}+{50}")

        Overlay_Window.after(Display_Duration_Ms, Overlay_Window.destroy)
        Overlay_Window.mainloop()
    except Exception:
        pass

def Start_Overlay_Thread(Display_Text, Text_Color, Display_Duration_Ms=1500):
    """Starts overlay window in a separate daemon thread."""
    Overlay_Thread = threading.Thread(
        target=Show_Overlay,
        args=(Display_Text, Text_Color, Display_Duration_Ms),
        daemon=True
    )
    Overlay_Thread.start()

# --------------------------------------------------------------
# Shooting Loop (Runs in a separate thread during fire)
# Sub-part smoothing + remainder carryover
# --------------------------------------------------------------
def Start_Shooting_Loop():
    if Active_Weapon_Name is None or Active_Weapon_Name not in Weapons_Data:
        return

    Current_Weapon = Weapons_Data[Active_Weapon_Name]
    Angle_List = Current_Weapon["vertical_angles"]
    Bullet_Delay = Current_Weapon["delay_between_bullets"]
    Part_Delay = Bullet_Delay / Part_Count

    Remainder_Carryover = 0.0

    for Bullet_Index in range(len(Angle_List)):
        if not Is_Left_Click_Pressed or not Is_System_Active or not Is_App_Running:
            break

        Current_Angle = Angle_List[Bullet_Index]
        if Current_Angle <= 0.0:
            sleep(Bullet_Delay)
            continue

        Total_Count = (Current_Angle / Count_Per_Degree) + Remainder_Carryover
        Part_Count_Decimal = Total_Count / Part_Count

        Total_Sent_Count = 0
        Part_Remainder = 0.0

        for Part_Index in range(Part_Count):
            if not Is_Left_Click_Pressed or not Is_System_Active or not Is_App_Running:
                break

            Part_Raw = Part_Count_Decimal + Part_Remainder
            Part_Integer = int(Part_Raw)
            Part_Remainder = Part_Raw - Part_Integer

            if Part_Integer > 0:
                Move_Mouse_Down(Part_Integer)
                Total_Sent_Count += Part_Integer

            sleep(Part_Delay)

        Remainder_Carryover = Total_Count - Total_Sent_Count

# --------------------------------------------------------------
# Mouse Event Listener
# --------------------------------------------------------------
def Handle_Mouse_Click(X_Pos, Y_Pos, Clicked_Button, Is_Pressed):
    global Is_Left_Click_Pressed, Is_System_Active, Active_Weapon_Name, Active_Order_Index

    if not Is_App_Running:
        return

    if Clicked_Button == Button.left:
        if Is_Pressed:
            Is_Left_Click_Pressed = True
            if Is_System_Active:
                threading.Thread(target=Start_Shooting_Loop, daemon=True).start()
        else:
            Is_Left_Click_Pressed = False

    elif Clicked_Button == Button.x1:
        if Is_Pressed:
            Active_Order_Index = (Active_Order_Index + 1) % len(Weapon_Order)
            Selected_Item = Weapon_Order[Active_Order_Index]

            if Selected_Item == "OFF":
                Is_System_Active = False
                Active_Weapon_Name = None
                print("STATUS: OFF")
                Start_Overlay_Thread("OFF", "#ff4444")
            else:
                Is_System_Active = True
                Active_Weapon_Name = Selected_Item
                print(f"STATUS: ACTIVE - {Active_Weapon_Name}")
                Start_Overlay_Thread(Active_Weapon_Name, "#00ff88")

# --------------------------------------------------------------
# Clean Application Exit Handler
# --------------------------------------------------------------
def Exit_Application():
    """Safely terminates listeners and exits process with visual feedback."""
    global Is_App_Running, Is_System_Active
    if not Is_App_Running:
        return
    Is_App_Running = False
    Is_System_Active = False

    print("\n[INFO] Exiting application...")
    
    # Show exit overlay briefly on screen before exiting
    try:
        Show_Overlay("PROGRAM CLOSED", "#ff2222", 1200)
    except Exception:
        pass

    try:
        if Mouse_Listener_Instance:
            Mouse_Listener_Instance.stop()
        if Keyboard_Listener_Instance:
            Keyboard_Listener_Instance.stop()
    except Exception:
        pass

    os._exit(0)

# --------------------------------------------------------------
# Keyboard Event Listener (Global Hotkey for Exit)
# --------------------------------------------------------------
def Handle_Keyboard_Press(Key_Pressed):
    """Listens for global exit hotkeys (End or F12)."""
    try:
        if Key_Pressed == Key.end or Key_Pressed == Key.f12:
            threading.Thread(target=Exit_Application, daemon=True).start()
    except Exception:
        pass

# --------------------------------------------------------------
# Main Application Entry Point
# --------------------------------------------------------------
if __name__ == "__main__":
    Set_Windows_App_Id()

    print("=" * 55)
    print("  PUBG Vertical Recoil Compensation Helper")
    print("-" * 55)
    print(f"  Conversion : 1 count = {Count_Per_Degree} degrees")
    print(f"  Smoothing  : {Part_Count} parts/bullet")
    print(f"  Order      : {' -> '.join(Weapon_Order)}")
    print("-" * 55)
    print("  Mouse Side Button (x1) : Switch Weapon / OFF")
    print("  End / F12 Key          : Exit Program Completely")
    print("  Ctrl+C                 : Exit (Console mode)")
    print("=" * 55)
    print("\n  Initial State: OFF\n")

    Mouse_Listener_Instance = MouseListener(on_click=Handle_Mouse_Click)
    Mouse_Listener_Instance.start()

    Keyboard_Listener_Instance = KeyboardListener(on_press=Handle_Keyboard_Press)
    Keyboard_Listener_Instance.start()

    try:
        while Is_App_Running:
            sleep(0.5)
    except KeyboardInterrupt:
        Exit_Application()