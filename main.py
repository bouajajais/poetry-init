import subprocess
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "it":
        # Run "poetry init" to create a new pyproject.toml file with prompts
        subprocess.run(["poetry", "init"])
    else:
        # Run "poetry init --no-interaction" to create a new pyproject.toml file without any prompts
        subprocess.run(["poetry", "init", "--no-interaction"])
    
if __name__ == "__main__":
    main()