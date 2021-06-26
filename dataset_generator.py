import os
import csv
import glob
import contextlib

from audio_recorder import AudioRecorder
from command_generator import CommandGenerator


class DatasetGenerator:
    __DATA_DIR = 'data'
    __CSV_FILE = os.path.join(__DATA_DIR, 'all_records.csv')

    def __init__(self) -> None:
        self.__command_generator = CommandGenerator()
        self.__audio_recorder = AudioRecorder()
        self.__counter = len(glob.glob1(self.__DATA_DIR, "*.wav"))

        self.__create_csv()

    def __call__(self) -> None:       
        file_name = os.path.join(self.__DATA_DIR, self.__get_file_name())
        command = self.__command_generator()

        with self.__command_context():
            print(f'Command: {command}')
            self.__audio_recorder.record(file_name)
            self.__append_to_csv(
                self.__get_file_name(),
                os.path.getsize(file_name),
                command
            )
            self.__counter += 1


    def __create_csv(self) -> None:
        if not os.path.exists(self.__CSV_FILE):
            with open(self.__CSV_FILE, 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['wav_filename', 'wav_filesize', 'transcript'])
    
    def __get_file_name(self) -> str:
        return str(self.__counter).zfill(5) + '.wav'
    
    def __append_to_csv(self, file_name: str, file_size: int, command: str) -> None:
        with open(self.__CSV_FILE, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([file_name, str(file_size), command])

    @contextlib.contextmanager
    def __command_context(self) -> None:
        self.__print_double()
        yield
        self.__print_double()

    @staticmethod
    def __print_double() -> None:
        print(50 * '=')
