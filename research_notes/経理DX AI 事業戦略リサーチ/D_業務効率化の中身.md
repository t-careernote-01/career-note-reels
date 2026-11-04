# D. 経理業務効率化の中身（業務棚卸し・自動化手段・ツール・生成AI・効果実績）

調査日: 2026-11-04。調査方法: WebSearch中心（約15回）。bill-one.com、aurant-technologies.com はこのセッションのネットワーク制限で本文を取得できなかった（取得するにはセッションのネットワーク設定でこれらのドメインを許可する必要がある）。そのため多くの数値は検索結果の要約による二次確認で、一次ページで裏取りしていない。記事を書く前に、各URLで一次ページを確認すること。

---

## 1. 経理業務の棚卸しと、業務ごとの所要時間データ

### Takeaway
「経理の業務別の時間配分」を全国規模で示した公的・業界統計は、今回の調査では見つからなかった。手に入る定量データは、インボイス制度で増えた工数（月8.5〜11.9時間／人）、月次決算の日数（実務では7〜10営業日が多く、改善後に5営業日になった事例）、請求書の目視確認が約7割、といった断片的なものに限られる。

### Cited Findings
- 社員80名規模の会社の経理担当者が「理想は5営業日で締めたいが、実際は7〜8営業日かかっている」と話している（OBC記事、2025年9月。1社の声で統計ではない）— [OBC 勘定奉行 acfield](https://www.obc.co.jp/acfield/list/post021)
- マネーフォワード社内の決算早期化プロジェクトで、財務会計の締めと部門別予実を含む管理会計の締めが10営業日から5営業日に短縮された — [マネーフォワード クラウドERP 解説（2026年4月更新）](https://biz.moneyforward.com/erp/basic/1326/)
- ROBOT PAYMENT が月次決算を9営業日から5営業日に早期化した事例をセミナーで紹介している — [税務研究会 セミナー案内（2022年）](https://www.zeiken.co.jp/zeikenpress/press/0014pp20220422)
- 東証は決算短信の開示を期末後45日以内が適当、30日以内がより望ましいとしている（上場企業の年次決算の時間軸）— [税務研究会](https://www.zeiken.co.jp/zeikenpress/press/0014pp20230201)
- インボイス制度の開始後、経理担当者が月次決算にかける時間は1名あたり月平均11.9時間増えた。適格請求書の要件確認は「経理担当者による目視確認」が約7割（2023年調査）— [BCN Retail（2023年11月）](https://www.bcnretail.com/market/detail/20231121_379856.html)
- Sansanの調査（請求書業務に携わる1,000人、うち経理部門700人。2024年1月発表）では、制度施行から3カ月後も3分の1以上が課題を抱えており、課題のある企業では経理の業務時間が1人あたり月平均8.5時間増えた — [IT Leaders / impress](https://it.impress.co.jp/articles/-/25882?page=2)
- LayerX（バクラク）の調査（2023年9月、827人、うち経理416人）: 経費精算の業務量が「増加する」と答えた経理担当者は53.6%。業務時間が増えた115人の平均は約1.46倍 — [Web担当者Forum（2023年11月）](https://webtan.impress.co.jp/n/2023/11/21/46010)、[バクラク ニュース](https://bakuraku.jp/news/20231027/)
- 自治体の例では、支出命令と請求書の突合チェックに1件約3分、月約400件かかっている（突合作業の工数の目安）— [奈良市資料](https://www.city.nara.lg.jp/uploaded/life/270435_605310_misc.pdf)
- 月次決算は月末から月初にかけて締めと決算作業が集中し、負担が偏る — [freee 解説](https://www.freee.co.jp/kb/kb-accounting/monthly-closing/)
- 手入力による転記エラー率は約0.5〜1%とする記述があるが、出典は示されていない — [issoh コラム](https://www.issoh.co.jp/column/details/11076/)

### Inferences
- 講座やコンテンツで使う業務棚卸しは、次の頻度別の枠組みにまとめるのが実用的（一般的な経理実務の整理で、特定の出典はない）。
  - 日次: 現預金管理、仕訳入力、証憑の受領と保管（電帳法対応）、経費申請のチェック
  - 月次: 請求書の発行、受領した請求書の処理、支払（振込データの作成）、入金消込、給与計算、月次決算（締め・残高確認・試算表）、管理会計レポート・予実
  - 年次: 年次決算、法人税・消費税の申告支援、固定資産の管理と償却資産申告、年末調整、法定調書、予算策定
- 定量データが「インボイスで増えた時間」と「月次決算の日数」に偏っているため、講座では「自社の業務時間を測る棚卸しシート」を受講者に記入させるワークが、根拠のない一般論の数字より説得力を持つと考えられる。
- 各社の事例では「月次決算を10営業日から5営業日へ」がよくある到達目標になっている。

### Gaps
- 業務別の時間配分（例: 仕訳◯%、消込◯%）を示す信頼できる調査は見つからなかった。Bill Oneの「経理の働き方 2026」ホワイトペーパーに含まれている可能性があるが、ドメイン制限で取得できなかった。
- 中小企業の月次決算日数の平均値を示す統計は見つからなかった。
- 年末調整、固定資産、給与の所要時間についての定量データは得られなかった。

---

## 2. 自動化しやすい業務と、その手段（クラウド会計・請求書受領・経費精算・AI-OCR・RPA・生成AI・AIエージェント）

### Takeaway
自動化の効果が大きいのは「紙やPDFを入力・突合する作業」（請求書受領、経費精算、振込、仕訳の起票）。2025〜2026年には各ベンダーが「AIエージェント」と名のつく機能を相次いで出している（freee: 税理士事務所向けの4種のエージェントとAgent Hub、マネーフォワード: 連結決算レビューエージェント、TOKIUM: 経理AIエージェント9体、バクラク: AI申請レビュー）。

### Cited Findings
**AIエージェント機能（2025〜2026年の発表）**
- freee は「freee Advisor Day 2026」（2026年8月28日開幕）で、税理士事務所向けの「freee顧問先管理 | AIエージェント」を公開した。資料回収から決算申告までを一気通貫で支援し、記帳・ルール整備・月次チェック・申告書チェックの4種のエージェントで構成される。2026年9月15日から有償提供の予定。同時に、士業向けのAIエージェント開発基盤「freee Agent Hub」の正式提供も始まった（Windows・macOS対応）— [digitalpr.jp プレスリリース](https://digitalpr.jp/r/141093)、[Mac Fan](https://macfan.book.mynavi.jp/business/article/114320/)
- freee は2026年5月の決算説明で「freee Agent Hub」の立ち上げを挙げている — [Quartr freee Q3 2026](https://quartr.com/events/freee-k-k-4478-q3-2026_FLvF9rq8)
- マネーフォワードは2025年4月2日に「Money Forward AI Vision 2025」を発表した。AIエージェント、AIエージェントプラットフォーム、AXコンサルティングを順次提供し、経費・会計・人事などの各領域でエージェントを展開する方針 — [マイナビニュース（2025年4月2日）](https://news.mynavi.jp/techplus/article/20250402-3172179/)
- マネーフォワードは2026年8月7日、「マネーフォワード クラウド連結会計」でAIエージェント「連結決算レビューエージェント」の提供を始めた。複数のチェック観点をAIがレポートにまとめ、見落としを防ぐ（見出しと要旨のみ確認）— [EnterpriseZine](https://enterprisezine.jp/news/detail/21774)
- 中小企業向けの経理BPO「マネーフォワード おまかせ経理」は、AIなどを使う新しいBPOサービスとして2025年6月に正式に追加された — [みんかぶ](https://minkabu.jp/news/4255553)
- 個人のブログには、2026年4月に「マネーフォワード AI Cowork」（バックオフィス向けの自律AI、7月開始予定）が発表されたという記述があるが、公式発表は確認できなかった — 未確認のため参考扱い
- TOKIUM は2025年5月に「経理AIエージェント」（AIと専門スタッフが連携する形）を発表し、第1弾の「TOKIUM AI出張手配」を2025年7月1日に提供開始した — [クラウドWatch](https://cloud.watch.impress.co.jp/docs/news/2016429.html)、[マイナビニュース（2025年6月25日）](https://news.mynavi.jp/techplus/article/20250625-3362445/)
- TOKIUM の求人票（2026年4月更新）には、「TOKIUM AI経費承認」など9体のAIエージェントをリリース済みとある。また、東証グロースへの上場予定日は2026年11月25日（変更の可能性あり）— [ビズリーチ求人](https://www.bizreach.jp/jobs/5265431/)、[トレーダーズ・ウェブ](https://www.traders.co.jp/ipo/664A)
- バクラクの「AI申請レビュー」（AIエージェント）を導入したタイミーは、経費精算の月次締め作業を1営業日短縮した — [バクラク導入事例一覧](https://bakuraku.jp/case/?paged=5)

**AI-OCR・RPA**
- NTTコミュニケーションズは、AI-OCRとUiPath（RPA）で紙の請求書の読み取りと業務システムへの入力を自動化し、3万件の請求書を自動処理して年間4,000時間超の稼働を削減した（大企業の事例）— [UiPath 事例PDF](https://www.uipath.com/hubfs/ja/resource/pdf/UiPath-NTTCommunications.pdf)
- パナソニック ホームズは、RPA・VBA・グループウェアを組み合わせて経理業務130プロセスを効率化し、年間15,000時間を削減した — [Yoom ブログ（RPA経理事例のまとめ）](https://lp.yoom.fun/blog-posts/rpa-accounting-case-studies)
- AI-OCRとRPAの組み合わせは、OCRの誤読、元データの不備、画面レイアウトの変更などで処理が止まることがあり、例外処理の体制が必要 — [Yoom ブログ](https://lp.yoom.fun/blog-posts/rpa-accounting)

**生成AIと会計SaaSの連携**
- freee MCP と Claude を組み合わせて仕訳を自動化する手順が、民間の解説記事で紹介されている — [start-link](https://start-link.jp/hubspot-ai/ai/freee-ai/freee-mcp-automated-journal)
- ChatGPT などの出力を会計ソフトへ転記したりアップロードしたりする手間、複数ツールを行き来する手間が残りやすい — [Yoom ブログ](https://lp.yoom.fun/blog-posts/how-to-automatically-journalize-with-chatgpt)

### Inferences
- 自動化しやすさの順位（事例と構造から推定）:
  1. 銀行明細・カード明細の取込と自動仕訳（クラウド会計の標準機能）
  2. 請求書の受領・データ化・振込データの作成（Bill One、バクラク、TOKIUM、invox）
  3. 経費精算の申請チェック（AI申請レビュー、AI経費承認）
  4. 入金消込（債権管理SaaS）
  5. 月次チェックと決算レビュー（AIエージェントが出始めた段階）
  6. 予算・管理会計・差異分析（生成AIで下書き。人の判断が中心）
- 2026年のAIエージェントは「チェック・レビュー型」（申請レビュー、月次チェック、連結決算レビュー）が中心。完全な自律処理ではなく、人が最終確認する形の設計になっている。
- 大企業のRPA事例（年4,000〜15,000時間）は中小企業にそのまま当てはまらない。中小企業ではSaaSの標準機能とExcel・GASで足りるケースが多いと考えられる。

### Gaps
- Excel（Power Query・マクロ）、Google Apps Script、Copilot in Excel を経理で使った定量事例は、今回の検索では見つからなかった。
- 弥生の2025〜2026年のAI機能（弥生会計 Next など）の詳細は確認できなかった。
- Bill One とバクラクの2026年のAIエージェント発表について、一次の詳細は取得できなかった。

---

## 3. 中小企業向け料金（主要ツール）

### Takeaway
クラウド会計（法人）は月2,000〜9,000円（年払い）が中心価格帯。請求書受領と経費精算は「要見積もり」が多く、公開価格は限られる。補助金は「デジタル化・AI導入補助金」（旧IT導入補助金）のインボイス枠で最大4/5。

### Cited Findings
- **freee会計（法人）**: ひとり法人 2,980円/月、スターター 5,480円/月〜、スタンダード 8,980円/月〜、アドバンス 39,780円/月〜（いずれも年払い時）。月払いの場合はスターター 7,280円、スタンダード 11,980円。これに従量課金がかかる（ITreviewでは経理・経営者相当のユーザー300円/月、経費精算1人300円/月、受発注書類の送付1件95円）— [freee 公式料金](https://www.freee.co.jp/pricing/)、[freee 新設法人向け料金](https://www.freee.co.jp/accounting/new-corporation/pricing/)。比較記事ではスターター 3,980円、スタンダード 5,980円、プレミアム 39,800円とする記述もあり、旧価格の可能性が高い — [aurant-technologies](https://aurant-technologies.com/blog/freee-vs-moneyforward-vs-yayoi-comparison/)
- **マネーフォワード クラウド会計（法人）**: ひとり法人 2,480円/月、スモールビジネス 4,480円/月、ビジネス 6,480円/月（年払い時）— [ITreview 価格](https://www.itreview.jp/products/mfcloudkaikei/price)。別の検索結果ではスモールビジネス 2,480円とも読める要約があり、比較記事にも Small Business 2,980円、Business 4,980円、Business Plus 7,980円という異なる数字がある — [aurant-technologies](https://aurant-technologies.com/blog/freee-vs-moneyforward-vs-yayoi-comparison/)。情報が食い違っているため、公式ページで要確認。
- **マネーフォワード クラウド経費**: 基本料金とアクティブユーザー数による従量課金 — [お名前.com 比較記事](https://www.onamae.com/business/article/162026/)
- **弥生**: 比較記事では「弥生会計クラウド」のセルフプランを年額26,000円とする記述がある — [aurant-technologies](https://aurant-technologies.com/blog/freee-vs-moneyforward-vs-yayoi-comparison/)。「弥生会計オンライン」は2026年4月時点で新規受付を終了したという記述（[kigyolog](https://kigyolog.com/service.php?id=1)）と、クラウド版「弥生会計 Next」に移行しているという記述（[atsoho](https://atsoho.com/blog/fintech-sole-proprietor-online-how-to-choose)）がある。
- **楽楽精算**: ITreviewの比較表に「基本月額費用 30,000」とある（条件は不明）— [ITreview](https://www.itreview.jp/products/invox-keihiseisan/competitors/alternatives)。公式の公開価格は確認できなかった。
- **invox受取請求書**: ミニマム 1,078円/月、ベーシック 10,780円/月、プロフェッショナル 32,780円/月。受領する枚数やオプションで変動する — [ITreview / BOXIL 検索結果](https://www.itreview.jp/products/invoice-post/price)
- **TOKIUM経費精算**: 価格は非公開。**Bill One**: 初期費用と年額費用の構成で、要見積もり — [BOXIL 比較](https://boxil.jp/mag/a11281/)
- **バクラク**: 公開価格は確認できなかった（要見積もりと推定）— [ITreview バクラク経費精算](https://www.itreview.jp/products/bakurakukeihiseisan/competitors/alternatives)
- **補助金**: 令和7年度補正予算の事業から、名称が「デジタル化・AI導入補助金（旧IT導入補助金）」に変わった — [中小企業庁 概要PDF](https://www.chusho.meti.go.jp/koukai/yosan/r8/digital_ai_summary.pdf)。インボイス枠の補助率は最大4/5（小規模事業者）で、会計・受発注・決済のソフトとPC・POSレジなどが対象 — [補助金ポータル](https://hojyokin-portal.jp/columns/degital_ai_invoice)、[freee 解説](https://freee.co.jp/kb/kb-accounting/it-shien/)。2026年の公募は3月30日開始で、締切は5月12日、6月15日、7月21日、8月25日（2026年11月時点で後続回があるかは未確認）— [ネットショップ担当者フォーラム（2026年5月1日）](https://netshop.impress.co.jp/e/2026/05/01/16018)

### Inferences
- 従業員10〜50名の中小企業が「会計 + 請求書受領 + 経費精算」を揃えると、月数万円規模になると見込まれる（会計 5,000〜10,000円 + 受領・経費 10,000〜30,000円以上。公開価格からの推定）。補助金で初期負担を下げられる点は、講座の訴求材料になる。

### Gaps
- バクラク、Bill One、TOKIUM、楽楽精算の公式価格は、非公開か未取得。
- 2026年度の補助上限額（類型別）は確認できなかった。

---

## 4. 経理に特化した生成AIの活用例・プロンプト・限界とリスク

### Takeaway
生成AIは、仕訳と勘定科目の「候補を出す」補助、Excel関数とVBAの生成、文書作成（規程、メール、コメント）に向いている。一方で、似た勘定科目の取り違え、税区分の誤り、機密情報の扱いがリスクになる。調査では「効率が上がった」と感じる回答は6割前後あるが、「意思決定の質まで上がった」は2割にとどまる。

### Cited Findings
- KPMGジャパン「CFOサーベイ 2026/27」（上場企業のCFO対象、2026年10月）: 生成AIやAIエージェントで業務効率が上がったと感じる企業は60%以上、意思決定の質が上がったと感じる企業は20%。71%が人材・スキル不足を課題に挙げ、AI投資を拡大する企業は90% — [KPMG プレスリリース](https://kpmg.com/jp/ja/media/press-releases/2026/10/cfo-survey-2026.html)
- KPMG「AI in Finance 2026」（20か国、13業種、CFO・経理財務リーダー1,013名）: 経理財務でのAI本格活用は2024年比で2倍超 — [KPMG レポートPDF](https://assets.kpmg.com/content/dam/kpmgsites/jp/pdf/2026/jp-kpmg-global-ai-in-finance-report.pdf)
- KPMG（2025年2月）: 日本で財務報告にAIを使う企業は、6か月で31%から39%に増えた — [AIsmiley](https://aismiley.co.jp/ai_news/kpmginternational-aifinancial/)
- 従業員50〜500名の企業の経理・総務担当者104名の調査（2025年2月）: 生成AIを毎日使う人は15.4%、たまに使う人は29.8%。業務負担が減ったと感じる人は78.8%、セキュリティに不安がある人は36.2%。主な用途は文章の要約と社内文書の作成 — [IT Leaders](https://it.impress.co.jp/articles/-/29305)（サンプル数が小さく、対象が経理専任に限らない点に注意）
- 仕訳の補助では、通信費と支払手数料、会議費と接待交際費のような意味の近い科目をAIが取り違えることがある。軽減税率などの税区分はプロンプトで明示し、登録後に検証することが推奨される — [claudelab](https://claudelab.jp/articles/689)、[start-link](https://start-link.jp/hubspot-ai/ai/freee-ai/freee-mcp-automated-journal)
- 税務判断はAIに任せきりにせず、判断業務では「候補を出させる」使い方が基本。57.5%の企業が社内のAI利用規程を整備できていないという調査が紹介されている — [SHIFT AI 経営](https://ai-keiei.shift-ai.co.jp/chatgpt-keiri/)
- 経理向けChatGPTプロンプト集は民間メディアに多数ある — [uravation](https://uravation.com/media/chatgpt-accounting-prompts/)（研修事業者による宣伝的な内容を含む）
- KPMGはAIによる仕訳分析（監査・不正検知向け）の事例を公開している — [KPMG（2026年2月）](https://kpmg.com/jp/ja/insights/2026/02/ai-je-analysis-clientstory.html)

### Inferences
- 講座で扱いやすいユースケース（リスクの低い順）:
  1. メール・社内通知の文案（支払遅延の督促、経費ルールの周知）
  2. 規程の雛形（経費精算規程、電帳法の事務処理規程）。最後は専門家が確認する
  3. Excel関数・VBA・GASのコード生成とエラーの解説
  4. 予実の差異分析コメントの下書き（数値は人が入れる）
  5. 決算資料・会議資料の要約
  6. 勘定科目と仕訳の候補提示（必ず人がチェック）
- 個人名・取引先名・口座情報をマスキングするルールと、法人向けプラン（学習に使われない設定）の選び方は、講座の必須単元にすべき。
- 差異分析向けプロンプトの具体例は、一次ソースが乏しかったため、講師が自分で例を作る必要がある。

### Gaps
- 差異分析コメント生成の定量効果を示す事例は見つからなかった。
- Copilot（Microsoft 365）やGeminiを経理に導入した日本国内の定量事例は見つからなかった。

---

## 5. 定量効果のある事例

### Takeaway
ベンダー事例では「月次締めを1〜7営業日早める」「振込作業を3日から数分に」「工数を半分以上削減」「年1,116万円のコスト削減」などが並ぶ。いずれも自己申告の数値で、導入前の状態に依存する。

### Cited Findings
- NSグループ（カラオケパセラ）: バクラク導入で年間1,116万円のコスト削減、月次締めを7日早期化 — [バクラク導入事例](https://bakuraku.jp/case/?paged=7)
- タイミー: AI申請レビューで、経費精算の月次締めを1営業日短縮 — [バクラク導入事例](https://bakuraku.jp/case/?paged=5)
- フォトラクション（1人経理）: 領収書回収の効率化と仕訳の自動化で、月次決算の工数を半日分削減 — [バクラク導入事例](https://bakuraku.jp/case/photoruction/)
- Morght: 振込作業が実質約3日から数分になり、月次決算の経理処理時間は10分の1以下 — [バクラク導入事例](https://bakuraku.jp/case/?paged=7)
- 坂善商事は業務工数を半分以上削減、FC東京は1人あたりの残業を最大10時間削減 — [バクラク導入事例](https://bakuraku.jp/case/tag/issue-04)
- バクラクのセミナーで「請求書処理の工数90%削減」（MUFG関連）を掲げている（宣伝資料）— [バクラク セミナー](https://bakuraku.jp/seminar/invoice_mufg/)
- マネーフォワード社内: 締めを10営業日から5営業日へ — [マネーフォワード](https://biz.moneyforward.com/erp/basic/1326/)
- NTTコミュニケーションズ: AI-OCRとRPAで年4,000時間超を削減 — [UiPath](https://www.uipath.com/hubfs/ja/resource/pdf/UiPath-NTTCommunications.pdf)。パナソニック ホームズ: 年15,000時間を削減 — [Yoom](https://lp.yoom.fun/blog-posts/rpa-accounting-case-studies)
- NTT東日本 千葉事業部: AI-OCRとRPAで、個人住民税の帳票処理を年間約602時間削減（行政系の帳票）— [Yoom](https://lp.yoom.fun/blog-posts/rpa-accounting-case-studies)

### Inferences
- 中小企業向けに一番伝わる訴求は「月次締めの日数を減らす」と「振込・請求書入力の時間ゼロ化」。年間時間の大きな数字は大企業の事例なので、伝えるときは区別する必要がある。

### Gaps
- 中小企業庁・IT導入補助金の効果検証（労働生産性の伸びなど）の公式データは、今回取得できなかった。
- ITreviewやBOXILのレビューで定量効果を集計したデータは得られなかった（個別レビューに「月次決算の早期化」という声がある程度）— [BOXIL レビュー](https://boxil.jp/service/6583/reviews/58567/)

---

## 6. 非IT経理担当者に講座で教えられる範囲と、コンサルが必要な範囲

### Takeaway
直接の調査データはないが、今回の材料から見ると、SaaSの標準機能の使い方、生成AIのプロンプトとリスク管理、Excelの効率化は講座で教えられる。一方、複数SaaSと会計の連携設計、RPAやAPI・MCPの連携、内部統制や電帳法を含む業務の再設計、AIエージェントの導入は、コンサルや伴走支援が必要な領域と判断できる。

### Cited Findings
- 上場企業のCFOの71%が、AI活用の課題に人材・スキル不足を挙げている — [KPMG CFOサーベイ 2026/27](https://kpmg.com/jp/ja/media/press-releases/2026/10/cfo-survey-2026.html)
- 中小企業の経理・総務で生成AIを毎日使う人は15.4%にとどまる（2025年2月）— [IT Leaders](https://it.impress.co.jp/articles/-/29305)
- RPAとAI-OCRの運用では例外処理の体制が必要 — [Yoom](https://lp.yoom.fun/blog-posts/rpa-accounting)
- マネーフォワードは「AXコンサルティング」を、TOKIUMは「AIと専門スタッフ」の組み合わせを、マネーフォワードはBPO（おまかせ経理）を提供している。ベンダー自身が、ツールだけでなく人による支援を併売している — [マイナビニュース](https://news.mynavi.jp/techplus/article/20250402-3172179/)、[クラウドWatch](https://cloud.watch.impress.co.jp/docs/news/2016429.html)、[みんかぶ](https://minkabu.jp/news/4255553)

### Inferences
- **講座で教えられる範囲**（非IT経理担当者向け）:
  - 業務棚卸しと時間計測のワーク
  - クラウド会計の自動仕訳ルールの作り方、銀行・カード連携
  - 生成AIの安全な使い方（マスキング、法人プラン、出力を検証する手順）と、経理向けプロンプトの型
  - Excel関数・ピボット・Power Query の基本（生成AIに作らせて理解する）
  - 補助金の概要とツール選定のチェックリスト
- **コンサル・伴走が必要な範囲**:
  - 複数SaaS間のデータ連携とマスタ設計、API・MCP・RPAの構築
  - 決算早期化プロジェクト（業務フローと承認フローの再設計）
  - 内部統制、電帳法、インボイスの運用設計
  - AIエージェントの導入と評価（現時点では会計事務所向けが中心）
- 「講座で基礎を教え、個別相談やコンサルにつなげる」二段構えのモデルが、ベンダーの「ツール＋人による支援」と同じ構造で成り立つと考えられる。

### Gaps
- 経理向けAI・DX講座の受講効果や市場規模のデータは、今回は調べていない（別のリサーチ担当の範囲の可能性がある）。
