#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on April 27, 2021, at 13:28
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = '000_LangMusic_FinalTask_PsychoPyBuilder'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Micaceous\\Desktop\\Research\\LangMusic\\Final_Task_psychopy\\000_LangMusic_FinalTask_PsychoPyBuilder.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welcome_back = visual.ImageStim(
    win=win, name='Welcome_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text="Welcome to the LangMusic experiment!\n\nPress spacebar when you're ready to continue.",
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=600, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()

Break_back = visual.ImageStim(
    win=win, name='Break_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Break_text = visual.TextStim(win=win, name='Break_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=800, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()

Trial_back = visual.ImageStim(
    win=win, name='Trial_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Trial_sound = sound.Sound('A', secs=-1, stereo=True)
Trial_sound.setVolume(1)
Trial_fix = visual.TextStim(win=win, name='Trial_fix',
    text='+',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Trial_word1 = visual.TextStim(win=win, name='Trial_word1',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Trial_word2 = visual.TextStim(win=win, name='Trial_word2',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Trial_word3 = visual.TextStim(win=win, name='Trial_word3',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Trial_word4 = visual.TextStim(win=win, name='Trial_word4',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Trial_word5 = visual.TextStim(win=win, name='Trial_word5',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Trial_word6 = visual.TextStim(win=win, name='Trial_word6',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
Trial_word7 = visual.TextStim(win=win, name='Trial_word7',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
Trial_word8 = visual.TextStim(win=win, name='Trial_word8',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "Question1"
Question1Clock = core.Clock()

Q1_back = visual.ImageStim(
    win=win, name='Q1_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Q1_text = visual.TextStim(win=win, name='Q1_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=800, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Question2"
Question2Clock = core.Clock()

Q2_back = visual.ImageStim(
    win=win, name='Q2_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Q2_test = visual.TextStim(win=win, name='Q2_test',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=800, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "TrialBreak"
TrialBreakClock = core.Clock()
TrialBreak_back = visual.ImageStim(
    win=win, name='TrialBreak_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
TrialBreak_text = visual.TextStim(win=win, name='TrialBreak_text',
    text='Press spacebar to continue',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
End_back = visual.ImageStim(
    win=win, name='End_back',units='pix', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(800, 600),
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
End_text = visual.TextStim(win=win, name='End_text',
    text='Thank you for your participation!',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Welcome_resp = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeComponents = [Welcome_back, Welcome_text, Welcome_resp]
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_back* updates
    if t >= 0.0 and Welcome_back.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome_back.tStart = t
        Welcome_back.frameNStart = frameN  # exact frame index
        Welcome_back.setAutoDraw(True)
    
    # *Welcome_text* updates
    if t >= 0.0 and Welcome_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome_text.tStart = t
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.setAutoDraw(True)
    
    # *Welcome_resp* updates
    if t >= 0.0 and Welcome_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome_resp.tStart = t
        Welcome_resp.frameNStart = frameN  # exact frame index
        Welcome_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Welcome_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Welcome_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Welcome_resp.keys = theseKeys[-1]  # just the last key pressed
            Welcome_resp.rt = Welcome_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Welcome_resp.keys in ['', [], None]:  # No response was made
    Welcome_resp.keys=None
thisExp.addData('Welcome_resp.keys',Welcome_resp.keys)
if Welcome_resp.keys != None:  # we had a response
    thisExp.addData('Welcome_resp.rt', Welcome_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RunLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('000_OuterLoop_LongerVersion.xlsx'),
    seed=None, name='RunLoop')
thisExp.addLoop(RunLoop)  # add the loop to the experiment
thisRunLoop = RunLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRunLoop.rgb)
if thisRunLoop != None:
    for paramName in thisRunLoop:
        exec('{} = thisRunLoop[paramName]'.format(paramName))

for thisRunLoop in RunLoop:
    currentLoop = RunLoop
    # abbreviate parameter names if possible (e.g. rgb = thisRunLoop.rgb)
    if thisRunLoop != None:
        for paramName in thisRunLoop:
            exec('{} = thisRunLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Break"-------
    t = 0
    BreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    msg = "Task Type:  " + str(Task) + ",      Press spacebar when ready"
    
    chunks=InnerLoopChunks
    
    Break_text.setText(msg
)
    Break_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    BreakComponents = [Break_back, Break_text, Break_resp]
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Break_back* updates
        if t >= 0.0 and Break_back.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_back.tStart = t
            Break_back.frameNStart = frameN  # exact frame index
            Break_back.setAutoDraw(True)
        
        # *Break_text* updates
        if t >= 0.0 and Break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_text.tStart = t
            Break_text.frameNStart = frameN  # exact frame index
            Break_text.setAutoDraw(True)
        
        # *Break_resp* updates
        if t >= 0.0 and Break_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_resp.tStart = t
            Break_resp.frameNStart = frameN  # exact frame index
            Break_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Break_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Break_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Break_resp.keys = theseKeys[-1]  # just the last key pressed
                Break_resp.rt = Break_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if Break_resp.keys in ['', [], None]:  # No response was made
        Break_resp.keys=None
    RunLoop.addData('Break_resp.keys',Break_resp.keys)
    if Break_resp.keys != None:  # we had a response
        RunLoop.addData('Break_resp.rt', Break_resp.rt)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    TrialLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(ConditionsFile, selection=chunks),
        seed=None, name='TrialLoop')
    thisExp.addLoop(TrialLoop)  # add the loop to the experiment
    thisTrialLoop = TrialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    for thisTrialLoop in TrialLoop:
        currentLoop = TrialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                exec('{} = thisTrialLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Trial"-------
        t = 0
        TrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(8.500000)
        # update component parameters for each repeat
        if setnum == "None" and musiccondnum == "None":
            musicfile = "silent.wav"
        else:
            musicfile = "set" + str(setnum) + "_" + str(musiccondnum) + ".wav"
        
        #chunks=InnerLoopChunks
        #print str(chunks) + str(3)
        Trial_sound.setSound(musicfile, secs=8.50)
        Trial_sound.setVolume(1, log=False)
        Trial_word1.setText(Word1)
        Trial_word2.setText(Word2)
        Trial_word3.setText(Word3)
        Trial_word4.setText(Word4)
        Trial_word5.setText(Word5)
        Trial_word6.setText(Word6)
        Trial_word7.setText(Word7)
        Trial_word8.setText(Word8)
        # keep track of which components have finished
        TrialComponents = [Trial_back, Trial_sound, Trial_fix, Trial_word1, Trial_word2, Trial_word3, Trial_word4, Trial_word5, Trial_word6, Trial_word7, Trial_word8]
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *Trial_back* updates
            if t >= 0.0 and Trial_back.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_back.tStart = t
                Trial_back.frameNStart = frameN  # exact frame index
                Trial_back.setAutoDraw(True)
            frameRemains = 0.0 + 8.50- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_back.status == STARTED and t >= frameRemains:
                Trial_back.setAutoDraw(False)
            # start/stop Trial_sound
            if t >= 0.0 and Trial_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_sound.tStart = t
                Trial_sound.frameNStart = frameN  # exact frame index
                win.callOnFlip(Trial_sound.play)  # screen flip
            frameRemains = 0.0 + 8.50- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_sound.status == STARTED and t >= frameRemains:
                Trial_sound.stop()  # stop the sound (if longer than duration)
            
            # *Trial_fix* updates
            if t >= 0.0 and Trial_fix.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_fix.tStart = t
                Trial_fix.frameNStart = frameN  # exact frame index
                Trial_fix.setAutoDraw(True)
            frameRemains = 0.0 + 2.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_fix.status == STARTED and t >= frameRemains:
                Trial_fix.setAutoDraw(False)
            
            # *Trial_word1* updates
            if t >= 2.25 and Trial_word1.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word1.tStart = t
                Trial_word1.frameNStart = frameN  # exact frame index
                Trial_word1.setAutoDraw(True)
            frameRemains = 2.25 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word1.status == STARTED and t >= frameRemains:
                Trial_word1.setAutoDraw(False)
            
            # *Trial_word2* updates
            if t >= 3.0 and Trial_word2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word2.tStart = t
                Trial_word2.frameNStart = frameN  # exact frame index
                Trial_word2.setAutoDraw(True)
            frameRemains = 3.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word2.status == STARTED and t >= frameRemains:
                Trial_word2.setAutoDraw(False)
            
            # *Trial_word3* updates
            if t >= 3.75 and Trial_word3.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word3.tStart = t
                Trial_word3.frameNStart = frameN  # exact frame index
                Trial_word3.setAutoDraw(True)
            frameRemains = 3.75 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word3.status == STARTED and t >= frameRemains:
                Trial_word3.setAutoDraw(False)
            
            # *Trial_word4* updates
            if t >= 4.50 and Trial_word4.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word4.tStart = t
                Trial_word4.frameNStart = frameN  # exact frame index
                Trial_word4.setAutoDraw(True)
            frameRemains = 4.50 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word4.status == STARTED and t >= frameRemains:
                Trial_word4.setAutoDraw(False)
            
            # *Trial_word5* updates
            if t >= 5.25 and Trial_word5.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word5.tStart = t
                Trial_word5.frameNStart = frameN  # exact frame index
                Trial_word5.setAutoDraw(True)
            frameRemains = 5.25 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word5.status == STARTED and t >= frameRemains:
                Trial_word5.setAutoDraw(False)
            
            # *Trial_word6* updates
            if t >= 6.0 and Trial_word6.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word6.tStart = t
                Trial_word6.frameNStart = frameN  # exact frame index
                Trial_word6.setAutoDraw(True)
            frameRemains = 6.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word6.status == STARTED and t >= frameRemains:
                Trial_word6.setAutoDraw(False)
            
            # *Trial_word7* updates
            if t >= 6.75 and Trial_word7.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word7.tStart = t
                Trial_word7.frameNStart = frameN  # exact frame index
                Trial_word7.setAutoDraw(True)
            frameRemains = 6.75 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word7.status == STARTED and t >= frameRemains:
                Trial_word7.setAutoDraw(False)
            
            # *Trial_word8* updates
            if t >= 7.50 and Trial_word8.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trial_word8.tStart = t
                Trial_word8.frameNStart = frameN  # exact frame index
                Trial_word8.setAutoDraw(True)
            frameRemains = 7.50 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Trial_word8.status == STARTED and t >= frameRemains:
                Trial_word8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        Trial_sound.stop()  # ensure sound has stopped at end of routine
        
        # ------Prepare to start Routine "Question1"-------
        t = 0
        Question1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        if randQMnum == 1:
            if randQnum == 1:
                Q1 = QLang1
        #        corans=QLang1Cor
            else:
                Q1 = QLang2
        #        corans=QLang2Cor
        else:
            Q1=QMusic
        
        
        Q1_text.setText(Q1)
        Q1_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        Question1Components = [Q1_back, Q1_text, Q1_resp]
        for thisComponent in Question1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Question1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Question1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *Q1_back* updates
            if t >= 0.0 and Q1_back.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q1_back.tStart = t
                Q1_back.frameNStart = frameN  # exact frame index
                Q1_back.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q1_back.status == STARTED and t >= frameRemains:
                Q1_back.setAutoDraw(False)
            
            # *Q1_text* updates
            if t >= 0.0 and Q1_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q1_text.tStart = t
                Q1_text.frameNStart = frameN  # exact frame index
                Q1_text.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q1_text.status == STARTED and t >= frameRemains:
                Q1_text.setAutoDraw(False)
            
            # *Q1_resp* updates
            if t >= 0.0 and Q1_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q1_resp.tStart = t
                Q1_resp.frameNStart = frameN  # exact frame index
                Q1_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Q1_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q1_resp.status == STARTED and t >= frameRemains:
                Q1_resp.status = FINISHED
            if Q1_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', 'space', 'capslock', 'return'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q1_resp.keys = theseKeys[-1]  # just the last key pressed
                    Q1_resp.rt = Q1_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Question1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Question1"-------
        for thisComponent in Question1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if Q1_resp.keys in ['', [], None]:  # No response was made
            Q1_resp.keys=None
        TrialLoop.addData('Q1_resp.keys',Q1_resp.keys)
        if Q1_resp.keys != None:  # we had a response
            TrialLoop.addData('Q1_resp.rt', Q1_resp.rt)
        
        # ------Prepare to start Routine "Question2"-------
        t = 0
        Question2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        if randQMnum == 2:
            if randQnum == 2:
                Q2 = QLang1
        #        corans=QLang1Cor
            else:
                Q2 = QLang2
        #        corans=QLang2Cor
        else:
            Q2=QMusic
        Q2_test.setText(Q2)
        Q2_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        Question2Components = [Q2_back, Q2_test, Q2_resp]
        for thisComponent in Question2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Question2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Question2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *Q2_back* updates
            if t >= 0.0 and Q2_back.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q2_back.tStart = t
                Q2_back.frameNStart = frameN  # exact frame index
                Q2_back.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q2_back.status == STARTED and t >= frameRemains:
                Q2_back.setAutoDraw(False)
            
            # *Q2_test* updates
            if t >= 0.0 and Q2_test.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q2_test.tStart = t
                Q2_test.frameNStart = frameN  # exact frame index
                Q2_test.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q2_test.status == STARTED and t >= frameRemains:
                Q2_test.setAutoDraw(False)
            
            # *Q2_resp* updates
            if t >= 0.0 and Q2_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q2_resp.tStart = t
                Q2_resp.frameNStart = frameN  # exact frame index
                Q2_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Q2_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Q2_resp.status == STARTED and t >= frameRemains:
                Q2_resp.status = FINISHED
            if Q2_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', 'capslock', 'return', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q2_resp.keys = theseKeys[-1]  # just the last key pressed
                    Q2_resp.rt = Q2_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Question2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Question2"-------
        for thisComponent in Question2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if Q2_resp.keys in ['', [], None]:  # No response was made
            Q2_resp.keys=None
        TrialLoop.addData('Q2_resp.keys',Q2_resp.keys)
        if Q2_resp.keys != None:  # we had a response
            TrialLoop.addData('Q2_resp.rt', Q2_resp.rt)
        
        # ------Prepare to start Routine "TrialBreak"-------
        t = 0
        TrialBreakClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        TrialBreak_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        TrialBreakComponents = [TrialBreak_back, TrialBreak_text, TrialBreak_resp]
        for thisComponent in TrialBreakComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "TrialBreak"-------
        while continueRoutine:
            # get current time
            t = TrialBreakClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialBreak_back* updates
            if t >= 0.0 and TrialBreak_back.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialBreak_back.tStart = t
                TrialBreak_back.frameNStart = frameN  # exact frame index
                TrialBreak_back.setAutoDraw(True)
            
            # *TrialBreak_text* updates
            if t >= 0.0 and TrialBreak_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialBreak_text.tStart = t
                TrialBreak_text.frameNStart = frameN  # exact frame index
                TrialBreak_text.setAutoDraw(True)
            
            # *TrialBreak_resp* updates
            if t >= 0.0 and TrialBreak_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialBreak_resp.tStart = t
                TrialBreak_resp.frameNStart = frameN  # exact frame index
                TrialBreak_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(TrialBreak_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if TrialBreak_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    TrialBreak_resp.keys = theseKeys[-1]  # just the last key pressed
                    TrialBreak_resp.rt = TrialBreak_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialBreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TrialBreak"-------
        for thisComponent in TrialBreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if TrialBreak_resp.keys in ['', [], None]:  # No response was made
            TrialBreak_resp.keys=None
        TrialLoop.addData('TrialBreak_resp.keys',TrialBreak_resp.keys)
        if TrialBreak_resp.keys != None:  # we had a response
            TrialLoop.addData('TrialBreak_resp.rt', TrialBreak_resp.rt)
        # the Routine "TrialBreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'TrialLoop'
    
    # get names of stimulus parameters
    if TrialLoop.trialList in ([], [None], None):
        params = []
    else:
        params = TrialLoop.trialList[0].keys()
    # save data for this loop
    TrialLoop.saveAsExcel(filename + '.xlsx', sheetName='TrialLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    TrialLoop.saveAsText(filename + 'TrialLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1 repeats of 'RunLoop'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [End_back, End_text]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_back* updates
    if t >= 0.0 and End_back.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_back.tStart = t
        End_back.frameNStart = frameN  # exact frame index
        End_back.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if End_back.status == STARTED and t >= frameRemains:
        End_back.setAutoDraw(False)
    
    # *End_text* updates
    if t >= 0.0 and End_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_text.tStart = t
        End_text.frameNStart = frameN  # exact frame index
        End_text.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if End_text.status == STARTED and t >= frameRemains:
        End_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
