import subprocess
import sys

scripts = [
    "clean_data.py",
    "rfm_analysis.py",
    "visualize.py"
]

for script in scripts:
    print(f"\n--- Running {script} ---")
    result = subprocess.run([sys.executable, f"scripts/{script}"], capture_output=False)
    if result.returncode != 0:
        print(f"Error while running {script}. Stopping.")
        break
else:
    print("\n✅ All steps completed successfully.")