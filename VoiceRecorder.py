import sys
import os
import datetime
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import pyaudio
import wave

class VoiceRecorder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.recording = False
        self.output_folder = "recordings"

    def init_ui(self):
        self.record_button = QtWidgets.QPushButton("Record")
        self.save_button = QtWidgets.QPushButton("Save")
        self.record_button.clicked.connect(self.toggle_recording)
        self.save_button.clicked.connect(self.save_recording)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.record_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Voice Recorder")

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.record_button.setText("Stop Recording")
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                     channels=1,
                                     rate=44100,
                                     input=True,
                                     frames_per_buffer=1024)
        self.frames = []

    def stop_recording(self):
        self.recording = False
        self.record_button.setText("Record")
        self.stream.stop_stream()
        self.stream.close()

    def save_recording(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        now = datetime.datetime.now()
        file_name = os.path.join(self.output_folder, now.strftime("%Y-%m-%d %H-%M-%S") + ".wav")
        wf = wave.open(file_name, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    recorder = VoiceRecorder()
    recorder.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
