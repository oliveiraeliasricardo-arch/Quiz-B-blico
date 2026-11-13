# -*- coding: utf-8 -*-
"""
Empacota dist/ em um único arquivo HTML 100% autônomo (single-file HTML)
capaz de rodar com dois cliques em qualquer navegador sem servidor (file:// ou http://).
"""
import glob
import os
import re

def build_standalone():
    if not os.path.exists('dist/index.html'):
        print("dist/index.html não encontrado. Rode npm run build primeiro.")
        return

    with open('dist/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    css_files = glob.glob('dist/assets/*.css')
    js_files = glob.glob('dist/assets/*.js')

    if not css_files or not js_files:
        print("Arquivos css/js não encontrados em dist/assets/")
        return

    with open(css_files[0], 'r', encoding='utf-8') as f:
        css = f.read()

    with open(js_files[0], 'r', encoding='utf-8') as f:
        js = f.read()

    # Escapa qualquer sequência </script> acidental dentro de strings JS
    js_safe = js.replace('</script>', '<\\/script>').replace('</SCRIPT>', '<\\/SCRIPT>')

    # Remove referências externas que dependem de servidor (/manifest.webmanifest, /registerSW.js, /apple-touch-icon, etc.)
    html = re.sub(r'<link rel="manifest"[^>]*>', '', html)
    html = re.sub(r'<script id="vite-plugin-pwa:register-sw"[^>]*></script>', '', html)
    html = re.sub(r'<link rel="apple-touch-icon"[^>]*>', '', html)
    html = re.sub(r'<link rel="alternate icon"[^>]*>', '', html)

    # Embute icon.svg como data URI se existir
    if os.path.exists('public/icon.svg'):
        import base64
        with open('public/icon.svg', 'rb') as f:
            svg_b64 = base64.b64encode(f.read()).decode('ascii')
        html = re.sub(
            r'<link rel="icon" type="image/svg\+xml" href="/icon\.svg"\s*/?>',
            f'<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,{svg_b64}" />',
            html
        )

    # Substitui tag do CSS por <style> inline no <head>
    html = re.sub(
        r'<link rel="stylesheet"[^>]+href="/assets/[^"]+"\s*/?>',
        lambda m: f'<style>\n{css}\n</style>',
        html
    )

    # Remove o script do <head> para injetar depois de <div id="root"></div> no final do <body>
    html = re.sub(r'<script type="module"[^>]+src="/assets/[^"]+"></script>', '', html)

    # Injeta o JS compilado antes de </body> (garante que #root já existe no DOM)
    html = html.replace('</body>', f'<script>\n{js_safe}\n</script>\n</body>')

    os.makedirs('public', exist_ok=True)
    out_public = 'public/quiz-biblico-standalone.html'
    out_dist = 'dist/quiz-biblico-standalone.html'

    with open(out_public, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(out_dist, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Sucesso! Gerado arquivo autônomo: {out_public} ({len(html)} bytes)")

if __name__ == '__main__':
    build_standalone()
