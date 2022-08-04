from koreanParser import *
import datagen
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



def cmd(input: str):
    commands = parseCmd(input)
    match commands[0]:
        case '?':
            return "{아이템 이름} {가격} : 새로운 아이템과  가격 등록. 아이템 이름에 뛰어쓰기 X\n초기화 {서버이름} {캐릭터이름} : 새로운 데이터 세트 생성"
        case '초기화':
            datagen.initdata(commands[1], commands[2])
        case '보기':
            df = datagen.getData()
            if len(commands) == 1:
                return df
            else:
                return df.loc[df['itemname'] == commands[1]]
        case '그래프':
            df = view(commands[1])
            plt.plot(df['date'] ,df['price'])
            plt.gcf().autofmt_xdate()
            plt.show()
            return df

        case _:
            datagen.addEntry(commands[0], parseNum(commands[1]))


def view(itemname):
    df = datagen.getData()
    return df.loc[df['itemname'] == itemname]
