import os
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "Output"
DOWNLOADS_DIR = Path.home() / "Downloads"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

BASE_IMAGE_PATH = Path("/Users/SammyWang/.gemini/antigravity-ide/brain/a4ffbc58-6f98-4149-bb98-25fa1a4df304/chiba_gloves_gravel_1793104352397.jpg")
BADGE_PILL_PATH = OUTPUT_DIR / "badge_pill_clean.png"
C1_PATH = OUTPUT_DIR / "c1_full_border.png"
C2_PATH = OUTPUT_DIR / "c2_full_border.png"

# Ultra-legible display fonts: Hiragino Sans GB W6 (Apple bold sans) + German DIN Alternate Bold
FONT_ZH_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_EN_PATH = "/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf"

def add_shadow(img, offset=(0, 6), blur=10, color=(0, 0, 0, 150)):
    pad = blur * 2
    sw, sh = img.width + pad * 2, img.height + pad * 2
    s = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    alpha = img.getchannel("A").point(lambda v: v * color[3] // 255)
    solid = Image.new("RGBA", img.size, color[:3] + (0,))
    solid.putalpha(alpha)
    s.paste(solid, (pad + offset[0], pad + offset[1]))
    s = s.filter(ImageFilter.GaussianBlur(blur))
    s.alpha_composite(img, (pad, pad))
    return s, pad

def make_qr_card(qr_img, pad=6, radius=10):
    fw, fh = qr_img.width + pad * 2, qr_img.height + pad * 2
    card = Image.new("RGBA", (fw, fh), (255, 255, 255, 255))
    mask = Image.new("L", (fw, fh), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([0, 0, fw - 1, fh - 1], radius=radius, fill=255)
    card.putalpha(mask)
    card.paste(qr_img, (pad, pad), qr_img)
    return card

def render_posters():
    base_img = Image.open(BASE_IMAGE_PATH).convert("RGBA")
    W, H = base_img.size  # 896, 1200

    # Fonts - Maximum Prominence, Sharpness & Legibility
    font_head1 = ImageFont.truetype(FONT_ZH_PATH, 31, index=2)  # W6 Bold
    font_head2 = ImageFont.truetype(FONT_ZH_PATH, 30, index=2)  # W6 Bold
    font_din_prod = ImageFont.truetype(FONT_EN_PATH, 28)        # DIN Bold
    font_zh_prod = ImageFont.truetype(FONT_ZH_PATH, 26, index=2) # W6 Bold
    font_zh_lbl = ImageFont.truetype(FONT_ZH_PATH, 22, index=2)  # W6 Bold
    font_din_url = ImageFont.truetype(FONT_EN_PATH, 24)         # DIN Bold

    # QR Codes (perfectly scaled ~100px width for harmonious proportions)
    c1 = Image.open(C1_PATH).convert("RGBA")
    c2 = Image.open(C2_PATH).convert("RGBA")
    qr_w = 100
    qr_h = int(c1.height * (qr_w / c1.width))  # ~127px
    c1_s = c1.resize((qr_w, qr_h), Image.Resampling.LANCZOS)
    c2_s = c2.resize((qr_w, qr_h), Image.Resampling.LANCZOS)

    card1 = make_qr_card(c1_s, pad=6, radius=9)
    card2 = make_qr_card(c2_s, pad=6, radius=9)

    card1_sh, pad1 = add_shadow(card1, offset=(0, 6), blur=10, color=(0, 0, 0, 180))
    card2_sh, pad2 = add_shadow(card2, offset=(0, 6), blur=10, color=(0, 0, 0, 180))

    # Top Badge
    badge = Image.open(BADGE_PILL_PATH).convert("RGBA")
    bw = 246
    bh = int(badge.height * (bw / badge.width))
    badge_s = badge.resize((bw, bh), Image.Resampling.LANCZOS)
    badge_sh, b_pad = add_shadow(badge_s, offset=(0, 5), blur=8, color=(0, 0, 0, 140))

    # =============================================================
    # 1. CINEMATIC POSTER (Full Bleed Action + 100% Text Legibility)
    # =============================================================
    cinematic = base_img.copy()
    cinematic.paste(badge_sh, (W - bw - 32 - b_pad, 32 - b_pad), badge_sh)

    # Smoothstep dark gradient scrim for maximum text contrast without abrupt edges
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    y_start = 710
    y_full = 910
    for y in range(y_start, H):
        if y < y_full:
            t = (y - y_start) / (y_full - y_start)
            smooth_t = t * t * (3 - 2 * t)
            alpha = int(225 * smooth_t)
        else:
            t2 = (y - y_full) / (H - y_full)
            alpha = int(225 + 28 * t2)
        v_draw.line([(0, y), (W, y)], fill=(6, 10, 16, alpha))
    cinematic.paste(vignette, (0, 0), vignette)

    tx = 42
    ty = 918
    tx_c = tx + 18

    # Multi-directional deep dark shadow / halo layer for 360-degree text edge separation
    s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_d = ImageDraw.Draw(s_layer)

    # Line 1 & Line 2 shadows
    s_d.text((tx_c, ty), "碎石塵土飛揚，路況瞬息萬變。", font=font_head1, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
    s_d.text((tx_c, ty + 42), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head2, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))

    # Line 3 (Product Highlight) shadow
    p_y = ty + 92
    w_chiba = font_din_prod.getbbox("CHIBA BioXCell")[2]
    s_d.text((tx_c, p_y), "CHIBA BioXCell", font=font_din_prod, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
    s_d.text((tx_c + w_chiba + 6, p_y), "手套 ｜ 為多變路況而設計", font=font_zh_prod, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))

    # Line 4 (Taiwan Official Store) shadow
    u1_y = p_y + 40
    w_lbl1 = font_zh_lbl.getbbox("探索台灣官網：")[2]
    s_d.text((tx_c, u1_y + 1), "探索台灣官網：", font=font_zh_lbl, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
    s_d.text((tx_c + w_lbl1 + 4, u1_y), "www.chibataiwan.com", font=font_din_url, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))

    # Line 5 (Germany Headquarters) shadow
    u2_y = u1_y + 32
    w_lbl2 = font_zh_lbl.getbbox("德國原廠官網：")[2]
    s_d.text((tx_c, u2_y + 1), "德國原廠官網：", font=font_zh_lbl, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
    s_d.text((tx_c + w_lbl2 + 4, u2_y), "www.chiba.de", font=font_din_url, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))

    s_layer = s_layer.filter(ImageFilter.GaussianBlur(3))
    cinematic.alpha_composite(s_layer)

    # Foreground Text & Badges Layer
    t_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(t_layer)

    # Rich crimson accent bar spanning headlines
    d.rounded_rectangle([tx, ty + 2, tx + 5, ty + 70], radius=2, fill=(235, 35, 75))

    # Line 1 & Line 2 (Crisp Pure White with dark anti-halo stroke)
    d.text((tx_c, ty), "碎石塵土飛揚，路況瞬息萬變。", font=font_head1, fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 200))
    d.text((tx_c, ty + 42), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head2, fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 200))

    # Line 3 (Product Highlight: Electric Crimson DIN Bold + Crisp White Chinese)
    d.text((tx_c, p_y), "CHIBA BioXCell", font=font_din_prod, fill=(255, 50, 85), stroke_width=1, stroke_fill=(0, 0, 0, 180))
    d.text((tx_c + w_chiba + 6, p_y), "手套 ｜ 為多變路況而設計", font=font_zh_prod, fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 180))

    # Line 4 (Taiwan Official Store: Platinum Label + Pure White DIN Bold URL)
    d.text((tx_c, u1_y + 1), "探索台灣官網：", font=font_zh_lbl, fill=(226, 232, 240), stroke_width=1, stroke_fill=(0, 0, 0, 200))
    d.text((tx_c + w_lbl1 + 4, u1_y), "www.chibataiwan.com", font=font_din_url, fill=(255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 200))

    # Line 5 (Germany Headquarters: Platinum Label + Radiant Warm Gold DIN Bold URL)
    d.text((tx_c, u2_y + 1), "德國原廠官網：", font=font_zh_lbl, fill=(226, 232, 240), stroke_width=1, stroke_fill=(0, 0, 0, 200))
    d.text((tx_c + w_lbl2 + 4, u2_y), "www.chiba.de", font=font_din_url, fill=(254, 240, 138), stroke_width=1, stroke_fill=(0, 0, 0, 200))

    cinematic.alpha_composite(t_layer)

    # QR Codes on the right (perfectly balanced with text block)
    qr_gap = 14
    total_qr_w = card1.width + card2.width + qr_gap
    qr_x = W - total_qr_w - 32
    qr_y = ty + 24
    cinematic.paste(card1_sh, (qr_x - pad1, qr_y - pad1), card1_sh)
    cinematic.paste(card2_sh, (qr_x + card1.width + qr_gap - pad2, qr_y - pad2), card2_sh)

    # =============================================================
    # 2. GLASSMORPHIC POSTER (Matching Upgraded Typography)
    # =============================================================
    glassmorphic = base_img.copy()
    glassmorphic.paste(badge_sh, (W - bw - 32 - b_pad, 32 - b_pad), badge_sh)

    card_margin = 28
    card_w = W - card_margin * 2
    card_h = 246
    card_y = H - card_h - 24

    glass = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glass)
    for y in range(card_h):
        prog = y / card_h
        r = int(12 + prog * 8)
        g = int(16 + prog * 8)
        b = int(22 + prog * 10)
        alpha = int(224 + prog * 20)
        g_draw.line([(0, y), (card_w, y)], fill=(r, g, b, alpha))

    glass_mask = Image.new("L", (card_w, card_h), 0)
    m_draw = ImageDraw.Draw(glass_mask)
    m_draw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=18, fill=255)
    glass.putalpha(glass_mask)

    g_border = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(g_border)
    b_draw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=18, outline=(255, 255, 255, 45), width=1)
    stripe_w = 42
    start_sx = 28
    b_draw.rectangle([start_sx, 0, start_sx + stripe_w, 3], fill=(30, 30, 30, 255))
    b_draw.rectangle([start_sx + stripe_w, 0, start_sx + stripe_w * 2, 3], fill=(225, 29, 72, 255))
    b_draw.rectangle([start_sx + stripe_w * 2, 0, start_sx + stripe_w * 3, 3], fill=(234, 179, 8, 255))
    glass = Image.alpha_composite(glass, g_border)

    glass_sh, g_pad = add_shadow(glass, offset=(0, 10), blur=16, color=(0, 0, 0, 160))
    glassmorphic.paste(glass_sh, (card_margin - g_pad, card_y - g_pad), glass_sh)

    d_glass = ImageDraw.Draw(glassmorphic)
    tx_g = card_margin + 26
    ty_g = card_y + 20

    d_glass.rounded_rectangle([tx_g, ty_g + 2, tx_g + 5, ty_g + 70], radius=2, fill=(225, 29, 72))

    tx_gc = tx_g + 16
    d_glass.text((tx_gc, ty_g), "碎石塵土飛揚，路況瞬息萬變。", font=font_head1, fill=(255, 255, 255))
    d_glass.text((tx_gc, ty_g + 42), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head2, fill=(255, 255, 255))

    p_gy = ty_g + 92
    d_glass.text((tx_gc, p_gy), "CHIBA BioXCell", font=font_din_prod, fill=(255, 50, 85))
    d_glass.text((tx_gc + w_chiba + 6, p_gy), "手套 ｜ 為多變路況而設計", font=font_zh_prod, fill=(255, 255, 255))

    u1_gy = p_gy + 38
    d_glass.text((tx_gc, u1_gy + 1), "探索台灣官網：", font=font_zh_lbl, fill=(226, 232, 240))
    d_glass.text((tx_gc + w_lbl1 + 4, u1_gy), "www.chibataiwan.com", font=font_din_url, fill=(255, 255, 255))

    u2_gy = u1_gy + 30
    d_glass.text((tx_gc, u2_gy + 1), "德國原廠官網：", font=font_zh_lbl, fill=(226, 232, 240))
    d_glass.text((tx_gc + w_lbl2 + 4, u2_gy), "www.chiba.de", font=font_din_url, fill=(254, 240, 138))

    qr_gx = card_margin + card_w - total_qr_w - 24
    qr_gy = card_y + (card_h - card1.height) // 2
    glassmorphic.paste(card1_sh, (qr_gx - pad1, qr_gy - pad1), card1_sh)
    glassmorphic.paste(card2_sh, (qr_gx + card1.width + qr_gap - pad2, qr_gy - pad2), card2_sh)

    # =============================================================
    # 3. EXPORT FILES (User-specified file, Latest & Timestamps)
    # =============================================================
    timestamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M")

    # 1. Exact user-requested file in Downloads
    p_cin_specified = DOWNLOADS_DIR / "CHIBA_Gravel_Poster_Cinematic_20261027-2204.jpg"
    cinematic.convert("RGB").save(p_cin_specified, quality=96, optimize=True)

    # 2. Latest file in Downloads
    p_cin_latest_dl = DOWNLOADS_DIR / "CHIBA_Gravel_Poster_Cinematic_Latest.jpg"
    cinematic.convert("RGB").save(p_cin_latest_dl, quality=96, optimize=True)

    # 3. Timestamped files in Downloads and Output
    p_cin_ts_dl = DOWNLOADS_DIR / f"CHIBA_Gravel_Poster_Cinematic_{timestamp}.jpg"
    p_cin_out = OUTPUT_DIR / f"CHIBA_Gravel_Poster_Cinematic_{timestamp}.jpg"
    cinematic.convert("RGB").save(p_cin_ts_dl, quality=96, optimize=True)
    cinematic.convert("RGB").save(p_cin_out, quality=96, optimize=True)

    # Glassmorphic exports
    p_glass_latest_dl = DOWNLOADS_DIR / "CHIBA_Gravel_Poster_Glassmorphic_Latest.jpg"
    p_glass_ts_dl = DOWNLOADS_DIR / f"CHIBA_Gravel_Poster_Glassmorphic_{timestamp}.jpg"
    p_glass_out = OUTPUT_DIR / f"CHIBA_Gravel_Poster_Glassmorphic_{timestamp}.jpg"
    glassmorphic.convert("RGB").save(p_glass_latest_dl, quality=96, optimize=True)
    glassmorphic.convert("RGB").save(p_glass_ts_dl, quality=96, optimize=True)
    glassmorphic.convert("RGB").save(p_glass_out, quality=96, optimize=True)

    print("Posters successfully generated with 100% optimized typography:")
    print(f"  User Target:           {p_cin_specified}")
    print(f"  Cinematic (Latest):    {p_cin_latest_dl}")
    print(f"  Cinematic (Timestamp): {p_cin_ts_dl}")
    print(f"  Output Backup:         {p_cin_out}")

if __name__ == "__main__":
    render_posters()
