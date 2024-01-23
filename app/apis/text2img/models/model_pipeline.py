import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float16)
pipe.to(device)
pipe.enable_attention_slicing()

prompt = "A cat on rooftop"
image = pipe(prompt).images[0]
    
image.save("astronaut_rides_horse.png")

# def generate(prompt:str):
#     with autocast(device): 
#         image = pipe(prompt, guidance_scale=8.5).images[0]
    
#     image.save('generatedimage.png')
    
#     # return image

# generate(prompt)
    