# 日本の祝日API

日本の祝日を取得できるAPIです。

[国民の祝日について - 内閣府](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html) をデータソースとしています。

Inspired by [Holidays JP API](https://holidays-jp.github.io/)

## 制限
APIが返せるのは 1995年〜現在 までの範囲の祝日です。（データソースに依存）

## Examples

詳細は [APIドキュメント](https://jp-holiday.net/swagger-ui) を参照ください。

### 最近の祝日一覧を取得
去年・今年・来年（データがあれば）の祝日一覧を返します。

```sh
$ curl 'https://jp-holiday.net/api/v1/list'
```

```json
{
  "2022-01-01": "元日",
  "2022-01-10": "成人の日",
  "2022-02-11": "建国記念の日",
  "2022-02-23": "天皇誕生日",
  "2022-11-23": "勤労感謝の日",
  // ...
  "2023-01-01": "元日",
  "2023-01-02": "休日",
  "2023-01-09": "成人の日",
  "2023-11-03": "文化の日",
  // ...
  "2023-11-23": "勤労感謝の日",
  "2024-01-01": "元日",
  "2024-01-08": "成人の日",
  // ...
  "2024-11-04": "休日",
  "2024-11-23": "勤労感謝の日"
}
```

### 特定の年の祝日一覧を取得

特定の年の祝日一覧を返します。

```sh
# 2023 の祝日を取得
$ curl 'https://jp-holiday.net/api/v1/list/2023'
```

```json
{
  "2023-01-01": "元日",
  "2023-01-02": "休日",
  "2023-01-09": "成人の日",
  "2023-02-11": "建国記念の日",
  "2023-02-23": "天皇誕生日",
  "2023-03-21": "春分の日",
  "2023-04-29": "昭和の日",
  "2023-05-03": "憲法記念日",
  "2023-05-04": "みどりの日",
  "2023-05-05": "こどもの日",
  "2023-07-17": "海の日",
  "2023-08-11": "山の日",
  "2023-09-18": "敬老の日",
  "2023-09-23": "秋分の日",
  "2023-10-09": "スポーツの日",
  "2023-11-03": "文化の日",
  "2023-11-23": "勤労感謝の日"
}
```

### 全期間の祝日一覧を取得

特定の年の祝日一覧を返します。

```sh
$ curl 'https://jp-holiday.net/api/v1/list/all'
```

```json
{
  "1955-01-01": "元日",
  "1955-01-15": "成人の日",
  "1955-03-21": "春分の日",
  "1955-04-29": "天皇誕生日",
  // ...
  "2024-10-14": "スポーツの日",
  "2024-11-03": "文化の日",
  "2024-11-04": "休日",
  "2024-11-23": "勤労感謝の日"
}
```

### 特定の日が祝日かどうか判定する
特定の日にちが祝日かどうか判定します。

#### 祝日の場合

```sh
# 2023/09/23 は 秋分の日
$ curl 'https://jp-holiday.net/api/v1/holiday/2023/09/23'
```

```json
{
  "holiday": true,
  "name": "秋分の日"
}
```

#### 祝日でない場合

```sh
# 2023/09/24 は祝日でない
$ curl 'https://jp-holiday.net/api/v1/holiday/2023/09/24'
```

```json
{
  "holiday": false,
  "name": ""
}
```

## 利用規約
[利用規約](https://jp-holiday.net/documents/term-of-service) に同意いただければ、個人・法人・商用問わずご利用いただけます。

## ライセンス
[MIT](/LICENSE)
