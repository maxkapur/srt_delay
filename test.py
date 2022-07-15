import srt_delay


def assert_a_plus_b_equals_c(a, b, c):
    assert a.delay_by(b) == b.delay_by(a) == c
    assert c.advance_by(b) == a
    assert c.advance_by(a) == b


if __name__ == "__main__":
    # Simple example
    ts = [
        srt_delay.timestamp_from_string("00:00:14,526"),
        srt_delay.timestamp_from_string("00:45:00,001"),
        srt_delay.timestamp_from_string("00:45:14,527")
    ]

    assert_a_plus_b_equals_c(*ts)

    # Example with a lot of carried digits
    ts = [
        srt_delay.timestamp_from_string("01:01:56,500"),
        srt_delay.timestamp_from_string("12:59:14,566"),
        srt_delay.timestamp_from_string("14:01:11,066")
    ]

    assert_a_plus_b_equals_c(*ts)

    print("All tests passed.")