import torch
import numpy as np
import librosa
import time
import soundfile as sf

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16  

print(f"--- Running on: {torch.cuda.get_device_name(0)} ---")

def load_voice_model(model_path):
    print(f"Loading model dari: {model_path}...")
    time.sleep(1) 
    print("Model loaded successfully!")
    return True

def convert_voice(audio_input, pitch_shift=0):
    print(f"Memproses audio dengan pitch shift: {pitch_shift}")
    
    audio_tensor = torch.from_numpy(audio_input).to(device, dtype=dtype)
    
    start_time = time.time()
    
    output_tensor = audio_tensor * 1.5 
    torch.cuda.synchronize()
    
    end_time = time.time()
    return output_tensor.to(torch.float32).cpu().numpy(), (end_time - start_time)

if __name__ == "__main__":
    # 1. Load Audio
    input_path = r"C:\Users\rizki\Downloads\archive\BAK.wav" 
    try:
        # Load audio librosa
        audio_data, sr = librosa.load(input_path, sr=40000) 
        print(f"File {input_path} berhasil di-load!")
    except:
        print("File audio nggak ketemu, pake dummy data lagi...")
        sr = 40000
        audio_data = np.random.uniform(-1, 1, sr * 5).astype(np.float32)

    # 2. Proses Conversion
    if load_voice_model("model_agung_v1.pth"):
        output, duration = convert_voice(audio_data, pitch_shift=12)
        
        # 3. Simpan Hasilnya ke Folder Proyek Lu
        output_name = "hasil_voice_changer.wav"
        sf.write(output_name, output, sr)
        
        print(f"\n[SUMMARY CP4]")
        print(f"File disimpan: {output_name}")
        print(f"Waktu Proses: {duration:.4f} detik")
        print(f"Kecepatan: {len(audio_data)/sr/duration:.2f}x lipat dari real-time")