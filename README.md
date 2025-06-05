<img width="643" alt="image" src="https://github.com/user-attachments/assets/0940f999-35c2-4783-8ea5-ab193f948982" />

⸻

🎻 AI Violin Pitch Tracker + Real-Time Visualizer

A Python-based AI-assisted application that detects real-time violin pitch from microphone input and shows:
	•	The note being played (e.g. G3, D4)
	•	The Solfege equivalent (Do, Re, Mi…)
	•	The closest violin string
	•	A graphical violin string diagram indicating where you’re playing on the violin

⸻

📸 Screenshot Example

(Include a screenshot of the live graph showing a note being played, like Note: A4 (La) on string A4.)

⸻

🔧 Features
	•	🎵 Real-time pitch detection
	•	🔡 Note & Solfege display (e.g., A4 (La))
	•	🧠 Uses librosa’s advanced pitch detection with pyin
	•	📊 Graphical visualization of violin strings and position marker
	•	❌ Ignores background noise / silent segments

 How It Works
	1.	Records 0.5-second segments from the microphone
	2.	Uses librosa.pyin() to extract the fundamental frequency (pitch)
	3.	Converts pitch to note (like A4), and Solfege (like La)
	4.	Finds the closest matching violin string
	5.	Displays everything on a live Matplotlib violin diagram

 Install Requirements
 pip install -r requirements.txt
 librosa
numpy
matplotlib
sounddevice

RUN:
python violin_tracker.py

<img width="388" alt="image" src="https://github.com/user-attachments/assets/e26cba6a-ba6b-4b84-b7c9-fa5ddf7193aa" />

<img width="388" alt="image" src="https://github.com/user-attachments/assets/009fc18d-724b-4668-af34-6eb3285cbf69" />

MIT License – use freely, credit appreciated!
