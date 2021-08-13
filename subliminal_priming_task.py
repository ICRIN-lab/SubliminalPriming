import time
import os
from random import randint
from task_template import TaskTemplate
from psychopy import core


class SubliminalPrimingTask(TaskTemplate):
    bg = "white"
    text_color = "black"
    trials = 150
    yes_key_name = "bleue"  # TODO: À voir si c'est la bonne couleur
    no_key_name = "verte"  # TODO: Pareil
    yes_key_code = "o"  # TODO: À changer quand on passera au pad
    no_key_code = "n"  # TODO: Pareil
    quit_code = "q"  # TODO: À voir si on le garde
    keys = [yes_key_code, no_key_code, quit_code]
    instructions = [
        "Dans ce mini-jeu, un chiffre apparaîtra durant un cours moment à une position aléatoire, puis, "
        "après une durée variable, un masque apparaîtra. Vous devrez nous indiquer si vous avez vu le "
        "chiffre, puis indiquer si il était supérieur ou égal à 5.",
        f"Pour répondre oui, il faudra appuyer sur la touche {yes_key_name}, et pour répondre non, il "
        f"faudra appuyer sur la touche {no_key_name}."
    ]
    csv_headers = ['no_trial', 'id_candidate', 'digit', 'SOA', 'seen', 'gte_5', 'correct', 'time_from_start',
                   'start_SOA'
                   ]
    times_before_masking = [0.017, 0.033, 0.05, 0.067, 0.083, 0.1, 0.117, 0.133]  # TODO: À voir si ce sont les bonnes valeurs
    target_time = 0.5

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp):
        if no_trial == 0:
            if randint(0, 1):
                self.soa = self.starting_SOA_index = len(self.times_before_masking) - 1
            else:
                self.soa = self.starting_SOA_index = 0
        positions = [(-0.25, -0.25), (-0.25, 0.25), (0.25, -0.25), (0.25, 0.25)]
        position_masks = [
            [(-0.30, -0.25), (-0.25, -0.20), (-0.20, -0.25), (-0.25, -0.30)],
            [(-0.30, 0.25), (-0.25, 0.20), (-0.20, 0.25), (-0.25, 0.30)],
            [(0.30, -0.25), (0.25, -0.20), (0.20, -0.25), (0.25, -0.30)],
            [(0.30, 0.25), (0.25, 0.20), (0.20, 0.25), (0.25, 0.30)],
        ]
        croix = self.create_visual_text("+")
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
        core.wait(self.times_before_masking[self.soa])
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
        self.update_csv(no_trial, self.participant, digit, self.times_before_masking[self.soa], seen, digit_gte_5,
                        good_answer, time.time() - exp_start_timestamp,
                        self.times_before_masking[self.starting_SOA_index])
        if good_answer and self.soa != 0:
            self.soa -= 1
        elif not good_answer and self.soa != len(self.times_before_masking) - 1:
            self.soa += 1
        self.create_visual_text("").draw()
        self.win.flip()
        rnd_time = randint(8, 14)
        core.wait(rnd_time * 10 ** -3)


if not os.path.isdir("csv"):
    os.mkdir("csv")
exp = SubliminalPrimingTask("csv/")
exp.start()
