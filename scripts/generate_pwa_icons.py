# -*- coding: utf-8 -*-
"""
Gera ícones PNG válidos para PWA usando apenas a biblioteca padrão do Python (zlib + struct).
"""
import zlib
import struct
import math
import os

def make_png(width, height, is_maskable=False):
    # Buffer de pixels RGBA
    raw_rows = []
    
    # Cores
    bg_dark = (28, 25, 23)      # #1c1917
    bg_amber = (69, 26, 3)      # #451a03
    bg_bright = (120, 53, 15)   # #78350f
    gold_bright = (254, 240, 138) # #fef08a
    gold_mid = (245, 158, 11)     # #f59e0b
    page_color = (255, 251, 235)  # #fffbeb
    cross_color = (255, 255, 255) # white
    ribbon_color = (220, 38, 38)  # red

    cx = width / 2.0
    cy = height / 2.0
    radius = min(width, height) / 2.0

    # Margem segura se for maskable
    scale = 0.75 if is_maskable else 0.9

    for y in range(height):
        row = bytearray([0]) # filter type 0 (None)
        ny = (y - cy) / (radius * scale)
        for x in range(width):
            nx = (x - cx) / (radius * scale)
            dist = math.sqrt(nx * nx + ny * ny)

            # Gradiente de fundo
            grad_t = (y / float(height))
            r = int(bg_bright[0] * (1 - grad_t) + bg_dark[0] * grad_t)
            g = int(bg_bright[1] * (1 - grad_t) + bg_dark[1] * grad_t)
            b = int(bg_bright[2] * (1 - grad_t) + bg_dark[2] * grad_t)
            a = 255

            if not is_maskable:
                # Canto arredondado
                corner_radius = 0.25 * min(width, height)
                # Verifica bordas
                dx = max(0, abs(x - cx) - (cx - corner_radius))
                dy = max(0, abs(y - cy) - (cy - corner_radius))
                if math.sqrt(dx * dx + dy * dy) > corner_radius:
                    a = 0

            # Desenho estilizado da Bíblia aberta e Cruz (no centro)
            # Bíblia: retângulo inferior
            if -0.6 <= nx <= 0.6 and -0.1 <= ny <= 0.65:
                # Páginas
                r, g, b = page_color
                # Borda dourada
                if abs(nx) > 0.55 or ny > 0.6 or (abs(ny - (-0.1)) < 0.05 and abs(nx) > 0.05):
                    r, g, b = gold_mid
                # Linha central (costura)
                if abs(nx) < 0.04:
                    r, g, b = bg_amber
                # Fita marcadora vermelha
                if -0.05 <= nx <= 0.05 and -0.05 <= ny <= 0.75:
                    r, g, b = ribbon_color

            # Cruz no topo
            # Haste vertical
            if abs(nx) < 0.06 and -0.75 <= ny <= -0.15:
                r, g, b = cross_color
            # Haste horizontal
            elif abs(ny - (-0.5)) < 0.06 and -0.3 <= nx <= 0.3:
                r, g, b = cross_color
            # Brilho dourado ao redor da cruz
            elif math.sqrt(nx * nx + (ny - (-0.5)) * (ny - (-0.5))) < 0.45 and ny < -0.1:
                if a > 0:
                    r = min(255, r + 70)
                    g = min(255, g + 50)
                    b = min(255, b + 10)

            row.extend([r, g, b, a])
        raw_rows.append(bytes(row))

    raw_data = b"".join(raw_rows)
    compressed = zlib.compress(raw_data, 9)

    # IHDR
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    ihdr_chunk = b"IHDR" + ihdr
    ihdr_crc = struct.pack(">I", zlib.crc32(ihdr_chunk) & 0xffffffff)

    # IDAT
    idat_chunk = b"IDAT" + compressed
    idat_crc = struct.pack(">I", zlib.crc32(idat_chunk) & 0xffffffff)

    # IEND
    iend_chunk = b"IEND"
    iend_crc = struct.pack(">I", zlib.crc32(iend_chunk) & 0xffffffff)

    png = (
        b"\x89PNG\r\n\x1a\n"
        + struct.pack(">I", len(ihdr)) + ihdr_chunk + ihdr_crc
        + struct.pack(">I", len(compressed)) + idat_chunk + idat_crc
        + struct.pack(">I", 0) + iend_chunk + iend_crc
    )
    return png

def main():
    os.makedirs("public", exist_ok=True)

    icons = [
        ("public/pwa-192x192.png", 192, 192, False),
        ("public/pwa-512x512.png", 512, 512, False),
        ("public/pwa-maskable-512x512.png", 512, 512, True),
        ("public/apple-touch-icon.png", 180, 180, False),
        ("public/favicon.ico", 64, 64, False), # Modern browsers accept PNG favicon or we write png data
    ]

    for path, w, h, maskable in icons:
        png_data = make_png(w, h, maskable)
        with open(path, "wb") as f:
            f.write(png_data)
        print(f"Gerado {path} ({w}x{h}, {len(png_data)} bytes)")

if __name__ == "__main__":
    main()
