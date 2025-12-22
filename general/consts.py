TURNGPT_PREPARE_THRESHOLD = 0.2
ASR_PREPARE_TIMEOUT = 200
SIMILARITY_PREPARE_THRESHOLD = 0.8

VAP_PNOW_INTERRUPT_THRESHOLD = 0.4
VAP_PFUT_YIELD_THRESHOLD = 0.4

MIN_GAP_TIME = 500


TURNGPT_YIELD_TIMEOUTS = [
    {"threshold": 0.3, "timeout": 500},
    {"threshold": 0.2, "timeout": 1000},
    {"threshold": 0.1, "timeout": 2000},
    {"threshold": 0.0, "timeout": 3000},
]
