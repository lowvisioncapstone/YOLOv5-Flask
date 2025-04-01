import sys
print("Python executable:", sys.executable)

import subprocess
result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
print(result.stdout)