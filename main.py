# Entry point for Harvester Bot
from modules.high_risk_strategy import run_strategy
from modules.mangadao import run_mangadao
from modules.ai_frames import run_ai_frames

if __name__ == '__main__':
    run_strategy()
    run_mangadao()
    run_ai_frames()
