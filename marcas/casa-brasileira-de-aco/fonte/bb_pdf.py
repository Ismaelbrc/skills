# -*- coding: utf-8 -*-
import asyncio, pathlib
from playwright.async_api import async_playwright

D = pathlib.Path(__file__).parent
SRC = D / "CASA_BRASILEIRA_brandbook.html"
OUT = D / "CASA_BRASILEIRA_brandbook.pdf"

RODAPE = """
<div style="width:100%;font-family:ui-monospace,monospace;font-size:7pt;
 letter-spacing:.08em;color:#8A8B90;padding:0 15mm;display:flex;
 justify-content:space-between;-webkit-print-color-adjust:exact">
  <span>CASA BRASILEIRA DE A&Ccedil;O &middot; BRANDBOOK &middot; ED.1</span>
  <span class="pageNumber"></span>
</div>"""
VAZIO = '<div style="display:none"></div>'


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(
            executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = await b.new_page()
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(SRC.as_uri(), wait_until="networkidle")
        await pg.emulate_media(media="print")
        await pg.wait_for_timeout(1400)
        await pg.pdf(path=str(OUT), format="A4", print_background=True,
                     display_header_footer=True,
                     header_template=VAZIO, footer_template=RODAPE,
                     margin={"top": "15mm", "bottom": "16mm",
                             "left": "15mm", "right": "15mm"})
        await b.close()
        print("erros:", len(errs), errs[:4])
    print("pdf:", OUT.stat().st_size, "bytes")

asyncio.run(main())
