#!/usr/bin/env python3
"""20_ワークブック.md から、配布用のHTML（→PDF）とテキスト版を作る。
使い方: python3 build_workbook.py <ワークブック.md> <出力フォルダ>
"""
import re, sys, pathlib, html
import markdown

src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
md = src.read_text(encoding="utf-8")

# ---- テキスト版（スマホのメモ用）----
txt = md
txt = txt.replace("（Udemy講座「自己分析ワーク」付属。PDF版・スプレッドシート版の元原稿）\n", "（Udemy講座「自己分析ワーク」受講者用・テキスト版。スマホのメモに貼って使えます）\n")
txt = re.sub(r"^---$", "", txt, flags=re.M)
txt = txt.replace("- ⏸ … 今日はここまででOKの区切り", "- 【今日はここまで】… そこでやめていい区切り")
txt = txt.replace("- 🆘 … 止まったら見る欄（質問・迷ったときの決め方・AIプロンプト）", "- 【止まったら】… 手が止まったときに見る欄（質問・迷ったときの決め方・AIプロンプト）")
txt = txt.replace("🆘 **止まったら**", "【止まったら】").replace("🆘 **AIを使うなら（コピペ用）**", "【AIを使うなら（コピペ用）】")
txt = re.sub(r"⏸ 今日はここまで(でも)?OKです。?", "－－ 今日はここまででもOKです －－", txt)
txt = re.sub(r"^# (.+)$", r"■■ \1 ■■", txt, flags=re.M)
txt = re.sub(r"^## (.+)$", r"\n━━━━━━━━━━\n■ \1\n━━━━━━━━━━", txt, flags=re.M)
txt = re.sub(r"^### (.+)$", r"\n▼ \1", txt, flags=re.M)
txt = txt.replace("**", "").replace("```", "")
txt = re.sub(r"^\|[-| ]+\|$\n", "", txt, flags=re.M)          # 表の区切り行
txt = re.sub(r"^\| ?(.*?) ?\|$", lambda m: "・" + "／".join(c.strip() for c in m.group(1).split("|")), txt, flags=re.M)
txt = re.sub(r"\n{3,}", "\n\n", txt)
(out / "自己分析ワークブック_テキスト版.txt").write_text(txt.strip() + "\n", encoding="utf-8")

# ---- HTML（PDF用）----
body_md = md.split("\n", 1)[1]  # 先頭の # タイトル行は表紙で出す
body_md = body_md.replace("🆘 **止まったら**", '<p class="badge help">止まったら</p>')
body_md = body_md.replace("🆘 **AIを使うなら（コピペ用）**", '<p class="badge ai">AIを使うなら（コピペ用）</p>')
body_md = re.sub(r"⏸ 今日はここまで(でも)?OKです。?", '<p class="pause">今日はここまででもOKです</p>', body_md)
body_md = body_md.replace("（Udemy講座「自己分析ワーク」付属。PDF版・スプレッドシート版の元原稿）", "")
body_md = body_md.replace("- ⏸ … 今日はここまででOKの区切り", "- 「今日はここまで」… そこでやめていい区切り")
body_md = body_md.replace("- 🆘 … 止まったら見る欄（質問・迷ったときの決め方・AIプロンプト）", "- 「止まったら」… 手が止まったときに見る欄（質問・迷ったときの決め方・AIプロンプト）")
# リストの前に空行を入れる（Markdownの仕様で段落に吸収されるのを防ぐ）
lines=body_md.split("\n"); fixed=[]
islist=lambda s: bool(re.match(r"^(\s*[-*] |\s*\d+\. )", s))
for i,l in enumerate(lines):
    if islist(l) and fixed and fixed[-1].strip() and not islist(fixed[-1]) and not fixed[-1].startswith("|"):
        fixed.append("")
    fixed.append(l)
# リスト項目の間の空行を消す（ゆるいリストにしない）
clean=[]
for i,l in enumerate(fixed):
    if not l.strip() and clean and islist(clean[-1]) and i+1<len(fixed) and islist(fixed[i+1]):
        continue
    clean.append(l)
body_md="\n".join(clean)
# ★見出しを強調
body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists", "nl2br"])
body = body.replace("<h3>", '<h3 class="step">')
body = re.sub(r'<h3 class="step">(\d-[A-C]) ★', r'<h3 class="step"><span class="no">\1</span><span class="star">★</span>', body)
body = re.sub(r'<h3 class="step">(\d-[A-C]) ', r'<h3 class="step"><span class="no">\1</span>', body)
# ワーク・付録ごとに改ページ
body = re.sub(r"<h2>(ワーク\d|付録1|進み具合)", r'<h2 class="newpage">\1', body)
# □のチェックリストを2列のチェック欄に
body = re.sub(r"<li>□ ", '<li class="chk">', body)
body = re.sub(r'(<li class="chk">.*?</li>\s*)<li>上にないもの', r'\1<li class="chk">上にないもの', body)
body = re.sub(r"<ul>(\s*<li class=\"chk\">)", r'<ul class="chklist">\1', body)
# 小さい表は途中で切らない
def tbl(m):
    rows=m.group(0).count("<tr>")
    return m.group(0).replace("<table>", '<table class="keep">' if rows<=10 else "<table>",1)
body = re.sub(r"<table>.*?</table>", tbl, body, flags=re.S)
# 書き込み欄：空のセルに高さ
body = body.replace("<td></td>", '<td class="blank"></td>')
# 「（　　　）」の書き込みを下線の欄に
body = re.sub(r"（[　 ]{4,}）", '<span class="line"></span>', body)
body = re.sub(r"〔[　 ]{4,}〕", '<span class="line short"></span>', body)

