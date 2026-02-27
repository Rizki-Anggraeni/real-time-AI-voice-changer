import sounddevice as sd
from .config import *
from .inference import RVCInference

class AudioEngine:  # <--- Pastikan penulisan 'A' dan 'E' kapital
    def __init__(self):
        self.stream = None

        self.ai = RVCInference(model_path="models/miku.pth")

    def audio_callback(self, indata, outdata, frames, time, status):
        if status:
            print(status)
        
        processed_audio = self.ai.process(indata)
        outdata[:] = processed_audio

    def start(self):
        print(f"--- Memulai Engine Voice Changer ---")
        try:
            self.stream = sd.Stream(
                device=(INPUT_DEVICE_ID, OUTPUT_DEVICE_ID),
                samplerate=SAMPLE_RATE,
                blocksize=BLOCK_SIZE,
                dtype=DTYPE,
                channels=CHANNELS,
                callback=self.audio_callback
            )
            self.stream.start()
            print("Engine AKTIF. Suara lo sekarang ngalir ke Virtual Cable.")
        except Exception as e:
            print(f"Gagal memulai engine: {e}")

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            print("Engine dimatikan.")