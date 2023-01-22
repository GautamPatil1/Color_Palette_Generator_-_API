from flask import Flask, jsonify, render_template
import random
import colorsys

app = Flask(__name__)


def convert_color(color_str):
    if color_str[0] == '#':
        # HEX format
        color = tuple(int(color_str[i:i+2], 16) for i in (1, 3, 5))
        return color
    elif color_str[0] == 'r':
        # RGB format
        color = tuple(map(int, color_str[4:-1].split(',')))
        return color
    elif color_str[0] == 'h':
        # HSL format
        h, s, l = map(float, color_str[4:-1].split(','))
        r, g, b = [int(i * 255) for i in colorsys.hls_to_rgb(h, l, s)]
        return (r, g, b)
    else:
        raise ValueError("Invalid color format")

def generate_palette(base_color = None, n_colors = 4):
    if base_color is None:
        base_color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    h, s, v = colorsys.rgb_to_hsv(*base_color)
    hue, sat, val = h, s, v
    sat_step = (1-s)/n_colors
    val_step = (1-v)/n_colors
    palette = []
    for i in range(n_colors):
        s_i = s - i*sat_step
        v_i = v - i*val_step
        r, g, b = colorsys.hsv_to_rgb(hue, s_i, v_i)
        r, g, b = (int(r * 255), int(g * 255), int(b * 255))
        palette.append('#{:02x}{:02x}{:02x}'.format(r, g, b))
    return palette



palette = {
    'source' : 'https://gautampatil.pythonanywhere.com/palette-generator',
    'palette' : None
}

@app.route('/palette-generator')
def index():
    return render_template('index.html')


@app.route('/palette')
def default():
    palette['palette'] = generate_palette()
    return jsonify(palette)

@app.route('/palette/<int:n_colors>')
def custom_n(n_colors):
    palette['palette'] = generate_palette(n_colors=n_colors)
    return jsonify(palette)


@app.route('/palette/<string:color>')
def custom(color):
    color = convert_color(color)
    palette['palette'] = generate_palette(color)
    return jsonify(palette)
 
if __name__ == '__main__':
    app.run(debug=True)
