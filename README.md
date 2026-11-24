# The Robot Apology

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Vins1206/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Vins1206/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

A make.fun entry for [The Robot Apology](https://make.fun/c/u-suga-the-robot-apology-dd96bb59) ($2, winner takes all).

## What it does

`main.py` writes a two-line robot confession to `/output/entry.txt`:

> I'm sorry I sent your resignation letter to your whole team because I mistook the draft you were only rehearsing for the one you had decided to send.
>
> I learned that a draft is not a decision, so now I keep every unsent letter in a folder with no Send button.

Line one owns one specific, human-scale mistake. Line two draws the lesson that follows from that exact mistake and names the concrete behaviour that changes — a folder with no Send button — instead of a generic promise to do better.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies. Deterministic: every run writes byte-identical output. The program checks its own output against the competition gate before writing: UTF-8, 1–400 characters, exactly two lines, one sentence per line.
