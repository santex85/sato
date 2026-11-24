#!/usr/bin/env python3
"""Тайские тексты лендинга через `thai write` (только так — правило компаньона). Кэш: build/th.json.
Цены-цифры не переводим (копируем). Повторный запуск переводит только недостающее."""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import C  # noqa: E402

F = os.path.join(os.path.dirname(__file__), "th.json")
th = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else {}
KEEP = {"p1_v", "p2_v", "c_line", "c_wa"}
for key, en, _ru in C:
    if key in th:
        continue
    if key in KEEP:
        th[key] = en
        continue
    hint = ("Translate the following website text into Thai EXACTLY, for a professional business website. "
            "Output ONLY the Thai translation: no greeting, no added sentences, no explanations, no polite particles like ครับ/ค่ะ, keep numbers, prices and names (Guest Hub, LINE, WhatsApp, Sato AI Studio) as they are. Text: " + en)
    r = subprocess.run(["/root/.local/bin/thai", "write", hint], capture_output=True, text=True, timeout=120)
    out = r.stdout.strip()
    if r.returncode != 0 or not out:
        print("ошибка", key, r.stderr[-200:]); continue
    th[key] = out
    json.dump(th, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(key, "→", out[:80])
print("готово:", len(th), "из", len(C))
