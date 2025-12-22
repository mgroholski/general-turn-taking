import argparse
import time

from vap.model import VapGPT

from general.asr import ASR
from general.consts import *


def main(inp):
    audio_filepath = inp.filepath

    user_speak_end_time = time.time()
    user_turn_end_time = time.time()
    last_asr_time = time.time()
    asr_result = None
    last_sent_asr_result = None
    turngpt_output = 0

    ASR = ASR(audio_filepath)
    VAP = VapGPT()

    while True:
        current_time = time.time()
        # vap_output = VAP.get_current()
        #
        # Check if the ASR has updated it output
        if ASR.has_new_result():
            #   asr_result = ASR.get_result()
            #   DialogState.updateUser(asr_result)
            #   turngpt_output = TurnGPT.eval(DialogState.getHistory())
            #   last_asr_time = current_time
            #   last_asr_time = current_time
            print(ASR.get_new_result())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="General Turn-Taking Program")
    parser.add_argument(
        "filepath",
        help="The path of the file where the audio is being appended.",
        required=True,
    )
    args = parser.parse_args()
    main(args)
