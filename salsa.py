import music21 as m21
from music21 import stream, clef, instrument, note, duration, tie, scale, key, pitch, tempo, articulations, chord
import tkinter as tk
from enum import Enum

import random

class Salsa:
# --- CLASS VALUES --- #
    class PercMidi(Enum):
        COWBELL = 56
        BONGO_HIGH = 60
        BONGO_LOW = 61
        CONGA_HIGHMUTE = 62
        CONGA_HIGHOPEN = 63
        CONGA_LOW = 64
        AGOGO = 67
        WOODBLOCK = 76

    class Articulation(Enum):
        EMPTY = ''
        ACCENT = 'accent'
        TIE_START = 'start'
        TIE_STOP = 'stop'

    empty: str = Articulation.EMPTY.value
    accent: str = Articulation.ACCENT.value
    tie_start: str = Articulation.TIE_START.value
    tie_stop: str = Articulation.TIE_STOP.value

    cb: int = PercMidi.COWBELL.value
    b_h: int = PercMidi.BONGO_HIGH.value
    b_l: int = PercMidi.BONGO_LOW.value
    c_hm: int = PercMidi.CONGA_HIGHMUTE.value
    c_ho: int = PercMidi.CONGA_HIGHOPEN.value
    c_l: int = PercMidi.CONGA_LOW.value
    agb: int = PercMidi.AGOGO.value
    wb: int = PercMidi.WOODBLOCK.value

    sixteenth: float = .25 #Sechzehntel
    eighth: float = .5 #Achtel
    quarter: int = 1 #Viertel
    dotquarter: float = 1.5 #Punktierte Viertel
    half: int = 2 #Halbe
    full: int = 4 #Ganze

    is_note: bool = True
    is_rest: bool = False

    harm: str = "harm"
    perc: str = "perc"


