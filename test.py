from music21 import *
import random

#Stream für MuseScore
score = stream.Stream()

#Stream für Midi
midi_stream = stream.Stream()

pulse = 2
beat = 2
pattern = 0

#List of Chords arranged in an euclidean rhythm
chord_rhythm = []

#Viertelrhytmen
full_quarter = [1]
double_eigth = [0.5, 0.5]
sixteenth_one = [0.25, 0.25, 0.25, 0.25]
sixteenth_two = [0.25, 0.25, 0.5]
sixteenth_three = [0.25, 0.5, 0.25]
sixteenth_four = [0.5, 0.25, 0.25]
sixteenth_five = [0.75, 0.25]
sixteenth_six = [0.25, 0.75]

#Triolen-Rhythmen
triplet_one = [1/3, 1/3, 1/3] #Ist nicht nötig, weil repeatAppend(note.Note(), 3)
triplet_two = [1/3, 2/3]
triplet_three = [2/3, 1/3]

#Quintolen-Rhythmen
quintuplet_one = [1/5, 1/5, 1/5, 1/5, 1/5] #Ist nicht nötig, weil repeatAppend(note.Note(), 5)

quintuplet_two = [2/5, 1/5, 1/5, 1/5]
quintuplet_three = [1/5, 2/5, 1/5, 1/5]
quintuplet_four = [1/5, 1/5, 2/5, 1/5]
quintuplet_five = [1/5, 1/5, 1/5, 2/5]
quintuplet_six = [2/5, 2/5, 1/5]
quintuplet_seven = [2/5, 1/5, 2/5]
quintuplet_eight = [1/5, 2/5, 2/5]

quintuplet_nine = [3/5, 1/5, 1/5]
quintuplet_ten = [1/5, 3/5, 1/5]
quintuplet_eleven = [1/5, 1/5, 3/5]
quintuplet_twelve = [3/5, 2/5]
quintuplet_thirteen = [2/5, 3/5]

quintuplet_fourteen = [4/5, 1/5]
quintuplet_fifteen = [1/5, 4/5]

even_patterns = [full_quarter, double_eigth, sixteenth_one, sixteenth_two, sixteenth_three, sixteenth_four, sixteenth_five, sixteenth_six]
triplet_patterns = [triplet_one, triplet_two, triplet_three]
quintuplet_patterns = [quintuplet_one, quintuplet_two, quintuplet_three, quintuplet_four, quintuplet_five, quintuplet_six, quintuplet_seven, quintuplet_eight, quintuplet_nine, quintuplet_ten, quintuplet_eleven, quintuplet_twelve, quintuplet_thirteen, quintuplet_fourteen, quintuplet_fifteen]
all_patterns = [even_patterns, triplet_patterns, quintuplet_patterns]

"""
Durations for Clave(-like) Percussion, inspired by "Latinizing your School Jazz Ensemble" by Michele Fernandez Denlinger.
If no further infortmation regarding the metric is given, the default metric is 'Alla breve' or 2/2.
Furthermore, all rhythms are notated as 'forward', meaning 2/3 which can be changed later on while running the code.
"""
#Bossa Clave-like Pattern: [1/4, 1/8-Pause, 1/8, 1/4-Pause, 1/4], [1/4-Pause, 1/4, 1/8-Pause, 1/8, 1/4-Pause]
bossa_clave = [[1, .5, .5, 1, 1], [1, 1, .5, .5, 1]]

#Cuban "Son Clave" Pattern: [1/4, 1/8-Pause, 1/8, 1/4-Pause, 1/4], [1/4-Pause, 1/4, 1/4, 1/4-Pause]
cuban_sonClave = [[1, .5, .5, 1, 1], [1, 1, 1, 1]]

#Samba Pattern: [1/4, 1/4, 1/8-Pause, 1/8, 1/8-Pause, 1/8], [1/8-Pause, 1/8, 1/4-Pause, 1/4, 1/4]
samba_clave = [[1, 1, .5, .5, .5, .5], [.5, .5, 1, 1, 1]]

#Afro-Cuban 6/8 Clave: [1/4, 1/8, 1/8-Pause, 1/8, 1/8], [1/8-Pause, 1/4, 1/4, 1/8]
afro_cubanClave = [[1, .5, .5, .5, .5], [.5, 1, 1, .5]]

#Salsa Cascara (played on shell of floor tom or timbales): [1/4, 1/4, 1/8, 1/8, 1/8-Pause, 1/8], [1/4, 1/8, 1/8, 1/8-Pause, 1/8, 1/8-Pause, 1/8]
salsa_cascara = [[1, 1, .5, .5, .5, .5], [1, .5, .5, .5, .5, .5, .5]]

#Basic Agogo-Samba-Pattern. Alternating between high and low bell for 'Kang-Kang-Ko-Kong-Kang-Kang-Ka-Kong-Kong'
samba_agogo = [[1, 1, .5, .5, .5, .5], [.5, .5, .5, .5, 1, 1]]

#"Campaneo" (played on (cow)bell): [1/4, 1/4, 1/8, 1/8, 1/8, 1/8], [1/8-Pause, 1/8, 1/8, 1/8, 1/4, 1/8, 1/8]
cowbell_campaneo = [[1, 1, .5, .5, .5, .5], [.5, .5, .5, .5, 1, .5, .5]]



