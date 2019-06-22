'''
Function to Convert Text from Inkscape Inx File into GCode using custom Inkscape
Extension, Hershey Text, and GCode Tools
'''

def inx2GCode():
    
    # Convert SVG File to GCode using InkScape
    import subprocess
    import time
    import shlex
        
    inkscapeCmds = """inkscape blank.svg --verb=twitter.cnc.noprefs --verb=EditSelectAll
                    --verb=ObjectFlipHorizontally --verb=SelectionReverse
                    --verb=ru.cnc-club.filter.gcodetools_tools_library_no_options_no_preferences.noprefs
                    --verb=ru.cnc-club.filter.gcodetools_orientation_no_options_no_preferences.noprefs
                    --verb=EditSelectAll --verb=ru.cnc-club.filter.gcodetools_ptg.noprefs"""
        
    print(inkscapeCmds)
    process = subprocess.Popen(shlex.split(inkscapeCmds))
    time.sleep(50)
    process.kill()
