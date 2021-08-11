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
    expName = 'Subliminal Priming Task'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001', 'date': data.getDateStr(), 'expName': expName}
dlg = gui.DlgFromDict(expInfo, title='Subliminal Priming Task', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = expInfo['participant'] + '_' + expInfo['date']
if not os.path.isdir("csv"):
    os.mkdir("csv")
dataFile = open(f"{_thisDir}/csv/{fileName}.csv", 'w')
# dataFile.write('no_trial, id_candidate, digit, SOA, seen, gte_5, correct, practice, reaction_time, time_stamp\n')  # TODO : À remettre si on remet l'entraînement
dataFile.write('no_trial, id_candidate, digit, SOA, seen, gte_5, correct, time_stamp, start_SOA\n')


class SubliminalPrimingTask:
    # create init w/ users data
    def __init__(self):
        self.yes_key_code = "o"  # TODO: Temporaire, à modifier quand on passera sur le pad
        self.no_key_code = "n"  # TODO: Pareil
        self.keys = [self.yes_key_code, self.no_key_code, "q"]
        self.yes_key_name = "bleu"  # TODO: Voir si c'est la bonne couleur
        self.no_key_name = "vert"  # TODO: Pareil
        self.target_time = 0.5  # TODO: Je sais pas combien de temps la croix reste dans l'expérience originale, donc je mets cette variable
        self.times_before_masking = [0.017, 0.033, 0.050, 0.067, 0.083, 0.100, 0.117,
                                     0.133]  # TODO: Je n'ai pas trouvé les valeurs exactes dans l'article de Berkovitch
        self.trials = 150
        self.starting_SOA_index = 0 if randint(0, 1) else len(self.times_before_masking) - 1
        self.win = visual.Window(
            size=[1920, 1080],  # if needed, change the size in corcondance with your monitor
            fullscr=False,
            units="pix",
            screen=0,
            allowStencil=False,
            monitor='testMonitor',
            color='black',
            colorSpace='rgb')

    def create_visual_text(self, text, pos=(0, 0)):
        return visual.TextStim(
            win=self.win,
            text=text,
            font='Arial',
            units='height',
            pos=pos,
            height=0.06,
            wrapWidth=None,
            ori=0,
            color='white',
            colorSpace='rgb',
            opacity=1,
            languageStyle='LTR',
            depth=0.0)

    def run(self):
        positions = [(-0.25, -0.25), (-0.25, 0.25), (0.25, -0.25), (0.25, 0.25)]
        position_masks = [
            [(-0.30, -0.25), (-0.25, -0.20), (-0.20, -0.25), (-0.25, -0.30)],
            [(-0.30, 0.25), (-0.25, 0.20), (-0.20, 0.25), (-0.25, 0.30)],
            [(0.30, -0.25), (0.25, -0.20), (0.20, -0.25), (0.25, -0.30)],
            [(0.30, 0.25), (0.25, 0.20), (0.20, 0.25), (0.25, 0.30)],
        ]
        self.win.winHandle.set_fullscreen(True)
        self.win.flip()
        self.win.mouseVisible = False

        # Here, we create all of the different visuals which will be shown through the previously created window
        bienvenue = self.create_visual_text(text="Bienvenue")
        instr = self.create_visual_text(text='Dans ce mini-jeu, un chiffre apparaîtra durant un cours moment à une '
                                             'position aléatoire, puis, après une durée variable, un masque apparaîtra.'
                                             ' Vous devrez nous indiquer si vous avez vu le chiffre, puis indiquer si '
                                             'il était plus grand ou égal à 5.')
        instr2 = self.create_visual_text(text=f'Pour répondre oui, il faudra appuyer sur la touche '
                                              f'{self.yes_key_name}, et pour répondre non, il '
                                              f'faudra appuyer sur la touche {self.no_key_name}.')
        exemple = self.create_visual_text(text='Commençons par un exemple')
        pret_training = self.create_visual_text(
            text=f'Appuyez sur {self.yes_key_name} lorsque vous vous sentez prêt(e)')
        bonne_chance = self.create_visual_text(text='Bonne chance :)')
        croix = self.create_visual_text(text="+")
        silence = self.create_visual_text(text="")
        tutoriel_end = self.create_visual_text(text="Le tutoriel est désormais terminé")
        pret = self.create_visual_text(text=f'Appuyez sur la touche {self.yes_key_name} pour commencer le mini-jeu')
        pressure = self.create_visual_text(text="Le mini-jeu va maintenant commencer, ne vous inquiétez pas, si vous "
                                                "vous trompez ou si vous n'êtes pas sûr(e) ce n'est pas grave")
        end = self.create_visual_text(text='Le mini-jeu est désormais terminé')
        good_day = self.create_visual_text(text="Merci, et bonne journée :)")

        # Here is the practice, the objective is to make sure the user understands the task
        bienvenue.draw()
        self.win.flip()
        core.wait(2)
        instr.draw()
        self.win.flip()
        core.wait(5)
        instr2.draw()
        self.win.flip()
        core.wait(5)
        # TODO: À décommenter si on met un entraînement
        # exemple.draw()
        # self.win.flip()
        # core.wait(3)
        # pret_training.draw()
        # self.win.flip()
        # while self.get_response() != self.yes_key_code:
        #     pass
        # bonne_chance.draw()
        # self.win.flip()
        # core.wait(2)

        # for i in range(3):
        #     rnd = randint(0, 3)
        #     digit = randint(0, 9)
        #     croix.draw()
        #     self.win.flip()
        #     core.wait(self.target_time)
        #     digit_print = self.create_visual_text(text=digit, pos=positions[rnd])
        #     digit_print.draw()
        #     croix.draw()
        #     self.win.flip()
        #     core.wait(0.017)
        #     croix.draw()
        #     core.wait(self.times_before_masking[self.times_before_masking_last_index])
        #     mask = [self.create_visual_text(text="M" if n_letter % 2 == 0 else "E", pos=position_masks[rnd][n_letter])
        #       for n_letter in range(4)]
        #     for letter in mask:
        #         letter.draw()
        #     croix.draw()
        #     self.win.flip()
        #     core.wait(0.2)
        #     resp, rt = self.get_response()
        #     if resp == self.yes_key_code:
        #         good_answer = True
        #         score = score + 1
        #         congrats = self.create_visual_text(text="Bravo ! \n Vous avez " + str(score) + "/" + str(i + 1))
        #         congrats.draw()
        #         self.win.flip()
        #         core.wait(2)
        #     elif resp != good_ans:
        #         good_answer = False
        #         missed = self.create_visual_text(text="Dommage... \n Vous avez " + str(score) + "/" + str(i + 1))
        #         missed.draw()
        #         self.win.flip()
        #         core.wait(2)
        #     else:
        #         good_answer = None
        #     dataFile.write(
        #         str(i)
        #         +
        #         ','
        #         +
        #         expInfo['participant']
        #         +
        #         ','
        #         +
        #         str(L[rnd])
        #         +
        #         ','
        #         +
        #         str(condition)
        #         +
        #         ','
        #         +
        #         str(resp)
        #         +
        #         ','
        #         +
        #         str(good_ans)
        #         +
        #         ','
        #         +
        #         str(good_answer)
        #         +
        #         ','
        #         +
        #         'yes'
        #         +
        #         ','
        #         +
        #         str(round(rt, 2))
        #         +
        #         ','
        #         +
        #         str(round(time.time() - start, 2))
        #         +
        #         '\n')
        #     silence.draw()
        #     self.win.flip()
        #     rnd_time = randint(8, 14)
        #     core.wait(rnd_time * 10 ** -3)
        # croix.draw()
        # self.win.flip()
        # core.wait(1)
        # results = self.create_visual_text(text="Vous avez obtenu " + str(score) + "/3")
        # results.draw()
        # self.win.flip()
        # core.wait(5)
        # tutoriel_end.draw()
        # self.win.flip()

        # Here, the real test starts
        core.wait(3)
        pret.draw()
        self.win.flip()
        while self.get_response() != self.yes_key_code:
            pass
        pressure.draw()
        self.win.flip()
        core.wait(5)
        bonne_chance.draw()
        self.win.flip()
        core.wait(2)

        soa = self.starting_SOA_index

        for i in range(self.trials):
            rnd = randint(0, 3)
            digit = randint(0, 9)
            digit_gte_5 = digit >= 5
            croix.draw()
            self.win.flip()
            core.wait(self.target_time)
            self.create_visual_text(text=digit, pos=positions[rnd]).draw()
            croix.draw()
            self.win.flip()
            core.wait(0.017)
            croix.draw()
            self.win.flip()
            core.wait(self.times_before_masking[soa])
            [self.create_visual_text(text="M" if n_letter % 2 == 0 else "E", pos=position_masks[rnd][n_letter]).draw()
             for n_letter in range(4)]
            croix.draw()
            self.win.flip()
            core.wait(0.2)
            self.create_visual_text(text="Avez-vous vu le chiffre ?").draw()
            self.win.flip()
            resp = self.get_response()
            good_answer = None
            seen = False
            if resp == self.yes_key_code:
                seen = True
                self.create_visual_text(text="Est-ce que le chiffre est plus grand (ou égal) à 5 ?").draw()
                # TODO: À voir si c'est la bonne condition
                self.win.flip()
                resp = self.get_response()
                if (resp == self.yes_key_code and digit_gte_5) or (resp == self.no_key_code and not digit_gte_5):
                    good_answer = True
                else:
                    good_answer = False
            dataFile.write(f"{i}, {expInfo['participant']}, {digit}, {self.times_before_masking[soa]}, "
                           f"{seen}, {digit_gte_5}, {good_answer}, {time.time()}, "
                           f"{self.times_before_masking[self.starting_SOA_index]}\n")
            if good_answer and soa != 0:
                soa -= 1
            elif not good_answer and soa != len(self.times_before_masking) - 1:
                soa += 1
            silence.draw()
            self.win.flip()
            rnd_time = randint(8, 14)
            core.wait(rnd_time * 10 ** -3)
        end.draw()
        self.win.flip()
        core.wait(2)
        good_day.draw()
        self.win.flip()
        core.wait(5)

    @staticmethod
    def quit_experiment():
        exit()

    def get_response(self, keys=None):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        if keys is None:
            keys = self.keys
        resp = event.waitKeys(keyList=keys, clearEvents=True)
        if resp[0] == "q":
            self.quit_experiment()
        return resp[0]


exp = SubliminalPrimingTask()
exp.run()
