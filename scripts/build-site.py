"""Build the public bundle. Never deploys or changes domains."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent.parent
subprocess.run([sys.executable,str(root/'scripts/generate-current.py')],cwd=root,check=True)
subprocess.run(['node','--check','main.js'],cwd=root,check=True)
subprocess.run(['node','scripts/prepare-site.mjs'],cwd=root,check=True)
