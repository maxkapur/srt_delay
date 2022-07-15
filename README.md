# srt_delay.py

… is a small Python 3 script that you can use to **advance** or **delay** the timings
of a subtitle file in the `.srt` [file format](https://en.wikipedia.org/wiki/SubRip).

## How it works 

We will demonstrate `srt_delay.py` using the subtitles for the open-source movie
[*Elephants Dream*](https://en.wikipedia.org/wiki/Elephants_Dream). The file can 
be downloaded from this repo (`sample_input.srt`) or from
[Wikimedia Commons](https://commons.wikimedia.org/wiki/TimedText:Elephants_Dream.ogv.en.srt).

Here is what the input file looks like: 

```bash
$ head sample_input.srt
1
00:00:15,000 --> 00:00:17,951
At the left we can see...

2
00:00:18,166 --> 00:00:20,083
At the right we can see the...

3
00:00:20,119 --> 00:00:21,962
```

Each line contains either an index number for the subtitle (`1`), the subtitle’s
timing (`00:00:18,166 --> 00:00:20,083`), or the subtitle text itself.

### Delaying subtitles

Suppose we want to **delay** the subtitles by 1 hour and 5 minutes.
We can pass this interval in `.srt` timestamp format (`01:05:00,000`)
to `srt_delay` with the `-d` or `--delay` flag:

```bash
$ python3 srt_delay.py sample_input.srt -d 01:05:00,000 | head
1
01:05:15,000 --> 01:05:17,951
At the left we can see...

2
01:05:18,166 --> 01:05:20,083
At the right we can see the...

3
01:05:20,119 --> 01:05:21,962
```

### Advancing subtitles

Suppose we want to **advance** the subtitles by 1.5 seconds. We can pass
this interval in `.srt` timestamp format (`00:00:01,500`) to `srt_delay.py`
with the `-a` or `--advance` flag:

```bash
$ python3 srt_delay.py sample_input.srt -a 00:00:01,500 | head
1
00:00:13,500 --> 00:00:16,451
At the left we can see...

2
00:00:16,666 --> 00:00:18,583
At the right we can see the...

3
00:00:18,619 --> 00:00:20,462
```

### Typical usage

By default, `srt_delay.py` prints to standard output. In most cases,
you will want to save the output to another file:

```bash
$ python3 srt_delay.py sample_input.srt -a 00:00:01,500 > sample_input_advanced_by_1.5s.srt
```

### Bugs

If you find one, submit a PR or email me at [maxkapur@gmail.com](mailto:maxkapur@gmail.com).
