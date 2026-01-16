import warnings
import streamlit as st
from config import MY_API_KEY, MODEL_NAME, TU_DIEN_DATA
from data import ham_tim_kiem, lay_du_lieu_sidebar, lay_du_lieu_yahoo
from ai_service import configure_model, goi_ai_phan_tich
import ui
import streamlit.components.v1 as components

# --- 1. CẤU HÌNH HỆ THỐNG ---
st.set_page_config(
    page_title="AI Trading Pro", 
    layout="wide", 
    page_icon="🦁",
    initial_sidebar_state="expanded"
)
warnings.filterwarnings("ignore")

# Cấu hình AI
ok, err = configure_model(MY_API_KEY, MODEL_NAME)
if not ok:
    st.error(f"⚠️ Lỗi cấu hình API Key: {err}")

# Render CSS + Sidebar
ui.render_css()
search_box_val = ui.render_sidebar(ham_tim_kiem, lay_du_lieu_sidebar)

# --- state ---
if "symbol_chon" not in st.session_state:
    st.session_state.symbol_chon = None

# Chọn mã
final_key = None
if search_box_val:
    final_key = search_box_val
    st.session_state.symbol_chon = None
elif st.session_state.symbol_chon:
    final_key = st.session_state.symbol_chon

# --- MAIN CONTENT ---
if final_key:
    # Xử lý tìm kiếm
    yahoo_code, tv_code, display_name = "", "", ""

    if final_key in TU_DIEN_DATA:
        d = TU_DIEN_DATA[final_key]
        yahoo_code, tv_code, display_name = d['yahoo'], d['tv'], d['name']
    elif "DIRECT|" in final_key:
        tv_code = final_key.split("|")[1]
        display_name = tv_code
        sym = tv_code.split(":")[1] if ":" in tv_code else tv_code
        yahoo_code = f"{sym}=X" if "USD" in sym else sym
    elif "YAHOO_SEARCH|" in final_key:
        parts = final_key.split("|")
        yahoo_code, tv_code, display_name = parts[1], parts[2], parts[1]

    st.subheader(f"📊 {display_name}")

    # Tabs layout for better mobile UX
    tab1, tab2, tab3 = st.tabs(["📈 BIỂU ĐỒ", "🤖 AI PHÂN TÍCH", "📋 CHỈ SỐ"])

    # TAB 1: Chart (full width)
    with tab1:
        html_chart_main = f"""
        <div class="tradingview-widget-container" style="height: 500px; width: 100%;">
          <div id="tradingview_main" style="height: 100%; width: 100%;"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
            "autosize": true,
            "symbol": "{tv_code}",
            "interval": "D",
            "timezone": "Asia/Ho_Chi_Minh",
            "theme": "dark",
            "style": "1",
            "locale": "vi_VN",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "hide_side_toolbar": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_main"
          }});
          </script>
        </div>
        """
        components.html(html_chart_main, height=500)

    # TAB 2: AI Analysis (metrics + scrollable text)
    with tab2:
        with st.spinner('Sói Già đang phân tích...'):
            gia, rsi, tin = lay_du_lieu_yahoo(yahoo_code)

            if gia:
                c1, c2, c3 = st.columns(3)
                c1.metric("Giá", f"{gia:,.2f}")
                status_rsi = "🔴 Cao" if rsi > 70 else "🟢 Thấp" if rsi < 30 else "⚪ Ổn"
                c2.metric("RSI", f"{rsi:.1f}", status_rsi)

                nhan_dinh = goi_ai_phan_tich(yahoo_code, gia, rsi, tin)
                st.markdown("---")
                with st.container(height=400, border=True):
                    st.markdown(nhan_dinh)
            else:
                st.warning("Không có dữ liệu phân tích.")

    # TAB 3: Indicators
    with tab3:
        st.caption("Các chỉ báo hỗ trợ: MACD, Bollinger Bands")
        html_chart_indicators = f"""
        <div class="tradingview-widget-container" style="height: 450px; width: 100%;">
          <div id="tradingview_ind" style="height: 100%; width: 100%;"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
            "autosize": true,
            "symbol": "{tv_code}",
            "interval": "D",
            "timezone": "Asia/Ho_Chi_Minh",
            "theme": "dark",
            "style": "1",
            "locale": "vi_VN",
            "enable_publishing": false,
            "hide_top_toolbar": true,
            "hide_legend": false,
            "studies": ["RSI@tv-basicstudies","MACD@tv-basicstudies","BB@tv-basicstudies"],
            "container_id": "tradingview_ind"
          }});
          </script>
        </div>
        """
        components.html(html_chart_indicators, height=450)

else:
    st.info("👈 Mở Sidebar (góc trên trái) để chọn tài sản")