#Martillo Bongo: Hitting the accent lower bongo will make it sound like 'Pa-Kah-Pa-Kah, Pa-Kah-Po-Kah' for Salsa
bongo_martillo = [[.5, .5, .5, .5, .5, .5, .5, .5]]



#Rhythmusinstrumente
agogo = instrument.Agogo()
tambourine = instrument.Tambourine()
bongoDrums = instrument.BongoDrums()
woodblock = instrument.Woodblock() #recommended by Michele Fernandez Denlinger since no Clave is available
steelDrum = instrument.SteelDrum() #for Calypso if we get there
triangle = instrument.Triangle()

#Drumset

"""
Returns an Array containing Arrays to create a BASIC Bossa Nova Rhythm for Drumset à la Michele Fernandez, to be used in create_DrumSet.
Since Ride, Hi-Hat, Snare and Bass Drum will always be in that same order, to access them one can rest assured that
bossaDrumSet()[0] = Ride
bossaDrumSet()[1] = Hi-Hat
bossaDrumSet()[2] = Snare
bossaDrumSet()[3] = Bass Drum
"""
def bossaDrumSet():
    ride_pattern = [[[2, True], [2, True]], [[2, True], [2, True]]]
    hihat_pattern = [[[1, False], [1, True], [1, False], [1, True]], [[1, False], [1, True], [1, False], [1, True]]]
    snare_pattern = [[[1, True], [.5, False], [.5, True], [1, False], [1, True]], [[1, False], [1, True], [.5, False], [.5, True], [1, False]]]
    bassDrum_pattern = [[[1, True], [.5, False], [.5, True], [1, True], [.5, False], [.5, True]], [[1, True], [.5, False], [.5, True], [1, True], [.5, False], [.5, True]]]
    bossa_pattern = [ride_pattern, hihat_pattern, snare_pattern, bassDrum_pattern]
    
    return bossa_pattern

def sambaDrumSet():
    ride_pattern = [[[1, True], [1, True], [1, True], [1, True]], [[1, True], [1, True], [1, True], [1, True]]]
    hihat_pattern = [[[1, False], [1, True], [1, False], [1, True]], [[1, False], [1, True], [1, False], [1, True]]]
    snare_pattern = [[[1, True], [1, True], [.5, False], [.5, True], [.5, False], [.5, True]], [[.5, False], [.5, True], [1, False], [1, True], [1, True]]]
    bassDrum_Pattern = [[[1, True], [.5, False], [.5, True], [1, True], [.5, False], [.5, True]], [[1, True], [.5, False], [.5, True], [1, True], [.5, False], [.5, True]]]

    samba_pattern = [ride_pattern, hihat_pattern, snare_pattern, bassDrum_Pattern]
    return samba_pattern

def salsaDrumSet_grooveOne():
    ride_pattern = [[[4, False]], [[4, False]]]
    hihat_pattern = [[[1, False], [1, True], [1, False], [1, True]], [[1, False], [1, True], [1, False], [1, True]]]
    snare_pattern = [[[1, False], [1, True], [1, False], [1, True]], [[1, False], [1, True], [1, False], [1, True]]]
    bassDrum_Pattern = [[[1, False], [.5, False], [.5, True], [2, False]], [[1, False], [.5, False], [.5, True], [2, False]]]

    salsa_pattern = [ride_pattern, hihat_pattern, snare_pattern, bassDrum_Pattern]
    return salsa_pattern

def salsaDrumSet_grooveTwo():
    ride_pattern = [[[4, False]], [[4, False]]]
    hihat_pattern = [[[1, False], [1, True], [1, False], [1, True]], [[1, False], [1, True], [1, False], [1, True]]]
    snare_pattern = [[[1, False], [1, True], [1, False], [.5, False], [.5, True]], [[1, False], [.5, False], [.5, True], [1, True], [1, True]]]
    bassDrum_Pattern = [[[1.5, True], [.5, True], [2, False]], [[1.5, True], [.5, True], [2, False]]]

    salsa_pattern = [ride_pattern, hihat_pattern, snare_pattern, bassDrum_Pattern]
    return salsa_pattern

