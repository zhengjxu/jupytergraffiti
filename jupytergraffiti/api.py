from __future__ import absolute_import
from IPython.display import Javascript, display_javascript, HTML

def run_js(jscmd, force):
    if (force):
        jsf = Javascript(jscmd)
    else:
        jsf = Javascript("// Graffiti javascript\n" + "if (window.Graffiti !== undefined) {\n" + jscmd + "\n}\n")
    display_javascript(jsf)
    
# You don't need to call the initialize function, it is called by __init__.py
def initialize():
    run_js("require(['jupytergraffiti/js/loader.js']);", True)

# Play an existing movie recording back. Pass in the recording API key.
def play_recording(recording_id):
    run_js("window.Graffiti.playRecordingById('" + recording_id + "')", False)

# Display a clickable prompt in the Jupyter meu bar that will play an existing movie recording back when clicked. 
# Pass in the recording API key, and a markdown string that you want to be displayed.
def play_recording_with_prompt(recording_id, prompt_markdown):
    run_js("window.Graffiti.playRecordingByIdWithPrompt('" + recording_id + "','" + prompt_markdown.replace("'", "\\'") + "')", False)

# After you choose "make a copy" in Jupyter notebook, the notebook id will still point all graffitis at the original notebooks' graffitis.
# You must call this function after "Make a copy". This will assign a new graffiti id to the notebook, and copy the previous graffitis to a directory with
# the new graffiti id in the directory name.
def transfer_graffitis():
    run_js("window.Graffiti.transferGraffitis", False)

# Stop playback of any movie recording currently playing.
def stop_playback():
    run_js("window.Graffiti.cancelPlayback()", False)

# Remove all Graffiti from the current notebook. You will be prompted by a confirmation dialog.
def remove_all_annotations():
    run_js("window.Graffiti.removeAllGraffiti()", False)

def show_creators_chooser():
    run_js("window.Graffiti.showCreatorsChooser()", False)

# Set your access level to Graffiti, one of either "create" or "view".
def set_access_level(level):
    run_js("window.Graffiti.setAccessLevel('" + level + "')", False)
