import argparse
import time
from datetime import datetime

from turngpt import TurnGPT
from vap.model import (
    VapGPT,  # https://github.com/ErikEkstedt/VoiceActivityProjection/blob/main/vap/model.py#L125
)

from general.asr import ASR
from general.consts import *
from general.dialogState import DialogState


def format_time(current_time):
    return datetime.fromtimestamp(current_time).strftime("%H:%M:%S.%f")[:-3]


def main(inp):
    audio_filepath = inp.filepath

    user_speak_end_time = time.time()
    user_turn_end_time = time.time()
    last_asr_time = time.time()
    asr_result = None
    last_sent_asr_result = None
    turngpt_output = 0

    asr = ASR(audio_filepath)
    vap = VapGPT()
    turngpt = TurnGPT()

    """
    dialog_manager will take the place of DialogState object within the PsuedoCode. We need the following functions:
        1. updateUser
        2. getHistory

    Furthermore, we need to check how TurnGPT would take this in (DialogState.getHistory()).
    """
    dialog_state = DialogState()

    print("Beginning to listen...")
    while True:
        current_time = time.time()

        # Check if the ASR has updated it output
        if asr.has_new_result():
            asr_result = asr.get_result()
            # What is the DialogState class?
            # We let the dialog state be dialog_manager
            # DialogState.updateUser(asr_result)
            #   turngpt_output = TurnGPT.eval(DialogState.getHistory())
            #   last_asr_time = current_time
            #   last_asr_time = current_time

        # What does the get_current method do?
        # vap_output = vap.get_current()

        time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="General Turn-Taking Program")
    parser.add_argument(
        "filepath",
        help="The path of the file where the audio is being appended.",
    )
    args = parser.parse_args()
    main(args)
