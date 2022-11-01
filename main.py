from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(
    "osnova",
    api_id=2040,
    api_hash="b18441a1ff607e10a989891a5462e627"
)

def spaces(len_of):
    return " " * (len_of - 2) * 2 + " "


def str_spaces(text):
    return text.replace("", " ")[1:-1]


def get_swas(x):
    a = open("swas.txt", "w")
    len_x = len(x)
    r_x = x[::-1]
    for y in range(len_x):
        if y == 0:
            a.write(r_x[0] + spaces(len_x) + str_spaces(x) + "\n")
            continue
        elif y == len_x - 1:
            a.write(str_spaces(x) + " " + str_spaces(r_x[1:]) + "\n")
            continue
        a.write(r_x[y] + spaces(len_x) + x[y] + "\n")
    for y in range(len_x):
        if y == len_x - 2:
            a.write(str_spaces(r_x) + spaces(len_x) + x[y + 1] + "\n")
            break
        a.write(spaces(len_x) + " " + r_x[1:][y] + spaces(len_x) + x[1:][y] + "\n")
    a.close()
    return open("swas.txt", "r").read()


@app.on_message(filters.command("swas"))
def make_swas(_,m:Message):
    swas = get_swas(" ".join(m.command[1:]))
    m.reply(f"```{swas}```")


@app.on_message(filters.command("swas", ".") & filters.me)
def make_swas(_,m:Message):
    swas = get_swas(" ".join(m.command[1:]))
    m.edit(f"```{swas}```")

app.run()