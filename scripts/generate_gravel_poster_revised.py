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

FONT_ZH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_EN = "/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf"

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

    # Fonts
    font_head = ImageFont.truetype(FONT_ZH, 31)
    font_sub = ImageFont.truetype(FONT_ZH, 23)
    font_small = ImageFont.truetype(FONT_ZH, 18)

    # QR Codes (scaled to be consistent with the text height, ~110px width)
    c1 = Image.open(C1_PATH).convert("RGBA")
    c2 = Image.open(C2_PATH).convert("RGBA")
    qr_w = 110
    qr_h = int(c1.height * (qr_w / c1.width))  # ~140px
    c1_s = c1.resize((qr_w, qr_h), Image.Resampling.LANCZOS)
    c2_s = c2.resize((qr_w, qr_h), Image.Resampling.LANCZOS)

    card1 = make_qr_card(c1_s, pad=6, radius=9)
    card2 = make_qr_card(c2_s, pad=6, radius=9)

    card1_sh, pad1 = add_shadow(card1, offset=(0, 6), blur=10, color=(0, 0, 0, 170))
    card2_sh, pad2 = add_shadow(card2, offset=(0, 6), blur=10, color=(0, 0, 0, 170))

    # Top Badge
    badge = Image.open(BADGE_PILL_PATH).convert("RGBA")
    bw = 246
    bh = int(badge.height * (bw / badge.width))
    badge_s = badge.resize((bw, bh), Image.Resampling.LANCZOS)
    badge_sh, b_pad = add_shadow(badge_s, offset=(0, 5), blur=8, color=(0, 0, 0, 140))

    # -------------------------------------------------------------
    # OPTION 1: Premium Glassmorphic Card (Structured, High-End Luxury)
    # -------------------------------------------------------------
    opt1 = base_img.copy()
    opt1.paste(badge_sh, (W - bw - 32 - b_pad, 32 - b_pad), badge_sh)

    card_margin = 28
    card_w = W - card_margin * 2
    card_h = 226
    card_y = H - card_h - 30

    # Create frosted glass backplate
    glass = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glass)
    for y in range(card_h):
        prog = y / card_h
        r = int(12 + prog * 8)
        g = int(16 + prog * 8)
        b = int(22 + prog * 10)
        alpha = int(216 + prog * 24)
        g_draw.line([(0, y), (card_w, y)], fill=(r, g, b, alpha))

    glass_mask = Image.new("L", (card_w, card_h), 0)
    m_draw = ImageDraw.Draw(glass_mask)
    m_draw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=18, fill=255)
    glass.putalpha(glass_mask)

    # Border & German flag micro-accent
    g_border = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(g_border)
    b_draw.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=18, outline=(255, 255, 255, 42), width=1)
    stripe_w = 42
    start_sx = 28
    b_draw.rectangle([start_sx, 0, start_sx + stripe_w, 3], fill=(30, 30, 30, 255))
    b_draw.rectangle([start_sx + stripe_w, 0, start_sx + stripe_w * 2, 3], fill=(225, 29, 72, 255))
    b_draw.rectangle([start_sx + stripe_w * 2, 0, start_sx + stripe_w * 3, 3], fill=(234, 179, 8, 255))
    glass = Image.alpha_composite(glass, g_border)

    glass_sh, g_pad = add_shadow(glass, offset=(0, 10), blur=16, color=(0, 0, 0, 160))
    opt1.paste(glass_sh, (card_margin - g_pad, card_y - g_pad), glass_sh)

    # Draw copy
    d1 = ImageDraw.Draw(opt1)
    tx = card_margin + 26
    ty = card_y + 24

    # Red vertical bar
    d1.rounded_rectangle([tx, ty + 2, tx + 5, ty + 70], radius=2, fill=(225, 29, 72))

    tx_c = tx + 16
    d1.text((tx_c, ty), "碎石塵土飛揚，路況瞬息萬變。", font=font_head, fill=(255, 255, 255))
    d1.text((tx_c, ty + 42), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head, fill=(255, 255, 255))

    p_y = ty + 92
    tw_biox = d1.textbbox((0, 0), "CHIBA BioXCell 手套", font=font_sub)[2]
    d1.text((tx_c, p_y), "CHIBA BioXCell 手套", font=font_sub, fill=(255, 70, 90))
    d1.text((tx_c + tw_biox, p_y), " ｜ 為多變路況而設計", font=font_sub, fill=(226, 232, 240))

    u_y = p_y + 36
    d1.text((tx_c, u_y), "探索 CHIBA 德國手套系列：www.chibataiwan.com", font=font_small, fill=(160, 174, 192))

    # QR Codes on right inside card
    qr_gap = 14
    total_qr_w = card1.width + card2.width + qr_gap
    qr_x = card_margin + card_w - total_qr_w - 24
    qr_y = card_y + (card_h - card1.height) // 2
    opt1.paste(card1_sh, (qr_x - pad1, qr_y - pad1), card1_sh)
    opt1.paste(card2_sh, (qr_x + card1.width + qr_gap - pad2, qr_y - pad2), card2_sh)

    # -------------------------------------------------------------
    # OPTION 2: Seamless Cinematic Vignette (Edge-to-Edge Action Feel)
    # -------------------------------------------------------------
    opt2 = base_img.copy()
    opt2.paste(badge_sh, (W - bw - 32 - b_pad, 32 - b_pad), badge_sh)

    # Rich dark bottom gradient
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    for y in range(700, H):
        prog = (y - 700) / (H - 700)
        alpha = int(235 * (prog ** 1.5))
        v_draw.line([(0, y), (W, y)], fill=(8, 12, 18, alpha))
    opt2.paste(vignette, (0, 0), vignette)

    d2 = ImageDraw.Draw(opt2)
    tx2 = 44
    ty2 = 948

    # Red vertical bar
    d2.rounded_rectangle([tx2, ty2 + 2, tx2 + 5, ty2 + 70], radius=2, fill=(225, 29, 72))

    tx2_c = tx2 + 16
    # Drop shadows on text for razor sharpness
    d2.text((tx2_c + 1, ty2 + 1), "碎石塵土飛揚，路況瞬息萬變。", font=font_head, fill=(0, 0, 0, 220))
    d2.text((tx2_c, ty2), "碎石塵土飛揚，路況瞬息萬變。", font=font_head, fill=(255, 255, 255))

    d2.text((tx2_c + 1, ty2 + 43), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head, fill=(0, 0, 0, 220))
    d2.text((tx2_c, ty2 + 42), "雙手穩握車把，騎乘節奏由你掌握。", font=font_head, fill=(255, 255, 255))

    p2_y = ty2 + 92
    d2.text((tx2_c + 1, p2_y + 1), "CHIBA BioXCell 手套 ｜ 為多變路況而設計", font=font_sub, fill=(0, 0, 0, 220))
    d2.text((tx2_c, p2_y), "CHIBA BioXCell 手套", font=font_sub, fill=(255, 70, 90))
    d2.text((tx2_c + tw_biox, p2_y), " ｜ 為多變路況而設計", font=font_sub, fill=(226, 232, 240))

    u2_y = p2_y + 36
    d2.text((tx2_c + 1, u2_y + 1), "探索 CHIBA 德國手套系列：www.chibataiwan.com", font=font_small, fill=(0, 0, 0, 220))
    d2.text((tx2_c, u2_y), "探索 CHIBA 德國手套系列：www.chibataiwan.com", font=font_small, fill=(160, 174, 192))

    # QR Codes on right aligned with text
    qr2_x = W - total_qr_w - 40
    qr2_y = ty2 + 14
    opt2.paste(card1_sh, (qr2_x - pad1, qr2_y - pad1), card1_sh)
    opt2.paste(card2_sh, (qr2_x + card1.width + qr_gap - pad2, qr2_y - pad2), card2_sh)

    # Save outputs with timestamp per CHIBA Standard
    timestamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M")
    name1 = f"CHIBA_Gravel_Poster_Glassmorphic_{timestamp}.jpg"
    name2 = f"CHIBA_Gravel_Poster_Cinematic_{timestamp}.jpg"

    p1_out = OUTPUT_DIR / name1
    p1_dl = DOWNLOADS_DIR / name1
    opt1.convert("RGB").save(p1_out, quality=96, optimize=True)
    opt1.convert("RGB").save(p1_dl, quality=96, optimize=True)

    p2_out = OUTPUT_DIR / name2
    p2_dl = DOWNLOADS_DIR / name2
    opt2.convert("RGB").save(p2_out, quality=96, optimize=True)
    opt2.convert("RGB").save(p2_dl, quality=96, optimize=True)

    print(f"Generated successfully:\n  Option 1 (Glassmorphic): {p1_out}\n  Option 2 (Cinematic): {p2_out}")

if __name__ == "__main__":
    render_posters()
