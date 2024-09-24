import torch
from transformers import CLIPModel, CLIPProcessor

# Replace with your trained model path
model_path = 'path/to/your/trained/model.pt'

# Load the CLIP model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
model.load_state_dict(torch.load(model_path))
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def generate_caption(image):
  # Preprocess image (resize, convert to RGB, etc.)
  #...  (Implement your image preprocessing logic here)

  with torch.no_grad():
    image_input = processor(images=image, return_tensors="pt", padding=True)
    image_features = model.get_image_features(**image_input).to(device)

    # Implement your caption generation logic based on image features
    # This is a placeholder, replace with your approach
    caption = "A satellite image of..."  # Replace with actual generation

    return caption
