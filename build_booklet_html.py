import os
import sys
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

md_path = r"C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Robotics\Robotics senior course\book\Robotics_Senior_Self_Learning_Booklet.md"
output_path = r"c:\Users\rowan\Desktop\meeting\robotics-book-demo.html"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
toc_items = []
section_counter = 0

def slugify(s):
    s = re.sub(r'[^\w\s\u0600-\u06FF-]', '', s).strip()
    s = re.sub(r'[\s]+', '-', s)
    return s or f"sec-{section_counter}"

def render_markdown_inline(line):
    # Links: [text](url)
    line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" class="text-amber-600 hover:text-amber-800 underline font-medium">\1</a>', line)
    
    # Bold italic
    line = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', line)
    # Bold
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-bold text-slate-900">\1</strong>', line)
    # Italic
    line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
    # Inline code
    line = re.sub(r'`([^`]+)`', r'<code class="bg-slate-100 text-amber-700 px-1.5 py-0.5 rounded border border-slate-200 font-mono text-xs font-semibold">\1</code>', line)
    
    return line

def get_component_image(cell_text):
    cell_lower = cell_text.lower()
    if 'arduino' in cell_lower or 'أردوينو' in cell_text:
        return './images/arduino_uno.jpg'
    elif 'l298n' in cell_lower or 'مواجه المحركات' in cell_text or 'مشغل المحركات' in cell_text:
        return './images/L298N_L298_Motor_Driver_Module_Arduino_Motor_Driver_in_karachi_islamabad.jpg'
    elif 'ultrasonic' in cell_lower or 'hc-sr04' in cell_lower or 'فوق الصوتية' in cell_text:
        return './images/ultrasonic.jpg'
    elif '7-segment' in cell_lower or 'سباعية' in cell_text:
        return './images/7segment.png'
    elif 'buzzer' in cell_lower or 'بازر' in cell_text or 'طنان' in cell_text:
        return './images/buzzer_new.jpg'
    elif 'push button' in cell_lower or 'زر ضاغط' in cell_text or 'مفتاح ضاغط' in cell_text:
        return './images/push_button.jpg'
    elif 'servo' in cell_lower or 'سيرفو' in cell_text:
        return './images/servo.jpg'
    elif 'pir' in cell_lower or 'حركة' in cell_text:
        return './images/pir with 2led and buzzer.png'
    elif 'flame' in cell_lower or 'لهب' in cell_text:
        return './images/ir sensor with 2led and buzzer.png'
    elif 'led' in cell_lower or 'ليد' in cell_text:
        return './images/led.png'
    return None

def render_table(lines_table):
    if not lines_table:
        return ""
    headers = [c.strip() for c in lines_table[0].strip('|').split('|')]
    rows = []
    for line in lines_table[2:]:
        if not line.strip():
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(cells)
    
    out = ['<div class="overflow-x-auto my-6 rounded-2xl border border-slate-200 shadow-sm"><table class="w-full text-right border-collapse bg-white text-xs">']
    out.append('<thead class="bg-slate-900 text-amber-400 font-bold uppercase border-b border-slate-800"><tr>')
    out.append('<th class="py-3.5 px-4 text-xs tracking-wider">صورة/المكون</th>')
    for h in headers:
        out.append(f'<th class="py-3.5 px-4 text-xs tracking-wider">{render_markdown_inline(h)}</th>')
    out.append('</tr></thead><tbody class="divide-y divide-slate-100 text-slate-700">')
    
    for r_idx, r in enumerate(rows):
        bg = 'bg-slate-50/50' if r_idx % 2 == 1 else 'bg-white'
        first_cell_text = r[0] if len(r) > 0 else ''
        img_url = get_component_image(first_cell_text)
        
        out.append(f'<tr class="{bg} hover:bg-amber-50/40 transition">')
        if img_url:
            img_html = f'<div class="w-12 h-12 rounded-xl bg-white p-1 border border-slate-200 shadow-2xs flex items-center justify-center shrink-0 cursor-pointer" onclick="openLightbox(\'{img_url}\', \'{html.escape(first_cell_text)}\')"><img src="{img_url}" class="max-h-full max-w-full object-contain rounded"></div>'
        else:
            img_html = '<div class="w-10 h-10 rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center text-slate-400 font-bold text-xs">⚙️</div>'
            
        out.append(f'<td class="py-2.5 px-3 align-middle">{img_html}</td>')
        for cell in r:
            out.append(f'<td class="py-3 px-4 leading-relaxed font-normal align-middle">{render_markdown_inline(cell)}</td>')
        out.append('</tr>')
    out.append('</tbody></table></div>')
    return ''.join(out)

