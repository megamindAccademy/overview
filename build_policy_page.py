import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

output_path = r"c:\Users\rowan\Desktop\meeting\engineering-policy-update.html"

html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>دليل وسياسات مهندسي الأكاديمية • تحديثات مواقف السيستم | Megaminds Academy</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Cairo -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Cairo', system-ui, -apple-system, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
        }
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
        @media print {
            .no-print { display: none !important; }
            .print-content { margin: 0 !important; width: 100% !important; }
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-emerald-500 selection:text-white">

    <!-- Top Header Navigation -->
    <header class="sticky top-0 z-40 bg-slate-900/95 backdrop-blur-md text-white border-b border-slate-800 shadow-md no-print">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="./index.html" class="bg-slate-800 hover:bg-slate-700 text-emerald-400 p-2 rounded-xl transition border border-slate-700 flex items-center gap-1.5 text-xs font-bold">
                    <span>🔙</span>
                    <span class="hidden sm:inline">العودة للوحة القيادة</span>
                </a>
                <div class="h-6 w-px bg-slate-700 hidden sm:block"></div>
                <div>
                    <h1 class="text-sm sm:text-base font-black text-white tracking-tight flex items-center gap-2">
                        <span>🎓</span>
                        <span>دليل وسياسات مهندسي الأكاديمية (تحديثات المواقف التشغيلية)</span>
                    </h1>
                    <p class="text-[10px] text-emerald-400 font-semibold">Megaminds Academy • Educational Directorate & Engineering Policy</p>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center gap-2">
                <a href="https://megamindaccademy.github.io/Engineering-policy/" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
                    <span>🌐</span>
                    <span class="hidden sm:inline">موقع السياسات الخارجي</span>
                </a>
                <button onclick="window.print()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 p-2 rounded-xl text-xs font-bold border border-slate-700 transition" title="طباعة الدليل">
                    🖨️
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <div class="max-w-6xl mx-auto px-4 py-8 space-y-8">

        <!-- Banner Header -->
        <div class="p-6 sm:p-8 bg-gradient-to-r from-slate-900 via-slate-800 to-emerald-950 rounded-3xl text-white shadow-xl relative overflow-hidden">
            <div class="absolute -left-10 -bottom-10 opacity-10 text-9xl select-none font-mono">POLICY</div>
            <div class="relative z-10 space-y-3">
                <div class="inline-flex items-center gap-2 bg-emerald-500/20 text-emerald-300 text-xs font-bold px-3 py-1 rounded-full border border-emerald-400/30">
                    ⚙️ التحديث المعتمد لسيستم الأكاديمية الجديد 2026
                </div>
                <h1 class="text-2xl sm:text-4xl font-black text-white leading-tight tracking-tight">
                    إعادة صياغة ودليل المواقف التشغيلية لمهندس الأكاديمية
                </h1>
                <p class="text-xs sm:text-sm text-slate-300 font-medium max-w-3xl leading-relaxed">
                    مستند تفصيلي يوضح كافة المواقف والسيناريوهات التشغيلية للمهندسين: التعديلات الجديدة في السيستم، الإجراءات المستمرة بدون تغيير، والمواقف المضافة حديثاً، مع إبراز النظرة التنفيذية لمراجعة الـ CEO.
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs font-bold">
                    <span class="bg-slate-800/90 text-blue-300 px-3 py-1 rounded-lg border border-slate-700">🔵 موقف بدون تغيير (نفس الكلام)</span>
                    <span class="bg-slate-800/90 text-amber-300 px-3 py-1 rounded-lg border border-slate-700">🟡 موقف معدّل (تحديث السيستم)</span>
                    <span class="bg-slate-800/90 text-emerald-300 px-3 py-1 rounded-lg border border-slate-700">🟢 موقف جديد مضاف</span>
                    <span class="bg-slate-800/90 text-red-300 px-3 py-1 rounded-lg border border-slate-700">🚨 نقطة مراجعة واعتماد CEO</span>
                </div>
            </div>
        </div>

        <!-- Interactive Filter Controls -->
        <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4 no-print">
            <!-- Filter Buttons -->
            <div class="flex flex-wrap items-center gap-2">
                <button onclick="filterType('all')" id="btn-all" class="filter-btn active bg-slate-900 text-white text-xs font-bold px-4 py-2 rounded-xl border border-slate-800 transition">
                    📋 جميع المواقف (10)
                </button>
                <button onclick="filterType('modified')" id="btn-modified" class="filter-btn bg-amber-50 text-amber-900 hover:bg-amber-100 text-xs font-bold px-4 py-2 rounded-xl border border-amber-200 transition">
                    🟡 مواقف معدّلة (3)
                </button>
                <button onclick="filterType('unchanged')" id="btn-unchanged" class="filter-btn bg-blue-50 text-blue-900 hover:bg-blue-100 text-xs font-bold px-4 py-2 rounded-xl border border-blue-200 transition">
                    🔵 بدون تغيير / نفس الكلام (4)
                </button>
                <button onclick="filterType('added')" id="btn-added" class="filter-btn bg-emerald-50 text-emerald-900 hover:bg-emerald-100 text-xs font-bold px-4 py-2 rounded-xl border border-emerald-200 transition">
                    🟢 مواقف جديدة مضافة (3)
                </button>
            </div>
            <!-- Search Box -->
            <div class="w-full md:w-64 relative">
                <input type="text" id="policySearch" onkeyup="searchPolicy()" placeholder="بحث في المواقف والسيناريوهات..." class="w-full bg-slate-50 text-xs text-slate-800 placeholder-slate-400 rounded-xl px-3 py-2 pr-8 border border-slate-200 focus:outline-none focus:border-emerald-500 transition">
                <span class="absolute right-2.5 top-2.5 text-xs text-slate-400">🔍</span>
            </div>
        </div>

        <!-- CEO Urgent Review Alert Callout Card -->
        <div class="bg-gradient-to-r from-red-900/90 via-slate-900 to-slate-950 p-6 rounded-3xl border border-red-500/40 text-white shadow-lg space-y-3">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <span class="text-2xl">🚨</span>
                    <h3 class="font-black text-red-200 text-base">نقطة عاجلة محتاجة مراجعة وتأكيد م. أحمد (CEO)</h3>
                </div>
                <span class="text-xs bg-red-500/20 text-red-300 border border-red-400/30 px-3 py-1 rounded-full font-bold">الموقف الأول: غياب الطلاب</span>
            </div>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-medium">
                في السيستم الجديد، بمجرد أن يضغط المهندس على زر بدء الجلسة (<code class="text-amber-300 font-mono">Start Session</code>)، فإن الضغط لاحقاً على زر إنهاء الجلسة (<code class="text-amber-300 font-mono">Finish Session</code>) ينهي الجلسة ويحتسبها تقنياً كجلسة كاملة ومكتملة (<code class="text-emerald-300 font-mono">Finished Session</code>).
            </p>
            <div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-800 space-y-2 text-xs">
                <strong class="text-amber-400 font-bold block">الخياران المعروضان للتأكيد الإداري من م. أحمد CEO:</strong>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-slate-300 mt-2">
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800/80 space-y-1">
                        <strong class="text-emerald-400 font-bold block">الخيار الأول (أ): بدء وإنهاء السيشن بالسيستم</strong>
                        <p class="text-[11px] leading-relaxed text-slate-400">
                            يدخل المهندس الغرفة، يضغط <code class="text-slate-200">Start Session</code>، ينظر 15 دقيقة، وإذا لم يحضر أحد يضغط <code class="text-slate-200">Finish Session</code> لتسجيل الانتهاء التلقائي في السيستم.
                        </p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800/80 space-y-1">
                        <strong class="text-amber-400 font-bold block">الخيار الثاني (ب): عدم الضغط والإلغاء الإداري</strong>
                        <p class="text-[11px] leading-relaxed text-slate-400">
                            ينتظر المهندس 15 دقيقة دون الضغط على <code class="text-slate-200">Start Session</code>، ويكتفي بإبلاغ الإدارة إلغاء الجلسة لعدم الحضور دون تمكين أزرار التشغيل تقنياً.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Situations Matrix Grid -->
        <div id="situationsGrid" class="space-y-6">

            <!-- SITUATION 1 -->
            <div class="situation-card type-modified bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-amber-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm shrink-0">1</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الأول: غياب جميع الطلاب عن موعد السيشن</h3>
                            <p class="text-xs text-slate-500">عدم دخول أي طالب لغرفة الاجتماع بعد موعد بدء الجلسة الرسمي</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs bg-blue-50 text-blue-800 px-3 py-1 rounded-full border border-blue-200 font-bold">🔵 الانتظار: نفس الكلام</span>
                        <span class="text-xs bg-amber-50 text-amber-900 px-3 py-1 rounded-full border border-amber-200 font-bold">🟡 الإلغاء: معدّل تقنياً</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs leading-relaxed">
                    <!-- Unchanged Wait Policy -->
                    <div class="p-4 bg-blue-50/60 rounded-2xl border border-blue-200/80 space-y-2">
                        <div class="flex items-center justify-between">
                            <strong class="text-blue-900 font-bold flex items-center gap-1.5">
                                <span>⏱️</span>
                                <span>فترة الانتظار (نفس الكلام - بدون تغيير):</span>
                            </strong>
                            <span class="text-[10px] bg-blue-200/70 text-blue-950 px-2 py-0.5 rounded font-bold">15 دقيقة ثابتة</span>
                        </div>
                        <p class="text-blue-950 font-medium">
                            يلتزم المهندس بالانتظار داخل غرفة الميتنج لمدة <strong>15 دقيقة كاملة</strong> من بداية الموعد الرسمي، مع التأكد من جاهزية المايك والشاشة وعدم مغادرة الغرفة إطلاقاً قبل انقضاء الـ 15 دقيقة.
                        </p>
                    </div>

                    <!-- Modified Cancellation & System Mechanics -->
                    <div class="p-4 bg-amber-50/60 rounded-2xl border border-amber-200/80 space-y-2">
                        <div class="flex items-center justify-between">
                            <strong class="text-amber-900 font-bold flex items-center gap-1.5">
                                <span>⚙️</span>
                                <span>آلية الإلغاء (تحديث السيستم الجديد):</span>
                            </strong>
                            <span class="text-[10px] bg-red-200/70 text-red-950 px-2 py-0.5 rounded font-bold">🚨 بانتظار مراجعة CEO</span>
                        </div>
                        <p class="text-amber-950 font-medium">
                            في السيستم الجديد، بمجرد الضغط على <code class="bg-amber-100 text-amber-900 px-1 rounded border border-amber-300">Start Session</code> وثم <code class="bg-amber-100 text-amber-900 px-1 rounded border border-amber-300">Finish Session</code> تعتبر السيشن منتهية ومحسوبة. محتاجين مراجعة وتأكيد م. أحمد CEO في طريقة إغلاقها تقنياً.
                        </p>
                    </div>
                </div>
            </div>

            <!-- SITUATION 2 -->
            <div class="situation-card type-modified bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-amber-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm shrink-0">2</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الثاني: تأخر المهندس عن موعد الجلسة الرسمية</h3>
                            <p class="text-xs text-slate-500">تسجيل دخول المهندس بعد الموعد المجدول في اللوحة</p>
                        </div>
                    </div>
                    <span class="text-xs bg-amber-50 text-amber-900 px-3 py-1 rounded-full border border-amber-200 font-bold">🟡 موقف معدّل (تحديث السيستم)</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs leading-relaxed">
                    <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-1">
                        <strong class="text-slate-700 font-bold block">الإجراء السابق:</strong>
                        <p class="text-slate-600">تنبيه شفهي وخصم يدوياً من السيشن عند التكرار.</p>
                    </div>
                    <div class="p-4 bg-amber-50/70 rounded-2xl border border-amber-200 space-y-1 text-amber-950">
                        <strong class="text-amber-900 font-bold block">التحديث الجديد في السيستم:</strong>
                        <p class="font-medium">
                            يتم رصد زمن الضغط على <code class="bg-amber-100 px-1 rounded">Start Session</code> بالدقيقة. التأخر أكثر من 5 دقائق يرسل تنبيهاً أوتوماتيكياً للمشرف، والتأخر لأكثر من 15 دقيقة يوجب التعويض مجاناً وتطبيق مصفوفة اللوائح.
                        </p>
                    </div>
                </div>
            </div>

            <!-- SITUATION 3 -->
            <div class="situation-card type-modified bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-amber-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm shrink-0">3</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الثالث: حفظ ونقل تسجيلات الجلسات (Google Meet Recordings)</h3>
                            <p class="text-xs text-slate-500">إدارة فيديوهات السيشن وتفادي عشوائية مجلدات Drive</p>
                        </div>
                    </div>
                    <span class="text-xs bg-amber-50 text-amber-900 px-3 py-1 rounded-full border border-amber-200 font-bold">🟡 موقف معدّل (بروتوكول جديد)</span>
                </div>

                <div class="p-4 bg-amber-50/70 rounded-2xl border border-amber-200 text-xs text-amber-950 space-y-2">
                    <strong class="text-amber-950 font-bold block">البروتوكول التشغيلي الجديد للتسجيلات:</strong>
                    <p class="leading-relaxed">
                        نظراً لأن Google Meet يحفظ التسجيلات عشوائياً في مجلد عام باسم <code class="bg-amber-100 px-1 rounded font-mono">Google Meet Recordings</code> (سعة 5TB)، <strong>يلتزم المهندس بإنشاء مجلد خاص باسمه وقص ونقل الفيديو (Cut & Move) فور انتهاء السيشن مباشرةً</strong> وإعادة تسميته برقم الجروب والتاريخ لتسهيل مراجعة الكواليتي.
                    </p>
                </div>
            </div>

            <!-- SITUATION 4 -->
            <div class="situation-card type-unchanged bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-blue-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-sm shrink-0">4</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الرابع: وجود مشكلة تقنية أو عدم قدرة الطالب على الفتح</h3>
                            <p class="text-xs text-slate-500">تعطل الصوت أو الكاميرا أو المتصفح لدى أحد الطلاب أثناء الجلسة</p>
                        </div>
                    </div>
                    <span class="text-xs bg-blue-50 text-blue-900 px-3 py-1 rounded-full border border-blue-200 font-bold">🔵 نفس الكلام (بدون تغيير)</span>
                </div>

                <div class="p-4 bg-blue-50/60 rounded-2xl border border-blue-200 text-xs text-blue-950 leading-relaxed font-medium">
                    يمنع المهندس من إيقاف الجلسة أو تعطيل بقية الطلاب. يتم توجيه الطالب/ولي الأمر فوراً لرقم الدعم الفني للأكاديمية عبر الواتساب لتوليد حل تقني، مع طمأنة ولي الأمر بتزويده برابط تسجيل الجلسة كاملاً عقب انتهائها.
                </div>
            </div>

            <!-- SITUATION 5 -->
            <div class="situation-card type-added bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-emerald-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0">5</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الخامس: التحكم عن بُعد في جهاز الطالب (Remote Take Control)</h3>
                            <p class="text-xs text-slate-500">مساعدة الأطفال الصغار عند تعذر سحب البلوكات البرمجية</p>
                        </div>
                    </div>
                    <span class="text-xs bg-emerald-50 text-emerald-900 px-3 py-1 rounded-full border border-emerald-200 font-bold">🟢 موقف جديد مضاف</span>
                </div>

                <div class="p-4 bg-emerald-50/60 rounded-2xl border border-emerald-200 text-xs text-emerald-950 leading-relaxed space-y-1.5 font-medium">
                    <strong class="text-emerald-900 font-bold block">إجراء التعامل مع إضافة Chrome Remote Desktop:</strong>
                    <p>
                        في حال استخدام Google Meet، يوجه المهندس الطالب لتثبيت إضافة <code class="bg-emerald-100 text-emerald-900 px-1 rounded font-mono">Google Chrome Remote Desktop</code>، والضغط على <code class="bg-emerald-100 text-emerald-900 px-1 rounded">Generate Code</code>، وإدخال الكود لدى المهندس للمساعدة المباشرة عند الضرورة.
                    </p>
                </div>
            </div>

            <!-- SITUATION 6 -->
            <div class="situation-card type-added bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-emerald-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0">6</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف السادس: حضور طالب جديد غير مدون بقائمة الجلسة الرسمية</h3>
                            <p class="text-xs text-slate-500">دخول رابط الجلسة من طالب غير مسجل بكشف الحضور</p>
                        </div>
                    </div>
                    <span class="text-xs bg-emerald-50 text-emerald-900 px-3 py-1 rounded-full border border-emerald-200 font-bold">🟢 موقف جديد مضاف</span>
                </div>

                <div class="p-4 bg-emerald-50/60 rounded-2xl border border-emerald-200 text-xs text-emerald-950 leading-relaxed font-medium">
                    يُحظر منعاً باتاً قبول دخول أي طالب غير مدرج كشفه الرسمي بالسيستم إلا بعد مراجعة شات الدعم الفني والإدارة الفورية للتحقق من قيده بالجروب ومنع التداخل بين المجموعات.
                </div>
            </div>

            <!-- SITUATION 7 -->
            <div class="situation-card type-unchanged bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-blue-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-sm shrink-0">7</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف السابع: انقطاع الكهرباء أو الإنترنت المفاجئ لدى المهندس</h3>
                            <p class="text-xs text-slate-500">الظروف الطارئة المفاجئة أثناء البث المباشر</p>
                        </div>
                    </div>
                    <span class="text-xs bg-blue-50 text-blue-900 px-3 py-1 rounded-full border border-blue-200 font-bold">🔵 نفس الكلام (بدون تغيير)</span>
                </div>

                <div class="p-4 bg-blue-50/60 rounded-2xl border border-blue-200 text-xs text-blue-950 leading-relaxed font-medium">
                    يلتزم المهندس بالدخول من داتا الموبايل خلال أول 5 دقائق لإبلاغ جروب الواتساب الإداري، ويتم جدولة سيشن تعويضية مجانية للأطفال خلال 48 ساعة بالتنسيق مع قسم المتابعة.
                </div>
            </div>

            <!-- SITUATION 8 -->
            <div class="situation-card type-unchanged bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-blue-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-sm shrink-0">8</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف الثامن: طلب ولي الأمر تعديل موعد الجلسة بشكل فردي</h3>
                            <p class="text-xs text-slate-500">التواصل المباشر بين ولي الأمر والمهندس لتغيير المواعيد</p>
                        </div>
                    </div>
                    <span class="text-xs bg-blue-50 text-blue-900 px-3 py-1 rounded-full border border-blue-200 font-bold">🔵 نفس الكلام (بدون تغيير)</span>
                </div>

                <div class="p-4 bg-blue-50/60 rounded-2xl border border-blue-200 text-xs text-blue-950 leading-relaxed font-medium">
                    يُمنع المهندس منعاً باتاً من الاتفاق على أي مواعيد فردية مع أسر الطلاب، ويصرح دائماً بتوجيه ولي الأمر للإدارة وخدمة العملاء لتحديد المواعيد رسمياً عبر السيستم.
                </div>
            </div>

            <!-- SITUATION 9 -->
            <div class="situation-card type-added bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-emerald-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0">9</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف التاسع: متابعة وتصحيح الكويزات والواجبات التفاعلية MCQ</h3>
                            <p class="text-xs text-slate-600">اعتماد نماذج PictoBlox و Python التفاعلية بالسيستم</p>
                        </div>
                    </div>
                    <span class="text-xs bg-emerald-50 text-emerald-900 px-3 py-1 rounded-full border border-emerald-200 font-bold">🟢 موقف جديد مضاف</span>
                </div>

                <div class="p-4 bg-emerald-50/60 rounded-2xl border border-emerald-200 text-xs text-emerald-950 leading-relaxed font-medium">
                    التزام المهندس برفع وتصحيح نتائج الكويزات التفاعلية الفورية المسندة للطلاب في نهاية كل سيشن وتوثيق الدرجات بلوحة المتابعة.
                </div>
            </div>

            <!-- SITUATION 10 -->
            <div class="situation-card type-unchanged bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:border-blue-300 transition space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span class="w-9 h-9 rounded-2xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-sm shrink-0">10</span>
                        <div>
                            <h3 class="font-bold text-slate-900 text-base">الموقف العاشر: طلب المهندس لإجازة طارئة أو توفير بديل (Substitute)</h3>
                            <p class="text-xs text-slate-500">تقديم طلبات الاعتذار والتغطية الأكاديمية</p>
                        </div>
                    </div>
                    <span class="text-xs bg-blue-50 text-blue-900 px-3 py-1 rounded-full border border-blue-200 font-bold">🔵 نفس الكلام (بدون تغيير)</span>
                </div>

                <div class="p-4 bg-blue-50/60 rounded-2xl border border-blue-200 text-xs text-blue-950 leading-relaxed font-medium">
                    تقديم الطلب قبل الموعد بـ 24 ساعة على الأقل على الشات الإداري لتوفير مهندس بديل وتزويده بخطة الدرس ورقم الجلسة لضمان استمرارية التعلم.
                </div>
            </div>

        </div>

    </div>

    <!-- JavaScript Filtering & Search Script -->
    <script>
        function filterType(type) {
            // Update active button state
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('bg-slate-900', 'text-white');
                btn.classList.add('bg-slate-100', 'text-slate-700');
            });
            
            const activeBtn = document.getElementById('btn-' + type);
            if (activeBtn) {
                activeBtn.classList.remove('bg-slate-100', 'text-slate-700');
                activeBtn.classList.add('bg-slate-900', 'text-white');
            }

            const cards = document.querySelectorAll('.situation-card');
            cards.forEach(card => {
                if (type === 'all') {
                    card.style.display = '';
                } else if (type === 'modified' && card.classList.contains('type-modified')) {
                    card.style.display = '';
                } else if (type === 'unchanged' && card.classList.contains('type-unchanged')) {
                    card.style.display = '';
                } else if (type === 'added' && card.classList.contains('type-added')) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        function searchPolicy() {
            const query = document.getElementById('policySearch').value.toLowerCase();
            const cards = document.querySelectorAll('.situation-card');
            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                if (!query || text.includes(query)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
'''

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_path} with {len(html_content)} characters.")
