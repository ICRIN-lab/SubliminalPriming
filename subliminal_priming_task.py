import time

from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile

from random import randint

import os

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    # Store info about the experiment session
    expName = 'Flanker'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001', 'date': data.getDateStr(), 'expName': expName}
dlg = gui.DlgFromDict(expInfo, title='Flanker', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = expInfo['participant'] + '_' + expInfo['date']
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
dataFile = open('~/PycharmProjects/FlankerTask/Flankercsv/' + str(fileName) + '.csv',
                'w')  # a simple text file with
# 'comma-separated-values'
dataFile.write('no_trial, id_candidate, visual, condition, ans_candidate, good_ans, correct, '
               'practice, reaction_time, time_stamp\n')

filename = _thisDir + os.sep + u'Flanker/Flankerlog/%s_%s' % (expInfo['participant'], expInfo['date'])


class Flanker:
    # create init w/ users data
    def __init__(self, start):
        self.start = start
        self.keys = ['a', 'p']

    def run(self):
        global good_answer
        L = ["<<<<<<<<<", ">>>><>>>>", "<<<<><<<<", ">>>>>>>>"]
        rnd = 0
        score = 0
        i = 0

        # We create an empty window
        win = visual.Window(
            size=[1920, 1080],  # if needed, change the size in corcondance with your monitor
            fullscr=False,
            units="pix",
            screen=0,
            allowStencil=False,
            monitor='testMonitor',
            color='black',
            colorSpace='rgb')
        win.winHandle.set_fullscreen(True)
        win.flip()
        win.mouseVisible = False

        # Here, we create all of the different visuals which will be shown through the previously created window
        bienvenue = visual.TextStim(
            win=win,
            name='bienvenue',
            text="Bienvenue",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        instr = visual.TextStim(
            win=win,
            name='instr',
            text='Dans ce mini-jeu, appuyez sur "a" si la flèche centrale est en direction de la gauche, \n et sur "p" si elle l\'est vers la droite.',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        exemple = visual.TextStim(
            win=win,
            name='exemple',
            text='Commençons par un exemple',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        attention2 = visual.TextStim(
            win=win,
            name='attention2',
            text="S'il-vous-plaît, n'appuyez que lorsqu'on vous le demande ou lors du mini-jeu",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        doigts = visual.TextStim(
            win=win,
            name='doigts',
            text='Placez vos doigts sur les touches "a" et "p" s\'il-vous-plaît',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        pret = visual.TextStim(
            win=win,
            name='prêt',
            text='Appuyez sur "a" ou "p" lorsque vous vous sentez prêt(e)',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        bonne_chance = visual.TextStim(
            win=win,
            name='bonne_chance',
            text='Bonne chance :)',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        croix = visual.TextStim(
            win=win,
            name='croix',
            text="+",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        silence = visual.TextStim(
            win=win,
            name='silence',
            text="",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        arrows = visual.TextStim(
            win=win,
            name='arrows',
            text=L[rnd],
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        tutoriel_end = visual.TextStim(
            win=win,
            name='tutoriel',
            text="Le tutoriel est désormais terminé",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        pret_V2 = visual.TextStim(
            win=win,
            name='pret_V2',
            text='Appuyez sur "a" ou "p" pour commencer le mini-jeu',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        pressure = visual.TextStim(
            win=win,
            name='pressure',
            text="Le mini-jeu va maintenant commencer, \n c'est comme tout à l'heure \n  alors pas de pression",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        end = visual.TextStim(
            win=win, name='end',
            text='Le mini-jeu est désormais terminé',
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        good_day = visual.TextStim(
            win=win,
            name='good day',
            text="Merci, et bonne journée :)",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)

        # Here is the practice, the objective is to make sure the user understands the task
        bienvenue.draw()
        win.flip()
        core.wait(2)
        instr.draw()
        win.flip()
        core.wait(5)
        exemple.draw()
        win.flip()
        core.wait(3)
        attention2.draw()
        win.flip()
        core.wait(3)
        doigts.draw()
        win.flip()
        core.wait(5)
        pret.draw()
        win.flip()
        event.waitKeys(keyList=['a', 'p'], maxWait=10, clearEvents=True)
        bonne_chance.draw()
        win.flip()
        core.wait(2)

        for i in range(3):
            rnd = randint(0, 3)
            if (rnd == 0) or (rnd == 1):
                good_ans = "a"
            else:
                good_ans = "p"
            if (rnd == 0) or (rnd == 3):
                condition = "Congruent"
            else:
                condition = "Incongruent"
            croix.draw()
            win.flip()
            core.wait(0.5)
            arrows = visual.TextStim(
                win=win,
                name='arrows',
                text=L[rnd],
                font='Arial',
                units='height',
                pos=(0, 0),
                height=0.06,
                wrapWidth=None,
                ori=0,
                color='white',
                colorSpace='rgb',
                opacity=1,
                languageStyle='LTR',
                depth=0.0)
            arrows.draw()
            win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                good_answer = True
                score = score + 1
                congrats = visual.TextStim(
                    win=win,
                    name='congrats',
                    text="Bravo ! \n Vous avez " + str(score) + "/" + str(i + 1),
                    font='Arial',
                    units='height',
                    pos=(0, 0),
                    height=0.06,
                    wrapWidth=None,
                    ori=0,
                    color='white',
                    colorSpace='rgb',
                    opacity=1,
                    languageStyle='LTR',
                    depth=0.0)
                congrats.draw()
                win.flip()
                core.wait(2)
            elif resp != good_ans:
                good_answer = False
                missed = visual.TextStim(
                    win=win,
                    name='missed',
                    text="Dommage... \n Vous avez " + str(score) + "/" + str(i + 1),
                    font='Arial',
                    units='height',
                    pos=(0, 0),
                    height=0.06,
                    wrapWidth=None,
                    ori=0,
                    color='white',
                    colorSpace='rgb',
                    opacity=1,
                    languageStyle='LTR',
                    depth=0.0)
                missed.draw()
                win.flip()
                core.wait(2)
            else:
                good_answer = None
            dataFile.write(
                str(i)
                +
                ','
                +
                expInfo['participant']
                +
                ','
                +
                str(L[rnd])
                +
                ','
                +
                str(condition)
                +
                ','
                +
                str(resp)
                +
                ','
                +
                str(good_ans)
                +
                ','
                +
                str(good_answer)
                +
                ','
                +
                'yes'
                +
                ','
                +
                str(round(rt, 2))
                +
                ','
                +
                str(round(time.time() - start, 2))
                +
                '\n')
            silence.draw()
            win.flip()
            rnd_time = randint(8, 14)
            core.wait(rnd_time * 10 ** -3)
        croix.draw()
        win.flip()
        core.wait(1)
        results = visual.TextStim(
            win=win,
            name='results',
            text="Vous avez obtenu " + str(score) + "/3",
            font='Arial',
            units='height',
            pos=(0, 0),
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)
        results.draw()
        win.flip()
        core.wait(5)
        tutoriel_end.draw()
        win.flip()

        # Here, the real test starts
        core.wait(3)
        pret_V2.draw()
        win.flip()
        event.waitKeys(keyList=['a', 'p'], maxWait=10, clearEvents=True)
        doigts.draw()
        win.flip()
        core.wait(5)
        pressure.draw()
        win.flip()
        core.wait(5)
        bonne_chance.draw()
        win.flip()
        core.wait(2)

        for i in range(10):
            rnd = randint(0, 3)
            if (rnd == 0) or (rnd == 1):
                good_ans = "a"
            else:
                good_ans = "p"
            if (rnd == 0) or (rnd == 3):
                condition = "Congruent"
            else:
                condition = "Incongruent"
            croix.draw()
            win.flip()
            core.wait(0.5)
            arrows = visual.TextStim(
                win=win,
                name='arrows',
                text=L[rnd],
                font='Arial',
                units='height',
                pos=(0, 0),
                height=0.06,
                wrapWidth=None,
                ori=0,
                color='white',
                colorSpace='rgb',
                opacity=1,
                languageStyle='LTR',
                depth=0.0)
            arrows.draw()
            win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                score = score + 1
                good_answer = True
            elif resp != good_ans:
                good_answer = False
            else:
                good_answer = None
            dataFile.write(
                str(i)
                +
                ','
                +
                expInfo['participant']
                +
                ','
                +
                str(L[rnd])
                +
                ','
                +
                str(condition)
                +
                ','
                +
                str(resp)
                +
                ','
                +
                str(good_ans)
                +
                ','
                +
                str(good_answer)
                +
                ','
                +
                'no'
                +
                ','
                +
                str(round(rt, 2))
                +
                ','
                +
                str(round(time.time() - start, 2))
                +
                '\n')
            silence.draw()
            win.flip()
            rnd_time = randint(8, 14)
            core.wait(rnd_time * 10 ** -3)
        end.draw()
        win.flip()
        core.wait(2)
        good_day.draw()
        win.flip()
        core.wait(5)

    def quit_experiment(self):
        exit()

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        resp = event.waitKeys(keyList=['a', 'p'], timeStamped=rt_timer, maxWait=2, clearEvents=True)

        if 'q' in resp[0]:
            self.quit_experiment()
        return resp[0][0], resp[0][1] * 1000  # key and rt in milliseconds


start = time.time()
exp = Flanker(start)
exp.run()