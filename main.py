# main.py
import time
from src.engine import AudioEngine # Pastikan 'src.engine' bukan 'src/engine'

def main():
    engine = AudioEngine()
    
    try:
        engine.start()
        print("Tekan Ctrl+C buat berhenti...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        engine.stop()
        print("\nSelesai, Progress hari ini mantap.")

if __name__ == "__main__":
    main()