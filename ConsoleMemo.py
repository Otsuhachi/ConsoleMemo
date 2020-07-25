import sys
from pathlib import Path
DEFAULT_NAME = 'Memo'
SUFFIX = '.txt'
ADD = ';a;'
CANSEL = ';c;'
DELETE = ';d;'
HELP = ';h;'
NAME = ';n;'
SHOW = ';s;'
lines = []
name = ''
HELP_STR = [
    'メモを生成します。', f'行末に"{NAME}"を追加することで、その行の入力内容をファイル名にできます。', '同じファイルが既に存在する場合、確認を行わずに上書きしてしまうので注意してください。', f'行末に"{ADD}"を入力することで、続けて行を追加することができます。',
    f'"{DELETE}"を入力することで直前の行を削除できます。', f'"{CANSEL}"を入力することで、入力内容をすべて破棄して、終了します。', f'"{SHOW}"を入力することで出力内容を確認することができます。',
    f'"{HELP}"を入力することでこの説明は何度でも見ることができます。', f'"{CANSEL}"が入力されるか、行末に"{ADD}"が無い、メモ行を追加することでこのアプリを終了します。'
]


def show_help():
    print('\n'.join(HELP_STR))


def get_text(name):
    if not name:
        name = DEFAULT_NAME
    return name.strip() + SUFFIX, '\n'.join(lines)


show_help()
while 1:
    line = input('> ').strip()
    if not line:
        continue
    end = line[-3:]
    if end == NAME:
        name = line[:-3]
    elif end == HELP:
        show_help()
    elif end == DELETE:
        if lines:
            print(f'"{lines.pop()}"を削除しました。')
    elif end == SHOW:
        tn, tt = get_text(name)
        print(f'以下の文が({tn})に出力されます。\n{tt}')
    elif end == CANSEL:
        print('メモの生成を中止します。')
        sys.exit()
    elif end == ADD:
        lines.append(line[:-3])
    else:
        lines.append(line)
        break
name, text = get_text(name)
with open(Path(name), 'w', encoding='utf-8') as f:
    f.write(text)