# --- PRE-SET DICTIONARIES --- #
    STYLE: dict = {
        "Son Montuno" : {
            "horns" : {
                "forward" : {},
                "reverse" : {
                    "major" : {
                        "one_bar" : {},
                        "two_bar" : {
                            "ii-V" : {
                                "0" : [[[is_note, half, [5]], [is_rest, eighth], [is_note, eighth, [4]], [is_note, eighth, [2]], [is_note, eighth, [1]]],
                                        [[is_rest, eighth], [is_note, eighth, [2]], [is_rest, eighth], [is_note, eighth, [4]], [is_rest, eighth], [is_note, eighth, [5]], [is_rest, eighth], [is_note, eighth, [7]]]],
                                "1" : [[[is_rest, eighth], [is_note, eighth, [6]], [is_note, eighth, [5]], [is_note, eighth, [12]], [is_note, eighth, [9]], [is_note, eighth, [5]], [is_rest, eighth], [is_note, eighth, [4]]],
                                        [[is_rest, eighth], [is_note, eighth, [5]], [is_note, eighth, [6]], [is_note, eighth, [7]], [is_rest, eighth], [is_note, eighth, [-5]], [is_rest, eighth], [is_note, eighth, [0]]]]
                            },
                            "iii-VI" : {
                                "0" : [[[is_note, half, [7]], [is_rest, eighth], [is_note, eighth, [5]], [is_note, eighth, [4]], [is_note, eighth, [3]]],
                                        [[is_rest, eighth], [is_note, eighth, [4]], [is_rest, eighth], [is_note, eighth, [9]], [is_rest, eighth], [is_note, eighth, [4]], [is_rest, eighth], [is_note, eighth, [7]]]]
                            },
                            "VII-I" : {
                                "0" : [[[is_note, full, [0]]],
                                        [[is_rest, dotquarter], [is_note, dotquarter, [7]], [is_note, quarter, [12]]]]
                            },
                            "I-vi-ii-V" : {
                                "0" : [[[is_rest, eighth], [is_note, eighth, [0, 4]], [is_rest, eighth], [is_note, eighth, [0, 4]], [is_note, eighth, [-1, 2]], [is_note, eighth, [-3, 0]], [is_rest, eighth], [is_note, eighth, [-5, -1]]],
                                        [[is_rest, eighth], [is_note, eighth, [-1, 2]], [is_rest, eighth], [is_note, dotquarter, [2, 5]], [is_note, quarter, [-5]]]]
                            },
                            "ii-V-I-I" : {
                                "0" : [[[is_note, eighth, [-5]], [is_note, eighth, [-5]], [is_note, eighth, [-5]], [is_note, eighth, [-1]], [is_note, eighth, [2, 5]], [is_note, eighth, [5, 9]], [is_rest, eighth], [is_note, eighth, [4, 7]]],
                                        [[is_rest, eighth], [is_note, eighth, [0, 4]], [is_rest, quarter], [is_rest, quarter], [is_rest, eighth], [is_note, eighth, [0, 4]]]],
                                "1" : [[[is_note, eighth, [-5]], [is_note, eighth, [-5]], [is_note, eighth, [-5]], [is_note, eighth, [-1]], [is_note, eighth, [2, 5]], [is_note, eighth, [5, 9]], [is_rest, eighth], [is_note, eighth, [4, 7]]],
                                        [[is_rest, eighth], [is_note, eighth, [0, 4]], [is_rest, quarter], [is_rest, half]]]
                            }
                        }
                    }
                }
            },
            "piano" : {
                "forward" : {
                    "major" : {
                        "one_bar" : {
                            "progression" : {
                                "arpeggio" : {

                                },
                                "chords" : {

                                },
                                "montuno" : {

                                }     
                            }
                        },
                        "two_bar" : {
                            "I-I" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 4, 9, 12), [empty, empty]], [is_note, quarter, (0, 4, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7, 11), [empty, tie_start]], [is_note, half, (-1, 4, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 4, 9, 12), [empty, empty]], [is_note, quarter, (0, 4, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, quarter, (0, 4, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "ponche" : {
  
                                }
                            },
                            "I-ii" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, quarter, (2, 7, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, quarter, (2, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 9, 14), [empty, empty]], [is_note, dotquarter, (2, 7, 9, 14), [empty, empty]], [is_note, quarter, (2, 7, 9, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 9), [empty, empty]], [is_note, quarter, (2, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7, 11), [empty, tie_start]], [is_note, half, (-1, 4, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, quarter, (0, 7, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }      
                            }, 
                            "I-IV" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, quarter, (0, 7, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7, 11), [empty, tie_start]], [is_note, half, (-1, 4, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 7, 9, 12), [empty, empty]], [is_note, quarter, (0, 7, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 9), [empty, empty]], [is_note, dotquarter, (0, 7, 9), [empty, empty]], [is_note, quarter, (0, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (7, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (7, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }                                                        
                            }, 
                            "I-V" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, quarter, (2, 7, 11, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7, 11), [empty, tie_start]], [is_note, half, (-1, 4, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 7, 9, 11), [empty, empty]], [is_note, dotquarter, (-1, 7, 9, 11), [empty, empty]], [is_note, quarter, (-1, 7, 9, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 7, 9), [empty, empty]], [is_note, dotquarter, (-1, 7, 9), [empty, empty]], [is_note, quarter, (-1, 7, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-3, 9), [empty, empty]]],
                                                  [[is_note, quarter, (-3, 9), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-3, 9), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-3,), [empty, empty]]],
                                                  [[is_note, quarter, (-3,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-3,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 4, 7, 11), [empty, tie_start]], [is_note, half, (-1, 4, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-3, 2, 7, 9), [empty, empty]], [is_note, dotquarter, (-3, 2, 7, 9), [empty, empty]], [is_note, quarter, (-3, 2, 7, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 4, 7), [empty, tie_start]], [is_note, half, (-1, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-3, 2, 7), [empty, empty]], [is_note, dotquarter, (-3, 2, 7), [empty, empty]], [is_note, quarter, (-3, 2, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                  [[is_note, quarter, (-3, 9), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-3,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-3,), [empty, tie_start]]]]
                                    }
                                }                           
                            }, 
                            "ii-V" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,)]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,)]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                [[is_note, eighth, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, half, (0, 5, 9, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 9, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9, 11), [empty, empty]], [is_note, dotquarter, (-1, 5, 9, 11), [empty, empty]], [is_note, quarter, (-1, 5, 9, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0, 12), [empty, tie_stop]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                [[is_note, eighth, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                }
                            }, 
                            "iii-VI" : {#STAND 260217 - ALL DONE | NO PONCHE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3,), [empty, empty]]],
                                                   [[is_note, eighth, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, tie_stop]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3,), [empty, empty]]],
                                                  [[is_note, eighth, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 2, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-3, 1, 7), [empty, empty]], [is_note, dotquarter, (-3, 1, 7), [empty, empty]], [is_note, quarter, (-3, 1, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]], [is_note, dotquarter, (-1, 2, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-3, 1, 7), [empty, empty]], [is_note, dotquarter, (-3, 1, 7), [empty, empty]], [is_note, quarter, (-3, 1, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-1,), [empty, tie_stop]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3,), [empty, empty]]],
                                                   [[is_note, eighth, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (-1,), [empty, tie_stop]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3,), [empty, empty]]],
                                                  [[is_note, eighth, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1,), [empty, tie_start]]]]
                                    }                         
                                }
                            }, 
                            "V-I" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11, 14), [empty, tie_start]], [is_note, half, (2, 7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 7, 12), [empty, empty]], [is_note, dotquarter, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (0, 4, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }                    
                            },
                            "V-IV" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11, 14), [empty, tie_start]], [is_note, half, (2, 7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 9, 12), [empty, empty]], [is_note, dotquarter, (0, 5, 9, 12), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, dotquarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }
                            }, 
                            "I-IV-V-IV" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        "left" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (0, 4, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9)], [is_note, eighth, (2, 14), [empty, empty]]],
                                                    [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9)], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "4" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (0, 4, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (0, 4, 7), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                    [[is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                }                             
                            },
                            "I-vi-ii-V" : { #STAND 270217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        "left" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9, 14), [empty, empty]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, quarter, (2, 7, 11, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_rest, eighth], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 4, 7, 12), [empty, tie_start]], [is_note, half, (0, 4, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9, 14), [empty, empty]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, quarter, (2, 7, 11, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 4, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                }
                            }, 
                            "ii-V-I-I" : { #STAND 260217 - ALL DONE | NO PONCHE | S. 75
                                "0" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7), [empty, empty]], [is_note, dotquarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7), [empty, empty]], [is_note, dotquarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : { 
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, half, (0, 5, 9, 12), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7, 11), [empty, empty]], [is_note, dotquarter, (-3, 4, 7, 9), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7), [empty, empty]], [is_note, dotquarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : { 
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }
                            },
                            "V-IV-I-IV" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : { #V-IV-I-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7), [empty, empty]], [is_note, dotquarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 4, 7), [empty, empty]], [is_note, dotquarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #V-IV-I-ii Contrary Motion 
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, eighth, (14), [empty, empty]], [is_note, eighth, (19,), [empty, empty]], [is_note, quarter, (9, 21), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]]],
                                                   [[is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (12,), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (5, 17), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, eighth, (5, 17), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (7,), [empty, tie_stop]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (11, 14, 19, 23), [empty, tie_start]], [is_note, half, (11, 14, 19, 23), [empty, tie_stop]], [is_note, dotquarter, (9, 12, 17, 21), [empty, empty]]],
                                                  [[is_note, dotquarter, (4, 7, 12, 16), [empty, empty]], [is_note, dotquarter, (5, 9, 14, 17), [empty, empty]], [is_note, quarter, (5, 9, 14, 17), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (7, 11, 14), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]], [is_note, dotquarter, (5, 9, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 4, 7), [empty, empty]], [is_note, dotquarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (9, 21), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]]],
                                                   [[is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (12,), [empty, empty]], [is_note, eighth, (4, 16), [empty, empty]], [is_note, eighth, (5, 17), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, eighth, (5, 17), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (7,), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (9,), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                }                                    
                            }   
                        }
                    },
                    "minor" : {
                        "one_bar" : {
                            "progression" : {
                                "arpeggio" : {

                                },
                                "chords" : {

                                },
                                "montuno" : {

                                }     
                            }
                        },
                        "two_bar" : {
                            "i-i" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7, 10), [empty, tie_start]], [is_note, half, (-2, 3, 7, 10), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 3, 8, 12), [empty, empty]], [is_note, quarter, (0, 3, 8, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }
                            },
                            "i-ii" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 8, 14), [empty, empty]], [is_note, dotquarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7, 10), [empty, tie_start]], [is_note, half, (-2, 3, 7, 10), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }      
                            }, 
                            "i-iv" : { #STAND 261217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7, 10), [empty, tie_start]], [is_note, half, (-2, 3, 7, 10), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }                                                        
                            }, 
                            "i-V" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, quarter, (2, 7, 11, 14), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (0, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, quarter, (2, 7, 11), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7, 10), [empty, tie_start]], [is_note, half, (-2, 3, 7, 10), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 2, 7, 11), [empty, empty]], [is_note, dotquarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 2, 7), [empty, empty]], [is_note, dotquarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 3, 7, 10), [empty, tie_start]], [is_note, half, (-2, 3, 7, 10), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 2, 5, 11), [empty, empty]], [is_note, dotquarter, (-1, 2, 5, 11), [empty, empty]], [is_note, quarter, (-1, 2, 5, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 3, 7), [empty, tie_start]], [is_note, half, (-2, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 2, 7), [empty, empty]], [is_note, dotquarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, empty]]],
                                                  [[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, empty]]],
                                                  [[is_note, quarter, (-1,), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                }                           
                            }, 
                            "ii-V" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,)]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,)]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                [[is_note, eighth, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 8, 12), [empty, tie_start]], [is_note, half, (0, 5, 8, 12), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9, 11), [empty, empty]], [is_note, dotquarter, (-1, 5, 9, 11), [empty, empty]], [is_note, quarter, (-1, 5, 9, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, dotquarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0, 12), [empty, tie_stop]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]],
                                                [[is_note, eighth, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (0,), [empty, tie_stop]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]],
                                                [[is_note, eighth, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, tie_start]]]]
                                    }
                                }
                            }, 
                            "III-VI" : {#STAND 260217 - ALL DONE | NO PONCHE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (-2,), [empty, tie_stop]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                [[is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]    
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (-2, 2, 7), [empty, tie_start]], [is_note, half, (-2, 2, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 2, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2, 2, 7), [empty, tie_start]], [is_note, half, (-2, 2, 7), [empty, tie_stop]], [is_note, dotquarter, (-2, 2, 7), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, dotquarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-2,), [empty, tie_stop]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (-2,), [empty, tie_stop]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                [[is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }                         
                                }
                            }, 
                            "V-i" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11, 14), [empty, tie_start]], [is_note, half, (2, 7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7, 12), [empty, empty]], [is_note, dotquarter, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (0, 3, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }                    
                            },
                            "V-iv" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (2, 7, 11, 14), [empty, tie_start]], [is_note, half, (2, 7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, dotquarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (2, 7, 11), [empty, tie_start]], [is_note, half, (2, 7, 11), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, dotquarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, eighth, (2, 14), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]],
                                                  [[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (2,), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, quarter, (0,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]]
                                    }
                                }
                            }, 
                            "i-iv-V-iv" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        "left" : [[[is_rest, eighth], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]]],
                                        }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "2" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (0, 3, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8)], [is_note, eighth, (2, 14), [empty, empty]]],
                                                    [[is_note, quarter, (2, 14), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8)], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_rest, eighth], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "3" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                   [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                },
                                "4" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                   [[is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11, 14), [empty, empty]], [is_note, dotquarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (0, 3, 7, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]], [is_note, dotquarter, (2, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (2, 7, 11), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (0, 3, 7), [empty, empty]]]],
                                        },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                    [[is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                    [[is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]]],
                                        }
                                }                             
                            }, 
                            "ii-V-i-i" : { #STAND 260217 - ALL DONE | NO PONCHE | S. 75
                                "0" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-2, 3, 7), [empty, empty]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-2, 4, 7), [empty, empty]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]]]]
                                    },
                                    "montuno" : { 
                                        "right": [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (0, 5, 8, 12), [empty, tie_start]], [is_note, half, (0, 5, 8, 12), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11, 14), [empty, empty]]],
                                                  [[is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]], [is_note, dotquarter, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (-2, 3, 7, 10), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]], [is_note, dotquarter, (2, 7, 11), [empty, empty]]],
                                                  [[is_note, dotquarter, (-2, 4, 7), [empty, empty]], [is_note, dotquarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]]]]
                                    },
                                    "montuno" : { 
                                        "right": [[[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2, 14), [empty, empty]]],
                                                  [[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2, 10), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (2,), [empty, empty]]],
                                                  [[is_note, quarter, (-2,), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2,), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2,), [empty, tie_start]]]]
                                    }
                                }
                            },
                            "V-iv-i-iv" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0" : { #V-IV-I-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (7, 11, 14), [empty, tie_start]], [is_note, half, (7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (7, 11, 14), [empty, tie_start]], [is_note, half, (7, 11, 14), [empty, tie_stop]], [is_note, dotquarter, (0, 5, 8), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]],
                                        "left" : [[[is_note, quarter, (7,), [empty, tie_stop]], [is_note, eighth, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                    [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, quarter, (2,), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                },
                                "1" : { #V-IV-I-ii Contrary Motion 
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, eighth, (14,), [empty, empty]], [is_note, eighth, (19,), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]]],
                                                   [[is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (12,), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (5, 17), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, eighth, (5, 17), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (7,), [empty, tie_stop]], [is_note, eighth, (11,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, eighth, (11, 14, 19, 23), [empty, tie_start]], [is_note, half, (11, 14, 19, 23), [empty, tie_stop]], [is_note, dotquarter, (8, 12, 17, 20), [empty, empty]]],
                                                  [[is_note, dotquarter, (3, 7, 12, 15), [empty, empty]], [is_note, dotquarter, (5, 8, 14, 17), [empty, empty]], [is_note, quarter, (5, 8, 14, 17), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (7, 11, 14), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]], [is_note, dotquarter, (5, 8, 12), [empty, empty]]],
                                                  [[is_note, dotquarter, (0, 3, 7), [empty, empty]], [is_note, dotquarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]]],
                                                   [[is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (12,), [empty, empty]], [is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (5, 17), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (14,), [empty, empty]], [is_note, eighth, (5, 17), [empty, tie_start]]]],
                                        "left" : [[[is_note, eighth, (7,), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5,), [empty, empty]], [is_note, eighth, (8, 12), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]]],
                                                  [[is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (3,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, eighth, (0,), [empty, empty]], [is_note, eighth, (2,), [empty, empty]], [is_note, eighth, (5,), [empty, empty]], [is_note, eighth, (8,), [empty, empty]], [is_note, eighth, (2,), [empty, tie_start]]]]
                                    }
                                }                                    
                            }   
                        }
                    }
                },
                "reverse" : {
                    "major" : {
                        "one_bar" : {
                            "progression" : {
                                "arpeggio" : {

                                },
                                "chords" : {

                                },
                                "montuno" : {

                                }     
                            }
                        },
                        "two_bar" : {
                            "I-I" : { #STAND 260219 - ALL DONE
                                "0" : { #Imaj7 - Imaj6
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, half, (0, 4, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, half, (0, 4, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : { 
                                    "0" : {#Imaj7 - Imaj6
                                            "arpeggio" : {
                                                "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                                "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                            },
                                            "chords" : {
                                                "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, quarter, (0, 4, 9), [empty, tie_stop]], [is_note, eighth, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, empty]]]],
                                                "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, quarter, (0, 4, 9), [empty, tie_stop]], [is_note, eighth, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, empty]]]]
                                            },
                                            "montuno" : {
                                                "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                                "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                            }
                                    }
                                }
                            },
                            "I-ii" : { #STAND 260219 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : { 
                                    "0" : {
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, quarter, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, quarter, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    }
                                }
                            }, 
                            "I-IV" : { #STAND 260219 - ALL DONE 
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, half, (0, 4, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, half, (0, 4, 9), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (0, 4, 9, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 4, 9, 12), [empty, empty]], [is_note, eighth, (0, 4, 9, 12), [empty, tie_start]], [is_note, half, (0, 4, 9, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, half, (0, 4, 9), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, quarter, (0, 4, 9), [empty, tie_stop]], [is_note, eighth, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, quarter, (0, 4, 9), [empty, tie_stop]], [is_note, eighth, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                        }
                                    },
                                    "1":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (0, 4, 9, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 4, 9, 12), [empty, empty]], [is_note, eighth, (0, 4, 9, 12), [empty, tie_start]], [is_note, quarter, (0, 4, 9, 12), [empty, tie_stop]], [is_note, eighth, (0, 4, 9, 12), [empty, empty]], [is_note, eighth, (0, 4, 9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 9), [empty, tie_stop]], [is_note, quarter, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, tie_start]], [is_note, quarter, (0, 4, 9), [empty, tie_stop]], [is_note, eighth, (0, 4, 9), [empty, empty]], [is_note, eighth, (0, 4, 9), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]], [is_note, eighth, (4, 9), [empty, empty]]]]
                                        }
                                    }                                  
                                }                       
                            }, 
                            "I-V" : { #STAND 260219 - ALL DONE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7, 11), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]], [is_note, half, (-1, 2, 7, 11), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, quarter, (-1, 2, 7), [empty, tie_stop]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, quarter, (-1, 2, 7), [empty, tie_stop]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]]
                                        }
                                    },
                                    "1":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7, 11), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]], [is_note, quarter, (-1, 2, 7, 11), [empty, tie_stop]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, quarter, (-1, 2, 7), [empty, tie_stop]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]]]]
                                        }
                                    } 
                                }                       
                            }, 
                            "ii-V" : { #STAND 260219 - ALL DONE
                                "0" : { #iimin7 - Vmaj7
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 9), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 9), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1" : { #iimin7 - Vmaj7b5b9
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : { #iimin7 - Vmaj7
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 9), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, quarter, (-1, 5, 9), [empty, tie_stop]], [is_note, eighth, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 9), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, quarter, (-1, 5, 9), [empty, tie_stop]], [is_note, eighth, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    },
                                    "1" : { #iimin7 - Vmaj7b5b9
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]]]]
                                        
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, quarter, (-1, 5, 8), [empty, tie_stop]], [is_note, eighth, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, quarter, (-1, 5, 8), [empty, tie_stop]], [is_note, eighth, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]]]]
                                        }
                                    }                                   
                                }
                            }, 
                            "iii-VI" : { #STAND 260219 - ALL DONE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3, 1, 7), [empty, tie_stop]], [is_note, quarter, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]], [is_note, half, (-3, 1, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3, 1, 7), [empty, tie_stop]], [is_note, quarter, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]], [is_note, half, (-3, 1, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                    }                         
                                },
                                "ponche" : {
                                    "0": { #Minor Seventh - Minor Seventh
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3, 1, 7), [empty, tie_stop]], [is_note, quarter, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]], [is_note, quarter, (-3, 1, 7), [empty, tie_stop]], [is_note, eighth, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3, 1, 7), [empty, tie_stop]], [is_note, quarter, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, tie_start]], [is_note, quarter, (-3, 1, 7), [empty, tie_stop]], [is_note, eighth, (-3, 1, 7), [empty, empty]], [is_note, eighth, (-3, 1, 7), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]]
                                        }                         
                                    }                                    
                                }
                            }, 
                            "V-I" : { #STAND 260219 - ALL DONE 
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 7, 12), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, half, (0, 4, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, quarter, (0, 4, 7), [empty, tie_stop]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, quarter, (0, 4, 7), [empty, tie_stop]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        }
                                    },
                                    "1":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 7, 12), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, quarter, (0, 4, 7), [empty, tie_stop]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 4, 7), [empty, tie_stop]], [is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, tie_start]], [is_note, quarter, (0, 4, 7), [empty, tie_stop]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        }
                                    }  
                                }                                                   
                            }, 
                            "V-IV" : { #STAND 260219 - ALL DONE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, half, (0, 5, 9, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, quarter, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, quarter, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    },
                                    "1":{
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, quarter, (0, 5, 9, 12), [empty, tie_stop]], [is_note, eighth, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, quarter, (0, 5, 9), [empty, tie_stop]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]]]]                                        
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0, 12), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    }
                                }                        
                            }, 
                            "VII-I" : { #STAND 260216 - ALL DONE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                    [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-4, 0, 3, 8), [empty, empty]], [is_note, eighth, (-4, 0, 3, 8), [empty, empty]], [is_note, quarter, (-4, 0, 3, 8), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-4, 8), [empty, empty]], [is_note, eighth, (0, 3), [empty, empty]], [is_note, quarter, (-4, 8), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                    }                         
                                },
                                "ponche" : {
                                    "0": {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-3), [empty, tie_start]]],
                                                        [[is_note, eighth, (-3), [empty, tie_stop]], [is_note, quarter, (1, 7), [empty, empty]], [is_note, dotquarter, (-3), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]], [is_note, eighth, (1, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-4, 0, 3, 8), [empty, empty]], [is_note, eighth, (-4, 0, 3, 8), [empty, empty]], [is_note, quarter, (-4, 0, 3, 8), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-4, 8), [empty, empty]], [is_note, eighth, (0, 3), [empty, empty]], [is_note, quarter, (-4, 8), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                        }                        
                                    }                                    
                                }                    
                            },
                            "I-vi-ii-V" : { #STAND 260219 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-1,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]],
                                                    [[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]],
                                                    [[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1,), [empty, empty]], [is_note, eighth, (4,), [empty, empty]], [is_note, eighth, (7,), [empty, empty]], [is_note, quarter, (-3,), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0,), [empty, tie_start]]],
                                                    [[is_note, eighth, (0,), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1,), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1,), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7, 9), [empty, empty]], [is_note, quarter, (-3, 4, 7, 9), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (-1, 5, 9, 11), [empty, tie_start]], [is_note, half, (-1, 5, 9, 11), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, half, (-1, 5, 9), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    },
                                    "1" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1, 11), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-1, 4, 7, 11), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7, 9), [empty, empty]], [is_note, quarter, (-3, 4, 7, 9), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 9, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (-1, 5, 9, 11), [empty, tie_start]], [is_note, quarter, (-1, 5, 9, 11), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9, 11), [empty, empty]], [is_note, quarter, (-1, 5, 9, 11), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 9), [empty, tie_stop]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]], [is_note, quarter, (-1, 5, 9), [empty, tie_stop]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3, 9), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1, 11), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, dotquarter, (-1), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]]]]
                                        }
                                    }                                    
                                }
                            },
                            "I-IV-V-IV" : { #STAND 260219 -  DONE
                                "0" : { #I-IV-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1" : { #I-IV-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, half, (5, 9, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "2" : { #I-ii-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, half, (5, 9, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "3" : { #I-ii-V-ii
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, half, (5, 9, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "4" : { #I-ii-V-IV with Harmonization
                                    "arpeggio" : {
                                        "right" : [[[is_note, quarter, (4, 16), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (9, 21), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (4, 7, 12, 16), [empty, empty]], [is_note, eighth, (4, 7, 12, 16), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (11, 14, 19, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 14, 19, 23), [empty, tie_stop]], [is_note, quarter, (11, 14, 19, 23), [empty, empty]], [is_note, eighth, (9, 12, 17, 21), [empty, tie_start]], [is_note, half, (9, 12, 17, 21), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, half, (5, 9, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (4, 16), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (9, 21), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "5" : { #I-IV-V-IV bisi spicy                                   
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (4, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (9)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                   [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (9)], [is_note, eighth, (4, 12)], [is_note, eighth, (4, 12)]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                  [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (4, 7, 9, 12), [empty, empty]], [is_note, eighth, (4, 7, 9, 12), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (5, 7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (5, 7, 11, 14), [empty, tie_stop]], [is_note, quarter, (5, 7, 11, 14), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, half, (0, 5, 9, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (4, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (9)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                   [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (9)], [is_note, eighth, (4, 12)], [is_note, eighth, (4, 12)]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                  [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : { #I-IV-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        }
                                    },
                                    "1" : { #I-IV-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, quarter, (5, 9, 12, 17), [empty, tie_stop]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, quarter, (5, 9, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        }
                                    },
                                    "2" : { #I-ii-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, quarter, (5, 9, 12, 17), [empty, tie_stop]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        }
                                    },
                                    "3" : { #I-ii-V-ii
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 4, 7, 12), [empty, empty]], [is_note, eighth, (0, 4, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, quarter, (2, 5, 9, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, tie_start]], [is_note, quarter, (5, 9, 12, 17), [empty, tie_stop]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (5, 9, 12, 17), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5, 17)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        }
                                    },
                                    "4" : { #I-ii-V-IV with Harmonization
                                        "arpeggio" : {
                                            "right" : [[[is_note, quarter, (4, 16), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, dotquarter, (9, 21)], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (4, 7, 12, 16), [empty, empty]], [is_note, eighth, (4, 7, 12, 16), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, quarter, (5, 9, 12, 17), [empty, empty]], [is_note, eighth, (11, 14, 19, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 14, 19, 23), [empty, tie_stop]], [is_note, quarter, (11, 14, 19, 23), [empty, empty]], [is_note, eighth, (9, 12, 17, 21), [empty, tie_start]], [is_note, quarter, (9, 12, 17, 21), [empty, tie_stop]], [is_note, eighth, (9, 12, 17, 21), [empty, empty]], [is_note, eighth, (9, 12, 17, 21), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, quarter, (2, 5, 9), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, tie_start]], [is_note, quarter, (5, 9, 12), [empty, tie_stop]], [is_note, eighth, (5, 9, 12), [empty, empty]], [is_note, eighth, (5, 9, 12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (4, 16), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (9, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, dotquarter, (9, 21)], [is_note, eighth, (12, 17), [empty, empty]], [is_note, eighth, (12, 17), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, dotquarter, (5)], [is_note, eighth, (9, 12), [empty, empty]], [is_note, eighth, (9, 12), [empty, empty]]]]
                                        }
                                    },
                                    "5" : { #I-IV-V-IV bisi spicy 260219 PURGE ÜBERLEBT                                  
                                        "arpeggio" : {
                                            "right" : [[[is_rest, eighth], [is_note, eighth, (4, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (9)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                    [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (9)], [is_note, eighth, (4, 12)], [is_note, eighth, (4, 12)]]],
                                            "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (4, 7, 9, 12), [empty, empty]], [is_note, eighth, (4, 7, 9, 12), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, quarter, (0, 5, 9, 12), [empty, empty]], [is_note, eighth, (5, 7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (5, 7, 11, 14), [empty, tie_stop]], [is_note, quarter, (5, 7, 11, 14), [empty, empty]], [is_note, eighth, (0, 5, 9, 12), [empty, tie_start]], [is_note, half, (0, 5, 9, 12), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 4, 7), [empty, empty]], [is_note, eighth, (0, 4, 7), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, tie_start]], [is_note, half, (0, 5, 9), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_rest, eighth], [is_note, eighth, (4, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (9)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                    [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (9)], [is_note, eighth, (4, 12)], [is_note, eighth, (4, 12)]]],
                                            "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (4), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    }          
                                }
                            },
                            "ii-V-I-I" : { #STAND 260219 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 4, 7), [empty, tie_stop]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]], [is_note, half, (-3, 4, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 4, 7), [empty, tie_stop]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, tie_start]], [is_note, half, (-3, 4, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, quarter, (-3), [empty, empty]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (-3)], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (-3)], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 4, 7), [empty, tie_stop]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 9), [empty, empty]], [is_note, eighth, (0, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, quarter, (-1, 5, 9), [empty, empty]], [is_note, eighth, (-1, 4, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 4, 7), [empty, tie_stop]], [is_note, quarter, (-1, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]], [is_note, eighth, (-3, 4, 7), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (-3)], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 9), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (4, 7), [empty, empty]], [is_note, dotquarter, (-3)], [is_note, eighth, (4, 7), [empty, empty]], [is_note, eighth, (4, 7), [empty, empty]]]]
                                        }
                                    }                                
                                }
                            }
                        }
                    },
                    "minor" : {
                        "one_bar" : {
                            "progression" : {
                                "arpeggio" : {

                                },
                                "chords" : {

                                },
                                "montuno" : {

                                }     
                            }
                        },
                        "two_bar" : {
                            "i-i" : { #STAND 260216 - ALL DONE
                                "0" : { #imin7 - imin6
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : { 
                                    "0" : {#Imaj7 - Imaj6
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    }
                                }
                            },
                            "i-ii" : { #STAND 260217 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : { 
                                    "0" : {
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    }
                                }
                            }, 
                            "i-iv" : { #STAND 260216 - ALL DONE | NO PONCHE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (0, 3, 8, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8, 12), [empty, tie_stop]], [is_note, quarter, (0, 3, 8, 12), [empty, empty]], [is_note, eighth, (0, 3, 8, 12), [empty, tie_start]], [is_note, half, (0, 3, 8, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 8), [empty, tie_stop]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, eighth, (0, 3, 8), [empty, tie_start]], [is_note, half, (0, 3, 8), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                }                       
                            }, 
                            "i-V" : { #STAND 260217 - ALL DONE | NO PONCHE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-2, 10), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7, 11), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]], [is_note, half, (-1, 2, 7, 11), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2, 10), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1, 11), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                  [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                }                       
                            }, 
                            "ii-V" : { #STAND 260216 - ALL DONE
                                "0" : { #iidim min7 - Vmaj7
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1" : { #iimin7 - Vmaj7b5b9
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                    [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : { #iidim min7 - Vmaj7
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 9), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 2, 7), [empty, tie_stop]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        }
                                    },
                                    "1" : { #iimin7 - Vmaj7b5b9
                                        "arpeggio" : {
                                            "right": [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (9), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        
                                        },
                                        "chords" : {
                                            "right": [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1, 5, 8), [empty, tie_stop]], [is_note, quarter, (-1, 5, 8), [empty, empty]], [is_note, eighth, (-1, 5, 8), [empty, tie_start]], [is_note, half, (-1, 5, 8), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right": [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, tie_start]]],
                                                        [[is_note, eighth, (-1), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        }
                                    }                                   
                                }
                            }, 
                            "III-VI" : { #STAND 260216 - ALL DONE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4, 0, 7), [empty, tie_stop]], [is_note, quarter, (-4, 0, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]], [is_note, half, (-4, 0, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4, 0, 7), [empty, tie_stop]], [is_note, quarter, (-4, 0, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]], [is_note, half, (-4, 0, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                    [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                    }                         
                                },
                                "ponche" : {
                                    "0": { #Minor Seventh - Minor Seventh
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4, 0, 7), [empty, tie_stop]], [is_note, quarter, (-4, 0, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]], [is_note, half, (-4, 0, 7), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, quarter, (-2, 2, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4, 0, 7), [empty, tie_stop]], [is_note, quarter, (-4, 0, 7), [empty, empty]], [is_note, eighth, (-4, 0, 7), [empty, tie_start]], [is_note, half, (-4, 0, 7), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-4), [empty, tie_start]]],
                                                        [[is_note, eighth, (-4), [empty, tie_stop]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (0, 7), [empty, empty]], [is_note, eighth, (1), [empty, empty]]]]
                                        }                        
                                    }                                    
                                }
                            }, 
                            "V-i" : { #STAND 260216 - ALL DONE | NO PONCHE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 7), [empty, tie_stop]], [is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 7), [empty, tie_stop]], [is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 7, 12), [empty, tie_stop]], [is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, tie_start]], [is_note, half, (0, 3, 7, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 3, 7), [empty, tie_stop]], [is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, tie_start]], [is_note, half, (0, 3, 7), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]]
                                    }
                                }                                                   
                            }, 
                            "V-iv" : { #STAND 260216 - ALL DONE | NO PONCHE
                                "0":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1":{
                                    "arpeggio" : {
                                        "right": [[[is_note, eighth, (-1, 11), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-1), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right": [[[is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, quarter, (-1, 2, 7, 11), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]], [is_note, half, (0, 5, 8, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]                                        
                                    },
                                    "montuno" : {
                                        "right": [[[is_note, quarter, (-1, 11), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                  [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-1), [empty, empty]], [is_note, eighth, (2, 7), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                }                        
                            }, 
                            "VII-i" : { #STAND 260216 - ALL DONE
                                "0": { #Minor Seventh - Minor Seventh
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                   [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                  [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, eighth, (-2, 2, 5, 8), [empty, empty]], [is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, eighth, (-2, 2, 5, 8), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-4, 8), [empty, empty]], [is_note, eighth, (0, 3), [empty, empty]], [is_note, quarter, (-4, 8), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                    [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                    }                         
                                },
                                "ponche" : {
                                    "0": {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (2), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, eighth, (-2, 2, 5, 8), [empty, empty]], [is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, quarter, (-2, 2, 5, 8), [empty, empty]], [is_note, eighth, (-2, 2, 5, 8), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-4, 8), [empty, empty]], [is_note, eighth, (0, 3), [empty, empty]], [is_note, quarter, (-4, 8), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (2, 5), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (2, 5), [empty, empty]], [is_note, eighth, (-2), [empty, empty]]],
                                                        [[is_note, dotquarter, (0), [empty, empty]], [is_note, dotquarter, (7), [empty, empty]], [is_note, quarter, (12), [empty, empty]]]]
                                        }                         
                                    }                                    
                                }                    
                            },
                            "i-VI-ii-V" : { #STAND 260216 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "1" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (-2, 10), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (0, 3, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]], [is_note, half, (-1, 2, 7, 11), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                   [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                    [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (0, 3, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        }
                                    },
                                    "1" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (-2, 10), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (-2), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (-2, 3, 7, 10), [empty, empty]], [is_note, eighth, (-2, 3, 7, 10), [empty, empty]], [is_note, quarter, (0, 3, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 8, 12), [empty, tie_stop]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (-1, 2, 7, 11), [empty, tie_start]], [is_note, half, (-1, 2, 7, 11), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, quarter, (-3, 4, 7), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]]],
                                                        [[is_note, eighth, (0, 5, 8), [empty, tie_stop]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (-1, 2, 7), [empty, tie_start]], [is_note, half, (-1, 2, 7), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (-2, 10), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0, 12), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0, 12), [empty, tie_start]]],
                                                    [[is_note, eighth, (0, 12), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1, 11), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1, 11), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (-2), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (0), [empty, empty]], [is_note, quarter, (3, 8), [empty, empty]], [is_note, eighth, (0), [empty, tie_start]]],
                                                        [[is_note, eighth, (0), [empty, tie_stop]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-1), [empty, empty]]]]
                                        }
                                    }                                    
                                }
                            },
                            "i-iv-V-iv" : { #STAND 260216 - ALL DONE
                                "0" : { #I-IV-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "1" : { #I-IV-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "2" : { #I-ii-V-IV
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "3" : { #I-ii-V-ii
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "4" : { #I-ii-V-IV with Harmonization
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (3, 7, 12, 15), [empty, empty]], [is_note, eighth, (3, 7, 12, 15), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, eighth, (11, 14, 19, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 14, 19, 23), [empty, tie_stop]], [is_note, quarter, (11, 14, 19, 23), [empty, empty]], [is_note, eighth, (8, 12, 17, 20), [empty, tie_start]], [is_note, half, (8, 12, 17, 20), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (3, 15), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                    [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "5" : { #I-IV-V-IV bisi spicy                                   
                                    "arpeggio" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (3, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (8)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (10), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                   [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (8)], [is_note, eighth, (3, 12)], [is_note, eighth, (3, 12)]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                  [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (3, 7, 8, 12), [empty, empty]], [is_note, eighth, (3, 7, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (5, 7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (5, 7, 11, 14), [empty, tie_stop]], [is_note, quarter, (5, 7, 11, 14), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]], [is_note, half, (0, 5, 8, 12), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                    [[is_note, eighth, (7, 11), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]
                                    },
                                    "montuno" : {
                                        "right" : [[[is_rest, eighth], [is_note, eighth, (3, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (8)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (10), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                   [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (8)], [is_note, eighth, (3, 12)], [is_note, eighth, (3, 12)]]],
                                        "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                  [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : { #I-IV-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    },
                                    "1" : { #I-IV-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, quarter, (5, 8, 12), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5)], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    },
                                    "2" : { #I-ii-V-IV
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    },
                                    "3" : { #I-ii-V-ii
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0, 12), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 9), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 3, 7, 12), [empty, empty]], [is_note, eighth, (0, 3, 7, 12), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, quarter, (2, 5, 8, 14), [empty, empty]], [is_note, eighth, (7, 11, 14, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14, 19), [empty, tie_stop]], [is_note, quarter, (7, 11, 14, 19), [empty, empty]], [is_note, eighth, (5, 8, 12, 17), [empty, tie_start]], [is_note, half, (5, 8, 12, 17), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, [7, 11, 14], [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0, 12), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2, 14), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7, 19), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 19), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    },
                                    "4" : { #I-ii-V-IV with Harmonization
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (3, 15), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (3, 7, 12, 15), [empty, empty]], [is_note, eighth, (3, 7, 12, 15), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, quarter, (5, 8, 12, 17), [empty, empty]], [is_note, eighth, (11, 14, 19, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 14, 19, 23), [empty, tie_stop]], [is_note, quarter, (11, 14, 19, 23), [empty, empty]], [is_note, eighth, (8, 12, 17, 20), [empty, tie_start]], [is_note, half, (8, 12, 17, 20), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, quarter, (2, 5, 8), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11, 14), [empty, tie_stop]], [is_note, quarter, (7, 11, 14), [empty, empty]], [is_note, eighth, (5, 8, 12), [empty, tie_start]], [is_note, half, (5, 8, 12), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (3, 15), [empty, empty]], [is_note, eighth, (7, 12), [empty, empty]], [is_note, quarter, (5, 17), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (11, 23), [empty, tie_start]]],
                                                        [[is_note, eighth, (11, 23), [empty, tie_stop]], [is_note, quarter, (14, 19), [empty, empty]], [is_note, quarter, (8, 20), [empty, empty]], [is_note, quarter, (12, 17), [empty, empty]], [is_note, eighth, (0, 12), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (3, 7), [empty, empty]], [is_note, quarter, (2), [empty, empty]], [is_note, quarter, (5, 8), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                        [[is_note, eighth, (7), [empty, tie_stop]], [is_note, quarter, (11, 14), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, quarter, (8, 12), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    },
                                    "5" : { #I-IV-V-IV bisi spicy                                   
                                        "arpeggio" : {
                                            "right" : [[[is_rest, eighth], [is_note, eighth, (3, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (8)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (10), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                    [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (8)], [is_note, eighth, (3, 12)], [is_note, eighth, (3, 12)]]],
                                            "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (3, 7, 8, 12), [empty, empty]], [is_note, eighth, (3, 7, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, quarter, (0, 5, 8, 12), [empty, empty]], [is_note, eighth, (5, 7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (5, 7, 11, 14), [empty, tie_stop]], [is_note, quarter, (5, 7, 11, 14), [empty, empty]], [is_note, eighth, (0, 5, 8, 12), [empty, tie_start]], [is_note, half, (0, 5, 8, 12), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 3, 7), [empty, empty]], [is_note, eighth, (0, 3, 7), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (7, 11, 14), [empty, tie_start]]],
                                                        [[is_note, eighth, (7, 11), [empty, tie_stop]], [is_note, quarter, (7, 11), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, tie_start]], [is_note, half, (0, 5, 8), [empty, tie_stop]]]]
                                        },
                                        "montuno" : {
                                            "right" : [[[is_rest, eighth], [is_note, eighth, (3, 12), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (8)], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (10), [empty, empty]], [is_note, eighth, (11), [empty, tie_start]]],
                                                    [[is_note, eighth, (11), [empty, tie_stop]], [is_note, eighth, (7)], [is_note, eighth, (11)], [is_note, quarter, (5, 14)], [is_note, eighth, (8)], [is_note, eighth, (3, 12)], [is_note, eighth, (3, 12)]]],
                                            "left" : [[[is_rest, eighth], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (3), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, eighth, (7), [empty, tie_start]]],
                                                    [[is_note, eighth, (7), [empty, tie_stop]], [is_note, eighth, (11), [empty, empty]], [is_note, eighth, (7), [empty, empty]], [is_note, quarter, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, eighth, (0), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    }          
                                }
                            },
                            "ii-V-i-i" : { #STAND 260216 - ALL DONE
                                "0" : {
                                    "arpeggio" : {
                                        "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-4), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    },
                                    "chords" : {
                                        "right" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, tie_start]]],
                                                   [[is_note, eighth, (-2, 3, 7), [empty, tie_stop]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, half, (-2, 3, 7), [empty, tie_stop]]]],
                                        "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, tie_start]]],
                                                   [[is_note, eighth, (-2, 3, 7), [empty, tie_stop]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, half, (-2, 3, 7), [empty, tie_stop]]]],
                                    },
                                    "montuno" : {
                                        "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                        "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                    }
                                },
                                "ponche" : {
                                    "0" : {
                                        "arpeggio" : {
                                            "right" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                        [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, eighth, (0), [empty, empty]], [is_note, eighth, (5), [empty, empty]], [is_note, eighth, (8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                        [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        },
                                        "chords" : {
                                            "right" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2, 3, 7), [empty, tie_stop]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, half, (-2, 3, 7), [empty, tie_stop]]]],
                                            "left" : [[[is_note, quarter, (0, 5, 8), [empty, empty]], [is_note, eighth, (0, 5, 8), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, quarter, (-1, 2, 7), [empty, empty]], [is_note, eighth, (-2, 3, 7), [empty, tie_start]]],
                                                    [[is_note, eighth, (-2, 3, 7), [empty, tie_stop]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, quarter, (-2, 3, 7), [empty, empty]], [is_note, half, (-2, 3, 7), [empty, tie_stop]]]],
                                        },
                                        "montuno" : {
                                            "right" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                        [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]],
                                            "left" : [[[is_note, quarter, (0), [empty, empty]], [is_note, eighth, (5, 8), [empty, empty]], [is_note, quarter, (-1), [empty, empty]], [is_note, quarter, (2, 7), [empty, empty]], [is_note, eighth, (-2), [empty, tie_start]]],
                                                        [[is_note, eighth, (-2), [empty, tie_stop]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, quarter, (-2), [empty, empty]], [is_note, quarter, (3, 7), [empty, empty]], [is_note, eighth, (0), [empty, empty]]]]
                                        }
                                    }                                
                                }
                            }
                        }
                    }
                }
            },
            "bass" : {
                "forward" : {
                    "major" : {
                        "one_bar" : {

                        },
                        "two_bar" : {
                            "I-I" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                        [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "I-ii" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                }
                            },
                            "I-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                } 
                            },
                            "I-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                } 
                            },
                            "ii-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],  
                                },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]]                                   
                                       },                                    
                                "ponche" : {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, empty]]],
                                           [[is_note, dotquarter, -5, [empty, empty]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, empty]]]],
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, empty]]],
                                           [[is_note, dotquarter, -5, [empty, empty]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, empty]]]]                                    
                                }
                            },
                            "iii-VI" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],                                    
                                    #Beides
                                    "5": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                       [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                }
                            },
                            "V-I" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "V-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "VII-I" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "ponche" : {
                                    "0" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                }
                            },
                            "I-IV-V-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "I-vi-ii-V" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                       }
                            },
                            "ii-V-I-I" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],   
                                       }
                            },
                            "V-IV-I-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            }
                        }
                    },
                    "minor" : {
                        "one_bar" : {

                        },
                        "two_bar" : {
                            "i-i" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                        [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "i-ii" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                }
                            },
                            "i-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -9, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -9, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                } 
                            },
                            "i-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                } 
                            },
                            "ii-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],  
                                },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]]                                   
                                       },                                    
                                "ponche" : {
                                    "0": {
                                        "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                            #Erster Takt - Wiederholte Achtel
                                        "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Zweiter Takt  - Wiederholte Achtel
                                        "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Beide Takte - Wiederholte Achtel
                                        "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],  
                                    },
                                    "1": {
                                        #Standard Tumbao
                                        "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                        "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Zweiter Takt - Wiederholte Achtel
                                        "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Beides
                                        "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]]                                   
                                        }                                   
                                }
                            },
                            "III-VI" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],                                    
                                    #Beides
                                    "5": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                }
                            },
                            "V-i" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "V-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "VII-i" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "ponche" : {
                                    "0" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                }
                            },
                            "i-iv-V-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "I-vi-ii-V" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                       }
                            },
                            "ii-V-i-i" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],   
                                       }
                            },
                            "V-iv-i-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            }
                        }
                    }
                },
                "reverse" : {
                    "major" : {
                        "one_bar" : {

                        },
                        "two_bar" : {
                            "I-I" : {
                                "0": { #"0" Ponche
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                        [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                            [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, -12, [empty, empty]], [is_note, eighth, -12, [empty, empty]]]],
                                    }
                                }
                            },
                            "I-ii" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                            [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, eighth, -10, [empty, empty]], [is_note, eighth, -10, [empty, empty]]]],
                                    }
                                }
                            },
                            "I-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                            [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    }
                                } 
                            },
                            "I-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, eighth, -10, [empty, empty]], [is_note, eighth, -10, [empty, empty]]]],
                                    }
                                }
                            },
                            "ii-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -8, [empty, tie_start]]]],  
                                },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, -14, [empty, tie_start]]]]                                   
                                       },                                    
                                "ponche" : {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, empty]]],
                                           [[is_note, dotquarter, -5, [empty, empty]], [is_note, dotquarter, -11, [empty, empty]], [is_note, eighth, -8, [empty, empty]], [is_note, eighth, -8, [empty, empty]]]],
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -5, [empty, empty]]],
                                           [[is_note, dotquarter, -5, [empty, empty]], [is_note, dotquarter, -13, [empty, empty]], [is_note, eighth, -14, [empty, empty]], [is_note, eighth, -14, [empty, empty]]]]                                    
                                }
                            },
                            "iii-VI" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                          [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                          [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                          [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                          [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                           [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],                                    
                                    #Beides
                                    "5": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                          [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                           [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                           [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                           [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                },
                                "ponche" : {
                                    "0" : {
                                        "0": [[[is_note, dotquarter, -8, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -3, [empty, tie_start]]],
                                        [[is_note, dotquarter, -3, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, eighth, -10, [empty, empty]], [is_note, eighth, -10, [empty, empty]]]],
                                    }
                                }
                            },
                            "V-I" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                            [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, -12, [empty, empty]], [is_note, eighth, -12, [empty, empty]]]],
                                    }
                                }
                            },
                            "V-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -8, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -8, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "VII-I" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "ponche" : {
                                    "0" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, 0, [empty, empty]], [is_note, eighth, 0, [empty, empty]]]],
                                    "1" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, 0, [empty, empty]], [is_note, eighth, 0, [empty, empty]]]],
                                    "2" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, 0, [empty, empty]], [is_note, eighth, 0, [empty, empty]]]]
                                }
                            },
                            "I-IV-V-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, eighth, -12, [empty, empty]], [is_note, eighth, -12, [empty, empty]]]],
                                    }
                                }
                            },
                            "I-vi-ii-V" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                       },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                               [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, 0, [empty, empty]], [is_note, eighth, 0, [empty, empty]]]], 
                                    }
                                }
                            },
                            "ii-V-I-I" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],   
                                       },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                        [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, eighth, 0, [empty, empty]], [is_note, eighth, 0, [empty, empty]]]],
                                    }
                                }
                            },
                            "V-IV-I-IV" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                },
                                "ponche" : {
                                    "0" : {
                                        "0" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                            [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, eighth, -12, [empty, empty]], [is_note, eighth, -12, [empty, empty]]]],                                        
                                    }
                                }
                            }
                        }
                    },
                    "minor" : {
                        "one_bar" : {

                        },
                        "two_bar" : {
                            "i-i" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                        [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                       [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "i-ii" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                           [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                }
                            },
                            "i-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -9, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -9, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, 5, [empty, tie_start]]]],
                                } 
                            },
                            "i-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                } 
                            },
                            "ii-V" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],  
                                },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]]                                   
                                       },                                    
                                "ponche" : {
                                    "0": {
                                        "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                            #Erster Takt - Wiederholte Achtel
                                        "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Zweiter Takt  - Wiederholte Achtel
                                        "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        #Beide Takte - Wiederholte Achtel
                                        "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                        "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -11, [empty, empty]], [is_note, quarter, -11, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],  
                                    },
                                    "1": {
                                        #Standard Tumbao
                                        "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                        "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Zweiter Takt - Wiederholte Achtel
                                        "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        #Beides
                                        "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -13, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]],
                                        "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                            [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -13, [empty, empty]], [is_note, quarter, 7, [empty, tie_start]]]]                                   
                                        }                                   
                                }
                            },
                            "III-VI" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],                                    
                                    #Beides
                                    "5": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8": [[[is_note, dotquarter, -9, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -4, [empty, tie_start]]],
                                       [[is_note, dotquarter, -4, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                }
                            },
                            "V-i" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "V-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, dotquarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -10, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -9, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -10, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -7, [empty, tie_start]]],
                                           [[is_note, dotquarter, -7, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -9, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "VII-i" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "ponche" : {
                                    "0" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, dotquarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "1" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -14, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" :[[[is_note, dotquarter, -14, [empty, tie_stop]], [is_note, eighth, -4, [empty, empty]], [is_note, quarter, -4, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                       [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                }
                            },
                            "i-iv-V-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -5, [empty, tie_start]]],
                                           [[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            },
                            "I-vi-ii-V" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]]
                                       },
                                "1" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -3, [empty, empty]], [is_note, quarter, -3, [empty, empty]], [is_note, quarter, 2, [empty, tie_start]]],
                                       [[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, -10, [empty, tie_start]]]]
                                       }
                            },
                            "ii-V-i-i" : {
                                "0" : {
                                    #Standard Tumbao
                                    "0" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Zweiter Takt - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, dotquarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    #Beides
                                    "5" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, 0, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, 2, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, 2, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]],
                                           [[is_note, dotquarter, 0, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -5, [empty, empty]], [is_note, quarter, 0, [empty, tie_start]]]],   
                                       }
                            },
                            "V-iv-i-iv" : {
                                "0": {
                                    "0" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                        #Erster Takt - Wiederholte Achtel
                                    "1" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "2" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Zweiter Takt  - Wiederholte Achtel
                                    "3" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "4" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, dotquarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                       #Beide Takte - Wiederholte Achtel
                                    "5" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "6" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -5, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "7" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                    "8" : [[[is_note, dotquarter, -5, [empty, tie_stop]], [is_note, eighth, -7, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]],
                                           [[is_note, dotquarter, -12, [empty, tie_stop]], [is_note, eighth, -12, [empty, empty]], [is_note, quarter, -7, [empty, empty]], [is_note, quarter, -12, [empty, tie_start]]]],
                                }
                            }
                        }
                    }
                }

            },
            "clave" : {
                "forward" : [[[is_note, dotquarter], [is_note, dotquarter], [is_note, quarter]],
                            [[is_rest, quarter], [is_note, quarter], [is_note, quarter], [is_rest, quarter]]],
                "reverse" : [[[is_rest, quarter], [is_note, quarter], [is_note, quarter], [is_rest, quarter]],
                            [[is_note, dotquarter], [is_note, dotquarter], [is_note, quarter]]]
            },
            "timbales" : {
                "timbales" : [[[is_note, quarter], [is_note, quarter], [is_note, eighth], [is_note, eighth], [is_rest, eighth], [is_note, eighth]],
                            [[is_note, quarter], [is_note, eighth], [is_note, eighth], [is_rest, eighth], [is_note, eighth], [is_rest, eighth], [is_note, eighth]]],
                "bell" : [[[is_note, quarter], [is_note, quarter], [is_note, eighth], [is_note, eighth], [is_note, eighth], [is_note, eighth]],
                        [[is_rest, eighth], [is_note, eighth], [is_note, eighth], [is_note, eighth], [is_note, quarter], [is_note, eighth], [is_note, eighth]]],
                "cue" : {
                    "timbales" : [[[is_note, quarter], [is_note, quarter], [is_note, eighth], [is_note, eighth], [is_rest, eighth], [is_note, eighth]],
                                [[is_note, quarter], [is_note, eighth], [is_note, eighth], [is_rest, eighth], [is_note, eighth], [is_note, eighth], [is_note, eighth]]],
                    "bell" : [[[is_note, quarter], [is_note, quarter], [is_note, eighth], [is_note, eighth], [is_note, eighth], [is_note, eighth]],
                            [[is_rest, eighth], [is_note, eighth], [is_note, eighth], [is_note, eighth], [is_note, quarter], [is_note, eighth], [is_note, eighth]]],
                }
            },
            "bongos" : {
                "bongo" : {
                    "0" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                           [[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]]],
                    "1" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], accent]],
                           [[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]]],
                    "2" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                           [[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h, b_l], empty], [is_rest, quarter], [is_note, quarter, [b_h, b_l], empty], [is_rest, eighth], [is_note, eighth, [b_h, b_l], empty]]],
                    "3" : [[[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                           [[is_note, eighth, [b_h], accent], [is_note, sixteenth, [b_h], empty], [is_note, sixteenth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], accent]]]
                       },
                "bell" : [[[is_note, quarter, accent], [is_note, eighth, empty], [is_note, eighth, empty], [is_note, quarter, accent], [is_note, eighth, empty], [is_note, eighth, empty]],
                          [[is_note, quarter, accent], [is_note, quarter, empty], [is_note, quarter, accent], [is_note, eighth, empty], [is_note, eighth, empty]]],
                "cue" : {
                    "bongo" : {
                        "0" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                            [[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], accent], [is_note, eighth, [b_l], accent]]],
                        "1" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], accent]],
                            [[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], accent]]],
                        "2" : [[[is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                            [[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h, b_l], empty], [is_rest, quarter], [is_note, quarter, [b_h, b_l], empty], [is_note, eighth, [b_h, b_l], accent], [is_note, eighth, [b_h, b_l], accent]]],
                        "3" : [[[is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_l], empty], [is_note, eighth, [b_h], empty]],
                            [[is_note, eighth, [b_h], accent], [is_note, sixteenth, [b_h], empty], [is_note, sixteenth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], empty], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], accent], [is_note, eighth, [b_h], accent]]]
                        },
                    "bell" : [[[is_note, quarter, accent], [is_note, eighth, empty], [is_note, eighth, empty], [is_note, quarter, accent], [is_note, eighth, empty], [is_note, eighth, empty]],
                            [[is_note, quarter, accent], [is_note, quarter, empty], [is_note, quarter, empty], [is_note, eighth, accent], [is_note, eighth, accent]]],
                }
            },
            "congas" : {
                "conga" : {
                    "0": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_hm], empty],
                          [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], empty], [is_note, eighth, [c_ho], empty]],
                    "1": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_ho], empty],
                          [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], empty], [is_note, eighth, [c_ho], empty]]
                },
                "tumba" : {
                    "0": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_l], empty],
                          [is_note, eighth, [c_l], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], empty], [is_note, eighth, [c_ho], empty]],
                    "1": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_hm], empty],
                          [is_note, eighth, [c_l], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], empty], [is_note, eighth, [c_ho], empty]],
                    "2": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_l], empty],
                          [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], empty], [is_note, eighth, [c_ho], empty]]
                },
                "cue" : {
                    "conga" : {
                        "0": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_hm], empty],
                            [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], accent], [is_note, eighth, [c_ho], accent]],
                        "1": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_ho], empty],
                            [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], accent], [is_note, eighth, [c_ho], accent]]
                    },
                    "tumba" : {
                        "0": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_l], empty],
                            [is_note, eighth, [c_l], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], accent], [is_note, eighth, [c_ho], accent]],
                        "1": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_hm], empty],
                            [is_note, eighth, [c_l], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], accent], [is_note, eighth, [c_ho], accent]],
                        "2": [[is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], accent], [is_note, eighth, [c_l], empty],
                            [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_hm], empty], [is_note, eighth, [c_ho], accent], [is_note, eighth, [c_ho], accent]]
                    }
                }
            },
        },
        "rest" : {
            "piano" : {
                "right" : [[[is_rest, full]], [[is_rest, full]]],
                "left" : [[[is_rest, full]], [[is_rest, full]]]
            },
            "other" : [[[is_rest, full]], [[is_rest, full]]]
        }
    }

    STRUCTURE: dict = {
        "Son Montuno" : {
            "0" : {
                "section" : "intro",
                "reps" : 4, #number of for-loop-iterations
                "direction" : "reverse", #direction of clave
                "span" : "", #key to span-dictionary in STYLE
                "progression" : ["", "", ""], #Array of keys to a chord progression in STYLE
                "instruments" : {
                    "horns" : [is_rest],
                    "piano" : [is_rest],
                    "bass" : [is_rest],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "1" : {
                "section" : "intro",
                "reps" : 4,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["four_chord_prog", "I-vi-ii-V", "0"],
                "instruments" : {
                    "horns" : [is_rest],
                    "piano" : [is_note, harm, "arpeggio"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "2" : {
                "section" : "verse",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["four_chord_prog", "I-vi-ii-V", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "3" : {
                "section" : "verse",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["four_chord_prog", "ii-V-I-I", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "4" : {
                "section" : "verse",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["four_chord_prog", "I-vi-ii-V", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "5" : {
                "section" : "verse",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["four_chord_prog", "ii-V-I-I", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "6" : {
                "section" : "bridge",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["two_chord_prog", "ii-V", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "7" : {
                "section" : "bridge",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["two_chord_prog", "iii-VI", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "8" : {
                "section" : "bridge",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["two_chord_prog", "ii-V", "1"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            },
            "9" : {
                "section" : "bridge",
                "reps" : 1,
                "direction" : "reverse",
                "span" : "two_bar",
                "progression" : ["two_chord_prog", "VII-I", "0"],
                "instruments" : {
                    "horns" : [is_note, harm],
                    "piano" : [is_note, harm, "montuno"],
                    "bass" : [is_note, harm],
                    "clave" : [is_note, perc],
                    "timbales" : [is_note, perc],
                    "bongos" : [is_note, perc, str(random.randint(0, 3))],
                    "congas" : [is_note, perc, str(random.randint(0, 1)), str(random.randint(0, 2))]
                }
            }
        }
    }
    
    
# --- CONSTRUCTOR ---#
    def __init__(self, _style: str, _instruments: list, _part_list: list, _direction: str, _mode: str, _key: str, _midi: int, _play_piano: bool):
        style: str = _style
        part_list: list = _part_list
        instruments: list = _instruments
        direction: str = _direction
        mode: str = _mode
        main_key: str = _key
        midi: int = _midi
        play_piano: bool = _play_piano        
        
        self.score: stream.Stream = stream.Stream()
        self.mode: str = mode
        self.score_key: dict = self.set_key(main_key, midi, mode)

        speed = random.randint(160, 220)
        salsa_tempo = tempo.MetronomeMark('vivace', speed, note.Note(type='quarter'))
        
        self.score.insert(0, salsa_tempo)
        self.score.insert(0, self.score_key["main_key"])

        for inst in instruments:
            if inst == "horns" :
                self.horns_part: stream.Part = stream.Part()
                self.horns_part.insert(0, salsa_tempo)
                self.horns_part.append([self.score_key["trumpet_key"], instrument.Trumpet()])
                self.score.append(self.horns_part)
            if inst == "piano":
                self.righthand_part: stream.Part = stream.Part()
                self.lefthand_part: stream.Part = stream.Part()
                self.righthand_part.insert(0, salsa_tempo)
                self.righthand_part.append([self.score_key["main_key"]])
                self.lefthand_part.insert(0, salsa_tempo)
                self.lefthand_part.append([self.score_key["main_key"], clef.BassClef()])
                self.score.insert(0, self.righthand_part)
                self.score.insert(0, self.lefthand_part)
                piano_part: m21.layout.StaffGroup = m21.layout.StaffGroup([self.righthand_part, self.lefthand_part], name='Piano', abbreviation='Pno.', symbol='brace')
                piano_part.barTogether = 'Mensurstrich'
                self.score.append(piano_part)
            if inst == "bass":
                self.bass_part: stream.Part = stream.Part()
                self.bass_part.insert(0, salsa_tempo)
                self.bass_part.append([self.score_key["main_key"], instrument.AcousticBass(), clef.Bass8vbClef()])                
                self.score.append(self.bass_part)
            if inst == "clave":
                self.clave_part: stream.Part = stream.Part()
                self.clave_part.insert(0, salsa_tempo)
                self.clave_part.append([instrument.Woodblock()])                
                self.score.append(self.clave_part)
            if inst == "bongos":
                self.bongo_part: stream.Part = stream.Part()
                self.bbell_part: stream.Part = stream.Part()
                self.bongo_part.insert(0, salsa_tempo)
                self.bongo_part.append(instrument.BongoDrums())
                self.bbell_part.insert(0, salsa_tempo)
                self.bbell_part.append(instrument.Agogo())
                self.score.append([self.bongo_part, self.bbell_part])
            if inst == "congas":
                self.conga_part = stream.Part()
                self.conga_part.insert(0, salsa_tempo)
                self.conga_part.append(instrument.CongaDrum())                
                self.score.append(self.conga_part)
            if inst == "timbales":
                self.timbales_part: stream.Part = stream.Part()
                self.tbell_part: stream.Part = stream.Part()
                self.timbales_part.insert(0, salsa_tempo)
                self.timbales_part.append([instrument.Timbales()])
                self.tbell_part.insert(0, salsa_tempo)
                self.tbell_part.append([instrument.Cowbell()])                
                self.score.append([self.timbales_part, self.tbell_part])

        for part in part_list:
            new_part: dict = self.render_part(style, part, instruments, direction, play_piano)
            self.compose(style, new_part)

        self.score.show()        


# --- CREATE DICTIONARIES --- #
    def render_part(self, _style: str, _part: dict, _instruments: list, _direction: str, _play_piano: bool) -> dict:
        style: str = _style
        direction: str = _direction
        play: bool = _play_piano
        instrument_vars: list = _instruments
        section: str = _part["part_value"]
        progression: tuple = _part["prog_value"][self.mode]
        bars: int = int(_part["bars_value"] / 2)
        prog_modulo: int = len(progression)
        is_rest: bool = self.is_rest
        is_note: bool = self.is_note
        harm: str = self.harm
        perc: str = self.perc
        piano_styles: list = ["chords", "montuno"]
        rndm_piano: str = piano_styles[random.randint(0, 1)]
        ponche: str = ""
        cue: str = ""
        STRUCTURE =  {
            style : {}
        }

        print("Wir sind in Section", section)
        
        if section == "Intro":
            for i in range(2):
                PART = {
                    "section": "intro",
                    "reps" : int(bars / 2),
                    "direction" : direction,
                    "span" : "two_bar",
                    "progression" : progression[i%prog_modulo],
                    "instruments" : {}
                }
                for instrument in instrument_vars:
                    if instrument == "piano":
                        if play:
                            if i == 0:
                                PART["instruments"].update({instrument : [is_rest]})
                            else:
                                PART["instruments"].update({
                                    instrument : [
                                        is_note,
                                        harm,
                                        ponche,
                                        "arpeggio"]})
                        else:
                            PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "horns":
                        PART["instruments"].update({instrument : [is_rest]}) 
                    elif instrument == "bass":
                        if i == 0:
                            PART["instruments"].update({instrument : [is_rest]})
                        else:
                            PART["instruments"].update({
                                instrument : [
                                    is_note,
                                    harm,
                                    ponche
                                    ]})
                    elif instrument == "bongos":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest]})
                    elif instrument == "congas":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                str(random.randint(0, 1)),
                                str(random.randint(0, 2))
                                ]})
                    elif instrument == "timbales":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest
                                ]})
                    else:
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc
                                ]})

                STRUCTURE[style].update({str(i) : PART})
        elif section == "Verse" or section == "Outro":
            for i in range(bars):
                PART = {
                    "section": "",
                    "reps" : 1,
                    "direction" : direction,
                    "span" : "two_bar",
                    "progression" : progression[i%prog_modulo],
                    "instruments" : {}
                }

                if section == "Verse": 
                    PART["section"] = "verse"
                else: 
                    PART["section"] = "outro"
                    if i == bars - 1:
                        ponche = "ponche"
                        cue = "cue"

                for instrument in instrument_vars:
                    if instrument == "piano":
                        if play:
                            PART["instruments"].update({
                                instrument : [
                                    is_note,
                                    harm,
                                    ponche,
                                    rndm_piano]})
                        else:
                            PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "horns" or instrument == "bass":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                harm,
                                ponche]})
                    elif instrument == "bongos":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest]})
                    elif instrument == "congas":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                str(random.randint(0, 1)),
                                str(random.randint(0, 2))]})
                    elif instrument == "timbales":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest]})
                    else:
                        PART["instruments"].update({instrument : [is_note, perc]})
                    
                STRUCTURE[style].update({str(i) : PART})
        elif section == "Bridge":
            for i in range(bars):
                PART = {
                    "section": "bridge",
                    "reps" : 1,
                    "direction" : direction,
                    "span" : "two_bar",
                    "progression" : progression[i%prog_modulo],
                    "instruments" : {}
                }
                
                for instrument in instrument_vars:
                    if instrument == "piano":
                        if play:
                            PART["instruments"].update({
                                instrument : [
                                    is_note,
                                    harm,
                                    ponche,
                                    "montuno"
                                    ]})
                        else:
                            PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "horns" or instrument == "bass":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                harm,
                                ponche
                                ]})
                    elif instrument == "bongos":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_rest, 
                                is_note]})
                    elif instrument == "congas":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                str(random.randint(0, 1)),
                                str(random.randint(0, 2))
                                ]})
                    elif instrument == "timbales":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_note
                                ]})
                    else:
                        PART["instruments"].update({instrument : [is_note, perc]}) 

                STRUCTURE[style].update({str(i) : PART})
        elif section == "Montuno":
            for i in range(bars):
                PART = {
                    "section": "montuno",
                    "reps" : 1,
                    "direction" : direction,
                    "span" : "two_bar",
                    "progression" : progression[i%prog_modulo],
                    "instruments" : {}
                }

                if i == bars - 1:
                    ponche = "ponche"
                    cue = "cue"
                
                for instrument in instrument_vars:
                    if instrument == "piano":
                        if play:
                            PART["instruments"].update({
                                instrument : [
                                    is_note,
                                    harm,
                                    ponche,
                                    "montuno"
                                    ]})
                        else:
                            PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "horns":
                        PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "bass":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                harm,
                                ponche]})
                    elif instrument == "bongos":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_rest,
                                is_note]})
                    elif instrument == "congas":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                str(random.randint(0, 1)),
                                str(random.randint(0, 2))]})
                    elif instrument == "timbales":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_rest,
                                is_note]})
                    else:
                        PART["instruments"].update({instrument : [is_note, perc]}) 
                STRUCTURE[style].update({str(i) : PART})
        elif section == "Klavier Solo":
            for i in range(bars):
                PART = {
                    "section": "solo",
                    "reps" : 1,
                    "direction" : direction,
                    "span" : "two_bar",
                    "progression" : progression[i%prog_modulo],
                    "instruments" : {}
                }

                if i == bars - 1:
                    ponche = "ponche"
                    cue = "cue"
                
                for instrument in instrument_vars:
                    if instrument == "piano":
                        if play and i == bars - 1:
                            PART["instruments"].update({
                                instrument : [
                                    is_note,
                                    harm,
                                    ponche,
                                    "chords"]})
                        else:
                            PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "horns":
                        PART["instruments"].update({instrument : [is_rest]})
                    elif instrument == "bass":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                harm,
                                ponche
                                ]})
                    elif instrument == "bongos":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest
                                ]})
                    elif instrument == "congas":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                str(random.randint(0, 1)),
                                str(random.randint(0, 2))
                                ]})
                    elif instrument == "timbales":
                        PART["instruments"].update({
                            instrument : [
                                is_note,
                                perc,
                                cue,
                                is_note,
                                is_rest
                                ]})
                    else:
                        PART["instruments"].update({instrument : [is_note, perc]}) 

                STRUCTURE[style].update({str(i) : PART})
            
        return STRUCTURE

    def write_part(self, _style: str, _part: dict):
        style: str = _style
        section: str = _part["section"]
        reps: int = _part["reps"]
        direction: str = _part["direction"]
        span: str = _part["span"]
        progression: str = _part["progression"]
        instruments: dict = _part["instruments"]
        
        STYLE: dict = self.STYLE
        mode: str = self.mode
        main_key: m21.key = self.score_key["main_key"]
        trumpet_key: m21.key = self.score_key["trumpet_key"]
        cast_pitch: int = self.score_key["tonic"]

        for inst, state in instruments.items():
            if state[0] == False:
                if inst == "piano":
                    bar_content = STYLE["rest"]["piano"]
                else:
                    bar_content = STYLE["rest"]["other"]
            else:
                bar_content = STYLE[style][inst]
                try:
                    if state[1] == "harm":
                        variant = 0
                        if state[2] == "ponche":
                            bar_content = bar_content[direction][mode][span][progression]["ponche"]
                            variant = len(bar_content.keys())
                        else:
                            bar_content = bar_content[direction][mode][span][progression]
                            for pv in bar_content.keys():
                                if pv != "ponche": variant += 1
                        variant -= 1
                        prog_var = str(random.randint(0, variant))
                        bar_content = bar_content[prog_var]

                        if inst == "piano":
                            bar_content = bar_content[state[3]] #"arpeggio", "montuno" oder "chords"
                        elif inst == "bass":
                            if section == "intro" or section == "verse" or section == "solo":
                                rndm_bass: int = 0
                            else:
                                rndm_bass: int = random.randint(0, len(bar_content.keys()) - 1)  
                            bar_content = bar_content[str(rndm_bass)]
                        
                    elif state[1] == "perc":
                        if inst == "clave":
                            bar_content = bar_content[direction]
                        else:
                            if state[2] == "cue":
                                bar_content = bar_content["cue"]
                            else: pass

                            if inst == "bongos":
                                if state[3]:
                                    bongo = bar_content["bongo"]
                                    pattern = str(random.randint(0, len(bongo.keys()) - 1))
                                    bongo = bongo[pattern]
                                else: bongo = STYLE["rest"]["other"]
                                if state[4]: bbell = bar_content["bell"]
                                else: bbell = STYLE["rest"]["other"]
                                bar_content = [bongo, bbell]
                            elif inst == "congas": 
                                bar_content = [bar_content["conga"][state[3]], bar_content["tumba"][state[4]]]
                            elif inst == "timbales":
                                if state[3]: timbales = bar_content["timbales"]
                                else: timbales = STYLE["rest"]["other"]
                                if state[4]: tbell = bar_content["bell"]
                                else: tbell = STYLE["rest"]["other"]
                                bar_content = [timbales, tbell]
                except KeyError:
                    print(["Etwas ist falsch mit den Keys. Bar Content hat diese Keys:", bar_content.keys()])
            try:
                for i in range(reps):
                    if inst == "horns":
                        self.write_horns(bar_content, cast_pitch, trumpet_key)
                    elif inst == "piano":
                        self.write_piano(bar_content, cast_pitch, main_key)
                    elif inst == "bass":
                        self.write_bass(bar_content, cast_pitch, main_key)
                    elif inst == "clave":
                        self.write_clave(bar_content)
                    elif inst == "bongos":
                        self.write_bongos(direction, bar_content[0], bar_content[1])
                    elif inst == "congas":
                        self.write_congas(direction, section, bar_content)
                    elif inst == "timbales":
                        self.write_timbales(bar_content[0], bar_content[1])
            except KeyError:
                print("Die Zuweisungen laufen nicht. Instrument:", inst, "| Bar Content Keys:", direction, "|", mode, "|", span, "|", progression, "|", Exception.__cause__)


