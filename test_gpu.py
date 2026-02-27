import torch
import time

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU Name: {torch.cuda.get_device_name(0)}")
print(f"Supported Architectures: {torch.cuda.get_arch_list()}")

try:
    x = torch.randn(1).cuda()
    print("Success: Tensor operation completed on GPU.")
except RuntimeError as e:
    print(f"Error: {e}")


size = 25000
a = torch.randn(size, size, device='cuda')
b = torch.randn(size, size, device='cuda')

_ = torch.matmul(a, b)
torch.cuda.synchronize()

start = time.time()
for _ in range(10):
    c = torch.matmul(a, b)
torch.cuda.synchronize()
end = time.time()

print(f"Waktu rata-rata matmul {size}x{size}: {(end - start)/10:.4f} detik")
print(f"GPU Memory Allocated: {torch.cuda.memory_allocated(0) / 1024**2:.2f} MB")