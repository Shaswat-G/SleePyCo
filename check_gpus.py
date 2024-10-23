import torch

if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")
    for i in range(num_gpus):
        print(f"GPU ID: {i}, GPU Name: {torch.cuda.get_device_name(i)}")
else:
    print("No GPU available.")