# --- PREPARE SCORE
    def set_key(self, _key: str, _midi: int, _mode: str) -> dict:
        main_scale = scale.Scale

        if _mode == "major":
            main_key = key.Key(_key)
            main_scale = scale.MajorScale(_key)
        elif _mode == "minor":
            main_key = key.Key(_key + "m")
            main_scale = scale.MinorScale(_key)            
        trumpet_scale = main_scale.transpose(2)
        trumpet_key = main_key.transpose(2)
        midi_tonic = _midi

        return {
            "main_scale" : main_scale,
            "main_key" : main_key,
            "trumpet_scale" : trumpet_scale,
            "trumpet_key" : trumpet_key,
            "tonic" : midi_tonic
        }
    

# --- WRITE MUSIC --- #
    def compose(self, _style: str, _structure: dict):
        structure = _structure[_style]
        style = _style
        for part in structure.values():
            self.write_part(style, part)

    #Funktion erstellt mithilfe von ChatGPT
    def enforce_enharmonic(self, _key: key.Key, _pitch: pitch.Pitch) -> pitch.Pitch:
        """
        Passt alle Noten im Stream enharmonisch an die aktuelle Tonart an.
        Funktioniert für Part, Measure oder Score.
        """
        enharmonic = _pitch.getEnharmonic()
        if enharmonic.name in [p.name for p in _key.pitches]:
            _pitch = enharmonic
        if _pitch.accidental != None:
            _pitch.accidental.displayType = 'never'
        return _pitch

    def write_bass(self, _bassline: list, _tonic: int, _key: key.Key):
        bassline: list = _bassline
        tonic: int = _tonic
        main_key: key.Key = _key
        accent: str = self.accent
        tie_start: str = self.tie_start
        tie_stop: str = self.tie_stop

        if tonic >= 72: tonic -= 12

        _pitch = pitch.Pitch(midi=tonic).transpose(-24)

        #Für die Anzahl an gewünschten Takten
        for i in range(len(bassline)):
            bass_measure = stream.Measure()
            for clave in bassline[i]:
                if clave[0] == False:
                    tumbao_note = note.Rest()
                else:
                    tumbao_pitch = self.enforce_enharmonic(main_key, _pitch.transpose(clave[2]))
                    if tumbao_pitch.midi < 28:
                        tumbao_pitch = tumbao_pitch.transpose(12)
                    tumbao_note = note.Note(tumbao_pitch)
                    for acc in clave[3]:
                        if acc == accent:
                            tumbao_note.articulations.append(articulations.StrongAccent())
                        if acc == tie_start or acc == tie_stop:
                            tumbao_note.tie = tie.Tie(acc)

                tumbao_note.duration = duration.Duration(clave[1])

                bass_measure.append(tumbao_note)
            self.bass_part.append(bass_measure)

    def write_bongos(self, _direction: str, _bongos: list, _bell: list):
        direction: str = _direction
        bongos: list = _bongos
        bell: list = _bell
        accent = self.accent
        agb = self.agb
        
        for i in range(len(bongos)):
            bongo_measure = stream.Measure()
            bell_measure = stream.Measure()                   
            bongo_section = bongos[i]

            if direction == "forward":
                if i % 2: bell_section = bell[0]
                else: bell_section = bell[1]
            elif direction == "reverse":
                if i % 2: bell_section = bell[1]
                else: bell_section = bell[0]

            for articulation in bongo_section:
                if articulation[0] == True:
                    bongo_chord = chord.Chord()
                    try:
                        for j in range(len(articulation[2])):
                            bongo_note = note.Note(pitch=pitch.Pitch(midi=articulation[2][j]))
                            bongo_chord.add(bongo_note)
                    except TypeError:
                        bongo_note = note.Note(pitch=pitch.Pitch(midi=articulation[2]))
                        bongo_chord.add(bongo_note)

                    if articulation[3] == accent:
                        bongo_chord.articulations.append(articulations.StrongAccent())
                else:
                    bongo_chord = note.Rest()

                bongo_chord.duration = duration.Duration(articulation[1])
                bongo_measure.append(bongo_chord)

            for articulation in bell_section:
                if articulation[0]:
                    bell_note = note.Note(pitch=pitch.Pitch(midi=agb))
                else:
                    bell_note = note.Rest()
                
                bell_note.duration = duration.Duration(articulation[1])
                bell_measure.append(bell_note)

            self.bongo_part.append(bongo_measure)
            self.bbell_part.append(bell_measure)


    def write_clave(self, _clave: list):
        wb = self.wb
        for i in range(len(_clave)):
            wb_measure = stream.Measure()

            for clv in _clave[i % 2]:
                if clv[0]:
                    wb_note = note.Note(pitch=pitch.Pitch(midi=wb))
                else:
                    wb_note = note.Rest()
                
                wb_note.duration = duration.Duration(clv[1])

                wb_measure.append(wb_note)
            
            self.clave_part.append(wb_measure)

    def write_congas(self, _direction: str, _songsection: str, _congas: list):
        direction: str = _direction
        songsection: str = _songsection
        congas: list = _congas
        accent: str = self.accent

        for i in range(len(congas)):
            congaMeasure = stream.Measure()
            if songsection == "intro" or songsection == "verse": #One drum pattern during Intros and Verses
                section = congas[0]
            else: #Switch between Arrays for two drum patterns
                if direction == "forward":
                    if i % 2: section = congas[0]
                    else: section = congas[1]
                elif direction == "reverse":
                    if i % 2: section = congas[1]
                    else: section = congas[0]

            for articulation in section:
                if articulation[0] == True:
                    conga_chord = chord.Chord()
                    for j in range(len(articulation[2])):
                        congaNote = note.Note(pitch=pitch.Pitch(midi=articulation[2][j]))
                        conga_chord.add(congaNote)

                    if articulation[3] == accent:
                        conga_chord.articulations.append(articulations.StrongAccent())
                else:
                    conga_chord = note.Rest()

                conga_chord.duration = duration.Duration(articulation[1])
                congaMeasure.append(conga_chord)
            self.conga_part.append(congaMeasure)

    def write_horns(self, _vamp: list, _root_pitch: int, _key: key.Key):
        root = _root_pitch + 2
        for i in range(len(_vamp)): 
            measure = stream.Measure()
            
            for clave in _vamp[i]:
                if clave[0] == True:
                    montuno_chord = chord.Chord()
                    for j in range(len(clave[2])):
                        chord_pitch = self.enforce_enharmonic(_key, pitch.Pitch(midi=root + clave[2][j]))

                        montuno_chord.add(chord_pitch)

                else: montuno_chord = note.Rest()
                
                montuno_chord.duration = duration.Duration(clave[1])
                measure.append(montuno_chord)

            self.horns_part.append(measure)

    def write_piano(self, _vamp: dict, _root: int, _key: key.Key):
        vamp: dict = _vamp
        root: int = _root
        main_key: key.Key = _key
        accent: str = self.accent
        tie_start: str = self.tie_start
        tie_stop: str = self.tie_stop

        #Akkorduntermalung
        for i in range(len(vamp["right"])): 
            right_measure: stream.Measure = stream.Measure()
            left_measure: stream.Measure = stream.Measure()

            if root >= 72: root -= 12
            
            for clave in vamp["right"][i]:
                if clave[0] == True:
                    montuno_chord: chord.Chord = chord.Chord()
                    try:
                        for j in range(len(clave[2])):
                            chord_pitch: pitch.Pitch = self.enforce_enharmonic(main_key, pitch.Pitch(midi=root + clave[2][j]))
                            montuno_chord.add(chord_pitch)
                    except TypeError: #Falls einem Integer das Komma fehlt
                            chord_pitch: pitch.Pitch = self.enforce_enharmonic(main_key, pitch.Pitch(midi=root + clave[2]))
                            montuno_chord.add(chord_pitch)
                    for acc in clave[3]:
                        if acc == accent:
                            montuno_chord.articulations.append(articulations.StrongAccent())
                        if acc == tie_start or acc == tie_stop:
                            montuno_chord.tie = tie.Tie(acc)


                else: montuno_chord: note.Rest = note.Rest()
                
                montuno_chord.duration = duration.Duration(clave[1])
                right_measure.append(montuno_chord) 

            for clave in vamp["left"][i]:
                if clave[0] == True:
                    montuno_chord: chord.Chord = chord.Chord()
                    try:
                        for j in range(len(clave[2])):
                            chord_pitch: pitch.Pitch = self.enforce_enharmonic(main_key, pitch.Pitch(midi=root + clave[2][j]).transpose(-12))
                            montuno_chord.add(chord_pitch)
                    except TypeError:
                        chord_pitch: pitch.Pitch = self.enforce_enharmonic(main_key, pitch.Pitch(midi=root + clave[2]).transpose(-12))
                        montuno_chord.add(chord_pitch)

                    for acc in clave[3]:
                        if acc == accent:
                            montuno_chord.articulations.append(articulations.StrongAccent())
                        elif acc == tie_start or acc == tie_stop:
                            montuno_chord.tie = tie.Tie(acc)
                        
                else: montuno_chord: note.Rest = note.Rest()
                
                montuno_chord.duration = duration.Duration(clave[1])
                left_measure.append(montuno_chord)

            self.righthand_part.append(right_measure)
            self.lefthand_part.append(left_measure)

    def write_timbales(self, _timbales: list, _bell: list):
        
        for i in range (len(_timbales)):
            timbales_measure = stream.Measure()
            bell_measure = stream.Measure()

            for cascara in _timbales[i % 2]:
                if cascara[0]:
                    timbales_note = note.Unpitched()
                else:
                    timbales_note = note.Rest()

                timbales_note.duration = duration.Duration(cascara[1])
                timbales_measure.append(timbales_note)
            
            for campaneo in _bell[i % 2]:
                if campaneo[0]:
                    bell_note = note.Unpitched()
                else:
                    bell_note = note.Rest()
                
                bell_note.duration = duration.Duration(campaneo[1])
                bell_measure.append(bell_note)
                
            self.timbales_part.append(timbales_measure)
            self.tbell_part.append(bell_measure)


