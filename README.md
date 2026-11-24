# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Krwanz/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Krwanz/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

A make.fun entry for the [Fortune Cookie Wisdom for Developers bounty](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44): one original fortune-cookie line for a software developer, 120 characters or fewer. A judge model playing a tired senior engineer picks the line that makes it smile and nod.

## The fortune

> A bug found in review is a gift; a bug found in production is the same gift, unwrapped by strangers.

100 characters. It is true about a developer's day — review catches bugs gently, production catches them in front of strangers — and the second half turns the first: the same gift, unwrapped by the wrong audience. The line also carries a quiet double meaning: the "gift" is the bug itself, and who unwraps it decides whether it feels like luck or embarrassment.

## How it works

`main.py` (standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), checks it is a single line of 1–120 characters, and reads it back to confirm the exact bytes.

```sh
python3 main.py
```

Referral: [a15ed58m](https://make.fun?ref=a15ed58m)