"""
create_DrumSet creates and returns a Drum Set Part containing a given pattern. Durations will be pass down as an Array containing typically two arrays with the note direction for each instrument in each bar.
Hi-Hat and Snare Drum will have to be fixed later to create and offset if need be.
"""
def create_DrumSet(_durRide, _durHiHat, _durSnare, _durBassDrum, _measure: int, _tempo: tempo.MetronomeMark):
    global score
    global midi_stream

    drumSet = stream.Part()
    drumSet.append([_tempo, clef.PercussionClef()])

    ridePart = stream.Part()
    hihatPart = stream.Part()
    snarePart = stream.Part()
    bassDrumPart = stream.Part()

    ridePart.append(_tempo)
    hihatPart.append(_tempo)
    snarePart.append(_tempo)
    bassDrumPart.append(_tempo)
    
    #creates every voice bar by bar
    for i in range(_measure):
        #Creates a new measure
        drumMeasure = stream.Measure()

        rideMeasure = stream.Measure()
        hihatMeasure = stream.Measure()
        snareMeasure = stream.Measure()
        bassDrumMeasure = stream.Measure()

        #We create a voice for each instrument so the can be easily inserted into the measure without disturbing the flow

        rideVoice = stream.Voice()
        hihatVoice = stream.Voice()
        snareVoice = stream.Voice()
        bassDrumVoice = stream.Voice()

        rideVoice.append(instrument.RideCymbals())
        hihatVoice.append(instrument.HiHatCymbal())
        snareVoice.append(instrument.SnareDrum())
        bassDrumVoice.append(instrument.BassDrum())

        crashRest = note.Rest()
        crashRest.duration = duration.Duration(4)

        #To fit the two bar rhythm into every bar regardless of length, we must work with i % 2 to keep switching between 0 and 1.
        #The Notes will then be appended to the Voice, for comfortable, polyrhythmic work.
        for dur in _durRide[i % 2]:
            #Falls der mitgebene Parameter 'isNote' == True ist, wird eine Note ausgegeben
            if dur[1] == True:
                rideNote = note.Unpitched(displayName='F3', storedInstrument=instrument.RideCymbals())
            #Falls der mitgebene Parameter 'isNote' == False ist, wird eine Pause ausgegeben
            else:
                rideNote = note.Rest()

            rideNote.duration = duration.Duration(dur[0])
            rideVoice.append(rideNote)
        
        #Repeat the process for HiHat
        for dur in _durHiHat[i % 2]:
            if dur[1] == True:
                hihatNote = note.Unpitched(displayName='G#2', storedInstrument=instrument.HiHatCymbal())
            else:
                hihatNote = note.Rest()

            hihatNote.duration = duration.Duration(dur[0])
            hihatVoice.append(hihatNote)
        
        #Repeat the process for Snare Drum
        for dur in _durSnare[i % 2]:
            if dur[1] == True:
                snareNote = note.Unpitched(displayName='D2', storedInstrument=instrument.SnareDrum())
            else:
                snareNote = note.Rest()

            snareNote.duration = duration.Duration(dur[0])
            snareVoice.append(snareNote)

        for dur in _durBassDrum[i % 2]:
            if dur[1] == True:
                bassDrumNote = note.Unpitched(displayName='C2', storedInstrument=instrument.BassDrum())
            else:
                bassDrumNote = note.Rest()

            bassDrumNote.duration = duration.Duration(dur[0])
            bassDrumVoice.append(bassDrumNote)
        
        #An array containing all voices for prettier coding
        drumVoices = [rideVoice, hihatVoice, snareVoice, bassDrumVoice]

        #Adds all the voices to the measure from the beginning of the measure
        for voice in drumVoices:
            drumMeasure.insert(0, voice)
        
        rideMeasure.insert(0, rideVoice)
        hihatMeasure.insert(0, hihatVoice)
        snareMeasure.insert(0, snareVoice)
        bassDrumMeasure.insert(0, bassDrumVoice)

        #Add the measure to the Drum Set Part
        #drumSet.insert(i, drumMeasure)
        ridePart.insert(i, rideMeasure)
        hihatPart.insert(i, hihatMeasure)
        snarePart.insert(i, snareMeasure)
        bassDrumPart.insert(i, bassDrumMeasure)

    #Add Parts to part
    drumParts = [ridePart, hihatPart, snarePart, bassDrumPart]

    for part in drumParts:
        score.append(part)

    #Return the composed Drums Part to later add it to the score
    #return drumSet


"""
create_Maracas creates and returns a Maraca Part, to later be added to the score.
As of now - 251002 - the Maracas play a simple rhythm twice per measure. Hence the code is limited to this very repetition, as of now.
"""
def create_Maracas(_measure: int):
    #Maraca Part to be returned
    maracaPart = stream.Part()

    #Create Maraca Instrument and add to maracaPart
    maracas = instrument.Maracas()
    maracaPart.append(maracas)

    #For every measure, a new stream.Measure object is created
    for i in range(_measure):  
        maracaMeasure = stream.Measure()

        #Twice
        for j in range(2):
            #Create four eighths
            for k in range(4):
                maracaNote = note.Unpitched(displayName='C4', storedInstrument=instrument.Maracas())
                maracaNote.duration = duration.Duration(0.5)
                
                #The first note of the four will always be accented
                if k == 0:
                    maracaNote.articulations.append(articulations.Accent())
                
                #Add the note to the measure
                maracaMeasure.append(maracaNote)

        #Add the measure to the part
        maracaPart.append(maracaMeasure)

    #Return part to later be added to the score    
    return maracaPart

"""
create_Congas creates and returns a Conga Part, to later be added to the score.
Since music21 can not handle more detailed rhythmic articulations, the function will will cycle through a given Array containing two int-Arrays with 0, 1, 2 and 3
0 = No articulation
1 = Unstress
2 = Accent
3 = StrongAccent

Might need to be revisited, to potentionally be able to alternate between different Congas
"""

conga_rhythm = [[['h', 0], ['h', 1], ['h', 2], ['h', 1], ['h', 0], ['h', 1], ['h', 3], ['h', 3]], [['h', 0], ['h', 1], ['h', 2], ['l', 0], ['l', 0], ['h', 1], ['h', 3], ['h', 3]]]

