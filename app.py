from flask import Flask, render_template, request
from PIL import Image
import numpy as np

app = Flask(__name__)

# Route to render the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle image upload and display the most common colors
@app.route('/colors', methods=['POST'])
def colors():
    # Get the uploaded image file
    image_file = request.files['image']
    # Open the image using PIL
    image = Image.open(image_file)
    # Convert the image to RGB format
    image = image.convert('RGB')
    # Convert the image to a NumPy array
    image_array = np.array(image)
    # Get the colors from the image as a list of tuples
    colors = image_array.reshape(-1, 3)
    # Count the occurrence of each color
    color_count = {}
    for color in colors:
        hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
        if hex_color in color_count:
            color_count[hex_color] += 1
        else:
            color_count[hex_color] = 1
    # Sort the colors by count (most common first)
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)
    # Get the top 10 most common colors
    top_colors = sorted_colors[:10]
    # Render the template to display the most common colors
    return render_template('colors.html', top_colors=top_colors)

if __name__ == '__main__':
    app.run(debug=True)
