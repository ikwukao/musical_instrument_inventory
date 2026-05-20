class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type


instrument_1 = MusicalInstrument("Oboe", "woodwind")
instrument_2 = MusicalInstrument("Trumpet", "brass")


print(instrument_1.name)
print(instrument_1.instrument_type)

print(instrument_2.name)
print(instrument_2.instrument_type)