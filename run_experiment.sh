#!/bin/bash
#SBATCH --job-name=SleePyCo_Run       # Job name (%j: job ID)
#SBATCH --output=SleePyCo_Logs.out          # Standard output log
#SBATCH --error=SleePyCo_Errors.err           # Standard error log
#SBATCH --time=24:00:00                   # Maximum runtime
#SBATCH --cpus-per-task=8                # Number of CPU cores per task
#SBATCH --gpus=1                         # Request 1 GPU
#SBATCH --mem-per-cpu=4096                # Memory per CPU core
#SBATCH --mail-type=END,FAIL             # Notifications for job done and fail
#SBATCH --mail-user=shagupta@ethz.ch     # Email to send notifications


# Get config file from first argument, use default if not provided
PRETRAIN_CONFIG_FILE=${1:-configs/configs/SleePyCo-Transformer_SL-01_numScales-1_Sleep-EDF-2018_pretrain.json}
TRAIN_CONFIG_FILE=${2:-configs/configs/SleePyCo-Transformer_SL-10_numScales-3_Sleep-EDF-2018_freezefinetune.json}

# Activate the conda environment
echo "Activating conda environment 'sleepnet'..."
source ~/.bashrc                                # Initialize conda
conda activate sleepnet

echo "Changing directory to /home/shagupta/SleePyCo..."
cd /home/shagupta/SleePyCo

# Define GPU_IDs
GPU_IDs=0

echo "Starting pretraining with config $PRETRAIN_CONFIG_FILE on GPU $GPU_IDs..."
python train_crl.py --config "$PRETRAIN_CONFIG_FILE" --gpu $GPU_IDs
echo "Pretraining completed."

echo "Starting fine-tuning with config $TRAIN_CONFIG_FILE on GPU $GPU_IDs..."
python train_mtcl.py --config "$TRAIN_CONFIG_FILE" --gpu $GPU_IDs
echo "Fine-tuning completed."