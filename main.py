from PIL import Image, ImageDraw, ImageFont
import random

def apply_polaroid_effect(image_path, output_path):
    # Open the original image
    image = Image.open(image_path)
    
    # Create a white border to simulate Polaroid
    border_size = 50
    new_width = image.width + border_size * 2
    new_height = image.height + border_size * 3  # Extra space at the bottom
    polaroid = Image.new('RGB', (new_width, new_height), 'white')
    polaroid.paste(image, (border_size, border_size))
    
    # Add random two words
    words = ['Sunset', 'Adventure', 'Memory', 'Journey', 'Smile', 'Dream']
    text = ' '.join(random.sample(words, 2))
    
    draw = ImageDraw.Draw(polaroid)
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((new_width - text_width) / 2, new_height - border_size + 10)
    draw.text(text_position, text, fill='black', font=font)
    
    # Save the processed image
    polaroid.save(output_path)
