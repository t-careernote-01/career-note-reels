#!/usr/bin/env python3
"""書き込み用スプレッドシート（Excel / Googleスプレッドシートで開ける）を作る。
使い方: python3 build_xlsx.py <出力.xlsx>"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

NAVY, TERRA, BG, INPUT = "27364B", "C96F4A", "F6F3EE", "FFFDF5"
thin = Side(style="thin", color="CFC6B8")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
F = "Noto Sans JP"

wb = Workbook()
wb.remove(wb.active)

def sheet(name, title, lead):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 34
    ws.column_dimensions["C"].width = 58
    ws.column_dimensions["D"].width = 46
    ws["B1"] = title; ws["B1"].font = Font(name=F, size=15, bold=True, color=NAVY)
    ws["B2"] = lead; ws["B2"].font = Font(name=F, size=10, color="555555")
    ws["B2"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells("B2:D2"); ws.row_dimensions[2].height = 34
    ws._r = 4
    return ws

def header(ws, text, star=False):
    r = ws._r + 1
    ws.cell(r, 2, ("★ " if star else "") + text).font = Font(name=F, size=11.5, bold=True, color=TERRA if star else NAVY)
    ws._r = r + 1

def cols(ws, a, b, c="記入例（架空の人）"):
    r = ws._r
    for i, t in enumerate([a, b, c]):
        cell = ws.cell(r, 2 + i, t)
        cell.font = Font(name=F, size=9.5, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=NAVY); cell.border = BOX
    ws._r = r + 1

def row(ws, q, example="", h=36, answer_ref=None):
    r = ws._r
    c1 = ws.cell(r, 2, q); c1.font = Font(name=F, size=10); c1.fill = PatternFill("solid", fgColor=BG)
    c2 = ws.cell(r, 3, ""); c2.fill = PatternFill("solid", fgColor=INPUT)
    c3 = ws.cell(r, 4, example); c3.font = Font(name=F, size=9, color="777777")
    for c in (c1, c2, c3):
        c.border = BOX; c.alignment = Alignment(wrap_text=True, vertical="top")
    c2.font = Font(name=F, size=10.5)
    ws.row_dimensions[r].height = h
    ws._r = r + 1
    return f"'{ws.title}'!C{r}"

def note(ws, text, color="8D4529"):
    r = ws._r
    c = ws.cell(r, 2, text); c.font = Font(name=F, size=9, color=color)
    c.alignment = Alignment(wrap_text=True, vertical="top"); ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    ws.row_dimensions[r].height = 15 * max(1, text.count("\n") + 1 + len(text) // 90)
    ws._r = r + 1

refs = {}

# ---- 使い方 ----
ws = sheet("使い方", "自己分析ワークブック（書き込み用）", "Udemy講座「自己分析ワーク」の書き込み用シートです。クリーム色の欄に書き込んでください。最後の「1枚まとめ」シートには、各ワークの★の答えが自動で写ります。一覧や詳しい説明・止まったときの欄は、PDF版のワークブックを見てください。")
header(ws, "3つの約束")
for t in ["白紙から考えなくていい。PDF版の一覧から選んでから書きます", "全部やらなくていい。★の欄だけ書けば次に進めます", "深掘りしなくていい。最近の小さな出来事で十分。つらくなったら飛ばしてください"]:
    note(ws, "・" + t, "333333")
header(ws, "進み具合")
cols(ws, "ワーク", "済んだら「済」と書く", "★だけの目安")
for w, m in [("ワーク0 最初の5分", "5分"), ("ワーク1 苦手", "10分"), ("ワーク2 価値観", "10分"), ("ワーク3 力が出る環境", "10分"), ("ワーク4 強み", "15分"), ("ワーク5 生活の土台", "5分"), ("ワーク6 1文にする", "10分"), ("ワーク7 点検と今週の一歩", "10分")]:
    row(ws, w, m, h=20)

# ---- ワーク0 ----
ws = sheet("ワーク0", "ワーク0｜最初の5分", "最近1週間の仕事で、次の3つを1行ずつ。正解はありません。思い出せなければ「今日」か「昨日」で。")
header(ws, "最近1週間の3行", star=True); cols(ws, "質問", "あなたの1行")
refs["w0_1"] = row(ws, "① ちょっとイヤだったこと", "ミカさん：課長からの急ぎの依頼で、午前の予定が全部ずれた")
refs["w0_2"] = row(ws, "② ちょっとほっとしたこと・うれしかったこと", "ミカさん：作った資料を「見やすい」と言われた")
refs["w0_3"] = row(ws, "③ 人に頼まれたこと（小さなことでいい）", "ミカさん：新人さんに経費精算のやり方を聞かれた")

# ---- ワーク1 ----
ws = sheet("ワーク1", "ワーク1｜苦手：イヤだったことを細かく分ける", "PDF版1-Aの一覧（イヤだった場面36項目）に○をつけてから、特にイヤだったものを3つまで書きます。書くのがつらいものは、項目名だけでかまいません。")
header(ws, "1-A 特にイヤだったもの（3つまで）", star=True); cols(ws, "選んだ項目", "そのときの場面（1行）")
for i, ex in enumerate(["急な予定変更・割り込みが多い", "電話やメールの対応で作業が何度も止まる", "何をしても評価が見えない"]):
    r = ws._r; ws.cell(r, 2).fill = PatternFill("solid", fgColor=INPUT)
    row(ws, "", "ミカさん：" + ex)
    ws.cell(r, 2).fill = PatternFill("solid", fgColor=INPUT)
header(ws, "1-B 1つだけ変えられたら", star=True); cols(ws, "質問", "答え")
row(ws, "その場面で、もし1つだけ変えられたら、何を変える？", "ミカさん：急ぎの依頼を、午後にまとめてもらう")
header(ws, "1-B 4つの切り口（時間がある人）"); cols(ws, "切り口", "答え", "記入例（ケンタさん）")
for k, ex in [("何を：作業そのもの？", "話すこと自体はイヤではない"), ("誰と：相手や人数？", "知らない相手に断られ続けるのがつらい。知っている取引先なら平気"), ("どう進める：ペースや決め方？", "1日50件という数のノルマがイヤだった"), ("どんな状況で：量・時間・場所・緊張？", "断られ続けて、夕方には気持ちが削れていた")]:
    row(ws, k, ex)
header(ws, "1-C 避けたい／工夫すればできる", star=True); cols(ws, "", "答え")
refs["avoid"] = row(ws, "どうしても避けたい（条件にする）", "ミカさん：1日中割り込みが続いて、自分の作業が進まない状況", h=48)
row(ws, "工夫すればできる（条件にしない）", "ミカさん：電話対応そのもの（時間が決まっていれば平気）", h=48)
note(ws, "迷ったら：①もう一度選び直せるとしたら、それがある仕事を選ぶか？（選ばない＝避けたい）②人や職場が変わったら平気になりそうか？（平気＝「〇〇な職場」と書く）")

# ---- ワーク2 ----
ws = sheet("ワーク2", "ワーク2｜価値観：イヤだったことの裏返し", "1-Aの場面を裏返して「本当はどうしたかったか」を書き、PDF版の価値観の言葉（40語）から近いものを選びます。つらい人は、一覧から「あったらうれしいもの」を直接選んでください。")
header(ws, "2-A 裏返す", star=True); cols(ws, "イヤだったこと", "裏返すと → 一覧から選んだ言葉")
for ex in ["ミカさん：急な予定変更が多い → 見通しが立つ", "ミカさん：誰の役に立っているか分からない → 結果が誰かに届く", "ミカさん：電話で作業が何度も止まる → 一人で集中できる"]:
    r = ws._r; row(ws, "", ex); ws.cell(r, 2).fill = PatternFill("solid", fgColor=INPUT)
header(ws, "2-B 3つに絞る", star=True); cols(ws, "順位", "価値観（守られていた場面を1行。なくてもいい）")
refs["v1"] = row(ws, "1位", "見通しが立つ ─ 前の週に予定が分かっていた月は落ち着いて働けた")
refs["v2"] = row(ws, "2位", "結果が誰かに届く ─ 新人さんが「助かった」と言ってくれた")
row(ws, "3位", "一人で集中できる ─ （空欄）")
note(ws, "迷ったら：「これが欠けたら、ほかがよくても辞めたくなるもの」を残す")

# ---- ワーク3 ----
ws = sheet("ワーク3", "ワーク3｜力が出る環境", "最近1年の仕事で、力が出た場面を1〜2つ。そのとき何がそろっていたか（何を・誰と・どう進める・どんな状況で）を取り出します。")
header(ws, "3-A 力が出た場面", star=True); cols(ws, "", "場面（1行）")
row(ws, "場面1", "ミカさん：新人さん向けに経費精算の手順書を作ったら、質問がほとんど来なくなった")
row(ws, "場面2", "")
header(ws, "3-B 条件を1文に", star=True); cols(ws, "", "私は、〔　〕のとき、力が出る。")
refs["env"] = row(ws, "力が出る条件（2〜3個）", "ミカさん：自分のペースで、終わりの見える作業を任されて、使ってくれる人がいる", h=48)

# ---- ワーク4 ----
ws = sheet("ワーク4", "ワーク4｜強み：出来事と動詞で見つける", "ここまでのワークの出来事から、自分がしたことをPDF版の動詞の一覧（48語）で拾います。名前をつけなくて大丈夫です。")
header(ws, "4-A 出来事から動詞を拾う", star=True); cols(ws, "出来事（ここまでのワークから写す）", "自分がしたこと（動詞を2〜3個）")
r = ws._r; row(ws, "", "ミカさん：手順書を作った → 整理する・手順を作る・伝わる形にする"); ws.cell(r, 2).fill = PatternFill("solid", fgColor=INPUT)
for _ in range(2):
    r = ws._r; row(ws, "", ""); ws.cell(r, 2).fill = PatternFill("solid", fgColor=INPUT)
header(ws, "4-B 確かめる（時間がある人）"); cols(ws, "質問", "答え")
row(ws, "人によく頼まれること・聞かれることは？", "ミカさん：「この資料、見やすくして」「やり方を教えて」")
row(ws, "それを頼んできたのは誰？", "ミカさん：新人さん・同じ課の人")
row(ws, "長くやっても、あまり疲れないことは？", "ミカさん：表やファイルの整理")
row(ws, "4-Aの動詞と重なるものは？", "ミカさん：整理する・伝わる形にする")
header(ws, "4-C 強みを1文に", star=True); cols(ws, "", "〔何を〕〔動詞〕ことで、〔誰〕の〔何〕を〔よくする・減らす・助ける〕ことができる。")
refs["strength"] = row(ws, "強みの1文", "ミカさん：ばらばらの手順を整理して、迷わない形にまとめることで、チームの手間とミスを減らすことができる", h=54)
note(ws, "「誰の」が思いつかないときは、ワーク0の③で頼んできた人を入れる。後半は「〇〇さんの手間を減らす」で仮置きしてもいい")

# ---- ワーク5 ----
ws = sheet("ワーク5", "ワーク5｜生活の土台", "PDF版5-Aのチェック項目に○をつけてから、「これが守れないなら続かない」線を1つずつ。数字で書けるものは数字で。")
header(ws, "5-B 削れない線", star=True); cols(ws, "", "削れない線")
refs["money"] = row(ws, "お金", "ミカさん：今の手取りから大きく下げない")
refs["time"] = row(ws, "時間", "ミカさん：残業は月20時間まで。平日夜の習い事を続けたい")
refs["body"] = row(ws, "体力", "ミカさん：特になし（空欄）")
note(ws, "迷ったら：「1年間その状態が続いたら、体か生活がもたない」と思うもの")

# ---- ワーク6・7 ----
ws = sheet("ワーク6・7", "ワーク6・7｜1文にする／点検と今週の一歩", "「1枚まとめ」シートを見ながら、自分に合う働き方を1文にします。")
header(ws, "6-B 自分に合う働き方の1文", star=True); cols(ws, "型", "あなたの1文")
refs["oneline"] = row(ws, "〔強み〕仕事を、〔価値観・力が出る環境〕で。〔苦手〕は避けて、〔生活の土台〕は守る。", "ミカさん：ばらばらの手順を整理して、迷わない形にまとめる仕事を、見通しが立ち、使ってくれる人がいる環境で。1日中割り込みが続いて、自分の作業が進まない働き方は避けて、残業は月20時間までに抑える。", h=80)
header(ws, "7-A 今の仕事の点検", star=True); cols(ws, "枠", "○△×　とひとこと", "記入例（ミカさん）")
for k, ex in [("強みが使えている", "△ 手順書づくりは年に数回だけ"), ("価値観が守られている", "× 見通しが立たない日が多い"), ("力が出る環境がある", "△ 作業は任されているが、割り込みが多い"), ("苦手（避けたい条件）が少ない", "× 1日中、電話と急ぎの依頼で中断される"), ("生活の土台が守れている", "○ 残業は月15時間くらい")]:
    row(ws, k, ex, h=26)
header(ws, "7-B 今週の一歩（1つだけ）", star=True); cols(ws, "", "答え")
refs["road"] = row(ws, "選んだ道（A 今の場所で調整する／B 役割や部署を変える／C 外を調べ始める）", "A", h=30)
refs["step"] = row(ws, "一歩", "「手順書・マニュアル整備をもっと担当したい」と上司に伝えるメモを3行書く", h=40)
refs["when"] = row(ws, "いつやる", "金曜の面談で話す", h=24)

# ---- 1枚まとめ（自動で写る）----
ws = sheet("1枚まとめ", "自分に合う働き方シート（1枚まとめ）", "各ワークの★の答えが自動で写ります。直したいときは、元のワークのシートを直してください。印刷する場合は、このシートだけ印刷するとA4で1枚になります。")
ws.column_dimensions["D"].width = 2
cols(ws, "枠", "あなたの答え（自動）", "")
for label, ref in [("強み", refs["strength"]), ("価値観（1位）", refs["v1"]), ("価値観（2位）", refs["v2"]), ("力が出る環境", refs["env"]), ("苦手（避けたい条件）", refs["avoid"]), ("生活の土台：お金", refs["money"]), ("生活の土台：時間", refs["time"]), ("生活の土台：体力", refs["body"])]:
    r = ws._r
    row(ws, label, "", h=40)
    ws.cell(r, 3).value = f'=IF({ref}="","",{ref})'
    ws.cell(r, 3).fill = PatternFill("solid", fgColor="FFFFFF")
header(ws, "自分に合う働き方の1文")
r = ws._r; row(ws, "1文", "", h=80); ws.cell(r, 3).value = f'=IF({refs["oneline"]}="","",{refs["oneline"]})'
header(ws, "今週の一歩")
for label, key in [("道", "road"), ("一歩", "step"), ("いつ", "when")]:
    r = ws._r; row(ws, label, "", h=28); ws.cell(r, 3).value = f'=IF({refs[key]}="","",{refs[key]})'
ws.page_setup.paperSize = ws.PAPERSIZE_A4; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = f"B1:C{ws._r}"

for s in wb.worksheets:
    s.freeze_panes = "B4"
wb.save(sys.argv[1])
print("ok", [s.title for s in wb.worksheets])
