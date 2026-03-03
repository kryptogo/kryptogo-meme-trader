# KryptoGO Meme Trader

[English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

**ミームコインのゴッドアイ** — 業界初のオールインワン・オンチェーン取引アシスタント。

スマートマネー追跡 · マーケットメーカー分析 · クジラ監視 · シグナルアラート

## なぜ KryptoGO なのか

| 機能 | 説明 | ツール |
|---|---|---|
| **独自クラスター検出** | すべての保有アドレスからクジラクラスターを精密検出。買い集め中か売り抜け中かが一目瞭然 | `analyze_token` |
| **クラスターポジション動向** | 価格横ばい + クラスター保有上昇 = 蓄積（強気）。価格上昇 + クラスター保有減少 = 分配（弱気） | `get_cluster_trends` |
| **隠れポジションの復元** | Jupiter の指値注文や DCA 分割購入による隠れポジションを正確に復元。他ツールでは空と表示されるウォレットの実態を可視化 | `get_dca_limit_orders` |
| **ネットワーク全体の蓄積シグナル** | 第一段階：新規トークンの急速蓄積を捕捉。第二段階：成熟トークンの再蓄積を検出。主力の動向を精密に把握 | `get_signal_dashboard` |
| **包括的アドレスラベル** | スマートマネー、ブルーチップ高収益、クジラ、DEV、スナイパー、バンドル取引など。ラベルカバレッジは Nansen を大幅に上回る | `get_token_wallet_labels` |

### マーケットメーカーの動きを読む

クラスターポジションの変化から、クジラの操作3段階を識別：

| フェーズ | 価格動向 | クラスター保有 | シグナル |
|---|---|---|---|
| **蓄積** | 横ばい推移 | 着実に上昇 | 強気 — クジラが静かに収集中 |
| **ポンプ** | 急上昇 | 高水準維持 | ホールド — クジラはまだ売っていない |
| **分配** | 高値圏を維持 | 下降開始 | 撤退 — クジラが後追い勢に分配中 |

> *人は嘘をつくかもしれないが、オンチェーンデータは嘘をつかない。*

## MCP サーバー

### Claude Code クイックスタート

```bash
claude mcp add kryptogo-meme-trader -e KRYPTOGO_API_KEY=your_key -- uvx kryptogo-meme-trader
```

### 取引機能付き

```bash
claude mcp add kryptogo-meme-trader \
  -e KRYPTOGO_API_KEY=your_key \
  -e SOLANA_PRIVATE_KEY=your_base58_key \
  -e SOLANA_WALLET_ADDRESS=your_wallet \
  -- uvx kryptogo-meme-trader
```

### Claude Desktop / Cursor / Windsurf

```json
{
  "mcpServers": {
    "kryptogo-meme-trader": {
      "command": "uvx",
      "args": ["kryptogo-meme-trader"],
      "env": {
        "KRYPTOGO_API_KEY": "your_key"
      }
    }
  }
}
```

## Skill

### OpenClaw

```bash
npx clawhub install kryptogo-meme-trader
```

### Claude Code

```bash
npx degit kryptogo/kryptogo-meme-trader/skill ~/.claude/skills/kryptogo-meme-trader
```

インストール後、Claude Code を再起動してアクティベートしてください。詳細なドキュメントは [skill/SKILL.md](./skill/SKILL.md) をご覧ください。

## ドキュメント

| | English | 繁體中文 | 简体中文 |
|---|---|---|---|
| 製品ガイド | [User Guide](https://kryptogo.notion.site/Product-Guide-EN-26c3499de8a28179aafacb68304458ea) | [使用手冊](https://kryptogo.notion.site/kryptogo-xyz-usage-guide) | [使用手册](https://kryptogo.notion.site/kryptogo-xyz-productguide-zhcn) |
| ホワイトペーパー | [PDF](https://wallet-static.kryptogo.com/public/whitepaper/kryptogo-xyz-whitepaper-v1.0.pdf) | [白皮書](https://kryptogo.xyz/whitepaper) | [白皮书](https://kryptogo.xyz/whitepaper) |

## 前提条件

- [kryptogo.xyz/account](https://kryptogo.xyz/account) から API キーを取得
- Python 3.10+

## 環境変数

| 変数 | 必須 | 説明 |
|------|------|------|
| `KRYPTOGO_API_KEY` | はい | kryptogo.xyz から取得した API キー |
| `SOLANA_PRIVATE_KEY` | いいえ | 取引用の Base58 秘密鍵 |
| `SOLANA_WALLET_ADDRESS` | いいえ | ポートフォリオ/取引用のウォレットアドレス |

## 利用可能なツール (22)

### 分析 (13)

| ツール | 説明 |
|--------|------|
| `get_token_overview` | 価格、時価総額、メタデータを含むトークンの総合概要を取得 |
| `analyze_token` | クラスター分析 — 関連ウォレットをグループ化してインサイダー保有を可視化（無料版：最初の2クラスターのみ） |
| `get_cluster_trends` | スマートマネークラスターのトレンドと動向を分析 |
| `get_balance_history` | ウォレットの残高履歴を追跡 |
| `get_balance_increase` | 残高が大幅に増加したウォレットを特定 |
| `get_top_holders_snapshot` | トークンの上位ホルダーの現在のスナップショットを取得 |
| `get_historical_top_holders` | 上位ホルダーの時系列データを表示 |
| `get_fresh_addresses` | トークンを蓄積している新規ウォレットを検出 |
| `get_dca_limit_orders` | トークンの DCA および指値注文アクティビティを照会 |
| `get_price_chart` | OHLCV 価格チャートデータを取得 |
| `get_batch_prices` | 1 回の呼び出しで複数トークンの価格を取得 |
| `get_cluster_connections` | クラスター内のウォレット間の接続関係をマッピング |
| `get_wallet_assets` | ウォレットの全トークン保有を一覧表示 |

### ディスカバリー (3)

| ツール | 説明 |
|--------|------|
| `get_trending_tokens` | チェーン横断の現在のトレンドトークンを取得 |
| `get_signal_dashboard` | ネットワーク全体の蓄積シグナル — インサイダーが買い増し中のトークン（Pro/Alpha限定） |
| `get_signal_history` | 過去の取引シグナルを閲覧 |

### ポートフォリオ (2)

| ツール | 説明 |
|--------|------|
| `get_account_info` | API 使用量とプラン情報を含むアカウント情報を取得 |
| `get_portfolio` | 損益追跡付きのウォレットポートフォリオを表示 |

### 取引 (1)

| ツール | 説明 |
|--------|------|
| `swap_tokens` | Solana 上でトークンスワップを実行 |

### ラベルとリスク (3)

| ツール | 説明 |
|--------|------|
| `get_wallet_labels` | ウォレットアドレスのラベルとタグを取得 |
| `get_token_wallet_labels` | トークンに関連するラベル付きウォレットを取得 |
| `check_rug_risk` | トークンのラグプルリスクを評価 |

## 対応チェーン

| チェーン | chain_id | 取引 |
|----------|----------|------|
| Solana | 501 | 対応 |
| BSC | 56 | 分析のみ |
| Base | 8453 | 分析のみ |
| Monad | 143 | 分析のみ |

## プラン

| プラン | 1日あたりの API コール数 | 取引手数料 | シグナル |
|--------|--------------------------|------------|----------|
| Free | 100 | 1% | なし |
| Pro | 1,000 | 0.5% | あり |
| Alpha | 5,000 | 0% | あり |

## セキュリティ

すべてのトランザクション署名はお使いのローカルマシン上で実行されます。秘密鍵が KryptoGO サーバーや第三者に送信されることはありません。MCP サーバーはローカルでトランザクションを構築し、署名済みトランザクションのみを Solana RPC エンドポイントに送信します。

## ライセンス

MIT