# --- HERE RESTS THE DRUMSET --- #
    """
    create_DrumSet creates and returns a Drum Set Part containing a given pattern.
    Durations will be pass down as an Array containing typically two arrays with the note direction for each instrument in each bar.
    Hi-Hat and Snare Drum will have to be fixed later to create and offset if need be.
    """
    def write_drumset(self, _drumset: list, _measure: int, _tempo: tempo.MetronomeMark):
        #drumSet.append(instrument.UnpitchedPercussion())
        
        #creates every voice bar by bar
        for i in range(len(_drumset)):
            #Creates a new measure
            drumMeasure = stream.Measure()

            #We create a voice for each instrument so the can be easily inserted into the measure without dself.isturbing the flow

            rideVoice = stream.Voice()
            hihatVoice = stream.Voice()
            snareVoice = stream.Voice()
            bassDrumVoice = stream.Voice()

            crashRest = note.Rest()
            crashRest.duration = duration.Duration(4)

            #To fit the two bar rhythm into every bar regardless of length, we must work with i % 2 to keep switching between 0 and 1.
            #The Notes will then be appended to the Voice, for comfortable, polyrhythmic work.
            for dur in _drumset[0][i % 2]:
                #Falls der mitgebene Parameter 'self.isNote' == True self.ist, wird eine Note ausgegeben
                if dur[1] == True:
                    rideNote = note.Unpitched(storedInstrument=instrument.RideCymbals())
                #Falls der mitgebene Parameter 'self.isNote' == False self.ist, wird eine Pause ausgegeben
                else:
                    rideNote = note.Rest()

                rideNote.duration = duration.Duration(dur[0])
                rideVoice.append(rideNote)
            
            #Repeat the process for HiHat
            for dur in _drumset[1][i % 2]:
                if dur[1] == True:
                    hihatPitch = pitch.Pitch(midi=42)
                    hihatPitch.accidental.displayType = "never"
                    hihatNote = note.Note(hihatPitch)
                else:
                    hihatNote = note.Rest()

                hihatNote.duration = duration.Duration(dur[0])
                hihatVoice.append(hihatNote)
            
            #Repeat the process for Snare Drum
            for dur in _drumset[2][i % 2]:
                if dur[1] == True:
                    snarePitch = pitch.Pitch(midi=37)
                    snarePitch.accidental.displayType = "never"
                    snareNote = note.Note(snarePitch)
                else:
                    snareNote = note.Rest()

                snareNote.duration = duration.Duration(dur[0])
                snareVoice.append(snareNote)

            for dur in _drumset[3][i % 2]:
                if dur[1] == True:
                    bdPitch = pitch.Pitch(midi=35)
                    bassDrumNote = note.Note(bdPitch)
                else:
                    bassDrumNote = note.Rest()

                bassDrumNote.duration = duration.Duration(dur[0])
                bassDrumVoice.append(bassDrumNote)
            
            #An array containing all voices for prettier coding
            drumVoices = [rideVoice, hihatVoice, snareVoice, bassDrumVoice]

            #Adds all the voices to the measure from the beginning of the measure
            for voice in drumVoices:
                drumMeasure.insert(0, voice)

            #Add the measure to the Drum Set Part
            self.drumset_part.append(drumMeasure)

    def return_drumset(self) -> list[list]:
        ride_1 = [[[self.full, self.is_rest]], [[self.full, self.is_rest]]]
        ride_2 = [[[self.full, self.is_rest]], [[self.full, self.is_rest]]]
        ride_pattern = [ride_1, ride_2]

        hihat_1 = [[[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_rest], [self.quarter, self.is_note]], [[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_rest], [self.quarter, self.is_note]]]
        hihat_2 = [[[self.quarter, self.is_note], [self.quarter, self.is_note], [self.eighth, self.is_note], [self.eighth, self.is_note], [self.eighth, self.is_rest], [self.eighth, self.is_note]], [[self.quarter, self.is_note], [self.eighth, self.is_note], [self.eighth, self.is_note], [self.eighth, self.is_rest], [self.eighth, self.is_note], [self.eighth, self.is_rest], [self.eighth, self.is_note]]]
        hihat_pattern = [hihat_1, hihat_2]

        snare_1 = [[[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_rest], [self.quarter, self.is_note]], [[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_rest], [self.quarter, self.is_note]]]
        snare_2 = [[[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_rest], [self.eighth, self.is_rest], [self.eighth, self.is_note]], [[self.quarter, self.is_rest], [self.eighth, self.is_rest], [self.eighth, self.is_note], [self.quarter, self.is_note], [self.quarter, self.is_note]]]
        snare_3 = [[[self.quarter, self.is_rest], [self.quarter, self.is_note], [self.quarter, self.is_note], [self.quarter, self.is_rest]], [[self.dotquarter, self.is_note], [self.dotquarter, self.is_note], [self.quarter, self.is_note]]]
        snare_pattern = [snare_1, snare_2, snare_3]

        bassdrum_1 = [[[self.quarter, self.is_rest], [self.eighth, self.is_rest], [self.eighth, self.is_note], [self.half, self.is_rest]], [[self.quarter, self.is_rest], [self.eighth, self.is_rest], [self.eighth, self.is_note], [self.half, self.is_rest]]]
        bassdrum_2 = [[[self.dotquarter, self.is_note], [self.eighth, self.is_note], [self.half, self.is_rest]], [[self.dotquarter, self.is_note], [self.eighth, self.is_note], [self.half, self.is_rest]]]
        bassdrum_pattern = [bassdrum_1, bassdrum_2]

        clave = random.randint(0, 1)
        if clave == 0:
            hihat = hihat_pattern[0]
            snare = snare_pattern[random.randint(0, 1)]
        elif clave == 1:
            hihat = hihat_pattern[1]
            snare = snare_pattern[2]

        salsa_pattern = [ride_pattern[random.randint(0, 1)], hihat, snare, bassdrum_pattern[random.randint(0, 1)]]
        return salsa_pattern