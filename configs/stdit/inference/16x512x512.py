num_frames = 16
fps = 24 // 3
image_size = (512, 512)

# Define model
model = dict(
    type="STDiT-XL/2",
    space_scale=1.0,
    time_scale=1.0,
    enable_flashattn=True,
    enable_layernorm_kernel=True,
    from_pretrained=""
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=2,
)
text_encoder = dict(
    type="t5",
    from_pretrained="DeepFloyd/t5-v1_1-xxl",
    model_max_length=120,
)
scheduler = dict(
    type="iddpm",
    num_sampling_steps=100,
    cfg_scale=7.0,
)

dtype = "fp16"
#dtype = "bf16"

# Others
batch_size = 2
seed = 42
prompt_path = "./assets/texts/evalcrafter.txt"
start_idx = 0
end_idx = 700
save_dir = "./outputs/samples/"
