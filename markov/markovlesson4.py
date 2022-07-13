import markovify
import pandas
import re


# 受け取ったdataを成形して文字列に代入する関数
def data_for_text(data):
    text = ""

    for w in data:
        # 全角カッコ、各種記号
        w = re.sub(r"[（）「」『』｛｝【】＠"'！？｜～・]", "", w)
        # 半角カッコ、各種記号
        w = re.sub(r"[()\[\]{}@\'\"!?|~-]", "", w)
        # 全角空白
        w = re.sub(r"\u3000", "", w)
        # 半角空白
        w = re.sub(r" ", "", w)
        # 元々ある改行コード
        w = re.sub(r"\n", "", w)

        # 句点の後に改行コードを追加
        w = re.sub(r"。", "。\n", w)

        # 単語を区切るための空白を追加
        text += " "
        text += w

    return text


# markovifyを用いて学習を実行する関数
def markoving(text):
    # NewLineTextは改行されたところまでを一つの文章と判断する。日本語の文章にはTextよりもこちらの方が向いている
    # state_sizeで連結する単語の数を指定できる。多いほど元の文章に近くなるが、多すぎると文章がうまく生成されなくなる
    text_model = markovify.NewlineText(text, state_size=3)
    try:
        with open("model/model_test.json") as f:
            current_model = markovify.NewlineText.from_json(f.read())
            models = [text_model, current_model]
            # 既存のモデルと学習したモデルを合体。第2引数でモデルの比重を設定可能
            text_model = markovify.combine(models)
    except FileNotFoundError:
        pass

    for i in range(1, 6):
        # make_short_sentenceは短い文章を生成する。第1引数で最大長、triesで最大試行回数を指定できる
        print("Line", i, ":",
              re.sub(" ", "", text_model.make_short_sentence(100, tries=100)))
    # make_sentence_with_startで指定した単語から文章を始めることもできる
    # print(モデル名.make_sentence_with_start(beginning="単語"))

    with open("model/model_test.json", "w") as f:
        f.write(text_model.to_json())

    # 学習データの保存
    # with open("ファイル名.json", "w") as f:
    #     f.write(モデル名.to_json())

    # 学習データの読み込み
    # with open("ファイル名.json") as f:
    #     モデル名 = markovify.NewlineText.from_json(f.read())


# 学習はせず、既存のモデルから文章を生成するだけの関数
def test_markoving():
    try:
        with open("model/model_test.json") as f:
            text_model = markovify.NewlineText.from_json(f.read())

        for i in range(1, 6):
            print("Line", i, ":",
                  re.sub(" ", "", text_model.make_short_sentence(100, tries=100)))

    except FileNotFoundError:
        print("既存のモデルはありませんでした。")


while True:
    try:
        name = input("\n読み込むcsvファイル名(endで終了): ")
        if name == "end":
            print("終了します")
            break

        data = pandas.read_csv(name)
        text = data_for_text(data.iloc[:, 3])
        markoving(text)
    except FileNotFoundError:
        print("ファイルが見つかりませんでした。既存のモデルから文章を生成します。\n ")
        test_markoving()
