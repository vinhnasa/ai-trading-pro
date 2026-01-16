# ...new module for constants and asset dictionaries...
MY_API_KEY = "AIzaSyBQV5sXWWlDY-KUx3kOpTQ24vH17MElYT4"
MODEL_NAME = "gemini-flash-latest"

TU_DIEN_DATA = {
    # ==================================================
    # 1. HÀNG HÓA (COMMODITIES) - VÀNG, BẠC, DẦU
    # ==================================================
    "xauusd": {"yahoo": "GC=F", "tv": "OANDA:XAUUSD", "name": "🥇 Vàng (Gold Spot)"},
    "gold":   {"yahoo": "GC=F", "tv": "OANDA:XAUUSD", "name": "🥇 Vàng (Gold Spot)"},
    "vang":   {"yahoo": "GC=F", "tv": "OANDA:XAUUSD", "name": "🥇 Vàng (Gold Spot)"},
    
    "silver": {"yahoo": "SI=F", "tv": "OANDA:XAGUSD", "name": "🥈 Bạc (Silver)"},
    "bac":    {"yahoo": "SI=F", "tv": "OANDA:XAGUSD", "name": "🥈 Bạc (Silver)"},
    "xagusd": {"yahoo": "SI=F", "tv": "OANDA:XAGUSD", "name": "🥈 Bạc (Silver)"},
    
    "usoil":  {"yahoo": "CL=F", "tv": "TVC:USOIL",    "name": "🛢️ Dầu WTI (Crude Oil)"},
    "oil":    {"yahoo": "CL=F", "tv": "TVC:USOIL",    "name": "🛢️ Dầu WTI (Crude Oil)"},
    "dau":    {"yahoo": "CL=F", "tv": "TVC:USOIL",    "name": "🛢️ Dầu WTI (Crude Oil)"},
    
    "ukoil":  {"yahoo": "BZ=F", "tv": "TVC:UKOIL",    "name": "🛢️ Dầu Brent"},

    # ==================================================
    # 2. TIỀN ĐIỆN TỬ (CRYPTO) - TOP COINS
    # ==================================================
    "btc":  {"yahoo": "BTC-USD", "tv": "BINANCE:BTCUSDT", "name": "₿ Bitcoin (BTC)"},
    "eth":  {"yahoo": "ETH-USD", "tv": "BINANCE:ETHUSDT", "name": "💎 Ethereum (ETH)"},
    "sol":  {"yahoo": "SOL-USD", "tv": "BINANCE:SOLUSDT", "name": "☀️ Solana (SOL)"},
    "bnb":  {"yahoo": "BNB-USD", "tv": "BINANCE:BNBUSDT", "name": "🔶 Binance Coin (BNB)"},
    "xrp":  {"yahoo": "XRP-USD", "tv": "BINANCE:XRPUSDT", "name": "❌ Ripple (XRP)"},
    "doge": {"yahoo": "DOGE-USD","tv": "BINANCE:DOGEUSDT","name": "🐶 Dogecoin"},
    "ada":  {"yahoo": "ADA-USD", "tv": "BINANCE:ADAUSDT", "name": "🔵 Cardano (ADA)"},
    "link": {"yahoo": "LINK-USD","tv": "BINANCE:LINKUSDT","name": "🔗 Chainlink"},

    # ==================================================
    # 3. CHỨNG KHOÁN VIỆT NAM (TOP VN30 & HOT)
    # ==================================================
    "vnindex": {"yahoo": "^VNINDEX", "tv": "HOSE:VNINDEX", "name": "🇻🇳 VN-Index"},
    
    # Ngân hàng
    "vcb": {"yahoo": "VCB.VN", "tv": "HOSE:VCB", "name": "🏦 Vietcombank"},
    "bid": {"yahoo": "BID.VN", "tv": "HOSE:BID", "name": "🏦 BIDV"},
    "ctg": {"yahoo": "CTG.VN", "tv": "HOSE:CTG", "name": "🏦 VietinBank"},
    "tcb": {"yahoo": "TCB.VN", "tv": "HOSE:TCB", "name": "🏦 Techcombank"},
    "mb":  {"yahoo": "MBB.VN", "tv": "HOSE:MBB", "name": "🏦 MB Bank"},
    "mbb": {"yahoo": "MBB.VN", "tv": "HOSE:MBB", "name": "🏦 MB Bank"},
    "stb": {"yahoo": "STB.VN", "tv": "HOSE:STB", "name": "🏦 Sacombank"},
    "acb": {"yahoo": "ACB.VN", "tv": "HOSE:ACB", "name": "🏦 ACB"},
    "vpb": {"yahoo": "VPB.VN", "tv": "HOSE:VPB", "name": "🏦 VPBank"},

    # Bất động sản & Thép
    "vic": {"yahoo": "VIC.VN", "tv": "HOSE:VIC", "name": "🏙️ Vingroup"},
    "vhm": {"yahoo": "VHM.VN", "tv": "HOSE:VHM", "name": "🏘️ Vinhomes"},
    "vre": {"yahoo": "VRE.VN", "tv": "HOSE:VRE", "name": "🛍️ Vincom Retail"},
    "nvl": {"yahoo": "NVL.VN", "tv": "HOSE:NVL", "name": "🏘️ Novaland"},
    "hpg": {"yahoo": "HPG.VN", "tv": "HOSE:HPG", "name": "🏗️ Hòa Phát"},
    "hsg": {"yahoo": "HSG.VN", "tv": "HOSE:HSG", "name": "🏗️ Hoa Sen"},
    "nkg": {"yahoo": "NKG.VN", "tv": "HOSE:NKG", "name": "🏗️ Nam Kim"},

    # Chứng khoán & Bán lẻ & Khác
    "ssi": {"yahoo": "SSI.VN", "tv": "HOSE:SSI", "name": "📈 SSI Securities"},
    "vnd": {"yahoo": "VND.VN", "tv": "HOSE:VND", "name": "📈 VNDirect"},
    "fpt": {"yahoo": "FPT.VN", "tv": "HOSE:FPT", "name": "💻 FPT Corp"},
    "mwg": {"yahoo": "MWG.VN", "tv": "HOSE:MWG", "name": "📱 Thế Giới Di Động"},
    "msn": {"yahoo": "MSN.VN", "tv": "HOSE:MSN", "name": "🍜 Masan Group"},
    "vnm": {"yahoo": "VNM.VN", "tv": "HOSE:VNM", "name": "🥛 Vinamilk"},
    "sab": {"yahoo": "SAB.VN", "tv": "HOSE:SAB", "name": "🍺 Sabeco"},
    "gas": {"yahoo": "GAS.VN", "tv": "HOSE:GAS", "name": "⛽ PV Gas"},

    # ==================================================
    # 4. CHỨNG KHOÁN MỸ (US STOCKS)
    # ==================================================
    # Công nghệ (Big Tech)
    "tsla": {"yahoo": "TSLA", "tv": "NASDAQ:TSLA", "name": "🚗 Tesla Inc"},
    "aapl": {"yahoo": "AAPL", "tv": "NASDAQ:AAPL", "name": "🍎 Apple Inc"},
    "msft": {"yahoo": "MSFT", "tv": "NASDAQ:MSFT", "name": "💻 Microsoft"},
    "goog": {"yahoo": "GOOGL","tv": "NASDAQ:GOOGL","name": "🔍 Google (Alphabet)"},
    "amzn": {"yahoo": "AMZN", "tv": "NASDAQ:AMZN", "name": "📦 Amazon"},
    "meta": {"yahoo": "META", "tv": "NASDAQ:META", "name": "♾️ Meta (Facebook)"},
    "nvda": {"yahoo": "NVDA", "tv": "NASDAQ:NVDA", "name": "🤖 NVIDIA"},
    "amd":  {"yahoo": "AMD",  "tv": "NASDAQ:AMD",  "name": "💾 AMD"},
    "nflx": {"yahoo": "NFLX", "tv": "NASDAQ:NFLX", "name": "🎬 Netflix"},
    "intc": {"yahoo": "INTC", "tv": "NASDAQ:INTC", "name": "💾 Intel"},

    # Các mã phổ biến khác
    "ko":   {"yahoo": "KO",   "tv": "NYSE:KO",     "name": "🥤 Coca-Cola"},
    "pep":  {"yahoo": "PEP",  "tv": "NASDAQ:PEP",  "name": "🥤 PepsiCo"},
    "mcd":  {"yahoo": "MCD",  "tv": "NYSE:MCD",    "name": "🍔 McDonald's"},
    "dis":  {"yahoo": "DIS",  "tv": "NYSE:DIS",    "name": "🏰 Disney"},
    "nke":  {"yahoo": "NKE",  "tv": "NYSE:NKE",    "name": "👟 Nike"},
    
    # ==================================================
    # 5. NGOẠI HỐI (FOREX) & CHỈ SỐ (INDICES)
    # ==================================================
    "eurusd": {"yahoo": "EURUSD=X", "tv": "FX:EURUSD", "name": "💶 EUR/USD"},
    "gbpusd": {"yahoo": "GBPUSD=X", "tv": "FX:GBPUSD", "name": "💷 GBP/USD"},
    "usdjpy": {"yahoo": "JPY=X",    "tv": "FX:USDJPY", "name": "💴 USD/JPY"},
    "audusd": {"yahoo": "AUDUSD=X", "tv": "FX:AUDUSD", "name": "🇦🇺 AUD/USD"},
    "usdcad": {"yahoo": "CAD=X",    "tv": "FX:USDCAD", "name": "🇨🇦 USD/CAD"},
    
    "dxy":    {"yahoo": "DX-Y.NYB", "tv": "TVC:DXY",   "name": "💲 DXY (Dollar Index)"},
    
    # Chỉ số chứng khoán Mỹ
    "us30":   {"yahoo": "^DJI",     "tv": "TVC:DJI",   "name": "🇺🇸 Dow Jones (US30)"},
    "dow":    {"yahoo": "^DJI",     "tv": "TVC:DJI",   "name": "🇺🇸 Dow Jones (US30)"},
    "us500":  {"yahoo": "^GSPC",    "tv": "TVC:SPX",   "name": "🇺🇸 S&P 500"},
    "spx":    {"yahoo": "^GSPC",    "tv": "TVC:SPX",   "name": "🇺🇸 S&P 500"},
    "us100":  {"yahoo": "^IXIC",    "tv": "TVC:IXIC",  "name": "🇺🇸 Nasdaq 100"},
    "nasdaq": {"yahoo": "^IXIC",    "tv": "TVC:IXIC",  "name": "🇺🇸 Nasdaq 100"},
}