css = """
@page { size: A4; margin: 16mm 15mm 18mm; }
:root { --bg:#f6f3ee; --navy:#27364b; --terra:#c96f4a; --ink:#2b2b2b; --muted:#6b6b6b; --rule:#d9d2c7; --soft:#efe9df; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin:0; font-family:'Noto Sans JP',sans-serif; font-weight:500; color:var(--ink); font-size:10.5pt; line-height:1.75; background:#fff; }
h1,h2,h3 { font-family:'Noto Serif JP',serif; color:var(--navy); line-height:1.4; }
h2 { font-size:17pt; font-weight:900; margin:0 0 4mm; padding:3mm 0 2.5mm; border-bottom:2.5px solid var(--navy); }
h2.newpage { break-before: page; }
h3.step { font-size:12.5pt; font-weight:700; margin:7mm 0 2.5mm; display:flex; align-items:center; gap:2.5mm; break-after: avoid; }
h3 .no { background:var(--navy); color:#fff; font-family:'Noto Sans JP',sans-serif; font-size:10pt; padding:0.5mm 2.5mm; border-radius:2mm; }
h3 .star { color:var(--terra); font-size:13pt; }
p { margin:1.5mm 0 2.5mm; }
strong { color:var(--navy); }
ul,ol { margin:1mm 0 3mm; padding-left:6mm; }
li { margin:0.6mm 0; }
table { width:100%; border-collapse:collapse; margin:2mm 0 4mm; font-size:9.6pt; break-inside:auto; }
th { background:var(--navy); color:#fff; font-weight:700; text-align:left; padding:1.6mm 2.2mm; }
td { border:1px solid var(--rule); padding:1.6mm 2.2mm; vertical-align:top; }
tr { break-inside: avoid; }
table.keep { break-inside: avoid; }
ul.chklist { list-style:none; padding-left:0; columns:2; column-gap:8mm; margin:1mm 0 3mm; }
ul.chklist li { break-inside:avoid; padding-left:6mm; position:relative; margin:0.4mm 0; }
ul.chklist li::before { content:""; position:absolute; left:0; top:0.45em; width:3.4mm; height:3.4mm; border:1.3px solid var(--navy); border-radius:0.6mm; background:#fff; }
p + ul.chklist { margin-top:0; }
td.blank { height:13mm; background:#fff; }
tbody tr:nth-child(even) td:not(.blank) { background:#faf8f4; }
pre { background:var(--soft); border-left:3px solid var(--terra); padding:2.5mm 3.5mm; white-space:pre-wrap; font-family:'Noto Sans JP',sans-serif; font-size:9pt; line-height:1.6; border-radius:1.5mm; break-inside: avoid; margin:1mm 0 4mm; }
code { font-family:inherit; }
.badge { display:inline-block; font-weight:700; font-size:9.5pt; padding:0.6mm 3mm; border-radius:10mm; margin:4mm 0 1mm; }
.badge.help { background:#f3e3da; color:#8d4529; }
.badge.ai { background:#e3e8ef; color:var(--navy); }
.pause { text-align:center; color:var(--terra); font-weight:700; font-size:9.5pt; border-top:1px dashed var(--terra); border-bottom:1px dashed var(--terra); padding:1.2mm 0; margin:5mm 15mm; }
.line { display:inline-block; min-width:60mm; border-bottom:1px solid var(--ink); height:1.2em; vertical-align:bottom; }
.line.short { min-width:35mm; }
blockquote { margin:2mm 0; padding:1mm 4mm; border-left:3px solid var(--navy); background:#faf8f4; }
/* 表紙 */
.cover { height:257mm; display:flex; flex-direction:column; justify-content:center; padding:0 6mm; background:var(--bg); margin:-16mm -15mm 0; padding:0 21mm; break-after: page; }
.cover .kicker { color:var(--terra); font-weight:700; letter-spacing:0.15em; font-size:10.5pt; }
.cover h1 { font-size:30pt; font-weight:900; margin:4mm 0 6mm; line-height:1.35; }
.cover .sub { font-size:12pt; color:var(--navy); margin-bottom:12mm; }
.cover .frames { display:flex; gap:2.5mm; flex-wrap:wrap; margin-bottom:14mm; }
.cover .frames span { border:1.5px solid var(--navy); color:var(--navy); padding:1.2mm 3.5mm; border-radius:10mm; font-weight:700; font-size:10pt; background:#fff; }
.cover .gets { background:#fff; border-left:4px solid var(--terra); padding:4mm 6mm; font-size:10.5pt; }
.cover .gets b { color:var(--navy); }
.cover .by { margin-top:16mm; color:var(--muted); font-size:9.5pt; }
"""
cover = """
<section class="cover">
  <div class="kicker">WORKBOOK｜書き込み式</div>
  <h1>自己分析ワークブック</h1>
  <div class="sub">一覧から選んで、1行ずつ。<br>5つの枠で、自分に合う働き方を1文にする。</div>
  <div class="frames"><span>苦手</span><span>価値観</span><span>力が出る環境</span><span>強み</span><span>生活の土台</span></div>
  <div class="gets"><b>最後に手元に残るもの</b><br>5つの枠を埋めた1枚／「自分に合う働き方」の1文／今週の小さな一歩</div>
  <div class="by">タクマ｜キャリアノート　Udemy講座「自己分析ワーク」受講者用</div>
</section>
"""
page = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<title>自己分析ワークブック</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@700;900&display=block" rel="stylesheet">
<style>{css}</style></head><body>{cover}{body}</body></html>"""
(out / "workbook.html").write_text(page, encoding="utf-8")
print("ok")
