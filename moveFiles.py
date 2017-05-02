
import os
import glob
import shutil

def main():

    for root, dirs, files in os.walk("ENC_ROOT/"):
        for file in files:
          if file.endswith(".000"):
              src = os.path.join(root, file)
              print(os.path.join(root, file))
              shutil.copy(src, "merged/"+file)

if __name__ == '__main__': main()
