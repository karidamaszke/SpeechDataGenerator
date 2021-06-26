import math
import struct
import time
import contextlib
from typing import List

import pyaudio
from pydub import AudioSegment


class AudioRecorder:
    __CHANNELS = 1
    __TIMEOUT_LENGTH = 2
    __SAMPLE_WIDTH = 2
    __SHORT_NORMALIZE = (1.0 / 32768.0)
    __THRESHOLD = 30
    __CHUNK_SIZE = 1024
    __SAMPLE_RATE = 16000

    def __init__(self) -> None:
        self.__p = pyaudio.PyAudio()
        self.__stream: pyaudio.Stream = None

    def record(self, file_name: str) -> None:
        samples = []
        with self.__recording():
            current = time.time()
            end = time.time() + self.__TIMEOUT_LENGTH
            while current <= end:
                data = self.__stream.read(self.__CHUNK_SIZE)
                if self.__rms(data) >= self.__THRESHOLD:
                    end = time.time() + self.__TIMEOUT_LENGTH
                current = time.time()
                samples.append(data)
        self.__save(samples, file_name)

    def __save(self, samples: List[bytes], file_name: str) -> None:
        AudioSegment(
            data=b''.join(samples),
            sample_width=self.__SAMPLE_WIDTH,
            frame_rate=self.__SAMPLE_RATE,
            channels=self.__CHANNELS
        ).export(file_name, format='wav')

    def __rms(self, frame: bytes) -> float:
        count = len(frame) / 2
        shorts = struct.unpack("%dh" % count, frame)
        sum_squares = sum([(sample * self.__SHORT_NORMALIZE) ** 2 for sample in shorts])
        rms = math.pow(sum_squares / count, 0.5)
        return rms * 1000

    @contextlib.contextmanager
    def __recording(self) -> None:
        print('Listening start...')
        self.__stream = self.__p.open(format=pyaudio.paInt16,
                                      channels=self.__CHANNELS,
                                      rate=self.__SAMPLE_RATE,
                                      input=True,
                                      output=True,
                                      frames_per_buffer=self.__CHUNK_SIZE)
        yield
        self.__stream.close()
        print("Listening stop...")
