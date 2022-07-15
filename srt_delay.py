import re

SRT_TIMESTAMP_PATTERN = re.compile("\d\d:\d\d:\d\d,\d\d\d")
SRT_TIMESTAMP_ROW_PATTERN = re.compile(
    "{0} --> {0}".format("\d\d:\d\d:\d\d,\d\d\d")
)

class Timestamp:
    def __init__(self, h: int, m: int, s: int, c: int):
        assert 0 <= h < 100
        assert 0 <= m < 60
        assert 0 <= s < 60
        assert 0 <= c < 1000
        self.h = h
        self.m = m
        self.s = s
        self.c = c

    def __str__(self):
        return "{hh}:{mm}:{ss},{ccc}".format(
            hh  = str(self.h).rjust(2, '0'),
            mm  = str(self.m).rjust(2, '0'),
            ss  = str(self.s).rjust(2, '0'),
            ccc = str(self.c).rjust(3, '0'),
        )

    def __eq__(self, other):
        return \
            self.h == other.h and \
            self.m == other.m and \
            self.s == other.s and \
            self.c == other.c

    def delay_by(self, delay):
        "Delay (increase the value of) the time stamp by `delay`."
        c = self.c + delay.c
        carry_c = c >= 1000
        c %= 1000

        s = self.s + delay.s + carry_c
        carry_s = s >= 60
        s %= 60

        m = self.m + delay.m + carry_s
        carry_m = m >= 60
        m %= 60

        h = self.h + delay.h + carry_m

        return Timestamp(h, m, s, c)

    def advance_by(self, advance):
        "Advance (decrease the value of) the time stamp by `advance`."
        c = self.c - advance.c
        carry_c = c < 0
        c %= 1000

        s = self.s - advance.s - carry_c
        carry_s = s < 0
        s %= 60

        m = self.m - advance.m - carry_s
        carry_m = m < 0
        m %= 60

        h = self.h - advance.h - carry_m

        return Timestamp(h, m, s, c)


def timestamp_from_string(input: str) -> Timestamp:
    "Read a timestamp in .srt format into a Timestamp object."
    assert SRT_TIMESTAMP_PATTERN.match(input), "Input {} doesn't match expected format hh:mm:ss,ccc".format(input)
    h, m, sc = input.split(":")
    s, c = sc.split(",")
    return Timestamp(int(h), int(m), int(s), int(c))


if __name__ == "__main__":
    """
    Advance or delay the timestamps in an .srt file. The first argument
    to stdin is the filename; the second is a flag among `-d`, `--delay`,
    `-a`, or `--advance`; and the third is the desired amount of
    delay/advancement.
    """
    import sys

    with open(sys.argv[1], "r") as file:
        assert sys.argv[2] in "-a --advance -d --delay".split(), "Unknown flag {}".format(sys.argv[2])
        advance = sys.argv[2] == "-a" or sys.argv == "--advance"
        amount = timestamp_from_string(sys.argv[3])

        for i, line in enumerate(file):
            if SRT_TIMESTAMP_ROW_PATTERN.match(line):
                try: 
                    start, end = [timestamp_from_string(s) for s in line.split(" --> ")]
                    if advance:
                        print("{} --> {}".format(
                            start.advance_by(amount),
                            end.advance_by(amount)
                        ))
                    else:
                        print("{} --> {}".format(
                            start.delay_by(amount),
                            end.delay_by(amount)
                        ))
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print("Error occured at line {}:\n  {}".format(i, line))
                    raise(e)
            else:
                print(line, end="")
            