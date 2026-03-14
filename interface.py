import tkinter as tk
from tkinter import ttk, messagebox

import salsa

class MyGUI:
    root = tk.Tk()
    root.title("Salsanist")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=1)
    
    KEYS: dict = {
        "F" : ["F", 65],
        "B" : ["B-", 70],
        "Es" : ["E-", 75],
        "As" : ["A-", 68],
        "Des" : ["D-", 73],
        "Ges" : ["G-", 66],
        "C" : ["C", 72],
        "G" : ["G", 67],
        "D" : ["D", 74],
        "A" : ["A", 69],
        "E" : ["E", 76],
        "H" : ["B", 71],
        "Fis" : ["F#", 66]
    }

    STYLES: dict = {
        "Cha-cha-chá" : {
            "violins" : tk.BooleanVar,
            "piano" : tk.BooleanVar,
            "bass" : tk.BooleanVar,
            "clave" : tk.BooleanVar,
            "güiro" : tk.BooleanVar,
            "congas" : tk.BooleanVar,
            "timbales" : tk.BooleanVar
        },
        "Guaguancó" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "timbales bell" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Güiro" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "cymbal" : tk.BooleanVar(),
            "bongos" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Mambo" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "clave" : tk.BooleanVar(),
            "timbales bell" : tk.BooleanVar(),
            "bongo bell" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Merengue" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "clave" : tk.BooleanVar(),
            "güiro" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Mozambique" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "clave" : tk.BooleanVar(),
            "timbales bell" : tk.BooleanVar(),
            "bongo bell" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Pachanga" : {
            "violins" : tk.BooleanVar(),
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "clave" : tk.BooleanVar(),
            "güiro" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Plena" : {
            "piano" : tk.BooleanVar(),
            "bass" : tk.BooleanVar(),
            "clave" : tk.BooleanVar(),
            "güicharo" : tk.BooleanVar(),
            "timbales bell" : tk.BooleanVar(),
            "bongo bell" : tk.BooleanVar(),
            "congas" : tk.BooleanVar()
        },
        "Son Montuno" : {
            "horns" : tk.BooleanVar(value=True),
            "bass" : tk.BooleanVar(value=True),
            "clave" : tk.BooleanVar(value=True),
            "timbales" : tk.BooleanVar(value=True),
            "bongos" : tk.BooleanVar(value=True),
            "congas" : tk.BooleanVar(value=True)
            }
        }
    
    PARTS: dict = {
        "Intro" : "intro",
        "Verse" : "verse",
        "Bridge" : "bridge",
        "Montuno" : "montuno",
        "Klavier Solo" : "solo",
        #"Mambo" : "mambo",
        "Outro" : "outro"
    }

    PROG: dict = {
        "I-VI | II-V" : {
            "major": ("I-vi-ii-V",),
            "minor": ("i-VI-ii-V",)
            },
        "I-VI | II-V | II-V | I-I" : {
            "major": ("I-vi-ii-V", "ii-V-I-I"),
            "minor": ("i-VI-ii-V", "ii-V-i-i")
            },
        "II | V | III | VI | II | V | VII | I" : {
            "major": ("ii-V", "iii-VI", "ii-V", "VII-I"),
            "minor": ("ii-V", "III-VI", "ii-V", "VII-i")
            },
        "II | V | III | VI | II | V | I | I" : {
            "major": ("ii-V", "iii-VI", "ii-V", "I-I"),
            "minor": ("ii-V", "III-VI", "ii-V", "i-i")
            },
        "V-IV | I-IV" : {
            "major": ("V-IV-I-IV",),
            "minor": ("V-iv-i-iv",)
        },
        "V | IV | I | IV | V | IV | I | I" : {
            "major": ("V-IV", "I-IV", "V-IV", "I-I"),
            "minor": ("V-iv", "i-iv", "V-iv", "i-i")
        },
        "V | IV | I | IV | V | IV | I | II" : {
            "major": ("V-IV", "I-IV", "V-IV", "I-ii"),
            "minor": ("V-iv", "i-iv", "V-iv", "i-ii")
        },
    }

    default_song: list = [
        ["Intro", "I-VI | II-V", 8],
        ["Verse", "I-VI | II-V | II-V | I-I", 16],
        ["Bridge", "II | V | III | VI | II | V | VII | I", 8]
    ]

    part_count: int = 0

    def __init__(self):
        #--------State durch ChatGPT--------
        self.selected_key = tk.StringVar(value="C")
        self.selected_style = tk.StringVar(value="Son Montuno")
        self.selected_mode = tk.StringVar(value="major")
        self.selected_direction = tk.StringVar(value="reverse")
        self.play_piano = tk.BooleanVar(value=True)
        self.part_frame = ttk.LabelFrame(self.root, text="Liedstruktur")
        self.part_frame.grid(row=1)

        self.all_parts = []

        self.create_instrument_vars(self.STYLES[self.selected_style.get()].keys())

        #--- UI durch ChatGPT ---
        self.create_widgets()
        self.update_instruments()
        default_song = self.default_song
 
        for section in default_song:
            self.create_part(self.part_frame, section[0], section[1], section[2])

        self.root.mainloop()
    
    def create_widgets(self):
        default = self.default_song[0]
        salsa_frame = ttk.Labelframe(self.root, text="Salsa")
        salsa_frame.columnconfigure(0, weight=3)
        salsa_frame.columnconfigure(1, weight=1)
        salsa_frame.grid(row=0, sticky=tk.EW)

        # --- Frame für Stil, Tonart, Modus und (stummes) Klavier
        style_frame = ttk.Frame(salsa_frame)
        style_frame.columnconfigure(0, weight=1)
        style_frame.columnconfigure(1, weight=2)
        style_frame.rowconfigure(0, weight=1)
        style_frame.rowconfigure(1, weight=1)
        style_frame.rowconfigure(2, weight=1)
        style_frame.rowconfigure(3, weight=1)
        style_frame.rowconfigure(4, weight=1)
        style_frame.grid(column=0, sticky=tk.EW)

        # --- Labels für Stil, Tonart Modus und (stummes) Klavier
        style_label = ttk.Label(style_frame, text="Stil:")
        style_label.grid(column=0, row=0)

        scale_label = ttk.Label(style_frame, text="Tonart:")
        scale_label.grid(column=0, row=1)

        mode_label = ttk.Label(style_frame, text="Modus:")
        mode_label.grid(column=0, row=2)

        clave_label = ttk.Label(style_frame, text="Clave:")
        clave_label.grid(column=0, row=3)

        piano_label = ttk.Label(style_frame, text="Klavier:")
        piano_label.grid(column=0, row=4)

        style_options = ttk.OptionMenu(
            style_frame,
            self.selected_style,
            self.selected_style.get(),
            *self.STYLES.keys(),
            command=self.on_style_change            
        )
        style_options.grid(column=1, row=0, sticky=tk.EW)

        scale_options = ttk.OptionMenu(
            style_frame,
            self.selected_key,
            self.selected_key.get(),
            *self.KEYS.keys()
        )
        scale_options.grid(column=1, row=1, sticky=tk.EW)

        mode_frame = ttk.Frame(style_frame)
        mode_frame.grid(column=1, row=2, sticky=tk.EW)

        mode = (("Dur", "major"), ("Moll", "minor"))
        for md in mode:
            rbtn = ttk.Radiobutton(
                mode_frame,
                text=md[0],
                value=md[1],
                variable=self.selected_mode,
                #anchor="w"
            )
            rbtn.pack()

        clave_frame = ttk.Frame(style_frame)
        clave_frame.grid(column=1, row=3, sticky=tk.EW)
        clave = (("3-2", "forward"), ("2-3", "reverse"))
        for cl in clave:
            rbtn = ttk.Radiobutton(
                clave_frame,
                text=cl[0],
                value=cl[1],
                variable=self.selected_direction
            )
            rbtn.pack()

        piano_frame = ttk.Frame(style_frame)
        piano_frame.grid(column=1, row=4)
        piano = (("Play", True), ("Mute", False))
        for pno in piano:
            rbtn = ttk.Radiobutton(
                piano_frame,
                text=pno[0],
                value=pno[1],
                variable=self.play_piano
            )
            rbtn.pack()

        #Instrumente
        self.instrument_frame = ttk.Labelframe(salsa_frame, text="Besetzung")
        self.instrument_frame.grid(column=1, row=0, sticky=tk.E)

        #Part-Button
        part_btn = ttk.Button(
            self.root,
            text="Neuer Part",
            command=lambda: self.create_part(self.part_frame, default[0], default[1], default[2])
            )
        part_btn.grid(row=2)

        #Fertig-Button
        finish_btn = ttk.Button(self.root, text="Komponieren!", command=self.finish)
        finish_btn.grid(row=3)

    def create_instrument_vars(self, _instruments):
        self.instrument_vars = {
            name: tk.BooleanVar()
            for name in _instruments
        }
    
    def update_instruments(self):
        #Alte Checkbuttons entfernen
        for widget in self.instrument_frame.winfo_children():
            widget.destroy()
        
        self.instrument_vars.clear()

        #Neue Instrumente für den Stil
        style = self.selected_style.get()

        self.create_instrument_vars(self.STYLES[style])

        for instrument in self.instrument_vars:
            chk = ttk.Checkbutton(
                self.instrument_frame,
                text=instrument,
                variable=self.instrument_vars[instrument]
            )
            chk.pack(anchor="w", padx=10, pady=2)

    def on_style_change(self, *_):
        self.update_instruments()

    def finish(self):
        style = self.selected_style.get()
        score_key = self.KEYS[self.selected_key.get()]
        mode = self.selected_mode.get()
        direction = self.selected_direction.get()
        play_piano = self.play_piano.get()
        instrument_vars = self.instrument_vars       
        all_parts = self.all_parts

        selected_instruments = ["piano"]
        for instrument, selected in instrument_vars.items():
            if selected.get():
                selected_instruments.append(instrument)

        try:
            song = salsa.Salsa(style,
                               selected_instruments,
                               all_parts,
                               direction,
                               mode,
                               score_key[0],
                               score_key[1],
                               play_piano)
            song.__init__
        except KeyError:
            messagebox.showinfo('Sorry!',
                                'Dieses Genre gibt es noch nicht. Bitte wähle Son Montuno :D')


    #---Funktion zum erstellen von Parts in Form von Dictionaries---
    def create_part(self, _root: ttk.LabelFrame, _part: str, _prog: str, _bars: int):
        index = self.part_count
        PART: dict = {
            "index" : index,
            "part": tk.StringVar(value=_part),
            "prog": tk.StringVar(value=_prog),
            "bars" : tk.IntVar(value=_bars),
            "part_value" : _part,
            "prog_value" : self.PROG[_prog],
            "bars_value" : _bars
        }
        self.all_parts.append(PART)

        frame = ttk.Frame(_root)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

        part_label: ttk.Label = ttk.Label(frame, text='Abschnitt:')
        part_label.grid(column=0, row=0, sticky=tk.W)
        part_options = ttk.OptionMenu(
            frame,
            PART["part"],
            PART["part"].get(),
            *self.PARTS.keys(),
            command=lambda _: self.update_part(PART["index"], "part")        
        )
        part_options.grid(column=1, row=0, sticky=tk.EW)
        
        prog_label: ttk.Label = ttk.Label(frame, text='Akkordfolge (pro Takt):')
        prog_label.grid(column=0, row=1, sticky=tk.W)
        prog_options: ttk.OptionMenu = ttk.OptionMenu(
            frame,
            PART["prog"],
            PART["prog"].get(),
            *self.PROG.keys(),
            command=lambda _: self.update_part(PART["index"], "prog")
        )
        prog_options.grid(column=1, row=1, sticky=tk.EW)

        bar_label: ttk.Label = ttk.Label(frame, text='Takte:')
        bar_label.grid(column=0, row=2, sticky=tk.W)
        bar_spinbox: ttk.Spinbox = ttk.Spinbox(
            frame,
            from_=2,
            to=32,
            values=(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32),
            textvariable=PART["bars"],
            wrap=False,
            command=lambda: self.update_part(PART["index"], "bars"))
        bar_spinbox.grid(column=1, row=2, sticky=tk.EW)
        del_btn: ttk.Button = ttk.Button(
            frame,
            text="Doch nicht.",
            command=lambda: self.delete_part(frame, PART["index"])
        )
        del_btn.grid(column=1, row=4, sticky=tk.EW)
        frame.pack()
        self.part_count += 1           

    def display_keys(self):
        buttonframe = tk.Frame(self.root)
        buttonframe.pack()

        major_names = ['F', 'B', 'Es', 'As', 'Des', 'Ges', 'C', 'G', 'D', 'A', 'E', 'H', 'Fis']
        direction = ["forward", "reverse"]

        for key in major_names:
            rbtn = tk.Radiobutton(
                buttonframe,
                text=key,
                value=key,
                variable=self.selected_key,
                anchor="w"
            )
            rbtn.pack()

        for clave in direction:
            rbtn = tk.Radiobutton(
                buttonframe,
                text=clave,
                value=clave,
                variable=self.selected_direction,
                anchor="w"
            )
            rbtn.pack()

    def update_part(self, _index: int, _key: str):
        PART = self.all_parts[_index]
        if _key == "prog":
            label = PART["prog"].get()
            PART["prog_value"] = self.PROG[label]
        else:
            PART[_key + "_value"] = PART[_key].get()
        
        self.all_parts[_index] = PART
        value = self.all_parts[_index][_key + "_value"]
        print(f"Part {_index} | {_key} = {value}")

    def update_allparts(self):
        for i in range(len(self.all_parts)):
            self.all_parts[i]["index"] = i

    def delete_part(self, _frame: ttk.Frame, _index: int):
        _frame.destroy()
        self.all_parts.pop(_index)
        print(len(self.all_parts))
        self.part_count -= 1
        self.update_allparts()
   
MyGUI()