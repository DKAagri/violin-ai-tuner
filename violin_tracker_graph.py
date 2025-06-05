import numpy as np
import sounddevice as sd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import time

# Violin strings and Solfege
violin_strings = {
    'G3': 196.00,
    'D4': 293.66,
    'A4': 440.00,
    'E5': 659.25
}

solfege_map = {
    'C': 'Do',
    'C#': 'Di',
    'D': 'Re',
    'D#': 'Ri',
    'E': 'Mi',
    'F': 'Fa',
    'F#': 'Fi',
    'G': 'So',
    'G#': 'Si',
    'A': 'La',
    'A#': 'Li',
    'B': 'Ti'
}

# Convert frequency to closest note with octave
def freq_to_note(freq):
    if freq < 20 or freq > 2000:
        return None
    note_names = list(solfege_map.keys())
    A4 = 440
    semitone = 12 * np.log2(freq / A4)
    midi_num = int(round(semitone + 69))
    octave = midi_num // 12 - 1
    note = note_names[midi_num % 12]
    solfege = solfege_map[note]
    return f"{note}{octave}", solfege

# Get closest string
def closest_string(freq):
    if not freq:
        return None
    closest = min(violin_strings.items(), key=lambda x: abs(x[1] - freq))
    return closest[0]

# Real-time audio callback
duration = 0.5  # seconds
sample_rate = 22050
threshold = 0.01  # silence threshold

plt.ion()
fig, ax = plt.subplots()
ax.set_title("🎻 Violin String Position Tracker")
ax.set_xlim(-1, 4)
ax.set_ylim(0, 1)
strings = list(violin_strings.keys())

dots = ax.scatter([], [], s=200, c='red')
text_label = ax.text(1.5, 0.9, '', fontsize=14, ha='center')
for i, s in enumerate(strings):
    ax.plot([i, i], [0.2, 0.8], color='black', lw=4)
    ax.text(i, 0.1, s, fontsize=12, ha='center')

def update_plot(note, solfege, string_name):
    if string_name in strings:
        idx = strings.index(string_name)
        dots.set_offsets([[idx, 0.5]])
        text_label.set_text(f"Note: {note} ({solfege}) | String: {string_name}")
    else:
        dots.set_offsets([[-10, -10]])
        text_label.set_text("No valid sound")

    fig.canvas.draw()
    fig.canvas.flush_events()

# Main loop
print("🎻 Start playing your violin...")
while True:
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, blocking=True)
    y = audio.flatten()

    # Skip if too quiet
    if np.max(np.abs(y)) < threshold:
        update_plot(None, None, None)
        continue

    f0, voiced_flag, voiced_prob = librosa.pyin(
        y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=sample_rate
    )

    pitches = f0[~np.isnan(f0)]
    if len(pitches) == 0:
        update_plot(None, None, None)
        continue

    pitch = np.median(pitches)
    note, solfege = freq_to_note(pitch)
    string = closest_string(pitch)

    print(f"Freq: {pitch:.2f} Hz | Note: {note} ({solfege}) | Closest String: {string}")
    update_plot(note, solfege, string)