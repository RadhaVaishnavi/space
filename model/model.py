import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)

def generate_caption(image_file):
    image = Image.open(image_file)
    image = preprocess(image).unsqueeze(0).to(device)

    text = clip.tokenize(["A satellite image of a city", "A satellite image of a field"]).to(device)

    with torch.no_grad():
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    return "Generated Caption: A satellite image with high probability is ... [example caption]"

