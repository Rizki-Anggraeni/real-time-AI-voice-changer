# src/config.py

# Sesuaikan ID ini dari hasil cek_id.py
INPUT_DEVICE_ID = 1    # Mic Fisik
OUTPUT_DEVICE_ID = 4   # CABLE Input (VB-Audio)

# Global Audio Settings
SAMPLE_RATE = 44100
BLOCK_SIZE = 512       # Latency control (256, 512, atau 1024)
CHANNELS = 1           # Mono atau Stereo (1 atau 2)
DTYPE = 'float32'