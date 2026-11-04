# C. SNS発信の現状：経理DX／経理×AI／業務効率化／経理キャリアのコンテンツ地図（日本・2026年11月時点）

> 調査日：2026-11-04。YouTube の数字はすべて YouTube Data API v3 で当日取得したもの（生データ：`youtube_data/videos.csv`・`channels.csv`・`comments.jsonl`、チャンネル指定の追加取得は `youtube_data/channels_pass/`、テーマ別集計は `youtube_data/theme_stats.md`）。
> 伸び率＝その動画の再生数 ÷ そのチャンネルの最近30本の再生数の中央値（公開3日未満は除外）。「当たり」＝伸び率3倍以上かつ5,000回以上。
> **データ取得の制約（重要）**：API の検索クエリ上限（1日100回、並行調査と共有）に途中で達し、18キーワード中「経理 転職」「freee 使い方」「マネーフォワード 使い方」「インボイス 経理」「電子帳簿保存法 経理」「会計 AI 活用」は0件、「ひとり経理」「月次決算 早期化」は片方の並び順だけ（18本・6本）しか取れていない。検索で取れたのは計293本・205チャンネル。不足分は既知の経理・会計・税理士・Excel系26チャンネルの最近30本を直接取得（743本）して補った（ここには12か月より前の動画も含まれる）。note.com・udemy.com・tofu.misosil.com はこのセッションのネットワーク設定で直接取得できず、YouTube 以外の数字はウェブ検索結果の要約に頼っている（下記で個別に注記）。

## 1. YouTube の主要チャンネル（規模・投稿頻度・尺・収益導線）

### Takeaway
「経理」だけを看板にした日本語チャンネルは、登録者1万人を超えるものがほとんどない（経理くまch 8,340、ミライ経理 7,420、STUDYJOB 15,700）。経理×AIの需要は、汎用AI業務効率化の大手（ひかりのAI大学 11.8万、ユースフル 47.6万など）と、税理士・会計士の大手（スガワラくん 183万、くろいちゃんねる 7.2万）に取られている。経理×AI専門は、登録者1,000人台以下の小さい税理士・会計士・ITコンサルのチャンネルが2026年に急に増えた段階にある。

### Cited Findings
（数字はすべて API で取得。投稿頻度は取得した最近30本のうち公開90日以内の本数。尺は長尺動画の中央値。導線は概要欄の冒頭テキストに出てくる語なので、全部は拾えていない）

