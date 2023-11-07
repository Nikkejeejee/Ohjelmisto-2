from flask import Flask

dude = Flask(__name__)
print(__name__)
@dude.route('/')
def get_root():
    return 'Moro'

@dude.route('/booty')
def get_booty():
    return 'Not enough rizz'

dude.run(use_reloader=True)