# --- 🔥 DANH SÁCH HOT TREND (ĐÃ MỞ RỘNG) ---
HOT_ASSETS = [
    # --- 1. HÀNG HÓA & TIỀN TỆ QUỐC TẾ ---
    {"key": "xauusd", "symbol": "GC=F", "name": "Vàng (Gold)", "icon": "🥇"},
    {"key": "silver", "symbol": "SI=F", "name": "Bạc (Silver)", "icon": "🥈"},
    {"key": "usoil",  "symbol": "CL=F", "name": "Dầu WTI", "icon": "🛢️"},
    {"key": "ukoil",  "symbol": "BZ=F", "name": "Dầu Brent", "icon": "🛢️"},
    {"key": "natgas", "symbol": "NG=F", "name": "Khí Gas (Natural Gas)", "icon": "🔥"},
    {"key": "coffee", "symbol": "KC=F", "name": "Cà phê (Arabica)", "icon": "☕"},
    {"key": "dxy",    "symbol": "DX-Y.NYB", "name": "DXY (Dollar Index)", "icon": "💲"},
    {"key": "eurusd", "symbol": "EURUSD=X", "name": "EUR/USD", "icon": "🇪🇺"},
    {"key": "gbpusd", "symbol": "GBPUSD=X", "name": "GBP/USD", "icon": "🇬🇧"},
    {"key": "usdjpy", "symbol": "JPY=X",    "name": "USD/JPY", "icon": "🇯🇵"},

    # --- 2. CRYPTO (TIỀN ĐIỆN TỬ) ---
    {"key": "btc",    "symbol": "BTC-USD", "name": "Bitcoin", "icon": "₿"},
    {"key": "eth",    "symbol": "ETH-USD", "name": "Ethereum", "icon": "💎"},
    {"key": "sol",    "symbol": "SOL-USD", "name": "Solana", "icon": "☀️"},
    {"key": "bnb",    "symbol": "BNB-USD", "name": "Binance Coin", "icon": "🔶"},
    {"key": "xrp",    "symbol": "XRP-USD", "name": "Ripple (XRP)", "icon": "✖️"},
    {"key": "doge",   "symbol": "DOGE-USD", "name": "Dogecoin", "icon": "🐕"},
    {"key": "ada",    "symbol": "ADA-USD", "name": "Cardano", "icon": "🔵"},
    {"key": "link",   "symbol": "LINK-USD", "name": "Chainlink", "icon": "🔗"},
    {"key": "ltc",    "symbol": "LTC-USD", "name": "Litecoin", "icon": "Ł"},
    {"key": "near",   "symbol": "NEAR-USD", "name": "Near Protocol", "icon": "🌈"},

    # --- 3. CHỨNG KHOÁN MỸ (US TECH & INDICES) ---
    {"key": "us30",   "symbol": "^DJI", "name": "Dow Jones (US30)", "icon": "🇺🇸"},
    {"key": "us500",  "symbol": "^GSPC", "name": "S&P 500", "icon": "📈"},
    {"key": "us100",  "symbol": "^IXIC", "name": "Nasdaq 100", "icon": "🖥️"},
    {"key": "nvda",   "symbol": "NVDA", "name": "NVIDIA", "icon": "🤖"},
    {"key": "tsla",   "symbol": "TSLA", "name": "Tesla", "icon": "🚗"},
    {"key": "aapl",   "symbol": "AAPL", "name": "Apple", "icon": "🍎"},
    {"key": "msft",   "symbol": "MSFT", "name": "Microsoft", "icon": "💻"},
    {"key": "goog",   "symbol": "GOOGL", "name": "Google", "icon": "🔍"},
    {"key": "amzn",   "symbol": "AMZN", "name": "Amazon", "icon": "📦"},
    {"key": "meta",   "symbol": "META", "name": "Meta (Facebook)", "icon": "♾️"},
    {"key": "amd",    "symbol": "AMD", "name": "AMD Chip", "icon": "💾"},
    {"key": "coin",   "symbol": "COIN", "name": "Coinbase", "icon": "🏦"},
    {"key": "mstr",   "symbol": "MSTR", "name": "MicroStrategy", "icon": "🐳"},

    # --- 4. CHỨNG KHOÁN VIỆT NAM (VN30 & TOP) ---
    {"key": "vnindex","symbol": "^VNINDEX", "name": "VN-Index", "icon": "🇻🇳"},
    {"key": "fpt",    "symbol": "FPT.VN", "name": "FPT Corp", "icon": "💻"},
    {"key": "hpg",    "symbol": "HPG.VN", "name": "Thép Hòa Phát", "icon": "🏗️"},
    {"key": "vcb",    "symbol": "VCB.VN", "name": "Vietcombank", "icon": "🏦"},
    {"key": "bid",    "symbol": "BID.VN", "name": "BIDV", "icon": "🏦"},
    {"key": "ctg",    "symbol": "CTG.VN", "name": "VietinBank", "icon": "🏦"},
    {"key": "tcb",    "symbol": "TCB.VN", "name": "Techcombank", "icon": "🏦"},
    {"key": "mb",     "symbol": "MBB.VN", "name": "MB Bank", "icon": "🏦"},
    {"key": "stb",    "symbol": "STB.VN", "name": "Sacombank", "icon": "🏦"},
    {"key": "ssi",    "symbol": "SSI.VN", "name": "Chứng khoán SSI", "icon": "📉"},
    {"key": "vnd",    "symbol": "VND.VN", "name": "VNDirect", "icon": "📉"},
    {"key": "mwg",    "symbol": "MWG.VN", "name": "Thế Giới Di Động", "icon": "📱"},
    {"key": "msn",    "symbol": "MSN.VN", "name": "Masan Group", "icon": "🍜"},
    {"key": "vnm",    "symbol": "VNM.VN", "name": "Vinamilk", "icon": "🥛"},
    {"key": "vic",    "symbol": "VIC.VN", "name": "Vingroup", "icon": "🏙️"},
    {"key": "vhm",    "symbol": "VHM.VN", "name": "Vinhomes", "icon": "🏘️"},
    {"key": "nvl",    "symbol": "NVL.VN", "name": "Novaland", "icon": "🏘️"},
    {"key": "hsg",    "symbol": "HSG.VN", "name": "Thép Hoa Sen", "icon": "🏗️"},
    {"key": "nkg",    "symbol": "NKG.VN", "name": "Thép Nam Kim", "icon": "🏗️"},
    {"key": "gas",    "symbol": "GAS.VN", "name": "PV Gas", "icon": "⛽"},
    {"key": "bsr",    "symbol": "BSR.VN", "name": "Lọc hóa dầu Bình Sơn", "icon": "🛢️"},
]
