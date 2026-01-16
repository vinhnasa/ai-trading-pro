import requests
import yfinance as yf
import pandas_ta as ta
import streamlit as st
from config import TU_DIEN_DATA, HOT_ASSETS

def ham_tim_kiem(searchterm: str):
    # ...existing ham_tim_kiem logic moved here unchanged...
    if not searchterm:
        return [("🔥 Vàng (Gold)", "xauusd"), ("₿ Bitcoin (BTC)", "btc"), ("🇻🇳 VnIndex", "vnindex")]

    query = searchterm.lower().strip()
    ket_qua = []

    if ":" in query:
        return [(f"🌍 Mã sàn cụ thể: {searchterm.upper()}", f"DIRECT|{searchterm.upper()}")]

    count = 0
    for key, data in TU_DIEN_DATA.items():
        if query in key or query in data['name'].lower():
            ket_qua.append((f"✨ {data['name']}", key))
            count += 1
            if count >= 5: break
    
    if len(ket_qua) < 3:
        try:
            url = "https://query2.finance.yahoo.com/v1/finance/search"
            params = {'q': query, 'quotesCount': 5}
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, params=params, headers=headers, timeout=1).json()
            if 'quotes' in r:
                for i in r['quotes']:
                    sym = i.get('symbol', '')
                    name = i.get('shortname') or sym
                    tv_suggestion = sym
                    if ".VN" in sym: tv_suggestion = f"HOSE:{sym.replace('.VN','')}"
                    elif "=X" in sym: tv_suggestion = f"FX:{sym.replace('=X','')}"
                    elif "-USD" in sym: tv_suggestion = f"BINANCE:{sym.replace('-USD','USDT')}"
                    ket_qua.append((f"🌐 {name} ({sym})", f"YAHOO_SEARCH|{sym}|{tv_suggestion}"))
        except: pass
        
    return ket_qua

@st.cache_data(ttl=60)
def lay_du_lieu_sidebar():
    """Lấy dữ liệu nhanh cho list Hot Trend"""
    data_list = []
    try:
        for item in HOT_ASSETS:
            sym = item['symbol']
            try:
                t = yf.Ticker(sym)
                price = t.fast_info.last_price
                prev_price = t.fast_info.previous_close
                
                if price and prev_price:
                    change = ((price - prev_price) / prev_price) * 100
                    data_list.append({
                        "key": item['key'],
                        "name": item['name'],
                        "icon": item['icon'],
                        "price": price,
                        "change": change
                    })
            except: continue
    except: pass
    return data_list

@st.cache_data(ttl=600)
def lay_du_lieu_yahoo(symbol):
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="3mo")
        if df.empty: return None, None, None
        df['RSI'] = df.ta.rsi(length=14)
        return df['Close'].iloc[-1], df['RSI'].iloc[-1], ticker.news
    except: return None, None, None
