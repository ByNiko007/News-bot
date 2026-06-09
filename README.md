# 📰 Kripto & Səhm Bazarı Xəbər Botu

## Xəbər Mənbələri
**Kriptovalyuta:** CoinDesk, CryptoNews, Cointelegraph, Bitcoin Magazine  
**Səhm Bazarı:** Reuters, MarketWatch, Investing.com, Yahoo Finance

---

## ⚙️ Quraşdırma

### 1. Tələblər
- Python 3.10+
- Telegram hesabı

### 2. Bot Token Al
1. Telegramda [@BotFather](https://t.me/BotFather) aç
2. `/newbot` yaz
3. Botuna ad ver
4. Token al (məs: `123456:ABCdef...`)

### 3. Kanal Hazırla
1. Telegramda yeni kanal yarat
2. Botunu kanalın **Admin**-i et (Post yazma icazəsi ver)
3. Kanal username-ni al (məs: `@mychannelname`)

### 4. Konfiqurasiya
`config.py` faylını aç və dəyişdir:
```python
BOT_TOKEN = "buraya_token_yaz"
CHANNEL_ID = "@kanal_username"
CHECK_INTERVAL_MINUTES = 15  # neçə dəqiqədən bir
```

### 5. Kitabxanaları Yüklə
```bash
pip install -r requirements.txt
```

### 6. Botu İşə Sal
```bash
python bot.py
```

---

## 📁 Fayl Strukturu
```
news_bot/
├── bot.py            # Əsas fayl
├── config.py         # Konfiqurasiya
├── news_fetcher.py   # RSS xəbər çəkici
├── news_sender.py    # Telegram göndərici
├── requirements.txt  # Kitabxanalar
└── sent_articles.json # Göndərilmiş xəbərlər (avtomatik yaranır)
```

---

## 🔧 Fərdiləşdirmə

### Yeni RSS Mənbəsi Əlavə Et
`config.py`-da `RSS_FEEDS` siyahısına əlavə et:
```python
{
    "name": "Sayt Adı",
    "url": "https://sayt.com/rss",
    "category": "📈 Səhm Bazarı",
    "emoji": "🆕"
},
```

### Interval Dəyişdir
```python
CHECK_INTERVAL_MINUTES = 30  # 30 dəqiqədən bir
```
