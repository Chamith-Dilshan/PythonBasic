class MusicalInstrument:
    # The self-parameter is a standard way to refer to the instance of the class
    # and is required as the first parameter for all instance methods in a class.
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


def main():
    instrument_1 = MusicalInstrument('Oboe', 'woodwind')
    instrument_2 = MusicalInstrument('Trumpet', 'brass')

    instrument_1.play()
    print(instrument_1.get_fact())

    instrument_2.play()
    print(instrument_2.get_fact())

if __name__ == "__main__":
    main()