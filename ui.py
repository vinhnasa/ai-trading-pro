import streamlit as st
import streamlit.components.v1 as components
from streamlit_searchbox import st_searchbox

def render_css():
    st.markdown("""
    <style>
        /* =============================================
           1. CẤU HÌNH THANH CUỘN (SCROLLBAR)
           ============================================= */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #666; }

        /* =============================================
           2. KHẮC PHỤC LỖI BỊ CHE KHUẤT TRÊN MOBILE
           (QUAN TRỌNG NHẤT)
           ============================================= */
        
        /* Cấu hình chung cho thân trang */
        .block-container {
            /* 4rem là khoảng cách an toàn tiêu chuẩn cho Desktop */
            padding-top: 3.5rem !important; 
            padding-bottom: 2rem !important;
        }

        /* Khi màn hình nhỏ hơn 768px (Điện thoại/Tablet dọc) */
        @media only screen and (max-width: 768px) {
            .block-container {
                /* Tăng mạnh khoảng cách đỉnh để né thanh công cụ Streamlit */
                /* Đẩy nội dung xuống 6rem (khoảng 96px) - Đảm bảo không bao giờ bị che */
                padding-top: 6rem !important; 
                
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            
            /* Ẩn bớt tiêu đề quá khổ nếu cần */
            h1 { font-size: 1.6rem !important; }
            
            /* Đảm bảo iframe (biểu đồ) full chiều rộng */
            iframe { width: 100% !important; }
        }

        /* =============================================
           3. GIAO DIỆN TABS (KIỂU MOBILE APP)
           ============================================= */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #0e1117;
            /* Dính thanh Tab lên trên cùng khi cuộn, 
               cách đỉnh 60px để không bị thanh công cụ che */
            position: sticky;
            top: 0px; 
            z-index: 990;
            padding-top: 10px;
            padding-bottom: 5px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 45px;
            white-space: pre-wrap;
            background-color: #1f2937;
            border-radius: 8px 8px 0 0;
            gap: 2px;
            padding: 5px 10px;
            flex: 1; /* Chia đều độ rộng các tab */
            font-size: 0.9rem;
        }

        .stTabs [aria-selected="true"] {
            background-color: #4CAF50 !important;
            color: white !important;
            font-weight: bold;
        }

    </style>
    """, unsafe_allow_html=True)

def render_sidebar(ham_tim_kiem, lay_du_lieu_sidebar):
    with st.sidebar:
        # ---------------------------------------------------------
        # ⚓ PHẦN 1: KHU VỰC NEO (FIXED HEADER) - nằm NGOÀI vùng cuộn
        # ---------------------------------------------------------
        st.title("🦁 AI TRADING PRO")
        search_box_val = st_searchbox(ham_tim_kiem, key="main_search", label="🔍 Tìm kiếm tài sản")
        st.write("")  # khoảng cách nhỏ
        st.subheader("🔥 MARKET TRENDS")
        st.markdown("""<hr style="margin-top: 0; margin-bottom: 10px; border-top: 1px solid #444;">""", unsafe_allow_html=True)

        # ---------------------------------------------------------
        # 📜 PHẦN 2: KHU VỰC CUỘN (SCROLLABLE LIST)
        # ---------------------------------------------------------
        # Chiều cao container có thể chỉnh (550 hoặc 600)
        with st.container(height=550, border=False):
            with st.spinner("Đang cập nhật..."):
                trends = lay_du_lieu_sidebar()
                if trends:
                    # Bao 1 div scrollable để chỉ vùng danh sách có scrollbar
                    st.markdown('<div style="max-height:520px; overflow:auto; padding-right:6px;">', unsafe_allow_html=True)
                    for t in trends:
                        c1, c2 = st.columns([0.85, 0.15])
                        with c1:
                            color_class = "trend-up" if t['change'] >= 0 else "trend-down"
                            icon_trend = "▲" if t['change'] >= 0 else "▼"
                            html_code = f"""
                            <div class="trend-card">
                                <div><b>{t['icon']} {t['name']}</b></div>
                                <div style="display:flex; justify-content:space-between;">
                                    <span>{t['price']:,.2f}</span>
                                    <span class="{color_class}">{icon_trend} {abs(t['change']):.2f}%</span>
                                </div>
                            </div>
                            """
                            st.markdown(html_code, unsafe_allow_html=True)
                        with c2:
                            if st.button("👁️", key=f"btn_{t['key']}", help=f"Xem {t['name']}"):
                                st.session_state.symbol_chon = t['key']
                                st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.caption("Đang tải dữ liệu...")
    return search_box_val

def render_tradingview(tv_code, height_main=500, height_ind=400):
    html_main = f"""
    <div class="tradingview-widget-container" style="height: {height_main}px; width: 100%; margin-bottom: 20px;">
      <div id="tradingview_main" style="height: 100%; width: 100%;"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{tv_code}",
        "interval": "D",
        "timezone": "Asia/Ho_Chi_Minh",
        "theme": "dark",
        "style": "1",
        "locale": "vi_VN",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_main"
      }});
      </script>
    </div>
    """
    components.html(html_main, height=height_main)

    html_ind = f"""
    <div class="tradingview-widget-container" style="height: {height_ind}px; width: 100%;">
      <div id="tradingview_ind" style="height: 100%; width: 100%;"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
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
    components.html(html_ind, height=height_ind)
