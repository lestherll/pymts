from concurrent.futures import ProcessPoolExecutor

from avchd_util import convert_mts, get_mts_filepaths
from constants import DEFAULT_INPUT_DIRECTORY, DEFAULT_OUTPUT_DIRECTORY

if __name__ == "__main__":
    mts_filepaths = get_mts_filepaths(DEFAULT_INPUT_DIRECTORY)
    DEFAULT_OUTPUT_DIRECTORY.mkdir(exist_ok=True)

    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(convert_mts, f, "out/" + f.with_suffix(".mov").name)
            for f in mts_filepaths
        ]

    for future in futures:
        future.result()