def write_congas(_measure: int, _accent):
    global midi_stream

    #Create Conga Part
    congaPart = stream.Part()

    #Create Conga Instrument and add it to congaPart
    #congaDrum = instrument.CongaDrum()
    muteHighConga = midi.percussion.PercussionMapper().midiPitchToInstrument(62) #MIDI für hohe Conga

     
    #congaPart.append([openHighConga, lowConga])

    #Create every measure
    for i in range(_measure):
        openHighConga = midi.percussion.PercussionMapper().midiPitchToInstrument(63) #MIDI für hohe Conga
        lowConga = midi.percussion.PercussionMapper().midiPitchToInstrument(64) #Midi für tiefe Conga
        congaPart.append([openHighConga, lowConga])
        congaMeasure = stream.Measure()

        #Switch between the two Arrays within _accent, to correctly fill every measure
        for acc in _accent[i % 2]:
            congaNote = note.Unpitched()
            if acc[0] == 'h':
                #congaMeasure.append(openHighConga)
                congaNote.storedInstrument = openHighConga
            elif acc[0] == 'l':
                congaNote.storedInstrument = lowConga
                #congaMeasure.append(lowConga)

            congaNote.duration = duration.Duration(0.5)

            #If acc = 1, unstress the note
            if acc[1] == 1:
                congaNote.articulations.append(articulations.Unstress())
            #If acc = 2, add an accent
            elif acc[1] == 2:
                congaNote.articulations.append(articulations.Accent())
            #If acc = 3, add a strong accent
            elif acc[1] == 3:
                congaNote.articulations.append(articulations.StrongAccent())
            
            #Add note to measure
            congaMeasure.append(congaNote)

        
        #Add measure so part
        congaPart.insert(i, congaMeasure)

        #Add measure to midi_stream
        midi_stream.insert(i, congaMeasure)
    
    #Return congaPart
    return congaPart

"""
Conga "Tumbao" played on two congas. Further rhythmic sound is created through hand playstile:
Ot - Open Tone
Ct - Closed Tone
St - Slap Tone
Pt - Palm Tone
H - Heel of Hand
T - Tip of Hand

Resulting in a 'Bmm-T-KAH-T, Bmm-T-Boh-Boh, Bmm-T-KAH-Boh, Boh-Bim-Boh-Boh'
Since music21 can't translate Hand movement well, this will happen via accents
"""
conga_tumbao = [[.5, .5, .5, .5, .5, .5, .5, .5], [.5, .5, .5, .5, .5, .5, .5, .5]]

#Generiert eine "Tumbao"-Basslinie
def write_tumbao(_measure: int, _pitch: pitch.Pitch, _tempo: tempo.MetronomeMark):
    #Bassstimme
    bass_part = stream.Part()
    bass_clef = clef.BassClef()
    electric_bass = instrument.ElectricBass()
    bass_part.append([_tempo, electric_bass, bass_clef, key.Key('e')])
    #_pitch = _pitch.transpose(interval.Interval(-12))

    #Basic Salsa "Tumbao" Bass Pattern: Remeber to tie the 1/8 and 1/4. Could've coded a dotted 1/4 but didn't for score reasons
    minor_main = [[[-12, 1.5], [-5, 1.5], [0, 1]], [[0, 1.5], [-5, 1.5], [-12, 1]]]
    minor_switch = [[[-12, 1.5], [-5, 1.5], [0, 1]], [[0, 1.5], [-5, 1.5], [-14, 1]]]
    major_main = [[[-14, 1.5], [-7, 1.5], [-2, 1]], [[-2, 1.5], [-7, 1.5], [-14, 1]]]
    major_switch = [[[-14, 1.5], [-7, 1.5], [-2, 1]], [[-2, 1.5], [-7, 1.5], [-12, 1]]]

    bassline = [minor_main, minor_switch, major_main, major_switch]
    chord_mode = 0

    #Für die Anzahl an gewünschten Takten
    for i in range(_measure):
        bass_measure = stream.Measure()

        for clave in bassline[chord_mode][i % 2]:
            tumbao_note = note.Note(_pitch.transpose(clave[0]))
            tumbao_note.duration = duration.Duration(clave[1])

            if clave == [0, 1] or clave == [-12, 1] or clave == [-2, 1] or clave == [-14, 1]:
                tumbao_note.tie = tie.Tie('start')
            if clave == [0, 1.5] or clave == [-12, 1.5] or clave == [-2, 1.5] or clave == [-14, 1.5]:
                tumbao_note.tie = tie.Tie('stop')

            bass_measure.append(tumbao_note)
        bass_part.append(bass_measure)

        chord_mode += 1

        if chord_mode == 4: chord_mode = 0

    return bass_part