**経理特化（現役経理・元経理）**
- 経理くまch【未経験・上場企業・フリーランス経理】：登録者8,340／動画152本／最近30本の中央値4,940回。直近90日の投稿は2本だけで更新が止まりがち。最近30本のうちショート19本。上位はショートの「あるある」（「初見◯しの仕訳チェックが辛すぎる件」23,480回・伸び率4.75）。導線は転職・エージェント — [videos](https://www.youtube.com/watch?v=bUXqFOOKsR4)
- ミライ経理：登録者7,420／13本。直近90日に13本で長尺の中央値は21.9分。中央値19,182回と規模の割に再生が多い（「【AI時代の経理スキル】なくなる仕事となくならない仕事」68,849回・3.59倍、「福沢諭吉と経理の関わり方とは？」82,092回・4.28倍）。対談・歴史もの。経理派遣の事例回（「月末月初だけの経理派遣」）もある — [動画](https://www.youtube.com/watch?v=OcHIwTpRvMA)
- 世界一役に立つ【経理・会計】チャンネル STUDYJOB：登録者15,700。直近90日に30本で、最近30本はすべてショート（「【Excel神ワザ】」シリーズ）。最高は「100%入力ミスがなくなるExcel神設定！」20,529回・13.5倍。導線は公式LINE — [動画](https://www.youtube.com/watch?v=ZLoTPE7CpGA)
- 経理ねこの会計日記（公認会計士・東証プライム上場の経理部長、VTuber）：登録者3,040。直近90日の投稿は0本。当たりは2023〜24年の未経験転職・簿記の回（「簿記２級で未経験経理は不可能？」60,638回・40.9倍） — [動画](https://www.youtube.com/watch?v=ClWekKbS77Y)
- 爆速経理マン：登録者202／10本。未経験から上場企業経理への転職体験（ショート「面接で聞かれたことTOP3」31,378回・12.05倍）。2025年5月以降は投稿なし — [動画](https://www.youtube.com/watch?v=wyNwh2cp7Qg)
- みそまるの簿記塾（現役経理マン）：登録者5,430。簿記の講義が中心で、「簿記2級を持っている人の『本当の凄さ』を現役経理マンが説明します」32,562回・9.52倍。導線は公式LINE・書籍・特典 — [動画](https://www.youtube.com/watch?v=kc5Z9GMB5P4)

**会計士・税理士（大手）**
- 脱・税理士スガワラくん：登録者183万。直近90日に30本、長尺中央値21.9分、中央値199,306回。経理担当の不正を扱う回「経理担当の固定は超危険…」は379,221回・コメント133件 — [動画](https://www.youtube.com/watch?v=tLmfytP2R9A)
- 公認会計士YouTuberくろいちゃんねる：登録者72,100。直近90日に30本、長尺中央値26.1分、中央値9,486回。経理×AIの回は「【30分→1分】知識ゼロでOK！公認会計士が教える生成AI×Excel経理自動化術」13,695回・1.45倍、「AIで経理はどう変わる？上場企業の現場で見た現実」13,304回・1.40倍で、どちらも平均並み。当たりは会計不正の時事（ニデック、147,108回・15.51倍） — [動画](https://www.youtube.com/watch?v=AOlNf1IYaS8)
- 忖度しない公認会計士 いのちゃん先生：登録者13.4万。ショート「AIで自動化して経理をクビしたら会社崩壊しました」4,621回・1.70倍 — [動画](https://www.youtube.com/watch?v=EXkApdqpOII)
- 税理士河南：登録者28万／社長の資産防衛チャンネル：25.5万（直近90日に30本、導線は無料相談・プレゼント）／走る税理士かずぅ：6,290（直近90日に26本）。どれも確定申告・節税が中心で、経理DXはほとんど扱っていない（河南の最高は確定申告速報 337,773回・13.34倍） — [動画](https://www.youtube.com/watch?v=7Q_57dklRN8)、出典は `youtube_data/channels_pass/channels.csv`
- 会計事務所チャンネル!!【ヒロ税理士のセカンドch】：登録者20,600。「経理代行始めました。【一人社長や小さな会社様向け】」2,144回・2.68倍。導線はオンラインサロン・セミナー・転職エージェント — [動画](https://www.youtube.com/watch?v=zEdDbZ-9gNs)
- レックスたぬ吉の会計転職チャンネル：登録者4,950。「【転職】経理の年収と簿記1級の関係！」11,103回・7.67倍、「経理とAIの関係！徹底解説！」は1,549回・1.07倍。導線は会計転職の無料相談（転職エージェント型） — [動画](https://www.youtube.com/watch?v=LIQ-G0e4_kU)

**経理×AI専門（小規模・2026年に増えた層）**
- 荒井悠輔 AI・DX・税理士：登録者1,200。直近90日に27本で、新しいモデルが出た翌日に検証動画を出す。「【Claude Opus 5.5】弥生会計の仕訳入力から『達人』へのデータ移行までAIがPCを自動操作」10,157回・11.8倍、「GPT-6 Astra 弥生会計→所得税の達人へAIが自動転記」7,213回・8.38倍 — [動画](https://www.youtube.com/watch?v=iTN8JTFA8D0)
- NEXTバックオフィス研究所【AIと経営管理と】：登録者9,580。「【最先端AI経理】Claude codeとMCPをフル活用して、会計仕訳の完全自動化にトライ」14,635回・24.47倍（2026-02）。導線はメルマガ・書籍 — [動画](https://www.youtube.com/watch?v=zMA_kDUMk-U)
- Time Design Lab｜ひとり会計士 宮本大樹：登録者132。直近90日に30本、長尺中央値4.6分、中央値64回。「Geminiでレシート自動記帳アプリを作る」1,023回・15.86倍。導線は講座・メルマガ — [動画](https://www.youtube.com/watch?v=0KY42cKHQx4)
- 中小企業のAI自動化：登録者34。「【経理の入力が消える】マネーフォワード新機能×Claude Codeで月次仕訳を自動化」2,326回・122倍 — [動画](https://www.youtube.com/watch?v=MMWj5gyISRc)
- 正直税理士：登録者169。「AI経理｜4ステップで領収書を弥生会計に自動仕訳」2,628回・3.81倍 — [動画](https://www.youtube.com/watch?v=teoaFOhT0FA)
- AI経理の教科書：登録者8。60分の「経理で使えるAIプロンプト10選」は241回 — [動画](https://www.youtube.com/watch?v=X4XiircZHWQ)

**汎用AI・Excel業務効率化（経理の視聴者を取っている大手）**
- ひかりのAI大学：登録者11.8万、中央値8,489回。導線は公式LINEのプレゼント・特典 — [動画](https://www.youtube.com/watch?v=NmSUp4Gezc8)
- ユースフル／実務変革のプロ：登録者47.6万。直近90日に30本、長尺中央値13.1分、中央値14,916回。導線はLINE・講座・無料相談・特典。経理×AIそのものの当たりは今回のデータにない — [動画](https://www.youtube.com/watch?v=0rsWtPRwK4g)
- エクセル兄さん たてばやし淳：登録者11.3万。最近は生成AIの速報が中心。導線はLINE・note・書籍 — [動画](https://www.youtube.com/watch?v=b_IxIF1z2V8)
- 泥臭コンサルの非常識なDX学：登録者15,800。「【実演あり】Copilotだけで経理のExcel業務はどこまで自動化できるのか検証！」2,981回・1.69倍 — [動画](https://www.youtube.com/watch?v=52u3tOPqiLU)

**ベンダー公式**
- 弥生【公式】：登録者49,300、中央値407回／freeeの「これ、イイじゃん」秒速Tips【公式】：登録者293、直近90日に30本（29本がショート）、中央値438回／LayerX公式：11,700、中央値1,444回（出典は `youtube_data/channels_pass/channels.csv`） — [freee公式Tipsの最高回](https://www.youtube.com/watch?v=IryZA1Nd3ac)
- 【公式】OBC（勘定奉行）の15秒webCM「勘定奉行クラウド×AIで経理DXも…」は88,278,222回なのに高評価11件。広告配信による再生と見られ、伸び率の分析からは外した — [動画](https://www.youtube.com/watch?v=PxSC5i1naZs)
- PIVOT公式の経理AI関連回（「【経理AI導入ステップ 徹底解説】」109,385回・1.05倍、「脱・経理の属人化にはAIエージェントを使うべし」107,166回・1.03倍）は、毎回だいたい10万回前後で並んでいる — [動画](https://www.youtube.com/watch?v=QCSe9KCgUZ0)

### Inferences
- 「現役経理が経理×AIの実務を続けて出しているチャンネル」で登録者1万人を超えるものは、今回のデータでは見つからなかった。経理特化チャンネルは「あるある」ショートと転職・簿記で伸びていて、AI実務は税理士やITコンサルが扱っている。
- 収益導線ははっきり3つに分かれる。(a) 公式LINE＋特典配布（ひかり・ユースフル・STUDYJOB・みそまる）、(b) 転職エージェント・無料相談（たぬ吉・経理くま・ヒロ税理士）、(c) 自社サービスの集客（税理士の顧問・経理代行、ベンダー）。経理×AIの有料講座・コミュニティを本格的に回しているYouTuberは、今回の範囲では確認できなかった。
- PIVOT の経理AI回は再生数のばらつきが小さく、ベンダーとのタイアップ回の可能性がある（推測。タイアップかどうかは確認していない）。

### Gaps
- 「freee 使い方」「マネーフォワード 使い方」「経理 転職」「インボイス」「電子帳簿保存法」の検索は API の上限で取れていない。freee・マネーフォワード本体の公式チャンネルは @ハンドルの推測が外れて特定できなかった。
- 導線は概要欄の冒頭（約200字）からしか拾っていないので、LINE・講座の有無は抜けている可能性がある。
- 税理士系の大河内薫氏や経理部長系YouTuberなど、検索に出なかった既知のチャンネルは取れていない。

## 2. どの動画が伸びたか（伸び率）とテーマ・タイトルの型

### Takeaway
伸び率が一番大きいのは「汎用AI×Excel」（Copilot／Gemini）を職種・実務に寄せた解説で、大手が伸び率20〜80倍で何十万回も取っている。「経理×AI実務」は本数が多い（70本）のに再生数の中央値が845回と小さい。それでも登録者数百〜1万の小規模チャンネルが「会計ソフト名×最新AI×自動仕訳」の実演で10〜120倍の当たりを出している。将来性・なくなる系とキャリア・資格系は、本数は少ないが再生の中央値が大きい。

### Cited Findings
**テーマ別（検索で取った日本語・4分以上の長尺177本、キーワードで上から順に排他分類。`youtube_data/theme_stats.md`）**

| テーマ | 本数 | 再生数中央値 | 伸び率中央値 | 3倍以上 |
|---|---|---|---|---|
| 経理×AI実務（仕訳自動化・会計ソフト×AI） | 70 | 845 | 1.43 | 17 |
| 経理の将来性・なくなる | 3 | 78,916 | 4.29 | 1 |
| 経理転職・キャリア・資格 | 14 | 10,130 | 1.86 | 3 |
| 汎用AI業務効率化（Excel/Copilot/Gemini/Claude Code） | 42 | 88,014 | 3.25 | 14 |
| Excel・PC時短（AIなし） | 10 | 446 | 1.73 | 4 |
| 経理DX・業務改善（一般論・ツール） | 14 | 430 | 1.26 | 0 |

（「将来性」は先に「経理×AI」に分類された動画を除いた残りなので本数が少ない。どの行も片側10本未満のものは傾向の参考にとどまる）

- 「経理×AI」タイトルの公開本数は月を追うごとに増えている：2025-12が5本 → 2026-03が8本 → 2026-07が10本 → 2026-09が17本（GPT-6 Astra・Claude Opus 5.5が出た月）。投稿は74チャンネルに散らばり、登録者1万人未満のチャンネルが77本を出している（`theme_stats.md`）。

**当たり動画（長尺・テーマ内・ベンダーCMを除く）**
- 「【2026年最新版】Excelとも神連携！本当に使えるCopilot活用法10選【完全攻略】」ひかりのAI大学 703,451回・82.87倍・21分 — [動画](https://www.youtube.com/watch?v=NmSUp4Gezc8)
- 「【職種別】簡単便利！GeminiでExcel作業を最速化する方法を解説します！【業務効率化】」同 646,137回・76.11倍・14分 — [動画](https://www.youtube.com/watch?v=JoK4GGZ9JVQ)
- 「【抜け漏れゼロへ】日次・週次・月次を一元管理できるExcelタスク表」生産管理プロフェッショナルコミュニティ 166,732回・85.92倍 — [動画](https://www.youtube.com/watch?v=NltODucZb48)
- 「【初公開】大企業がCopilotをどう活用してるのか全部公開します。」バレないAIの使い方ch 381,582回・18.26倍 — [動画](https://www.youtube.com/watch?v=66bbpw8ZTp8)
- 「【実演あり】CopilotだけできるAI仕事術５選！」ダイさん 321,321回・21.93倍 — [動画](https://www.youtube.com/watch?v=hV4Yu6RiDmQ)
- 「【2026年完全版】業務改善の教科書 業務可視化・マニュアル作り・DX・生成AI導入まで…」泥臭コンサル 34,996回・19.85倍・31分 — [動画](https://www.youtube.com/watch?v=5V4mSRTFabg)
- 「【最先端AI経理】Claude codeとMCPをフル活用して、会計仕訳の完全自動化にトライ」NEXTバックオフィス研究所（登録者9,580）14,635回・24.47倍 — [動画](https://www.youtube.com/watch?v=zMA_kDUMk-U)
- 「【Claude Opus 5.5】弥生会計の仕訳入力から『達人』へのデータ移行までAIがPCを自動操作」荒井悠輔（1,200）10,157回・11.8倍 — [動画](https://www.youtube.com/watch?v=iTN8JTFA8D0)
- 「【AI時代の経理スキル】なくなる仕事となくならない仕事」ミライ経理 68,910回・3.52倍 — [動画](https://www.youtube.com/watch?v=OcHIwTpRvMA)
- 「【転職】経理の年収と簿記1級の関係！」レックスたぬ吉 11,103回・7.67倍 — [動画](https://www.youtube.com/watch?v=LIQ-G0e4_kU)
- 「【衝撃】Chat GPT時代、会計事務所4年目が感じるリアルな未来【ガチでヤバいかも…】」えりこの未経験日記（登録者728）7,703回・5.96倍・コメント33件 — [動画](https://www.youtube.com/watch?v=D_AzKMUiGmI)

**再生数は5,000回未満だが伸び率が大きい（小さいチャンネルでも再現しやすいテーマの手がかり）**
- 「【経理の入力が消える】マネーフォワード新機能×Claude Codeで月次仕訳を自動化」（登録者34）2,326回・122倍／「【マネーフォワード×Claude Code】経理の手作業がここまで消える—自社で動かす5つの連携」1,222回・64倍 — [動画](https://www.youtube.com/watch?v=MMWj5gyISRc)
- 「【AI×経理】毎月の経理処理を半分にする5つの方法【2026年5月版】」（登録者19）534回・50.86倍 — [動画](https://www.youtube.com/watch?v=4pn1h2TpVH8)
- 「【AI✖会計経理】経理の仕事はAIでなくなる？2026年AIエージェント時代の生存戦略と3つの進路」TaxJudge 890回・25.43倍 — [動画](https://www.youtube.com/watch?v=gaPOg_j4IaE)
- 「ChatGPT・Gemini・Claude、経理に使うならどれ？【2026年版の使い分け】」（ショート）2,431回・20.87倍 — [動画](https://www.youtube.com/watch?v=7-X06KWa8Z0)
- 「【経理自動化】会計ソフトを使わずClaude Code×スプシでここまでできる」無知ノ知ラジオ 2,229回・4.09倍 — [動画](https://www.youtube.com/watch?v=J8oLJ-2Nc1A)

**ショート**
- 「人間が『経理』をする時代、終了。AI置換率ほぼ100%の未来」キャスター公式 168,538回・203.67倍（高評価501） — [動画](https://www.youtube.com/watch?v=A59NvdJoK1w)
- 「最近出たエクセルAIがヤバいです！日本語を5秒入れるだけで…」えみ（登録者2,380）135,478回・96.63倍・コメント77件 — [動画](https://www.youtube.com/watch?v=yJ_SoJ3s-jU)
- 経理部を舞台にしたドラマ・映画切り抜き（ChillCraft「これは経費精算できません！」1,783,557回・7.38倍、うさぎの映画解説「厳格な経理の女性、経費不可の理由が多すぎる。」505,886回）。経理あるあるの寸劇は再生の規模が大きいが、実務の情報はない — [動画](https://www.youtube.com/watch?v=Oftx8U53Ago)

**タイトルの型（上の当たりから）**
- 数字・網羅型：「活用法10選【完全攻略】」「AI仕事術５選」「5つの方法」「プロンプト10選」 — [動画](https://www.youtube.com/watch?v=NmSUp4Gezc8)
- 職種・対象の指定：「【職種別】」「【一人社長必見】」「中小企業の」「経理・事務職必須」 — [動画](https://www.youtube.com/watch?v=JoK4GGZ9JVQ)
- 具体的なツール名×新しいモデル名：「マネーフォワード新機能×Claude Code」「GPT-6 Astra」「Claude Opus 5.5」「弥生会計→達人」 — [動画](https://www.youtube.com/watch?v=iTN8JTFA8D0)
- 結果を先に言う：「経理の入力が消える」「30分→1分」「抜け漏れゼロへ」 — [動画](https://www.youtube.com/watch?v=MMWj5gyISRc)
- 不安・警告：「経理はなくなる？」「時代、終了」「ガチでヤバいかも」「経理担当の固定は超危険」 — [動画](https://www.youtube.com/watch?v=tLmfytP2R9A)
- 年号・最新版：「【2026年最新版】」「【2026年5月版】」 — [動画](https://www.youtube.com/watch?v=4pn1h2TpVH8)

### Inferences
- 「経理×AI」というラベルだけでは伸びない（中央値845回）。伸びているのは (1) 会計ソフト名と最新AIの名前を並べ、実画面で自動仕訳まで見せる実演、(2) 汎用AI×Excelを職種別・実務別に網羅したまとめ、(3) 将来への不安を正面から扱う回、の3種類。
- 新しいモデルが出た直後の検証は、小さいチャンネルでも10倍前後の当たりになっている（荒井悠輔の3本）。ただし毎月追い続ける必要があり、似た動画もすぐに増えている（2026-09は17本）。

### Gaps
- サムネイル画像は見ていない（`gallery.html` に伸び率順で並んでいるので目で確認できる）。顔の有無・文字量の比較はできていない。
- 検索順位・検索ボリュームは API ではわからない。

## 3. コメント欄の声（質問・悩み・リクエスト）

### Takeaway
コメント欄で目立つのは次の4つ。(1) 社内データをAIに入れても大丈夫かというセキュリティ・情報漏洩の質問（多くの動画に共通し、いいねも多い）。(2) 「結局うちの実務では使えない」という、紙・例外処理・中小特有の事情からの反論。(3) ひとり経理の負担と不正リスクの告白。(4) 未経験転職・簿記・年収・「経理はなくなるのか」というキャリア不安。33本のコメント545件のうち、AIの実務導入（費用・手順・安全性）にきちんと答えている動画への言及は見当たらなかった。

### Cited Findings
（原文のまま・[いいね数]）

**セキュリティ・社内ルール**
- 「業務で活用できるのはすごい便利ですが、セキュリティ面（業務内容をCopilotに入れても問題ないのか） についても問題ないのか気になるところですね」[22] — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgwdfSKuVMYu_u1oVgZ4AaABAg)
- 「AIを使う上での情報セキュリティ面の注意点を説明している動画はあまり見た事ないです。漠然と使うのは危険だと思いますので説明お願いします。」 — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgwtnDfx3K0ziim9GUZ4AaABAg)
- 「質問があります。仕事に関する内容を入力する場合、情報漏れを防止する必要があると思います。対策はありますか？」[2] — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=Ugyasl3oslvlB_o6nZZ4AaABAg)
- 「セキュリティ、情報漏洩の問題はどうクリアされていますか？」（税理士がGPT-6 Astraで申告書へ自動転記する動画への質問） — [コメント](https://www.youtube.com/watch?v=S_oK15TypRw&lc=UgxG1cEVLOk_tEoOWxR4AaABAg)
- 「売り上げとかの社内データをそのままAIに丸投げいかがなものか」[19]（Gemini×Excelの動画） — [動画](https://www.youtube.com/watch?v=JoK4GGZ9JVQ)

**費用対効果・ツールの選び方**
- 「Astra極髙設定で作業をしていますが実際どれぐらいのトークン消費なのでしょうか？ 仕訳の入力量と利用料が釣り合うのかそこが気になります。」 — [コメント](https://www.youtube.com/watch?v=tTcRhglITeQ&lc=UgzO6hYIRov6dCFUCRR4AaABAg)
- 「ゆっくりでも勝手に仕事をしてくれるのであれば良いですね！！実際に実務に使おうと思えば最後はコストとの戦いになるのでしょうか・・・」 — [コメント](https://www.youtube.com/watch?v=iTN8JTFA8D0&lc=UgzrjXkrNDQF2duL2S14AaABAg)
- 「ChatGPT,Gemini、Copilot のそれぞれのメリット、デメリット、使い分けを教えてください」[2] — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgzsoA6_UqgG9QcX2-14AaABAg)
- 「有料版のCopilotを使ってますが、こんなに優秀ではないです。…実践では使い物にならないのが現在のAIだと思います。」 — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgzUpmxWyHVE0TXSI814AaABAg)

**現場の実務からの反論（例外処理・紙・中小企業）**
- 「税理士事務所で働いてるけど、単純な経費振り分けならAIでいいんだよ。もっと言えば個人事業主や、1人法人レベルなら確かにAIで十分。ただし、中小企業以上になると…資本的支出の判断や消費税判断、税効果、為替、減損会計なんかになると、とてもじゃないけど…」[3] — [コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=Ugw5J6B4nZNM_B3u7sl4AaABAg)
- 「経理はAI無理よ。 例えばセブンイレブンへの支払いは消耗品費ってルールを設けても実際は福利厚生費・雑費・交際費・会議費等…」[6] — [コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=Ugwb6o5tcb4os8u8pLl4AaABAg)
- 「人間がうっかり間違った修正を行ったり、今回限りの特例的な処理を行うことはよくあると思うのですが、AIがそれを恒久的なルールとして誤学習してしまうリスクはどう排除できるのか気になりますね。」[5] — [コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=UgxrcK-nbUn7i2uLu0x4AaABAg)
- 「紙文化がまだまだ残ってます。…中小では元々事務の人件費は抑えてるので、工数が減ったから人件費減る、というふうに直結しないので、新システム導入で経費増えてるやん！てなる…」 — [コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=Ugy8QDO_JYhStserDbd4AaABAg)
- 「トキウム使ってます。 電子で自動で読み取ってくれてもその番号を結局その伝票に入れ込む作業があり、2倍に作業が増えて疲弊してます。」[2] — [コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=UgypJBz2lfxsIOCQJtt4AaABAg)
- 「昔のマクロでも、RPAでもそうだったけど 何でも自動化、特に仕組みを理解しないまま自動化すると、何かの拍子に壊れた…完全に詰むこともある」[2] — [コメント](https://www.youtube.com/watch?v=AOlNf1IYaS8&lc=Ugybe5cete7bXnhRWXZ4AaABAg)
- 「エクセルをAIで使うんだからむしろエクセル時代が続くって事だろ。…それなり知識が無いと平気でハルシネーション起こす」[50] — [コメント](https://www.youtube.com/watch?v=yJ_SoJ3s-jU&lc=UgwRPmHnE_i_-v1JDmN4AaABAg)

**ひとり経理・中小企業**
- 「昔親族の営む中小企業で一人経理事務として勤務していました。…一人経理だと何とでもできてしまいます。退職時に社長にその危険性を何度も訴えたのですが全く理解ができずに…」[40] — [コメント](https://www.youtube.com/watch?v=tLmfytP2R9A&lc=Ugw7Yh_b-Dv-6j6SLy94AaABAg)
- 「小企業で6年間一人バックオフィスやってました。今考えるとつらかったw …業務範囲広すぎて、社長の経営相談と、一部営業相談までさせられてました。」[3] — [コメント](https://www.youtube.com/watch?v=QqX8veVpJRw&lc=UgyWD78qPYkuYUppjDl4AaABAg)
- 「30代、経理初心者です。小さい事務所でワンマン経理：通常記帳、債権債務管理と支払、月次、年次補助、税理士対応に加えて労務も担当…100社はエントリーしたのですが書類通過率5％未満…」 — [コメント](https://www.youtube.com/watch?v=ClWekKbS77Y&lc=Ugy1YSM3e6_MHjXXG3x4AaABAg)
- 「クロードコードの使い方に関して、クリニックの会計とかで役立つ場面があれば教えて頂きたいです」 — [コメント](https://www.youtube.com/watch?v=i_XOrMEmDn8&lc=UgxcW78u8j4GwOAiAyJ4AaABAg)

**キャリア・将来の不安**
- 「経理2年生だけどこの仕事続けるべきか悩んでる。…既に実務経験豊富でがっちり知識身に付いてる人ならAI上手く活用できるんだろうけど、自分みたいなひよっこだとこの先は希望なし😭」[3] — [コメント](https://www.youtube.com/watch?v=BTvIoxjq8OQ&lc=UgwfflYO5MThxlCm0h54AaABAg)
- 「28卒です。経理って今後なくなると思いますか？存在し続けると思いますか？」[3] — [コメント](https://www.youtube.com/watch?v=LIQ-G0e4_kU&lc=Ugy96d2bwkt0irlmk8B4AaABAg)
- 「25歳高卒未経験簿記2級持ち 140社応募して内定ゼロです^_^」[44] — [コメント](https://www.youtube.com/watch?v=ClWekKbS77Y&lc=UgzD-RTiIvq9J3x3ZW14AaABAg)
- 「友人で20代後半で未経験経理転職をした結果、残業の嵐で半年で夢破れた人の話聞いて…」[30] — [コメント](https://www.youtube.com/watch?v=9i-Pqlk960o&lc=UgzdKaHJjHNSN2XTk5V4AaABAg)
- 「良い未経験求人の見つけ方や見分け方も教えて欲しいです！意外と上場企業より従業員が少なすぎない中小企業の方が業務の難易度が程よくておすすめというのを聞いたりしていて、見分け方に困ってます…」[4] — [コメント](https://www.youtube.com/watch?v=QqX8veVpJRw&lc=UgwFn3pewbN-LBFdWbd4AaABAg)
- 「新卒経理で入社した1年目のペーペーなんですが、2年目の最初に会社で将来のビジョンや夢、目標を発表しないといけません😢 そもそも上の方たちがいったいなんの業務をしているのかさえわかっていない…」[5] — [コメント](https://www.youtube.com/watch?v=QqX8veVpJRw&lc=UgwdMJg2kQc15qILV1l4AaABAg)

### Inferences
- 「情報漏洩の注意点を説明している動画はあまり見た事ない」という声がそのまま出ているので、「経理データをAIに渡すときの社内ルール・設定・やってはいけないこと」は空いているテーマと見られる。
- 反論コメントの多くは「例外処理」「科目判断」「紙と電子の二重運用」に向いている。きれいな実演より「失敗例・AIが間違えた仕訳とその直し方・人が確認するところ」を見せた方が、現役経理には信頼される可能性が高い。
- キャリアの不安は「AIが来ても経理を続けてよいか」「未経験でどう入るか」の2つに分かれる。AI時代の経理キャリアを現役経理の目線で語る長尺は、ミライ経理の1本（68,910回）以外に強いものが見当たらない。

### Gaps
- コメントは関連度順の上位100件までなので、いいねの多い声に寄っている。ショートはコメントが少なく、ほとんど取れていない。
- freee・マネーフォワード操作解説や、インボイス・電帳法の動画のコメントは、検索の上限で取れていない。

## 4. YouTube 以外の SNS（X／Instagram・TikTok／note／Voicy・Podcast／Udemy）

### Takeaway
YouTube以外は、このセッションでは note・Udemy などのサイトを直接開けず、ウェブ検索の要約しか使えなかったので証拠が薄い。わかったのは次のとおり。X では現役経理の発信者のフォロワーが数千人規模（経理ねこ 7,291、エンジョイ経理編集長 4,582）。Instagram では「Excel時短」アカウントが数万〜十数万フォロワーいる。Udemy では「経理×AI」に絞った大きな講座は見つからず、汎用の生成AI業務効率化講座と、AIを使わない経理実務・Excel講座に分かれている。

### Cited Findings
**X**
- 松岡俊@マネフォ経理（@ShunMatsuoka40）：「企業経理一筋約30年。ソニー→マネーフォワード」。検索結果の要約によると著書『経理×AI入門』（2026）がある。フォロワー数は確認できなかった — [X](https://x.com/ShunMatsuoka40)
- エンジョイ経理編集長（@kfkanagawa）：IT大手の財務経理幹部の出身。AI・GAS・VBAを使った効率化と投資・節税を発信。フォロワー4,582（検索結果に表示された時点の数字） — [X](https://x.com/kfkanagawa)
- 経理ねこ（@keirineko_cpa）：BIG4監査法人 → 東証プライム上場企業の経理部長、公認会計士VTuber。フォロワー7,291（同上） — [X](https://x.com/keirineko_cpa)
- 旬刊経理情報（@keirijouhou、中央経済社）：フォロワー2,487（同上） — [X](https://x.com/keirijouhou?lang=ja)

**Instagram・TikTok**
- Excel時短系のInstagram：「まさと/エクセルの時短術を発信」は約4.2万フォロワー、「がじゅ｜1日1分で時短を叶えるPC術」は約14.3万フォロワー（2023年12月時点の紹介記事） — [find-model](https://find-model.jp/insta-lab/instagram-influencer-excel-work-efficiency/)
- アカウント売買サイトに「総フォロワー10.6万人超え」「フォロワー8.6万人」のExcel特化Instagramアカウントの譲渡案件が出ている（売り手の宣伝文なので数字は割り引いて見る必要がある） — [rakkoma](https://rakkoma.com/project/detail/7618)、[rakkoma](https://rakkoma.com/project/detail/3388)
- 「ゴリラExcel」が note で「3か月でフォロワー2.7万人達成」のデータを公開している — [note](https://note.com/gorilla_excel/n/na12c1d45ae37)
- 経理に特化したInstagram／TikTokの大きなアカウントは、検索では確認できなかった。

**note**
- 経理×ChatGPT の記事の例：「経理業務×ChatGPT活用リストを作成しました【生成AI活用ディレクター監修】※GPTsリンク付き」（ロコアシ）、「経理初心者でも簡単！ChatGPTの使い方完全ガイド」（AI顧問ワークス） — [note](https://note.com/locoassi/n/n53003ee39f1d)、[note](https://note.com/ai_komon/n/nae7388a25ef1)
- AI活用ジャンルの有料記事は500〜2,000円程度という整理がある（二次情報） — [lilys.ai](https://lilys.ai/ja/notes/ai-monetization-20251113/ai-note-side-hustle-secrets)
- 経理×AIの有料noteの具体的な価格・販売数（「〇部突破」などの表示）は、note.com を直接開けず確認できなかった。

**Voicy・Podcast**
- 税務研究会「声でとどける税務通信」：税理士・公認会計士・企業経理部で働く人向けのポッドキャスト — [税務研究会](https://www.zeiken.co.jp/lp/podcast/)
- 「大河内薫のお金の学びラジオ by Voicy」：税理士による個人のお金の話が中心 — [Apple Podcasts](https://podcasts.apple.com/jp/podcast/%E5%A4%A7%E6%B2%B3%E5%86%85%E8%96%AB%E3%81%AE%E3%81%8A%E9%87%91%E3%81%AE%E5%AD%A6%E3%81%B3%E3%83%A9%E3%82%B8%E3%82%AA-by-voicy/id1526275087?uo=2)
- 経理×AIや現役経理を軸にした音声番組は、検索では確認できなかった。

**Udemy**（数字は検索結果の要約に出ていたもの。講座ページは開けていない）
- 「【生成AI x ビジネス活用】生成AIを使った業務効率化を始めたい人が最初に受講するコース」：評価4.1（2,370件）、受講者11,953人 — [Udemy](https://www.udemy.com/course/gen-ai-biz/)
- 「【実践的！】いちばんわかりやすい『経理実務』の基本」：評価4.3（952件）、受講者6,328人 — [Udemy](https://www.udemy.com/course/accounting_operations/)
- 「簿記3級とセットで学びたい 経理1年目の教科書｜やさしい実務入門」：評価4.7（57件） — [Udemy](https://www.udemy.com/course/3-1-ewqt/)
- 「プロ経理養成講座 会計編 資金繰りの実務とキャッシュフロー計算書の作成」：評価4.1（32件）、受講者351人 — [Udemy](https://www.udemy.com/course/mnngodmu/)
- 「【現役経理マンが解説】ゼロから始めるExcel｜経理・事務で使える基本操作＆関数マスター」（数字は未確認） — [Udemy](https://www.udemy.com/course/misoexcel1/)
- 「【バックオフィス × ChatGPT】経理・総務・人事・法務が変わる！ChatGPTはじめて講座【初心者向け】」：約1時間の入門講座（受講者数は未確認） — [Udemy](https://www.udemy.com/course/back-office-chatgpt/)
- 「ゴリラと学ぶ！ChatGPT×Makeで中小企業の業務を体系的に自動化する実践コース」（仕訳に特化した内容ではない） — [Udemy](https://www.udemy.com/course/chatgptmake/)
- 検索の範囲では「経理×AIで仕訳を自動化する」ことを正面から扱った Udemy 講座は確認できなかった — [検索結果のまとめ記事](https://ai-kenkyujo.com/software/generative-ai/seiseiai-udemy-osusume-2/)

### Inferences
- X の経理アカウントは上場企業の経理・会計士の肩書きを持つ人が中心で、フォロワーは数千人規模。汎用AIのインフルエンサー（数万〜数十万）とは差が大きい。
- Udemy は「汎用の生成AI」と「AIなしの経理実務」の2つに分かれていて、その間（経理実務×AI）の講座が少ない可能性がある（確認できた範囲での話）。

### Gaps
- X の各アカウントの投稿内容とインプレッション、TikTok の経理あるあるアカウントのフォロワー数、note の有料記事の価格と販売数、Udemy の講座ページの最新数値は、サイトに接続できず確認できていない。note.com・udemy.com・x.com をセッションのネットワーク許可に加えれば再調査できる。

## 5. 発信者のタイプと、信頼され伸びているのは誰か

### Takeaway
発信者は5タイプに分かれる。①現役経理・元経理（あるある・転職）、②会計士・税理士（時事・税務・AIの検証）、③ITコンサル・AI系（汎用の効率化）、④ベンダー公式（CM・Tips）、⑤メディア（PIVOT・NewsPicks）。2026年に一番伸びが目立つのは「②の税理士・会計士がAIで会計ソフトを実際に動かして見せる」タイプ。大きな再生数を取っているのは③。①はAI実務にはまだほとんど入っていない。

### Cited Findings
- ②の伸びの例：荒井悠輔（登録者1,200）が直近30本の中で11.8倍・9.75倍・8.38倍の当たりを続けて出している／NEXTバックオフィス研究所 24.47倍 — [動画](https://www.youtube.com/watch?v=YJRMB3Czl2Q)、[動画](https://www.youtube.com/watch?v=zMA_kDUMk-U)
- ③の規模：ひかりのAI大学は登録者11.8万で70万回級を2本、ダイさん（3.9万）は32万回 — [動画](https://www.youtube.com/watch?v=hV4Yu6RiDmQ)
- ①：経理くまch（8,340）、経理ねこ（3,040）は直近90日の投稿が0〜2本。STUDYJOB（15,700）はExcelショートを毎日のように出している — [動画](https://www.youtube.com/watch?v=ZLoTPE7CpGA)
- ④：freee公式Tips（登録者293）は直近90日に30本出しているが、中央値は438回 — [動画](https://www.youtube.com/watch?v=hHtQPFjufqQ)
- 信頼のしかた：大手AI系の動画には「AIに丸投げはいかがなものか」「別のAI使ってませんか？」といった不信感のコメントがいいねを集めている。経理の内容そのものへの反論は、実務を知る税理士事務所職員などから来ている — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgzUpmxWyHVE0TXSI814AaABAg)、[コメント](https://www.youtube.com/watch?v=QCSe9KCgUZ0&lc=Ugw5J6B4nZNM_B3u7sl4AaABAg)

### Inferences
- 「資格や実務経験という裏付け」と「AIを実際に動かして見せる」の両方を持つ発信者が強い。現役経理（会社員）はセキュリティや社内規程の都合で実画面を出しにくいことが、①がAI実務に入っていない一因かもしれない（推測）。

### Gaps
- 登録者数の推移（伸び）は今回1時点しか取っていないので、チャンネルの成長率はわからない。

## 6. ギャップ：需要はあるのに質の高い発信者が少ないテーマ

### Takeaway
需要（コメント・伸び率）に対して供給が薄いのは次の5テーマ。(1) 経理データ×AIのセキュリティと社内ルール、(2) ひとり経理・中小企業向けの「現実的なAI導入」（費用・紙・例外処理まで込み）、(3) 会計ソフト×AIエージェントの「失敗・確認込み」の実務検証、(4) AI時代の経理キャリア（若手・未経験・2〜3年目）、(5) 汎用AI×Excelを経理の業務（月次・照合・仕訳チェック）に寄せた網羅型の動画。

### Cited Findings
- (1) 「情報セキュリティ面の注意点を説明している動画はあまり見た事ないです」というコメント。同じ趣旨の質問が、いいね22の質問を含め複数の動画に出ている — [コメント](https://www.youtube.com/watch?v=NmSUp4Gezc8&lc=UgwtnDfx3K0ziim9GUZ4AaABAg)
- (2) ひとり経理の不正リスクの告白にいいね40。供給側は「ひとり経理」検索で18本だけ。中小・ひとり経理向けのAI動画は登録者100人未満のチャンネル（DX課 登録者0「経理担当が急に辞めたら？」7回、久保田尚孝「経理を、ひとりで抱えていませんか。」46回）に限られている — [コメント](https://www.youtube.com/watch?v=tLmfytP2R9A&lc=Ugw7Yh_b-Dv-6j6SLy94AaABAg)、[動画](https://www.youtube.com/watch?v=-NuXpYEqmsk)
- (3) 会計ソフト×AIの実演は小さいチャンネルでも伸び率10〜120倍（マネーフォワード×Claude Code 122倍、弥生×Claude Opus 5.5 11.8倍）。一方で「トークン消費と仕訳量が釣り合うのか」「誤学習のリスク」という質問には答えが出ていない — [動画](https://www.youtube.com/watch?v=MMWj5gyISRc)、[コメント](https://www.youtube.com/watch?v=tTcRhglITeQ&lc=UgzO6hYIRov6dCFUCRR4AaABAg)
- (4) 将来性・なくなる系は長尺の中央値78,916回（ただし3本）。ミライ経理の68,910回以外に強い動画がなく、「28卒です。経理って今後なくなると思いますか？」「経理2年生だけど…この先は希望なし」という声がある — [動画](https://www.youtube.com/watch?v=OcHIwTpRvMA)、[コメント](https://www.youtube.com/watch?v=BTvIoxjq8OQ&lc=UgwfflYO5MThxlCm0h54AaABAg)
- (5) 汎用AI×Excelの【職種別】動画は646,137回・76倍。経理業務に絞った同じ型（泥臭コンサル「Copilotだけで経理のExcel業務はどこまで自動化できるのか」）は2,981回・1.69倍で、量・質ともにまだ足りない — [動画](https://www.youtube.com/watch?v=JoK4GGZ9JVQ)、[動画](https://www.youtube.com/watch?v=52u3tOPqiLU)
- 混んでいるテーマ：新しいモデルの速報（2026-09に経理×AIのタイトルが17本、税理士・AI系が同じ週に同じモデルを検証）、Excel神ワザショート（STUDYJOB・ベンダー・個人が多数） — 出典は `youtube_data/theme_stats.md`

### Inferences
- 一番再現しやすいのは「現役経理の目線 × 具体的な会計ソフト（freee／マネーフォワード／弥生） × AIエージェント × 人が確認するところとセキュリティ設定まで見せる」実務シリーズ。小さいチャンネルでも当たりが出ているテーマに、コメントで求められている安全面と費用面を足す形。
- キャリア面では「AI時代に経理の若手が今身につけるべきこと」を、転職エージェント型ではない立場で語る人がほとんどいない。転職の導線（たぬ吉・経理くま）と差別化できる余地がある。
- 経理DXの一般論（「経理DXとは？」）は伸び率の中央値1.26倍で当たりは0本。一般論の解説は避けた方がよい。

### Gaps
- 検索ボリューム（Googleトレンドなど）は今回取っていないので、「需要」はコメントと伸び率から見た推定にとどまる。
- freee・マネーフォワードの操作解説、インボイス・電帳法の供給状況は、API の上限で未取得。翌日以降に `youtube_data/keywords.txt` の未取得分だけ再実行すれば埋められる。
