"""
Features:
- Convert `mts` files into desired format
- Check for previously converted files, and skip conversion when needed to prevent reconversion
    - This prevents you from doing various hacks such as deleting all your videos and then running the script
- Configurable input and output directory
"""
import subprocess

import constants


def get_mts_filepaths(avchd_path, strip_extension=False):
    files = avchd_path.glob("*.MTS")
    if strip_extension:
        return [f.with_suffix("") for f in files]
    else:
        return [f for f in files]


def run_ffmpeg(*args):
    args = ["ffmpeg"] + list(args)
    return subprocess.run(args=args)


def convert_mts(input_file, output_file=None, target_type="mov"):
    if output_file is None:
        output_file = (
            constants.DEFAULT_OUTPUT_DIRECTORY
            / input_file.with_suffix(f".{target_type}").name
        )

    return run_ffmpeg("-i", input_file, "-f", target_type, output_file)