#Generiert eine "Montuno"-Piano Melodie
def write_montuno(_measure: int, _pitch: pitch.Pitch, _tempo: tempo.MetronomeMark):
    #Akkorduntermalung
    piano = instrument.Piano()
    piano_part = stream.Part()
    piano_part.append([_tempo, piano, key.Key('e')])

    montuno_steps = [[[False, .5], [True, .5, 7], [False, .5], [True, .5, -2], [False, .5], [True, .5, -1], [False, .5], [True, .5, 0]], [[True, 1, 0], [True, .5, 7], [True, .5, -2], [False, .5], [True, .5, -1], [False, .5], [True, .5, 0]]]
    montuno_major = [[[False, .5], [True, .5, 7], [False, .5], [True, .5, -2], [False, .5], [True, .5, -1], [False, .5], [True, .5, 0]], [[True, 1, -2], [True, .5, 5], [True, .5, -4], [False, .5], [True, .5, -3], [False, .5], [True, .5, -2]]]

    chord_mode = [0, True]

    for i in range(_measure):
        piano_measure = stream.Measure()

        if chord_mode[1]:
            root = _pitch
        else:
            root = _pitch.transpose(-2)

        for clave in montuno_steps[i % 2]:
            if clave[0]:
                montuno_note = note.Note(root.transpose(clave[2]))
            else:
                montuno_note = note.Rest()

            montuno_note.duration = duration.Duration(clave[1])
            piano_measure.append(montuno_note)

        piano_part.append(piano_measure)

        chord_mode[0] += 1
        if chord_mode[0] == 2:
            chord_mode[0] = 0
            chord_mode[1] = not(chord_mode[1])

    return piano_part


#Generiert einen Timbaöes Rhythmus für Timbales und Cowbell
def write_campaneo(_measure: int, _tempo: tempo.MetronomeMark):
    #globale Variablen
    global score

    #Standard Campaneo Rhythmus Durations
    timbales_dur = [[[True, 1], [True, 1], [True, .5], [True, .5], [False, .5], [True, .5]], [[True, 1], [True, .5], [True, .5], [False, .5], [True, .5], [False, .5], [True, .5]]]
    bell_dur = [[[True, 1], [True, 1], [True, .5], [True, .5], [True, .5], [True, .5]], [[False, .5], [True, .5], [True, .5], [True, .5], [True, 1], [True, .5], [True, .5]]]

    #Neuen Part mit Timbales als Instrument erstellen
    timbales_part = stream.Part()
    timbales_part.append([instrument.Timbales(), _tempo])

    #Neuen Part mit Cowbell als Instrument erstellen
    bell_part = stream.Part()
    bell_part.append([instrument.Cowbell(), _tempo])

    for i in range (_measure):
        timbales_measure = stream.Measure()
        bell_measure = stream.Measure()

        for cascara in timbales_dur[i % 2]:
            if cascara[0]:
                timbales_note = note.Unpitched()
            else:
                timbales_note = note.Rest()

            timbales_note.duration = duration.Duration(cascara[1])
            timbales_measure.append(timbales_note)
        
        for campaneo in bell_dur[i % 2]:
            if campaneo[0]:
                bell_note = note.Unpitched()
            else:
                bell_note = note.Rest()
            
            bell_note.duration = duration.Duration(campaneo[1])
            bell_measure.append(bell_note)
            
        timbales_part.insert(i, timbales_measure)
        bell_part.insert(i, bell_measure)

    score.insert(0, timbales_part)
    score.insert(0, bell_part)

#Generiert einen Rhytmus der Länge eines Viertels mit zufälliger Noter der gegebenen Tonleiter
def random_rhythm(_pitch, _scale: scale.Scale, _part, _chord: bool = False):

    #rhythm = random.randint(1, 7)
    vibe = all_patterns[pattern]
    division = random.randint(0, len(vibe)-1)
    
    for dur in vibe[division]:
        _part.append(return_harmony(_pitch, dur, _scale, _chord))

def random_pitch(_scale: scale.Scale, _degree: int = 1):
    return _scale.pitchFromDegree(_degree)
        


