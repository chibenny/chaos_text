import random
import string


def make_chaos(message_in: list[str]) -> list[str]:
    message_out: list[str] = []
    for char in message_in:
        result = random.random()
        if result < 0.03:
            char = random.choice(string.printable.strip())
        elif result < 0.06:
            char = random.choice(string.punctuation.strip())
        elif result < 0.09:
            char = random.choice("😀🦄🤖🔥🐙🚀🎉😎🤡👾🐍")
        elif result < 0.13:
            continue
        message_out.append(char)
    return message_out


def make_rage(
    rage_input: str,
    extra_rage: str,
    chaos_mode: bool = False,
) -> str:
    message: list[str] = []
    caps_first: bool = random.random() >= 0.3

    for i, char in enumerate(rage_input):
        if i == 0:
            char = char.upper() if caps_first else char.lower()
        elif not char.isalnum():
            message.append(char)
            continue
        else:
            last_char = next((c for c in reversed(message) if c.isalnum()), "")
            char = char.upper() if last_char.islower() else char.lower()
        message.append(char)

    if extra_rage:
        reordered = []
        for i, _ in enumerate(message):
            flip = message[i].upper() if random.randint(0, 1) else message[i].lower()
            reordered.append(flip)
        message = reordered

    if chaos_mode:
        message = make_chaos(message)

    return "".join(message)