body_html = []
i = 0
n = len(lines)

in_code_block = False
code_block_lang = ""
code_block_lines = []
in_table = False
table_lines = []

while i < n:
    line = lines[i]
    line_s = line.strip()
    
    # Code blocks
    if line_s.startswith('```'):
        if not in_code_block:
            in_code_block = True
            code_block_lang = line_s[3:].strip() or 'cpp'
            code_block_lines = []
            i += 1
            continue
        else:
            in_code_block = False
            code_code = html.escape('\n'.join(code_block_lines))
            code_id = f"code-box-{len(body_html)}"
            body_html.append(f'''
<div class="my-6 rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-lg text-left text-xs font-mono group relative">
    <div class="bg-slate-900 px-4 py-2.5 flex items-center justify-between border-b border-slate-800 text-slate-400 font-mono text-[11px]">
        <span class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
            <span class="font-bold text-amber-400 ml-2">{code_block_lang.upper()} Sketch</span>
        </span>
        <button onclick="copyToClipboard('{code_id}', this)" class="bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-slate-300 px-3 py-1 rounded-xl text-[10px] font-bold transition flex items-center gap-1 shadow-2xs">
            <span>📋 نسخ الكود البرمجي</span>
        </button>
    </div>
    <pre class="p-4 overflow-x-auto text-amber-200 leading-relaxed"><code id="{code_id}" class="language-{code_block_lang}">{code_code}</code></pre>
</div>
''')
            i += 1
            continue
            
    if in_code_block:
        code_block_lines.append(line)
        i += 1
        continue

    # Tables
    if line_s.startswith('|') and '|' in line_s[1:]:
        if not in_table:
            in_table = True
            table_lines = [line_s]
        else:
            table_lines.append(line_s)
        i += 1
        continue
    else:
        if in_table:
            in_table = False
            body_html.append(render_table(table_lines))
            table_lines = []

    # Headings
    if line_s.startswith('#'):
        m = re.match(r'^(#{1,4})\s+(.*)$', line_s)
        if m:
            level = len(m.group(1))
            htext = m.group(2).strip()
            section_counter += 1
            sec_id = slugify(htext)
            
            if level in [1, 2, 3]:
                toc_items.append((level, htext, sec_id))
            
            if level == 1:
                body_html.append(f'''
<div id="{sec_id}" class="scroll-mt-24 mt-12 mb-6 pb-4 border-b-2 border-amber-500 flex items-center gap-3">
    <div class="p-3 bg-amber-500/10 text-amber-600 rounded-2xl border border-amber-500/20 text-2xl font-bold">📘</div>
    <div>
        <h1 class="text-2xl md:text-3xl font-black text-slate-900 tracking-tight">{render_markdown_inline(htext)}</h1>
        <p class="text-xs text-slate-500 font-medium mt-0.5">قسم رئيسي في مسار السينيور • كتيب التعلم الذاتي</p>
    </div>
</div>
''')
            elif level == 2:
                body_html.append(f'''
<div id="{sec_id}" class="scroll-mt-24 mt-10 mb-4 pb-2 border-b border-slate-200 flex items-center gap-2">
    <span class="w-2.5 h-6 bg-amber-500 rounded-full inline-block"></span>
    <h2 class="text-xl md:text-2xl font-bold text-slate-800">{render_markdown_inline(htext)}</h2>
</div>
''')
            elif level == 3:
                # Check if heading mentions a component we have an image for
                comp_img = get_component_image(htext)
                img_side_html = ""
                if comp_img:
                    img_side_html = f'<img src="{comp_img}" class="w-10 h-10 object-contain rounded-lg border border-slate-200 bg-white p-0.5 cursor-pointer shadow-2xs ml-2" onclick="openLightbox(\'{comp_img}\', \'{html.escape(htext)}\')">'

                body_html.append(f'''
<div id="{sec_id}" class="scroll-mt-24 mt-8 mb-3 flex items-center justify-between">
    <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
        <span class="text-amber-500 text-base">◈</span>
        <span>{render_markdown_inline(htext)}</span>
    </h3>
    {img_side_html}
</div>
''')
            else:
                body_html.append(f'''
<h4 id="{sec_id}" class="scroll-mt-24 mt-6 mb-2 text-base font-bold text-slate-700">{render_markdown_inline(htext)}</h4>
''')
            i += 1
            continue

    # Blockquotes / Alerts
    if line_s.startswith('>'):
        quote_text = render_markdown_inline(line_s.lstrip('> ').strip())
        bg_class = "bg-amber-50/80 border-amber-400 text-amber-900"
        icon = "💡"
        if "⚠️" in line_s or "تنبيه" in line_s or "أمان" in line_s:
            bg_class = "bg-red-50/90 border-red-400 text-red-950"
            icon = "⚠️"
        elif "📝" in line_s or "واجب" in line_s or "تحدي" in line_s:
            bg_class = "bg-blue-50/90 border-blue-400 text-blue-950"
            icon = "📝"
        elif "🔧" in line_s or "خطوة" in line_s:
            bg_class = "bg-emerald-50/90 border-emerald-400 text-emerald-950"
            icon = "🔧"

        body_html.append(f'''
<div class="my-4 p-4 rounded-2xl border-r-4 {bg_class} shadow-2xs flex items-start gap-3">
    <span class="text-xl shrink-0">{icon}</span>
    <div class="text-xs md:text-sm leading-relaxed font-medium">{quote_text}</div>
</div>
''')
        i += 1
        continue

    # Empty lines
    if not line_s:
        i += 1
        continue

    # Horizontal rules
    if line_s in ['---', '***', '___']:
        body_html.append('<hr class="my-8 border-slate-200">')
        i += 1
        continue

    # Unordered / Ordered Lists
    if line_s.startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.\s+', line_s):
        list_items = []
        is_ordered = bool(re.match(r'^\d+\.\s+', line_s))
        
        while i < n and (lines[i].strip().startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.\s+', lines[i].strip())):
            item_str = lines[i].strip()
            item_content = re.sub(r'^(?:[-*+]||\d+\.)\s+', '', item_str)
            list_items.append(f'<li class="leading-relaxed">{render_markdown_inline(item_content)}</li>')
            i += 1
            
        tag = 'ol' if is_ordered else 'ul'
        list_class = "list-decimal pr-6 space-y-1.5 text-xs md:text-sm text-slate-700 my-3 font-normal" if is_ordered else "list-disc pr-6 space-y-1.5 text-xs md:text-sm text-slate-700 my-3 font-normal"
        body_html.append(f'<{tag} class="{list_class}">{"".join(list_items)}</{tag}>')
        continue

    # Paragraph
    body_html.append(f'<p class="text-xs md:text-sm text-slate-700 leading-relaxed my-3 font-normal">{render_markdown_inline(line_s)}</p>')
    i += 1

if in_table:
    body_html.append(render_table(table_lines))

# Build TOC HTML
toc_html = []
for level, htext, sec_id in toc_items:
    clean_title = re.sub(r'<[^>]+>', '', render_markdown_inline(htext))
    if level == 1:
        toc_html.append(f'''
<div class="mt-4 first:mt-0 font-bold text-xs text-amber-700 px-3 py-1 bg-amber-50 rounded-lg border border-amber-200/60 truncate">
    <a href="#{sec_id}" class="hover:text-amber-900 transition flex items-center gap-1.5">
        <span>📌</span>
        <span class="truncate">{clean_title}</span>
    </a>
</div>
''')
    elif level == 2:
        toc_html.append(f'''
<a href="#{sec_id}" class="toc-link block text-[11px] font-medium text-slate-600 hover:text-amber-600 hover:bg-slate-100 px-3 py-1 rounded-md transition truncate pr-5 border-r border-slate-200">
    {clean_title}
</a>
''')
    elif level == 3:
        toc_html.append(f'''
<a href="#{sec_id}" class="toc-link block text-[10px] text-slate-500 hover:text-amber-600 hover:bg-slate-100 px-3 py-0.5 rounded-md transition truncate pr-8 border-r border-slate-100">
    • {clean_title}
</a>
''')

full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>كتيب التعليم الذاتي الشامل - مسار الروبوتكس السينيور | Megaminds Academy</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Cairo -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <!-- KaTeX CDN for math formulas -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

    <style>
        body {{
            font-family: 'Cairo', system-ui, -apple-system, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #f1f5f9;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #94a3b8;
        }}
        @media print {{
            .no-print {{ display: none !important; }}
            .print-content {{ margin: 0 !important; width: 100% !important; }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-amber-500 selection:text-white">

    <!-- Top Header Navigation -->
    <header class="sticky top-0 z-40 bg-slate-900/95 backdrop-blur-md text-white border-b border-slate-800 shadow-md no-print">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="./index.html" class="bg-slate-800 hover:bg-slate-700 text-amber-400 p-2 rounded-xl transition border border-slate-700 flex items-center gap-1.5 text-xs font-bold">
                    <span>🔙</span>
                    <span class="hidden sm:inline">العودة للوحة القيادة</span>
                </a>
                <div class="h-6 w-px bg-slate-700 hidden sm:block"></div>
                <div>
                    <h1 class="text-sm sm:text-base font-black text-white tracking-tight flex items-center gap-2">
                        <span>🤖</span>
                        <span>كتيب أساسيات الروبوتكس والإلكترونيات الذكية</span>
                    </h1>
                    <p class="text-[10px] text-amber-400 font-semibold">Megaminds Academy • Senior Robotics Track (Ages 10-16+)</p>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center gap-2">
                <div class="relative hidden md:block w-64">
                    <input type="text" id="searchInput" onkeyup="filterContent()" placeholder="بحث في الكتيب والدروس..." class="w-full bg-slate-800 text-xs text-white placeholder-slate-400 rounded-xl px-3 py-1.5 pr-8 border border-slate-700 focus:outline-none focus:border-amber-400 transition">
                    <span class="absolute right-2.5 top-2 text-xs text-slate-400">🔍</span>
                </div>
                <a href="https://notebook.google.com/notebook/ba068196-9886-49eb-bca3-f33718919c77/artifact/8c2b324a-d227-4a20-a025-a06a442c6c7a?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_" target="_blank" class="bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
                    <span>📘</span>
                    <span class="hidden sm:inline">Google Notebook</span>
                </a>
                <button onclick="window.print()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 p-2 rounded-xl text-xs font-bold border border-slate-700 transition" title="طباعة الكتيب">
                    🖨️
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <div class="max-w-7xl mx-auto px-4 py-6 flex flex-col md:flex-row gap-6">
        
        <!-- Sidebar Navigation Drawer -->
        <aside class="w-full md:w-80 shrink-0 no-print">
            <div class="sticky top-20 bg-white p-4 rounded-2xl border border-slate-200 shadow-sm max-h-[calc(100vh-6rem)] overflow-y-auto space-y-3">
                <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                    <h2 class="font-bold text-slate-900 text-xs flex items-center gap-1.5">
                        <span>📑</span>
                        <span>فهرس الدروس والمستويات</span>
                    </h2>
                    <span class="text-[10px] bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full font-bold">7 فصول</span>
                </div>

                <div class="md:hidden">
                    <input type="text" onkeyup="filterContentMobile(this.value)" placeholder="بحث سريع..." class="w-full bg-slate-50 text-xs border border-slate-200 rounded-xl px-3 py-1.5 text-slate-800">
                </div>

                <nav id="tocNav" class="space-y-1">
                    {"".join(toc_html)}
                </nav>
            </div>
        </aside>

        <!-- Main Book Content Area -->
        <main class="flex-1 bg-white p-6 sm:p-10 rounded-3xl border border-slate-200 shadow-sm print-content overflow-hidden">
            
            <!-- Book Header Banner -->
            <div class="mb-10 p-6 sm:p-8 bg-gradient-to-r from-slate-900 via-slate-800 to-amber-950 rounded-3xl text-white shadow-xl relative overflow-hidden">
                <div class="absolute -left-10 -bottom-10 opacity-10 text-9xl select-none font-mono">ROBOTICS</div>
                <div class="relative z-10">
                    <div class="inline-flex items-center gap-2 bg-amber-500/20 text-amber-300 text-xs font-bold px-3 py-1 rounded-full border border-amber-400/30 mb-3">
                        ⚡ المنهج المعتمد • مسار السينيور 2026
                    </div>
                    <h1 class="text-2xl sm:text-4xl font-black text-white leading-tight tracking-tight">
                        دليل المبتكر الشامل في الروبوتكس والإلكترونيات الذكية
                    </h1>
                    <p class="text-xs sm:text-sm text-slate-300 font-medium mt-2 max-w-2xl leading-relaxed">
                        من الصفر حتى صناعة روبوت متنقل ذكي مجهز بحساسات الألتراسونيك والتحكم اللاسلكي عبر البلوتوث للهواتف الذكية.
                    </p>
                    <div class="mt-6 flex flex-wrap gap-3 text-xs font-semibold">
                        <span class="bg-slate-800/80 text-amber-400 px-3 py-1.5 rounded-xl border border-slate-700/60">👨‍💻 الأعمار: 10 - 16+ سنة</span>
                        <span class="bg-slate-800/80 text-amber-400 px-3 py-1.5 rounded-xl border border-slate-700/60">🔬 7 مستويات تطبيقية</span>
                        <span class="bg-slate-800/80 text-amber-400 px-3 py-1.5 rounded-xl border border-slate-700/60">📜 إجابات وتصحيح ذاتي</span>
                    </div>
                </div>
            </div>

            <!-- Rendered Markdown Body -->
            <div id="bookBody" class="prose prose-slate max-w-none">
                {"".join(body_html)}
            </div>

        </main>
    </div>

    <!-- Image Lightbox Modal -->
    <div id="lightbox" class="fixed inset-0 z-50 bg-slate-950/90 hidden items-center justify-center p-4 backdrop-blur-sm no-print" onclick="closeLightbox()">
        <div class="relative max-w-4xl max-h-[90vh] bg-white rounded-3xl overflow-hidden p-2 shadow-2xl flex flex-col items-center" onclick="event.stopPropagation()">
            <button onclick="closeLightbox()" class="absolute top-4 left-4 bg-slate-900/80 text-white hover:bg-red-600 w-9 h-9 rounded-full font-bold flex items-center justify-center text-sm transition">✕</button>
            <img id="lightboxImg" src="" alt="" class="max-h-[80vh] max-w-full object-contain rounded-2xl">
            <p id="lightboxCaption" class="text-xs font-bold text-slate-700 mt-3 mb-1 text-center"></p>
        </div>
    </div>

    <!-- JavaScript Controls -->
    <script>
        function copyToClipboard(elementId, btn) {{
            const el = document.getElementById(elementId);
            if (!el) return;
            navigator.clipboard.writeText(el.innerText).then(() => {{
                const originalText = btn.innerHTML;
                btn.innerHTML = '✅ تم النسخ!';
                btn.classList.add('bg-green-600', 'text-white');
                setTimeout(() => {{
                    btn.innerHTML = originalText;
                    btn.classList.remove('bg-green-600', 'text-white');
                }}, 2000);
            }});
        }}

        function openLightbox(src, caption) {{
            document.getElementById('lightboxImg').src = src;
            document.getElementById('lightboxCaption').innerText = caption || '';
            const lb = document.getElementById('lightbox');
            lb.classList.remove('hidden');
            lb.classList.add('flex');
        }}

        function closeLightbox() {{
            const lb = document.getElementById('lightbox');
            lb.classList.add('hidden');
            lb.classList.remove('flex');
        }}

        function filterContent() {{
            const query = document.getElementById('searchInput').value.toLowerCase();
            const paragraphs = document.querySelectorAll('#bookBody > p, #bookBody > div, #bookBody > ul, #bookBody > ol');
            paragraphs.forEach(el => {{
                if (!query || el.innerText.toLowerCase().includes(query)) {{
                    el.style.display = '';
                }} else {{
                    el.style.display = 'none';
                }}
            }});
        }}

        function filterContentMobile(query) {{
            document.getElementById('searchInput').value = query;
            filterContent();
        }}
    </script>
</body>
</html>
'''

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Successfully generated {output_path} with {len(full_html)} characters and integrated images.")
