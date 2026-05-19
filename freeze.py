from flask_frozen import Freezer
from app import app

# Tells Frozen-Flask to output static files directly to the root or a build folder
app.config['FREEZER_DESTINATION'] = 'build'
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("Static site successfully generated in the /build directory!")