#Funktion zur Generierung einer zufälligen Tonart
def set_scale(_scale: int, _key_mode: int, _spicy: int, _part: stream.Part):
    major_keys = ['F', 'B-', 'E-', 'A-', 'D-', 'G-', 'C', 'G', 'D', 'A', 'E', 'B', 'F#']
    minor_keys = ['d', 'g', 'c', 'f', 'b-', 'e-', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#']

    main_scale = scale.Scale

    if _key_mode == 0:
        key_root = major_keys[_scale]
        key_tonic = pitch.Pitch(key_root)
        key_major = key.Key(key_root)
        _part.append(key_major)

        main_scale = scale.MajorScale(key_tonic)
        print(key_major, main_scale)

    else:
        key_root = minor_keys[_scale]
        key_tonic = pitch.Pitch(key_root)
        key_minor = key.Key(key_root)
        _part.append(key_minor)

        # minor_mode = random.randint(0, 1)
        if _spicy == 0:
            main_scale = scale.MinorScale(key_tonic)
        elif _spicy == 1:
            main_scale = scale.HarmonicMinorScale(key_tonic)
        #elif minor_mode == 2:
        #    main_scale = scale.MelodicMinorScale(key_tonic)
        print(key_minor, main_scale)

    return main_scale


#Funktion zur Generierung 
def return_harmony(_pitch: pitch.Pitch, _dur: float, _scale: scale.Scale, _chord: bool = False):
    to_second = interval.Interval(2) #Major Second
    to_third = interval.Interval(3) #Minor Third
    to_fourth = interval.Interval(5) #Pure Fourth
    to_fifth = interval.Interval(7) #Pure Fifth
    to_seventh = interval.Interval(10) #Minor Seventh
    new_chord = chord.Chord()
    
    if _scale == scale.MajorScale():
        if _pitch == _scale.pitchFromDegree(1) or _pitch == _scale.pitchFromDegree(4) or _pitch == _scale.pitchFromDegree(5):
            to_third = interval.Interval(4) #Major Third

        if _pitch == _scale.pitchFromDegree(1) or _pitch == _scale.pitchFromDegree(4):
            to_seventh = interval.Interval(11) #Major Seventh
        elif _pitch == _scale.pitchFromDegree(4):
            to_fourth = interval.Interval(6) #Übermäßige Quarte
        elif _pitch == _scale.pitchFromDegree(7):
            to_fifth = interval.Interval(6) #Verminderte Quinte
        elif _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(7):
            to_second = interval.Interval(1)

        

        regular_triad = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth)])
        sus_two = chord.Chord([_pitch, _pitch.transpose(to_second), _pitch.transpose(to_fifth)])
        sus_four = chord.Chord([_pitch, _pitch.transpose(to_fourth), _pitch.transpose(to_fifth)])
        seventh_chord = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth), _pitch.transpose(to_seventh)])
        
        chords = [sus_two, regular_triad, seventh_chord, sus_four]
        if _pitch != _scale.pitchFromDegree(4):
            new_chord = chords[random.randint(0, 3)]
        elif _pitch == _scale.pitchFromDegree(4):
            new_chord = chords[random.randint(0, 2)]
        elif _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(7):
            new_chord = chords[random.randint(1, 3)]

#Äolisch Moll
    elif _scale == scale.MinorScale():
        if _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(6) or _pitch == _scale.pitchFromDegree(7):
            to_third = interval.Interval(4) #Major Third
        if _pitch == _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(6):
            to_seventh = interval.Interval(11) #Major Seventh
        elif _pitch == _scale.pitchFromDegree(6):
            to_fourth = interval.Interval(6) #Übermäßige Quarte
        elif _pitch == _scale.pitchFromDegree(2):
            to_fifth = interval.Interval(6) #Verminderte Quinte
        elif _pitch == _scale.pitchFromDegree(2) or _pitch == _scale.pitchFromDegree(6):
            to_second = interval.Interval(1)

        regular_triad = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth)])
        sus_two = chord.Chord([_pitch, _pitch.transpose(to_second), _pitch.transpose(to_fifth)])
        sus_four = chord.Chord([_pitch, _pitch.transpose(to_fourth), _pitch.transpose(to_fifth)])
        seventh_chord = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth), _pitch.transpose(to_seventh)])
        
        chords = [sus_two, regular_triad, seventh_chord, sus_four]
        if _pitch != _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(0, 3)]
        elif _pitch == _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(0, 2)]
        elif _pitch == _scale.pitchFromDegree(2) or _pitch == _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(1, 3)]

#Harmonisch Moll
    elif _scale == scale.HarmonicMinorScale():
        if _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(5) or _pitch == _scale.pitchFromDegree(6):
            to_third = interval.Interval(4) #Major Third
        elif _pitch == _scale.pitchFromDegree(3) or _pitch == _scale.pitchFromDegree(6):
            to_seventh = interval.Interval(11) #Major Seventh
        elif _pitch == _scale.pitchFromDegree(6):
            to_fourth = interval.Interval(6) #Übermäßige Quarte
        elif _pitch == _scale.pitchFromDegree(2):
            to_fifth = interval.Interval(6) #verminderte Quinte
        elif _pitch == _scale.pitchFromDegree(3):
            to_fifth = interval.Interval(8) #übermäßiger Akkord
        elif _pitch == _scale.pitchFromDegree(2) or _pitch == _scale.pitchFromDegree(6):
            to_second = interval.Interval(1)

        regular_triad = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth)])
        sus_two = chord.Chord([_pitch, _pitch.transpose(to_second), _pitch.transpose(to_fifth)])
        sus_four = chord.Chord([_pitch, _pitch.transpose(to_fourth), _pitch.transpose(to_fifth)])
        seventh_chord = chord.Chord([_pitch, _pitch.transpose(to_third), _pitch.transpose(to_fifth), _pitch.transpose(to_seventh)])
        
        chords = [sus_two, regular_triad, seventh_chord, sus_four]
        if _pitch != _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(0, 3)]
        elif _pitch == _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(0, 2)]
        elif _pitch == _scale.pitchFromDegree(2) or _pitch == _scale.pitchFromDegree(6):
            new_chord = chords[random.randint(1, 3)]
    

    if _chord == True:
        new_chord.duration = duration.Duration(_dur)
        return new_chord
    else:
        harmonic = 0 #random.randint(0, 1)
        if harmonic == 0:
            chord_second = _pitch.transpose(to_second)
            chord_third = _pitch.transpose(to_third)
            chord_fourth = _pitch.transpose(to_fourth)
            chord_fifth = _pitch.transpose(to_fifth)
            chord_seventh = _pitch.transpose(to_seventh)
            chord_harmonies = [_pitch, chord_second, chord_third, chord_fourth, chord_fifth, chord_seventh]

            #Regelt Enharmonische Verwechslung
            for newNote in chord_harmonies:
                newNote.simplifyEnharmonic()
                newNote.updateAccidentalDisplay()

            chord_note = note.Note(chord_harmonies[random.randint(0, 5)], duration = duration.Duration(_dur))
            #print(chord_harmonies)
            return chord_note
        elif harmonic == 1:
            return note.Rest(duration = duration.Duration(_dur))

    #regular_triad.duration = duration.Duration(_dur)
    #return regular_triad


