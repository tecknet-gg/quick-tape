import subprocess
import sys

from watchfiles import run_process

def main():
    try:
        run_process(
            ".",
            target=run_app,
            watch_filter=None
        )
    except KeyboardInterrupt:
        print("Exiting...")

def run_app():
    subprocess.run([sys.executable, "src/quick_tape/__main__.py"], check=False)



if __name__ == "__main__":
    main()