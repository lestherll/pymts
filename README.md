# PyMTS
MTS utility script for converting `.MTS` files to various formats using [ffmpeg](https://www.ffmpeg.org)

### Context
I could not figure out a *normal* way to bulk export MTS files from my camcorder so I wrote this script for it.
It can also utilise multiple CPU cores to run multiple ffmpeg processes in parallel, reducing wait times.


## Requirements
- [ffmpeg](https://www.ffmpeg.org)
- Tested only on Python 3.11

## Installation


## Usage
Pass your AVCHD folder OR a folder with .MTS files
```bash
# TODO
python -m pymts <your-AVCHD-folder OR any folder with .MTS files> --output <output-folder>
```




## Features
- Convert `.MTS` files into desired format (anything `ffmpeg` supports) in parallel
- TODO: Check for previously converted files, and skip conversion when needed to prevent reconversion
    - This prevents you from doing various hacks such as deleting all your videos and then running the script
- Configurable input and output directory