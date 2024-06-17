from concurrent.futures import ProcessPoolExecutor

from constants import DEFAULT_INPUT_DIRECTORY, DEFAULT_OUTPUT_DIRECTORY
from avchd_util import convert_mts, get_mts_filepaths

if __name__ == "__main__":
    mts_filepaths = get_mts_filepaths(DEFAULT_INPUT_DIRECTORY)
    DEFAULT_OUTPUT_DIRECTORY.mkdir(exist_ok=True)

    executor = ProcessPoolExecutor()

    for f in mts_filepaths:
        future = executor.submit(convert_mts, f, "out/" + f.with_suffix(".mov").name)

        if future.result().returncode != 0:
            raise EnvironmentError("error converting")
