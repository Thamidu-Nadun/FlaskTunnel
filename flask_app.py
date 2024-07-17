from flask import Flask, request, jsonify, render_template
import os
import subprocess
import argparse

app = Flask(__name__)

# Set up arguments
parser = argparse.ArgumentParser(description='A powerful tool for make a tunnel to your computer. Run the application to go crazy.')
parser.add_argument('directory', type=str, help='Directory to host the Flask app.')
parser.add_argument('-v', '--version', action='version', version='1.0', help='Show version information')
args = parser.parse_args()

# Set BASE_DIR from command-line argument
BASE_DIR = os.path.abspath(args.directory)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    command = request.json.get('command', '').strip()
    
    if command == '':
        return jsonify({'output': '', 'error': 'No command provided.'})

    if command.startswith('cd '):
        dir_name = command.split(' ', 1)[1]
        try:
            os.chdir(os.path.join(BASE_DIR, dir_name))
            return jsonify({'output': '', 'error': None})
        except Exception as e:
            return jsonify({'output': '', 'error': str(e)})
    
    try:
        output = subprocess.check_output(command, shell=True, cwd=BASE_DIR, text=True)
        result = {'output': output, 'error': None}
    except subprocess.CalledProcessError as e:
        result = {'output': '', 'error': str(e)}
    except Exception as e:
        result = {'output': '', 'error': str(e)}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
