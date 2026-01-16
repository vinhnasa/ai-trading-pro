import google.generativeai as genai

_model = None

def configure_model(api_key: str, model_name: str):
    global _model
    try:
        genai.configure(api_key=api_key, transport='rest')
        _model = genai.GenerativeModel(model_name)
        return True, None
    except Exception as e:
        _model = None
        return False, str(e)

def goi_ai_phan_tich(symbol, gia, rsi, news):
    if _model is None:
        return "⚠️ AI chưa được cấu hình hoặc đang quá tải."
    tin = "Không có tin tức quan trọng."
    if news:
        dstt = [f"- {n.get('title','')}" for n in news[:3] if n]
        tin = "\n".join(dstt)

    prompt = f"""
    Bạn là Sói Già Phố Wall. Phân tích mã {symbol}:
    - Giá: {gia:,.2f}
    - RSI (14): {rsi:.2f}
    - Tin tức: {tin}
    
    Trả lời ngắn gọn, format Markdown:
    1. **Xu hướng**: (Tăng/Giảm/Sideway)
    2. **Phân tích kỹ thuật**: Đánh giá RSI và hành động giá.
    3. ** Phân tích tin tức**: Tóm tắt tác động chính toàn cầu đến mã này sau khi đọc tin tức từ các trang web nổi tiếng có liên quan đến tài chính toàn cầu và đặc biệt là trang web này: https://www.forexfactory.com/
    4. **KHUYẾN NGHỊ**: (MUA / BÁN / QUAN SÁT) kèm vùng giá.
    5. **CẢNH BÁO**: Rủi ro tiềm ẩn về các khoảng giá và biến động thị trường.
    6. **Lưu ý**: Nếu đang giao dịch sản phẩm phái sinh thì cần làm gì lúc này (LONG/SHORT/EXIT).
    7. Kết luận ngắn gọn.
    """
    try:
        return _model.generate_content(prompt).text
    except Exception as e:
        return f"⚠️ AI Busy: {str(e)}"