#Funktion zur enerierung von zufälligen Taktarten
def return_timesignature():
    all_pulses = ["2", "3", "4", "5", "6", "7", "8", "9"]
    beats = ["/4", "/8"]
    main_pulse = all_pulses[random.randint(0, 7)]
    main_beat = beats[random.randint(0, 1)]

    global pulse 
    pulse = int(main_pulse)

    return meter.TimeSignature(main_pulse + '/4')

#Code by youtube.com/@codemeowstro
def euclidean_rhythm(onsets: int, timesteps: int) -> list:
    """
    Generate a Euclidean Rhythm
    """

    #Calculate the base number of timesteps per onset
    base_duration = timesteps // onsets

    #Calculate the number of onsets to receive an extra time step
    remaining_timesteps = timesteps % onsets

    #Distribute the timesteps amongst the onsets to create durations
    rhythm = [[base_duration + 1] if i < remaining_timesteps else [base_duration] for i in range(onsets)]

    #Loop until all groups are the same
    while rhythm[0] != rhythm[-1]:
        for group in rhythm:

            #Check whether the group is the same as the final group
            if group != rhythm[-1]:

                #Move the last group to the end of the current group
                group += rhythm.pop(-1)

    #Retrieve the Euclidean rhythm
    rhythm = rhythm[0]
    return rhythm

#Arrange the correct Euclidean Rhythms for any case of timesignature
def play_euclidean(_measure: stream.Measure, _pitch: pitch.Pitch, _scale: scale.Scale, _chord: bool):
    global pulse
    global chord_rhythm

    if pulse == 2:
        for i in range(2):
            _measure.append(return_harmony(_pitch, chord_rhythm[0], _scale, _chord))
    elif pulse == 3:
        for i in range(2):
            _measure.append(return_harmony(_pitch, chord_rhythm[i], _scale, _chord))
    elif pulse == 4 or pulse == 8:
        for i in range(4):
            _measure.append(return_harmony(_pitch, chord_rhythm[0], _scale, _chord))
    else:
        if len(chord_rhythm) == 2:
            for play in chord_rhythm:
                for i in range(2):
                    _measure.append(return_harmony(_pitch, chord_rhythm[i], _scale, _chord))
        else:
            for i in range(4):
                _measure.append(return_harmony(_pitch, chord_rhythm[i], _scale, _chord))
    return

def write_music(_measure: stream.Measure, _pitch: pitch.Pitch, _scale: scale.Scale):
        global pulse
        global chord_rhythm
        global pattern

        #Choose either sixteenth or triplet patterns
        pattern = random.randint(0, 1)

        #Choose between three modes for the Violins: Ganze, Halbe und Euklydisch
        melody_mode = random.randint(0, 2)
        
        #Falls melody_mode = 0 ist, soll eine Ganze gespielt werden
        if melody_mode == 0:
            _measure.append(return_harmony(_pitch, pulse, _scale))

        #Falls melody_mode = 1 ist, kann eine Halbe gepielt werden, wenn sie in den Takt passt. Ansonsten soll eine Viertel bzw. ein Rhythmus der Länge einer Viertel gespielt werden.
        elif melody_mode == 1:
            #Variabel für den while loop
            step = 0
            #Geht Schlag für Schlag durch den Takt
            while step < pulse:
                #Falls pulse - 1 mindestens 2 ist, kann eine Münze Zwischen Halber und Viertel/Rhythmus geworfen werden
                print(step) #For Safety/Bugcheck purposes
                if pulse - 1 - step > 1:
                    print(["Halbe bei:", step])
                    coinflip = random.randint(0, 1)
                    #Ist coinflip = 0, wird eine Halbe gespielt. Dafür muss i dann um 2 anstatt um 1 erhöht werden
                    if coinflip == 0:
                        _measure.append(return_harmony(_pitch, 2, _scale))
                        step += 2
                    else:
                        random_rhythm(_pitch, _scale, _measure)
                        step += 1
                else:
                    random_rhythm(_pitch, _scale, _measure)
                    step += 1
        #Falls melody_mode = 2 ist, soll der Takt euklydisch ausgefüllt werden
        elif melody_mode == 2:
            play_euclidean(_measure, _pitch, _scale, False)

#Funktion dient Stand 250923, um eine Snaredrumstimme zu schreiben. Basically einfach random_rhythm für Snare
def write_percussion(_part):
    global pulse
    #rhythm = random.randint(1, 7)
    vibe = all_patterns[pattern]
    
    for i in range(pulse):
        #Creates SnareDrum notes in rhythmic fashion
        division = random.randint(0, len(vibe)-1)
        for dur in vibe[division]:
            snareNote = note.Unpitched(displayName='C4', storedInstrument=instrument.SnareDrum())
            snareNote.duration = duration.Duration(dur)
            _part.append(snareNote)


