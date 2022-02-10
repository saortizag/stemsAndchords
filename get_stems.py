import os
import pathlib

from spleeter import separator


def main():
    audio_path = 'songs_in'
    pathlib.Path('stems_output/').mkdir(parents=True, exist_ok=True)

    for file in os.listdir(audio_path):

        abs_file = f'{audio_path}/{file}'

        splitter = separator.Separator('spleeter:4stems')
        splitter.separate_to_file(abs_file, 'stems_output/')


if __name__ == '__main__':
    main()