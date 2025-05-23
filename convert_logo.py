from cairosvg import svg2png

# Convert SVG to PNG
svg2png(url='students/static/students/images/logo.svg',
        write_to='students/static/students/images/logo.png',
        output_width=200,
        output_height=200) 