def main():
    global chord_rhythm
    global score
    global midi_stream

    #This variable is for testing purposes only. I shall clean it up later
    speed = random.randint(160, 220)
    salsa_tempo = tempo.MetronomeMark('vivace', speed, note.Note(type='half'))

    score.append(salsa_tempo)

    print([speed, salsa_tempo.text, salsa_tempo.getQuarterBPM()])

    #Random ammount of measures between 4 and 8
    all_measures = random.randint(4, 8)

    tumbao = write_tumbao(all_measures, pitch.Pitch('E3'), salsa_tempo)
    montuno = write_montuno(all_measures, pitch.Pitch('E'), salsa_tempo)
    conga = write_congas(all_measures, conga_rhythm)
    score.append([montuno, tumbao, conga])

    write_campaneo(all_measures, salsa_tempo)
    create_DrumSet(salsaDrumSet_grooveOne()[0], salsaDrumSet_grooveOne()[1], salsaDrumSet_grooveOne()[2], salsaDrumSet_grooveOne()[3], all_measures, salsa_tempo)
    
    score.show()

    """
    #Create a random timesignature from 2-9/4
    #main_timesignature = return_timesignature()

    #Pick a random pitch of the chromatic scale as our scale tonic
    score_scale = random.randint(0, 12)

    #Coinflip between Major or Minor Key
    key_mode = random.randint(0, 1)
    """

    """
    #Needed in case of Minor Scale to decide whether aeolian or harmonic
    spicy = random.randint(0, 1)

    #The instruments created for the score    
    violin = instrument.Violin()
    second_violin = instrument.Violin()
    contrabass = instrument.Contrabass()
    piano = instrument.Piano()
    snare = instrument.SnareDrum()

    #Erststimme
    soprano_part = stream.Part()
    soprano_part.append([violin, main_timesignature])

    #Zweitstimme
    alto_part = stream.Part()
    alto_clef = clef.AltoClef()
    alto_part.append([second_violin, main_timesignature])

    #Bassstimme
    bass_part = stream.Part()
    bass_clef = clef.BassClef()
    bass_part.append([contrabass, bass_clef, main_timesignature])

    #Akkorduntermalung
    piano_part = stream.Part()
    piano_part.append([piano, main_timesignature])

    #SnareDrum
    snare_part = stream.Part()
    snare_part.append([snare, main_timesignature])

    #In case of 2/4 or 3/4, arranged 2 over 2 or 2 over 3
    if pulse < 4: chord_rhythm = euclidean_rhythm(2, pulse)
    #Else arrange 4 over whatever the pulse is
    else: chord_rhythm = euclidean_rhythm(4, pulse)

    print(chord_rhythm)

    #Add the scale to all respective parts
    soprano_scale = set_scale(score_scale, key_mode, spicy, soprano_part)
    alto_scale = set_scale(score_scale, key_mode, spicy, alto_part)
    bass_scale = set_scale(score_scale, key_mode, spicy, bass_part)
    piano_scale = set_scale(score_scale, key_mode, spicy, piano_part)

    for x in range(all_measures):
        soprano_measure = stream.Measure(number=x+1)
        alto_measure = stream.Measure(number=x+1)
        bass_measure = stream.Measure(number=x+1)
        piano_measure = stream.Measure(number=x+1)
        #snare_measure = stream.Measure(number=x+1)
        degree = random.randint(1, 7)

        #Start and finish the piece in Key
        if x == 0 or x == all_measures-1:
            soprano_pitch = random_pitch(soprano_scale)
        #Choose random chords in between
        else: soprano_pitch = random_pitch(soprano_scale, degree)

        alto_pitch = soprano_pitch.transpose(-12)
        bass_note = note.Note(alto_pitch.transpose(-12), duration = duration.Duration(pulse))
        bass_measure.append(bass_note)
        bass_part.append(bass_measure)

        write_music(soprano_measure, soprano_pitch, soprano_scale)
        write_music(alto_measure, soprano_pitch, alto_scale)
        #write_percussion(snare_measure)
        play_euclidean(piano_measure, soprano_pitch, piano_scale, True)

        soprano_part.append(soprano_measure)
        alto_part.append(alto_measure)
        piano_part.append(piano_measure)
        #snare_part.append(snare_measure)

    score.append([soprano_part, alto_part, bass_part, piano_part])    
    score.show()
    """

    #create_DrumSet(bossaDrumSet()[0], bossaDrumSet()[1], bossaDrumSet()[2], bossaDrumSet()[3], all_measures)
    #midi_stream.insert(0, salsa_tempo)
    #conga.insert(0, salsa_tempo)
    #drums = create_DrumSet(salsaDrumSet_grooveOne()[0], salsaDrumSet_grooveOne()[1], salsaDrumSet_grooveOne()[2], salsaDrumSet_grooveOne()[3], all_measures)
    #drums.insert(0, salsa_tempo)
    #score.insert(0, conga)
    #midi_stream.write(fmt='midi', fp='251009_Render/251009_10.mid')

    

if __name__ == '__main__':
    main()