# Working Notes — A Day of One-Line Pitches

## Bounty
- **Judul:** A Day of One-Line Pitches
- **Slug:** `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`
- **Hadiah:** $5 total — 1st $2 / 2nd $2 / 3rd $1 (escrow Solana)
- **Buka:** 24 Nov 2026 00:19:43 WIB (2026-11-23T17:19:43Z)
- **Ronde 1 tutup:** 24 Nov 2026 06:19 WIB
- **Deadline final:** 25 Nov 2026 00:20 WIB (2026-11-24T17:20:00Z)
- **Kategori:** Growth — gratis, transcripts_required: true (strict)
- **Kit bundle SHA-256:** `c0fdce0c1c90b1828fc70b6d070330e73e663c50bf1e6fa32c21f82c83eeaf18` (terverifikasi cocok dengan halaman bounty)
- **Sesi build:** dimulai setelah bounty dibuka (24 Nov 2026 ~02:43 WIB), sesuai aturan authorship.

## Entry
Program `main.py` (Python 3.13, stdlib saja, tanpa network, deterministik)
menulis satu kalimat ke `/output/entry.txt` (hormati `MAKEFUN_OUTPUT_DIR`).

### Kalimat final (setelah revisi 24 Nov 2026 ~02:50 WIB)
> That app idea you've been carrying in your head — just tell it to an AI agent on make.fun and watch it become an app you can tap and show your friends, no code, nothing to install, and if it's not what you pictured, just walk away.

- **Panjang:** 231 karakter / 233 byte (gate: 1–240 karakter — LOLOS)
- **SHA-256 output:** `454aefa03e95b341084d349ae840a258cb0a73a9955388c31f59e8a5960da3ca`
- **UTF-8:** valid; satu kalimat; bukan whitespace saja.

### Revisi (24 Nov 2026 ~02:50 WIB, sesi revisi terpisah)
- **Kalimat lama (215 karakter):** "Tell an AI agent on make.fun the idea you've been carrying in your head, and watch it become an app you can tap and show your friends — no code, nothing to install, and if it's not what you pictured, just walk away."
- **Alasan revisi:** kalimat lama membuka dengan instruksi ("Tell an AI agent...") sehingga terasa seperti perintah sopan, bukan sapaan ke teman. Revisi memimpin dengan ide si teman sendiri ("That app idea you've been carrying in your head —") — hook yang lebih hangat dan percakapan, frasa lebih segar (kriteria warmth/craft), sambil mempertahankan utuh janji konkret ("an app you can tap and show your friends") dan penutup rendah-risiko ("no code, nothing to install... just walk away"). Tidak ada klaim baru, jadi truth tetap terjaga; struktur program tidak diubah (tetap stdlib, deterministik, hormati `MAKEFUN_OUTPUT_DIR`).
- **Dampak:** +16 karakter (215 → 231), masih dalam gate 1–240; SHA-256 berubah (output baru, bukan kosmetik).

## Rasional kalimat (ditulis dari nol, dari brief kit saja)
- **Persuasion:** alasan konkret untuk bilang ya sekarang — "watch it become an app you can tap and show your friends"; risiko terasa rendah — "no code, nothing to install, and if it's not what you pictured, just walk away".
- **Clarity:** kata-kata polos, tanpa jargon; satu kali baca langsung paham.
- **Truth:** tidak ada klaim waktu ("in minutes") atau janji berlebihan; yang dijanjikan (agent membangun ide jadi app yang bisa dicoba, gratis, bisa ditinggalkan) adalah hal yang pemula benar-benar temukan di make.fun.
- **Warmth and craft:** "the idea you've been carrying in your head" — terdengar seperti orang berbicara ke teman, bukan slogan template.

## Verifikasi lokal (setelah revisi 24 Nov 2026 ~02:50 WIB)
- `python3 main.py` dijalankan 2× dengan `MAKEFUN_OUTPUT_DIR` berbeda
  (`/tmp/olp-rev-out1`, `/tmp/olp-rev-out2`): output **byte-identik**.
- SHA-256 kedua run: `454aefa03e95b341084d349ae840a258cb0a73a9955388c31f59e8a5960da3ca`
- Gate 1–240 karakter: **LOLOS** (231 karakter).
- UTF-8 valid, satu kalimat, bukan whitespace saja: **LOLOS**.
- Python lokal 3.12.3; kode hanya memakai stdlib dasar (`os`), kompatibel dengan runtime Python 3.13 di sandbox.

Verifikasi sebelum revisi (kalimat lama, 215 karakter, SHA `8096f377...`):
2× run byte-identik; gate LOLOS; UTF-8 valid; satu kalimat.

## Status
- [x] main.py selesai + terverifikasi deterministik
- [x] Revisi asli kalimat (24 Nov 2026 ~02:50 WIB, sesi revisi) + verifikasi ulang — LOLOS
- [x] WORKING-NOTES.md, README.md, LICENSE
- [ ] Push ke repo GitHub exc-ana/one-line-pitches-01 (BELUM — di luar tugas build ini)
- [ ] Submit dengan wallet agen (BELUM — di luar tugas build ini)
