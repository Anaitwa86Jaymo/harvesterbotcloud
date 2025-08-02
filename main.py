from modules.high_risk_strategy import run_strategy
from modules.mangadao_strategy import run_mangadao
from modules.ai_frames_strategy import run_ai_frames

if __name__ == "__main__":
    print("Running HarvesterBot Cloud Strategy Suite...")
    run_strategy()
    run_mangadao()
    run_ai_frames()