def workout_plan(kode):
    while True:
        try:
            tujuan = int(input("""\nApa tujuan Anda melakukan workout? 
1. menurunkan berat badan 
2. meningkatkan kebugaran fisik
3. meningkatkan massa otot
"""))

            if tujuan == 1:
                if 3 <= kode <= 6:
                    try:
                        hari = int(input("Dalam satu minggu, berapa kali Anda dapat berolahraga? "))
                        match hari:
                            case 1:
                                print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut

🧭 Prinsip Umum:
    Durasi: 45–60 menit
    Frekuensi: 1x per minggu, tapi intens dan aman
    Fokus: Full Body + Low Impact HIIT + Strength
    
💪 Workout Terbaik untuk Anda:
    1️⃣  Pemanasan (5–8 menit)
    Tujuan: naikkan detak jantung, siapkan sendi.
    March in place – 1 menit
    Shoulder roll – 30 detik
    Arm circle – 30 detik
    Side step + swing arm – 2 menit
    Squat ringan – 1 menit
    Dynamic stretching (hamstring, paha, betis) – 2 menit
    
    2️⃣  Sesi Utama: Full Body Low-Impact HIIT (30–35 menit)
        Format:
        40 detik latihan → 20 detik istirahat
        3 set total, tiap set berisi 6 gerakan
        Istirahat antar set: 2 menit
        Gerakan per Set:
        Step touch (gerak kanan–kiri cepat)
        Bodyweight squat (bisa pakai kursi kalau butuh tumpuan)
        Arm punch (tinju di udara, cepat tapi terkontrol)
        Glute bridge (angkat pinggul, posisi telentang)
        Standing knee lift (angkat lutut bergantian, seperti jalan di tempat)
        Wall push-up / knee push-up
        ➡️  Setelah 1 set = istirahat 2 menit, lalu ulangi 2 kali lagi (total 3 set)
        
    3️⃣  Kekuatan Inti (10 menit)
        Fokus: otot perut & punggung bawah (penopang tubuh)
        Standing side crunch – 12x per sisi
        Plank lutut / standing plank – 30 detik
        Superman pose (angkat tangan & kaki saat tengkurap) – 10x
        Dead bug (versi ringan) – 10x
        Ulangi 2–3 ronde.
     4️⃣  Pendinginan (5–10 menit)
        Peregangan betis, paha, punggung, bahu
        Deep breathing
        Gerakan yoga ringan seperti “child’s pose”
        
    ⚖️  Tips agar hasil tetap maksimal meski hanya olahraga 1x/minggu:
        Tetap aktif setiap hari: jalan kaki 15–30 menit, naik tangga, banyak berdiri.Defisit kalori ringan: makan 300–500 kalori di bawah kebutuhan harian.
        Tingkatkan protein: ayam, ikan, telur, tahu, tempe → menjaga massa otot.
        Minum air cukup & tidur 7–8 jam/hari.
                                    """)
                                return
                            case 2:
                                print("""
Anda membutuhkan latihan Low-Impact HIIT dan Strength & Core Activation dengan tujuan untuk:
1️⃣  Maksimalkan pembakaran kalori saat latihan
2️⃣  Bangun dan pertahankan massa otot (supaya metabolisme naik)
3️⃣  Lindungi sendi dengan latihan berdampak rendah (low impact)

🗓️  Strategi 2 Hari Workout per Minggu
Gunakan konsep:
Hari 1: Full Body Cardio + HIIT Low-Impact (Fokus pembakaran lemak)
Hari 2: Strength + Core (Fokus penguatan otot & metabolisme jangka panjang)
Durasi per sesi: 45–60 menit

🥇 HARI 1 – Full Body Fat Burn (Low-Impact HIIT)
Tujuan: membakar lemak, tingkatkan stamina, aman untuk sendi

Pemanasan (5–8 menit):
March in place – 1 menit
Shoulder roll + arm swing – 1 menit
Side step + arm reach – 2 menit
Dynamic stretch (hamstring, betis, paha) – 3 menit

Latihan utama (3 ronde):
➡️  Lakukan tiap gerakan 40 detik, istirahat 20 detik. Antar ronde istirahat 1,5–2 menit.
Step touch cepat (aktifkan kaki)
Bodyweight squat (boleh dibantu kursi)
Arm punch cepat
Glute bridge
Standing knee lift (angkat lutut bergantian)
Wall push-up atau knee push-up
Side step squat (tanpa lompatan)

Pendinginan (5 menit):
Peregangan betis, paha depan, punggung bawah
Napas dalam perlahan
🔥 Kalori terbakar: ±250–400 kkal tergantung berat badan & intensitas.

🥈 HARI 2 – Strength & Core Activation
Tujuan: bangun otot besar (agar metabolisme naik & pembakaran lemak berlanjut)

Pemanasan (5 menit):
March in place + peregangan dinamis
Latihan utama (3 set, istirahat antar set 60 detik):
Chair squat – 12–15x
Knee push-up / wall push-up – 10–12x
Dumbbell / botol air row – 12x per sisi
Glute bridge – 12–15x
Standing side crunch – 12x per sisi
Plank lutut / standing plank – tahan 30–40 detik

Pendinginan (5–10 menit):
Peregangan seluruh tubuh, terutama punggung, bahu, dan kaki.
🔥 Kalori terbakar: ±200–350 kkal, tapi efek pembakaran berlanjut 24–48 jam setelah latihan.


⚖️  Tips Maksimalkan Hasil (Walau Hanya 2 Hari/Minggu):
    Konsumsi protein cukup (20–30 g per makan) untuk menjaga massa otot.
    Tetap aktif di hari lain: jalan 6.000–8.000 langkah/hari, naik tangga, hindari duduk lama.
    Tidur 7–8 jam/hari — kurang tidur bisa menahan pembakaran lemak.
    Minum cukup air (2–3 L/hari).
                                    """)
                                return
                            case 3:
                                print("""
Anda membutuhkan latihan Low-Impact HIIT dan Strength & Core Activation dengan tujuan untuk:
1️⃣  Membakar lemak dengan aman
2️⃣  Meningkatkan metabolisme lewat pembentukan otot
3️⃣  Menjaga tubuh tetap bugar dan sendi aman

🥇 HARI 1 – Low-Impact HIIT (Fat Burn)
Tujuan: Meningkatkan denyut jantung, bakar kalori tinggi, tetap aman untuk sendi.

Format:
40 detik kerja, 20 detik istirahat
3 ronde total (istirahat antar ronde 2 menit)

Gerakan:
Step touch cepat
Bodyweight squat
Arm punch
Glute bridge
Standing knee lift
Wall push-up atau knee push-up
Side step squat

Pemanasan (5–8 menit): Jalan di tempat + peregangan dinamis
Pendinginan (5 menit): Peregangan kaki & punggung bawah
🔥 Kalori terbakar: ±300–450 kkal

🥈 HARI 2 – Strength Training (Full Body)
Tujuan: Bentuk otot besar agar metabolisme meningkat.

Format:
3 set tiap gerakan, istirahat antar set 45–60 detik.
Chair squat / goblet squat – 12–15x
Wall push-up / knee push-up – 10–12x
Dumbbell / botol air row – 12x per sisi
Glute bridge – 12–15x
Side lunge (perlahan) – 10x per sisi
Plank lutut / standing plank – 30–40 detik

Pemanasan & pendinginan: sama seperti hari 1

🔥 Kalori terbakar: ±250–400 kkal
💪 Afterburn effect: tubuh masih bakar kalori setelah latihan karena otot aktif.

🥉 HARI 3 – Cardio Ringan + Core Stability
Tujuan: Meningkatkan stamina, jaga sendi, aktifkan otot perut & punggung.

Cardio ringan (20–30 menit):
Pilih salah satu:
Jalan cepat (brisk walk)
Bersepeda santai
Zumba low impact
Renang (kalau tersedia)
Core & Mobility (10–15 menit):
Standing side crunch – 15x per sisi
Bird dog – 12x per sisi
Superman hold – 10x
Plank (lutut) – tahan 30–40 detik
Peregangan otot perut & punggung

🔥 Kalori terbakar: ±250–350 kkal

⚖️  Tips agar hasil optimal:
    Protein cukup (1,2–1,6 g/kg berat badan) agar otot tidak hilang
    Tidur 7–8 jam/hari – sangat berpengaruh ke hormon pembakar lemak
    Aktif di hari non-latihan: jalan kaki, naik tangga, hindari duduk lama
                                    """)
                                return
                            case 4:
                                print("""
Anda memerlukan latihan Full Body HIIT Low-Impact, Strength (Upper Body and Lower Body), dan Kardio + Core + Mobility dengan tujuan untuk:
1️⃣  Membakar lemak secara maksimal
2️⃣ Bangun massa otot agar metabolisme meningkat
3️⃣ Latih seluruh tubuh dengan aman (low-impact, tapi efektif)
4️⃣ Ciptakan kebiasaan konsisten & sustainable      

🥇 HARI 1 – Full Body Low-Impact HIIT (Fat Burn)
Tujuan: Membakar kalori tinggi tanpa membebani sendi.

Format:
40 detik kerja → 20 detik istirahat → 3 ronde total
Istirahat antar ronde: 2 menit

Gerakan:
Step touch cepat
Squat ke overhead reach
Arm punch (cepat tapi aman)
Glute bridge
Knee lift bergantian
Wall push-up / knee push-up
Side step squat

🔥 Kalori terbakar: 300–450 kkal
💡 Efek afterburn hingga 24 jam!

🥈 HARI 2 – Strength (Upper Body Focus)
Tujuan: Bentuk otot bagian atas untuk memperbaiki postur & tingkatkan metabolisme.

Gerakan (3 set, 10–12 repetisi per gerakan):
Wall push-up / incline push-up
Dumbbell / botol air shoulder press
Dumbbell row / resistance band row
Lateral raise (angkat tangan ke samping)
Bicep curl (pakai beban ringan)
Tricep dip (gunakan kursi stabil)

🔥 Kalori terbakar: ±250–350 kkal
💪 Otot aktif = pembakaran lemak meningkat.

🥉 HARI 3 – Strength (Lower Body Focus)
Tujuan: Melatih otot besar (paha, glutes, betis) agar pembakaran kalori tinggi.

Gerakan (3 set, 12–15 repetisi):
Squat (bisa dengan kursi)
Glute bridge
Step-up di kursi rendah / tangga
Side leg raise
Calf raise (berdiri jinjit)
Plank lutut / standing plank (30 detik)

🔥 Kalori terbakar: 300–400 kkal
💡 Otot kaki besar → efek metabolik besar.

🧘 HARI 4 – Cardio + Core + Mobility
Tujuan: Bakar lemak tambahan sambil bantu pemulihan otot.

Cardio ringan (20–30 menit):
Pilih salah satu:
Jalan cepat (brisk walk)
Sepeda santai
Zumba low-impact
Renang ringan

Core & Mobility (15–20 menit):
Standing side crunch – 15x per sisi
Bird dog – 12x per sisi
Superman hold – 10x
Plank (lutut) – 30–40 detik
Peregangan seluruh tubuh

🔥 Kalori terbakar: 250–350 kkal

⚖️  Tips Agar Hasil Maksimal:
    Protein cukup: 1,2–1,6 gram/kg berat badan
    Tidur 7–8 jam per malam
    Aktif di luar jadwal latihan: naik tangga, jalan kaki, hindari duduk lama                            
                                    """)
                                return
                            case 5:
                                print("""
Anda memerlukan latihan Full Body HIIT Low-Impact, Strength (Upper Body and Lower Body), dan Kardio + Core + Mobility dengan tujuan untuk:
1️⃣  Membakar lemak secara maksimal
2️⃣ Bangun massa otot agar metabolisme meningkat
3️⃣ Latih seluruh tubuh dengan aman (low-impact, tapi efektif)
4️⃣ Ciptakan kebiasaan konsisten & sustainable 

🥇 HARI 1 – Full Body Low-Impact HIIT (Fat Burn)
Format: 40 detik kerja – 20 detik istirahat × 3 ronde (istirahat antar ronde 2 menit)

Gerakan:
Step touch cepat
Squat to reach (tanpa lompatan)
Arm punch
Glute bridge
Standing knee lift
Side step squat
Wall push-up / knee push-up

🔥 Kalori terbakar: 300–450 kkal
💡 Efek afterburn 24 jam setelah latihan

🥈 HARI 2 – Strength Training (Upper Body)
Tujuan: Bentuk otot lengan, punggung, dan bahu

Latihan (3 set, 10–12 repetisi):
Wall push-up / incline push-up
Shoulder press (pakai dumbbell / botol air)
Dumbbell row / band row
Front raise
Bicep curl
Tricep dip (pakai kursi stabil)

🔥 Kalori terbakar: 250–350 kkal
💪 Bangun otot → metabolisme naik.

🥉 HARI 3 – Strength Training (Lower Body)
Tujuan: Fokus ke kaki & glutes (otot terbesar pembakar kalori)

Latihan (3 set, 12–15 repetisi):
Squat (bisa gunakan kursi)
Glute bridge
Step-up di kursi rendah / tangga
Side leg raise
Calf raise
Plank lutut 30–40 detik

🔥 Kalori terbakar: 300–400 kkal
💡 Kaki kuat → stabilitas meningkat.

🧘 HARI 4 – Cardio Steady (Fat-Burning Zone)
Tujuan: Bakar lemak tanpa tekanan berlebih.

Pilih salah satu (30–45 menit):
Jalan cepat (brisk walk, di luar atau treadmill)
Bersepeda santai
Zumba low impact
Berenang ringan

💡 Tips: jaga detak jantung di 60–75% maksimal (masih bisa bicara, tapi agak ngos-ngosan).
🔥 Kalori terbakar: 300–500 kkal

💪 HARI 5 – Core + Mobility
Tujuan: Kencangkan perut, perbaiki postur, bantu otot pulih.

Core Circuit (3 set, 10–15x per gerakan):
Standing side crunch
Bird dog
Superman hold
Plank lutut / standing plank
Leg extension lying (angkat kaki perlahan)

Mobility (10 menit):
Peregangan punggung bawah
Hamstring stretch
Shoulder & neck stretch
Child’s pose + deep breathing

🔥 Kalori terbakar: 200–300 kkal
💡 Hari ringan tapi tetap produktif.

⚖️  Tips agar hasil turun berat badan maksimal
    Protein cukup (1,2–1,6 g/kg berat badan) → jaga otot & rasa kenyang
    Tidur cukup (7–8 jam/hari)
    Tetap aktif di luar latihan: jalan kaki, hindari duduk lama                                  
                                    """)
                                return
                            case 6:
                                print("""
Anda memerlukan latihan Full Body HIIT Low-Impact, Strength (Upper Body and Lower Body), dan Cardio Steady + Core + Mobility dengan tujuan untuk:
1️⃣  Membakar lemak secara maksimal
2️⃣ Bangun massa otot agar metabolisme meningkat
3️⃣ Latih seluruh tubuh dengan aman (low-impact, tapi efektif)
4️⃣ Ciptakan kebiasaan konsisten & sustainable 
                                 
🥇 HARI 1 – Full Body HIIT (Low-Impact)
Format: 40 detik kerja, 20 detik istirahat, 3 ronde

Gerakan:
Step touch cepat
Squat reach
Arm punch
Glute bridge
Standing knee lift
Wall push-up
Side step squat

🔥 Kalori terbakar: 350–500 kkal
💡 Afterburn effect 24 jam.

🥈 HARI 2 – Strength (Upper Body)
Tujuan: Bentuk otot bahu, dada, punggung.

Latihan (3 set, 10–12 repetisi):
Wall / incline push-up
Dumbbell row
Shoulder press
Bicep curl
Tricep dip (kursi stabil)
Lateral raise

🔥 Kalori terbakar: 250–350 kkal

🥉 HARI 3 – Strength (Lower Body)
Tujuan: Bangun otot besar untuk pembakaran lemak jangka panjang.

Latihan (3 set, 12–15 repetisi):
Squat (kursi boleh digunakan)
Step-up di kursi rendah / tangga
Glute bridge
Side leg raise
Calf raise
Plank lutut – 30 detik

🔥 Kalori terbakar: 300–400 kkal

💨 HARI 4 – Cardio Steady (Fat-Burning Zone)

Durasi: 30–45 menit
Pilih salah satu:
Jalan cepat (brisk walk)
Sepeda santai
Zumba low-impact
Berenang ringan

💡 Detak jantung 60–75% dari maksimal (masih bisa bicara, tapi ngos-ngosan ringan).
🔥 Kalori terbakar: 300–500 kkal

💪 HARI 5 – Core + HIIT Ringan
Tujuan: Kencangkan perut, bakar kalori tambahan.

Core Circuit (3 set):
Standing side crunch – 15x per sisi
Bird dog – 12x per sisi
Superman hold – 10x
Plank (lutut) – 30–45 detik
Flutter kick ringan – 15 detik
Tambahan HIIT Ringan (opsional, 2 ronde):
Step touch cepat – 40 detik
Bodyweight squat – 40 detik
Arm punch – 40 detik

🔥 Kalori terbakar: 300–450 kkal

🧘 HARI 6 – Mobility + Recovery Cardio
Tujuan: Pulihkan otot, tingkatkan fleksibilitas, tetap aktif.

Rangkaian (30–40 menit):
Jalan santai 15–20 menit
Stretching seluruh tubuh:
Hamstring, betis, paha depan
Punggung bawah, bahu, leher
Yoga ringan (child’s pose, cat-cow, cobra pose)

🔥 Kalori terbakar: 150–250 kkal
💡 Membantu pemulihan, cegah cedera.

⚖️  Kunci Sukses Penurunan Berat Badan:
    Protein cukup (1,2–1,6 g/kg berat badan)
    Tidur cukup (7–8 jam) → hormon pembakar lemak optimal
    Aktif di luar latihan: naik tangga, jalan kaki, hindari duduk lama                                 
                                    """)
                                return
                            case 7:
                                print("\nAnda membutuhkan istirahat setidaknya 1 hari. Jangan memaksakan tubuh Anda.")
                                continue
                            case _:
                                print("\nDalam satu minggu hanya ada 7 hari dari hari ke-1 sampai ke-7.")
                                continue
                    except ValueError:
                        print("Inputan hanya berupa angka.")
                        continue
                elif kode == 2:
                    print("\nBerat badan Anda sudah ideal. Kami merekomendasikan untuk meningkatkan massa otot.")
                    continue
                else:
                    print("\nBerat badan Anda kurang. Kami merekomendasikan untuk meningkatkan kebugaran fisik.")
                    continue
            elif tujuan == 2:
                if 3 <= kode <= 6:
                    kfinput = input("\nAnda dapat meningkatkan kebugaran fisik Anda. Tetapi kami merekomendasikan untuk menurunkan berat badan. Apakah anda ingin lanjut meningkatkan kebugaran fisik (iya/tidak)? ").lower()
                    if kfinput == "iya":
                        while True:
                            try:
                                hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                                match hari:
                                    case 1:
                                        print("""
Anda membutuhkan latihan HIIT Camp + Full Body serta kekuatan inti dan mobilitas:
1️⃣ Meningkatkan metabolisme tubuh
2️⃣ Menjaga kebugaran jantung & pernapasan
3️⃣ Melatih kekuatan dasar otot dan stabilitas tubuh

🧩 Struktur Latihan (60 menit total)
1️⃣ Pemanasan – 10 menit
Tujuan: menaikkan detak jantung & menyiapkan otot.

Contoh:
Jalan cepat atau jogging ringan – 5 menit
Dynamic stretching: arm circle, leg swing, torso twist – 5 menit

2️⃣ Sesi Utama (HIIT Camp + Full Body) – 35 menit
Format: High Intensity Interval Training (HIIT)

40 detik kerja : 20 detik istirahat per gerakan
3–4 set, 1 menit istirahat antar set

Gerakan:
Jumping Jack (atau step jack bila kelebihan berat badan)
Squat (bisa bodyweight atau chair squat)
Push-up (bisa modifikasi di lutut)
Mountain climber
Plank (30–40 detik)
➡️ Istirahat 1 menit → ulangi total 3–4 kali

💡 Tips: Jika belum terbiasa, lakukan Low Impact HIIT (tanpa lompatan) tapi tetap menjaga tempo cepat.

3️⃣ Kekuatan Inti & Mobilitas – 10 menit
Tujuan: memperkuat core & postur

Glute bridge – 3x15
Superman hold – 3x30 detik
Side plank – 2x30 detik tiap sisi
Stretching (hamstring, bahu, punggung bawah)

4️⃣ Pendinginan – 5 menit
Tujuan: menurunkan detak jantung dan mencegah nyeri otot

Peregangan statis seluruh tubuh
Nafas dalam dan rileksasi

🔥 Tips Tambahan
    Fokus pada intensitas dan konsistensi: walau hanya 1x seminggu, buat sesi tersebut “berkualitas penuh”.
    Di hari lain, coba tetap aktif ringan: jalan kaki 15–20 menit, naik tangga, atau peregangan pagi.
    Kombinasikan dengan pola makan sehat & defisit kalori agar hasilnya terasa.
    Cukup tidur & hidrasi penting agar tubuh pulih optimal.                                        
                                            """)
                                        return
                                    case 2:
                                        print("""
Anda membutuhkan latihan Full Body HIIT/Cardio Mix dan Cardio Camp dengan tujuan untuk:
1️⃣ Meningkatkan kebugaran fisik (cardio + kekuatan + fleksibilitas)
2️⃣ Membakar lemak secara efisien
3️⃣ Membangun dasar otot agar metabolisme meningkat

📅 Hari 1 – Kardio & Pembakaran Lemak (Full Body HIIT/Cardio Mix)
Durasi total: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / jogging ringan – 5 menit
Dynamic stretching (ayunan kaki, putaran bahu, torso twist) – 5 menit

2️⃣ HIIT / Cardio Camp (30 menit)
Format: 40 detik kerja : 20 detik istirahat
Ulangi 3–4 set, istirahat 1 menit antar set

Gerakan:
Step Jack atau Jumping Jack
Squat atau Chair Squat
Mountain Climber (atau Slow Climber versi ringan)
Push-Up (bisa versi lutut)
Plank 30–40 detik
Alternatif low impact (jika berat badan masih tinggi):
→ March in place, wall push-up, side step squat, standing knee lift

3️⃣ Pendinginan & stretching (10 menit)
Fokus ke kaki, punggung, dan bahu
Pernapasan dalam 3 menit terakhir

📅 Hari 2 – Kekuatan Tubuh & Stabilitas (Strength & Core Training)
Durasi total: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan di tempat atau high knee ringan
Peregangan dinamis bahu dan pinggul

2️⃣ Latihan Kekuatan (40 menit)
Gunakan beban tubuh (bodyweight) dulu.
Lakukan 3 set, 12–15 repetisi per gerakan.

Squat, Glute Bridge	
Push-up, Triceps dip (pakai kursi)	
Plank, Side plank, Leg raise
Superman hold, Wall angel

3️⃣ Pendinginan (10 menit)
Stretch seluruh tubuh
Fokus pada pernapasan dan kelenturan

💡  Tips Penting
    Jika kamu hanya punya 2 hari, intensitas harus sedang–tinggi (HR 70–85% dari maksimal).
    Kombinasikan dengan aktivitas ringan harian: naik tangga, jalan kaki 15–20 menit tiap hari.
    Nutrisi lebih berperan besar: usahakan defisit kalori 300–500 kcal/hari.
    Tidur cukup (7–8 jam) agar pemulihan optimal.
    Setelah 4–6 minggu, kamu bisa menambah variasi: resistance band, skipping, atau latihan beban ringan.                                          
                                            """)
                                        return
                                    case 3:
                                        print("""
Anda membutuhkan latihan Cardio dan HIIT, Full Body Strength, dan Kebugaran Total dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan fisik
2️⃣ Membakar lemak
3️⃣ Membangun daya tahan tubuh   

📅 Hari 1 – Cardio & HIIT (Pembakaran Lemak)
Durasi total: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / joging ringan – 5 menit
Dynamic stretch (putaran bahu, torso twist, leg swing) – 5 menit

2️⃣ Sesi HIIT (30 menit)
Format: 40 detik kerja : 20 detik istirahat → 3–4 set

Gerakan:
Jumping jack / step jack (low impact)
Squat atau chair squat
Push-up (modifikasi boleh)
Mountain climber / slow climber
Plank 30–40 detik

3️⃣ Pendinginan (10 menit)
Peregangan kaki, punggung, dan bahu
Napas dalam

📅 Hari 2 – Kekuatan & Bentuk Tubuh (Full Body Strength)
Durasi total: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan di tempat
Ayunan tangan & kaki

2️⃣ Latihan Kekuatan (40 menit)
Gunakan berat tubuh (bodyweight) atau dumbbell kecil.


Squat, Lunges	                        3x12
Glute bridge, Step-up	                3x15
Push-up, Wall push-up	                3x10
punggung	Superman hold, Arm circle	3x15
Plank, Leg raise	                    3x30 

3️⃣ Pendinginan (10 menit)
Fokus peregangan otot besar
Postur dan napas dalam      

📅 Hari 3 – Kebugaran Total (Cardio + Core + Mobilitas)
Durasi total: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / skipping ringan
Dynamic stretch seluruh tubuh

2️⃣ Circuit Training (30–35 menit)
Lakukan 3–4 ronde, istirahat antar ronde 1 menit.

Step-up (20x)
Squat to press (bisa pakai botol air)
Mountain climber (30 detik)
Plank shoulder tap (30 detik)
Jumping jack / knee raise (30 detik)

3️⃣ Core Finisher (10 menit)

Plank – 3x30 detik
Side plank – 2x30 detik tiap sisi
Glute bridge – 3x15

4️⃣ Pendinginan (5–10 menit)

Stretch seluruh tubuh
Fokus pada napas dalam dan relaksasi
💡  Tips Tambahan
    Jaga intensitas sedang–tinggi, tapi utamakan form (teknik gerakan benar).
    Jangan lewatkan pemanasan & pendinginan — penting untuk mencegah cedera.
    Di luar hari latihan, tetap aktif ringan (jalan kaki, peregangan, naik tangga).
    Makan sehat dan defisit kalori ringan (300–500 kcal/hari) untuk hasil maksimal.
    Tidur cukup 7–8 jam untuk pemulihan otot dan metabolisme optimal.                                 
                                            """)
                                        return
                                    case 4:
                                        print("""
Anda membutuhkan latihan Kardio dan HIIT, Strength Training, dan Core Stability dengan tujuan untuk:
1️⃣ Penurunan Lemak Tubuh
2️⃣ Peningkatan kebugaran jantung
3️⃣ Pembentukan otot
4️⃣ Peningkatan energi harian

📅 Hari 1 – Cardio & Pembakaran Lemak (HIIT)
Durasi: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / jogging ringan – 5 menit
Dynamic stretch (ayunan kaki, torso twist, shoulder roll) – 5 menit

2️⃣ HIIT (30 menit)
Format: 40 detik kerja : 20 detik istirahat × 4 set

Gerakan:
Jumping jack / step jack
Squat
Push-up (bisa modifikasi di lutut)
Mountain climber
Plank

3️⃣ Pendinginan (10 menit)
Stretching tubuh bagian bawah & atas
Napas dalam

📅 Hari 2 – Strength Training (Upper Body + Core)
Durasi: 50–60 menit

1️⃣ Pemanasan (10 menit)
Gerakan bahu, tangan, punggung, dan dada ringan

2️⃣ Latihan utama (40 menit)
Gunakan beban tubuh atau dumbbell kecil.

Push-up / Wall push-up	    3×10–12
Shoulder press (botol air)	3×12
Superman hold	            3×15
Bicep curl / Triceps dip	3×12
Plank, Leg raise	        3×30–45 

3️⃣ Pendinginan (10 menit)
Stretch lengan, dada, dan punggung

📅 Hari 3 – Cardio Ringan + Mobilitas (Active Recovery)
Durasi: 45–50 menit
Tujuan: meningkatkan daya tahan jantung & fleksibilitas tanpa kelelahan otot.

1️⃣ Pemanasan ringan (5 menit)

2️⃣ Aktivitas utama (30–35 menit)
Pilih salah satu atau kombinasi:
Jalan cepat / sepeda santai / renang ringan
Yoga / Pilates dasar
Mobility flow (stretch & rotasi sendi besar)

3️⃣ Pendinginan (10 menit)
Fokus pada peregangan panjang & napas ritmis

📅 Hari 4 – Lower Body Strength + Core Stability
Durasi: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan di tempat, leg swing, hip circle

2️⃣ Latihan utama (40 menit)

Squat, Lunges	        3×12
Glute bridge, Step-up	3×15
Calf raise	            3×20
Side plank, Bird-dog	3×30 
Kardio tambahan	Jump rope / knee lift 1 menit × 3	

3️⃣ Pendinginan (10 menit)
Stretch paha, betis, punggung bawah

💡  Tips Tambahan

    Atur intensitas:
    Hari 1 & 4 → intensitas sedang–tinggi
    Hari 2 → kekuatan sedang
    Hari 3 → pemulihan & mobilitas

    Protein cukup (1.2–1.5 g/kg berat badan)
    Jaga rutinitas tidur: 7–8 jam per malam                                          
                                            """)
                                        return
                                    case 5:
                                        print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Meningkatkan kebugaran jantung, membentuk otot, dan mempercepat metabolisme.
2️⃣ Membentuk ototmempercepat metabolisme.
3️⃣ Mempercepat metabolisme          

📅 Hari 1 – Full Body HIIT (Cardio & Pembakaran Lemak)
Durasi: 50–60 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / jogging ringan – 5 menit
Dynamic stretch (ayunan kaki, torso twist, shoulder roll) – 5 menit

2️⃣ HIIT (30–35 menit)
Format: 40 detik kerja : 20 detik istirahat × 4 set

Gerakan:
Jumping jack / step jack
Squat
Push-up (modifikasi boleh)
Mountain climber
Plank
➡️ Istirahat 1 menit tiap set

3️⃣ Pendinginan (10 menit)
Peregangan seluruh tubuh

📅 Hari 2 – Strength Training (Upper Body)
Durasi: 50–60 menit


Push-up / Wall push-up	            3×12
Shoulder press (botol air/dumbbell)	3×12
Superman hold / Dumbbell row	    3×15
Bicep curl / Triceps dip	        3×12
Plank shoulder tap	                3×30 

Pendinginan: Stretch dada, bahu, punggung.

📅 Hari 3 – Cardio + Core
Durasi: 45–55 menit

1️⃣ Pemanasan (10 menit)
Jalan cepat / skipping ringan

2️⃣ Cardio Utama (25–30 menit)
Pilih salah satu:
Jalan cepat / jogging ringan
Bersepeda
Lompat tali interval (30 detik on, 30 detik off × 10–12 set)

3️⃣ Core (10–15 menit)
Leg raise – 3×15
Side plank – 2×30 detik per sisi
Glute bridge – 3×15
Flutter kick – 3×20 detik

4️⃣ Pendinginan: Stretch punggung dan perut.

📅 Hari 4 – Strength Training (Lower Body)
Durasi: 50–60 menit


Squat, Lunges	        3×12
Glute bridge, Step-up	3×15
Calf raise	            3×20
Bird dog, Plank	        3×30 
Tambahan: Cardio ringan 10 menit di akhir (jalan cepat / treadmill).

📅 Hari 5 – Mobility & Active Recovery (Fleksibilitas & Pemulihan)
Durasi: 40–50 menit

1️⃣ Pemanasan ringan (5 menit)
Jalan pelan + gerak sendi ringan

2️⃣ Mobilitas & Fleksibilitas (30–35 menit)
Yoga flow ringan
Peregangan aktif (hamstring, punggung, bahu, pinggul)
Latihan keseimbangan (tree pose, single-leg stand)

3️⃣ Pendinginan (10 menit)
Napas dalam dan relaksasi

💡  Tips Sukses
    Pola latihan:
    Hari 1 → HIIT
    Hari 2 → Upper body
    Hari 3 → Cardio + Core
    Hari 4 → Lower body
    Hari 5 → Mobility & Recovery

    Atur intensitas:
    3 hari intens (HIIT, Upper, Lower)
    2 hari sedang/ringan (Cardio + Mobility)

    Nutrisi:
    Konsumsi protein cukup (1.2–1.5 g/kg berat badan)
    
    Tidur 7–8 jam

    Progres:
    Minggu 1–2: fokus teknik & adaptasi
    Minggu 3–4: tingkatkan intensitas atau beban                               
                                            """)
                                        return
                                    case 6:
                                        print("""
Anda membutuhkan latihan HIIT, Strength, Cardio, dan Core dengan tujuan untuk:
1️⃣ Membakar lemak secara konsisten
2️⃣ Meningkatkan stamina & kekuatan
3️⃣ Melatih seluruh otot tubuh secara bergantian

🏋️‍♂️ Hari 1 – Full Body HIIT (High Intensity)
Durasi: 50–60 menit
Format: 40 detik kerja : 20 detik istirahat × 4 set

Gerakan:
Jumping Jack / Step Jack
Squat
Push-up (bisa modifikasi)
Mountain Climber
Plank
➡️ Istirahat 1 menit antar set
Pendinginan: Peregangan seluruh tubuh

💪 Hari 2 – Upper Body Strength
Durasi: 50–60 menit


Push-up / Wall Push-up	    3×10–12
Shoulder Press / Arm Raise	3×12
Superman hold / Row	        3×15
Bicep curl / Triceps dip	3×12
Plank shoulder tap	        3×30 

❤️ Hari 3 – Cardio + Core
Durasi: 45–55 menit

Cardio (30 menit):
Jalan cepat, jogging, atau bersepeda (zona detak jantung sedang)

Core (15 menit):
Leg raise – 3×15
Side plank – 2×30 detik per sisi
Glute bridge – 3×15
Flutter kick – 3×20 detik

🦵 Hari 4 – Lower Body Strength
Durasi: 50–60 menit

Squat, Lunges	        3×12
Glute bridge, Step-up	3×15
Calf raise	            3×20
Bird dog, Side plank	3×30 

🚴 Hari 5 – Steady Cardio (Endurance Day)
Durasi: 45–60 menit
Pilih salah satu:
Jalan cepat 45–60 menit
Sepeda statis / outdoor
Renang atau elliptical

💡  Tujuan: melatih jantung tetap kuat & efisien.
    Intensitas: 70–75% detak jantung maksimal (sedang tapi stabil).

🧘 Hari 6 – Mobility & Recovery (Pemulihan Aktif)
Durasi: 40–50 menit

Yoga / Pilates ringan
Dynamic stretching seluruh tubuh
Foam rolling (jika ada alat)
Nafas dalam & relaksasi

Tujuan: menjaga kelenturan, memperbaiki postur, dan mencegah cedera.

💡 Tips Sukses
    Pola intensitas:
    3 hari intens (HIIT + Strength)
    2 hari sedang (Cardio steady + Core)
    1 hari ringan (Mobility)

    Protein cukup (1.2–1.5 g/kg berat badan)
    Kurangi gula dan gorengan, perbanyak sayur & air putih
    Tidur: 7–8 jam/hari
    Aktivitas harian ringan: tetap jalan kaki atau stretching saat tidak latihan                                         
                                            """)
                                        return
                                    case 7:
                                        print("\nAnda membutuhkan istirahat setidaknya 1 hari. Jangan memaksakan tubuh Anda.")
                                        continue
                                    case _:
                                        print("\nDalam satu minggu hanya ada 7 hari dari hari ke-1 sampai ke-7.")
                                        continue
                            except ValueError:
                                print("Inputan hanya berupa angka.")
                                continue
                    elif kfinput == "tidak":
                        continue
                    else:
                        print("\nInputan Anda tidak valid. Silahkan mengisi ulang inputan Anda.")
                        continue
                elif kode == 2:              
                    kfinput = input("\nAnda dapat meningkatkan kebugaran fisik Anda. Tetapi kami merekomendasikan untuk meningkatkan massa otot. Apakah anda ingin lanjut meningkatkan kebugaran fisik (iya/tidak)? ").lower()
                    if kfinput == "iya":
                        while True:
                            try:
                                hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                                match hari:
                                    case 1:
                                        print("""
Anda membutuhkan latihan Full Body Functional Training dan Core and Balance Training dengan tujuan untuk:
💪  Menjaga kebugaran jantung kekuatan otot, kelenturan, dan keseimbangan tubuh.

🏋️‍♂️  Workout Terbaik 1 Hari per Minggu untuk BMI Normal
Durasi: 60 menit
Fokus: Kebugaran total (cardio + kekuatan + mobilitas)

🧩  Struktur Latihan
1️⃣  Pemanasan – 10 menit
Tujuan: menaikkan detak jantung dan melenturkan sendi.
Contoh:

Jalan cepat atau jogging ringan – 5 menit
Dynamic stretch (leg swing, arm circle, torso twist) – 5 menit

2️⃣  Sesi Utama – 40 menit (Full Body Functional Training)
Latihan sirkuit 4–5 gerakan utama:

💡 Format: 40 detik kerja : 20 detik istirahat × 3–4 ronde
Istirahat antar ronde: 1 menit

Ronde Latihan:
Squat Jump / Bodyweight Squat → melatih kaki & daya ledak
Push-up → dada, bahu, lengan
Mountain Climber → cardio & core
Glute Bridge / Step-up → bokong & paha belakang
Plank / Side Plank → kekuatan inti tubuh
Jika kamu ingin versi lebih ringan:
→ ganti “jump” dengan low impact step (misalnya squat biasa, knee lift).

3️⃣ Core & Balance Training – 5–10 menit
Latihan ini membantu menjaga stabilitas dan postur tubuh.

Contoh:
Bird Dog – 3×10
Leg Raise – 3×15
Side Plank – 2×30 detik tiap sisi

4️⃣ Pendinginan – 5–10 menit
Peregangan statis + pernapasan dalam:

Hamstring stretch
Shoulder & chest stretch
Deep breathing (3–5 menit)

💡  Tips Supaya Efektif
    Kualitas lebih penting daripada kuantitas. Lakukan 1 jam itu dengan fokus & intensitas sedang-tinggi.
    Di luar hari latihan, tetap aktif ringan: jalan 20 menit, naik tangga, atau stretching pagi.
    Jaga pola makan dan tidur agar hasil kebugaran tetap optimal.                                          
                                              """)
                                        return
                                    case 2:
                                        print("""
Anda membutuhkan latihan Strength and Core, Stability, dan Light Strength dengan tujuan untuk:
1️⃣ Menjaga kekuatan dan bentuk tubuh
2️⃣ Menjaga fleksibilitas & mencegah cedera
3️⃣ Meningkatkan stabilitas tubuh & postur   
4️⃣ Meningkatkan daya tahan jantung & paru  

📅 Rencana Mingguan
Hari 1 – Strength & Core (Kekuatan Tubuh dan Stabilitas)
Durasi: ±60 menit
Tujuan: meningkatkan kekuatan otot & postur

🔹 Pemanasan (10 menit)
Jalan cepat / skipping ringan – 5 menit
Dynamic stretch (arm circle, leg swing, torso twist) – 5 menit

🔹 Latihan Inti (40 menit)
Lakukan 3 set, 10–15 repetisi tiap gerakan:
Bodyweight Squat / Goblet Squat – paha & bokong
Push-up / Incline Push-up – dada & bahu
Hip Bridge / Glute Bridge – otot glute & punggung bawah
Dumbbell Row / Inverted Row – punggung atas
Plank – tahan 30–60 detik
Side Plank / Bird Dog – core stabilitas
→ Istirahat antar set: 60–90 detik

🔹 Pendinginan (10 menit)
Stretch seluruh tubuh, terutama otot yang digunakan.

Hari 2 – Cardio & Mobility (Daya Tahan + Kelenturan)
Durasi: ±60 menit
Tujuan: melatih jantung, paru, serta fleksibilitas sendi

🔹 Pemanasan (10 menit)
Jalan cepat, jogging ringan, atau skipping – 5 menit
Dynamic stretch – 5 menit

🔹 Latihan Inti (40 menit)
Pilih salah satu format (atau kombinasikan):
Pilihan A – HIIT ringan (20:40 detik kerja/istirahat × 4 ronde):
            Jumping Jack / Low Impact Step
            Mountain Climber / Slow Knee Drive
            Reverse Lunge
            High Knees / March in Place
            Plank Shoulder Tap

Pilihan B – Cardio steady (jika suka aktivitas outdoor):
            Jalan cepat / jogging 40 menit
            Atau bersepeda santai 45–60 menit

🔹 Pendinginan & Stretching (10 menit)
Fokus pada kaki, pinggul, dan punggung
Latihan pernapasan dalam (deep breathing 3–5 menit)

💡  Tips Agar Efektif
    Fokus ke intensitas & konsistensi, bukan durasi panjang.
    Jaga pola makan seimbang dan tidur cukup untuk pemulihan.
    Bisa tambah aktivitas ringan di luar dua hari itu: jalan 20–30 menit, naik tangga, atau peregangan pagi.                                            
                                              """)
                                        return
                                    case 3:
                                        print("""
Anda membutuhkan latihan Full Body Strength Training, Cardio, dan Mbobility and Balance dengan tujuan untuk:
1️⃣ Kekuatan otot (strength training)
2️⃣ Kebugaran jantung (cardio/endurance)
3️⃣ Kelenturan & keseimbangan (mobility & stability)  

💪 HARI 1 – Full Body Strength Training
Fokus: membangun kekuatan, menjaga massa otot, dan memperbaiki postur

🔸 Pemanasan (10 menit)
Jalan cepat / jogging ringan – 5 menit
Dynamic stretching – 5 menit (leg swing, arm circle, hip rotation)

🔸 Latihan Inti (40 menit)
3 set × 10–12 repetisi, istirahat 60–90 detik antar set:
Squat / Goblet Squat → paha, bokong
Push-up / Incline Push-up → dada, bahu, triceps
Bent Over Row (dumbbell/botol air) → punggung
Lunges / Step-up → kaki dan keseimbangan
Plank – tahan 30–45 detik
Glute Bridge → punggung bawah dan pinggul

🔸 Pendinginan (10 menit)
Stretch seluruh tubuh: quadriceps, hamstring, dada, bahu

🫀 HARI 2 – Cardio + Core
Fokus: meningkatkan daya tahan jantung-paru dan memperkuat inti tubuh

🔸 Pemanasan (10 menit)
Jogging ringan atau skipping – 5 menit
Dynamic mobility – 5 menit

🔸 Latihan Inti (40 menit)
Pilihan A – HIIT ringan (20 detik kerja / 40 detik istirahat × 4–5 ronde):
            Jumping Jack
            Mountain Climber
            High Knees / March in Place
            Squat to Reach
            Side Plank
Pilihan B – Cardio Steady:
            Jalan cepat, jogging, atau bersepeda selama 40–50 menit (intensitas sedang)

🔸 Core Finisher (10 menit)
Russian Twist – 3×20
Leg Raise – 3×15
Superman Hold – 3×30 detik

🧘 HARI 3 – Mobility, Balance & Recovery
Fokus: kelenturan, stabilitas, dan pemulihan otot

🔸 Pemanasan (5–10 menit)
Jalan santai + mobilitas sendi

🔸 Latihan Inti (40–45 menit)
Yoga flow (Down Dog → Cobra → Child Pose → Warrior)
Balance training: one-leg stand, heel-to-toe walk
Core ringan: Bird Dog, Dead Bug, Plank Shoulder Tap
Light bodyweight circuit (Squat, Push-up, Glute Bridge)

🔸 Pendinginan (5–10 menit)
Stretch statis seluruh tubuh + deep breathing

💡  Tips Agar Efektif
    Fokus pada kualitas gerakan, bukan sekadar banyaknya set/repetisi
    Tidur cukup (7–8 jam) agar otot pulih
    Cukupi nutrisi (protein, sayur, air) agar hasil optimal
    Di luar 3 hari latihan, lakukan aktivitas ringan seperti jalan kaki, peregangan, atau naik tangga
                                              """)
                                        return
                                    case 4:
                                        print("""
Anda membutuhkan latihan Strength, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan
2️⃣ Meningkatkan stamina
3️⃣ Meningkatkan kelincahan tubuh

💪 HARI 1 – Upper Body Strength (Tubuh Atas)
Fokus: melatih dada, punggung, bahu, dan lengan

🔹 Pemanasan (10 menit)
Jumping jack atau jalan cepat – 5 menit
Dynamic stretch bahu & punggung – 5 menit

🔹 Latihan Inti (40–45 menit)
3 set × 10–12 repetisi tiap gerakan:
Push-up / Incline Push-up
Dumbbell Row / Body Row
Shoulder Press (pakai dumbbell / botol air)
Bicep Curl
Tricep Dips (di kursi)
Plank – 30–45 detik

🔹 Pendinginan (10 menit)
Stretch bahu, dada, dan punggung

🦵 HARI 2 – Lower Body Strength (Tubuh Bawah)
Fokus: paha, bokong, betis, dan core bawah

🔹 Pemanasan (10 menit)
Jalan cepat / skipping ringan – 5 menit
Leg swing, hip rotation – 5 menit

🔹 Latihan Inti (40–45 menit)
3 set × 10–15 repetisi:
Squat / Goblet Squat
Lunges (kanan-kiri)
Glute Bridge / Hip Thrust
Step-up (naik tangga/kursi)
Calf Raise
Side Plank – 2×30 detik per sisi

🔹 Pendinginan (10 menit)
Stretch kaki & pinggul

🫀 HARI 3 – Cardio + Core
Fokus: meningkatkan daya tahan jantung dan kekuatan perut

🔹 Pemanasan (10 menit)
Jogging ringan atau skipping – 5 menit
Dynamic stretch – 5 menit

🔹 Latihan Inti (40–45 menit)
HIIT ringan (20 detik kerja / 40 detik istirahat × 4–5 ronde):
Jumping Jack
Mountain Climber
High Knees / March in Place
Squat Jump / Step Squat
Plank Shoulder Tap

Lalu Core Finisher (10 menit):
Russian Twist – 3×20
Leg Raise – 3×15
Superman Hold – 3×30 detik

🔹 Pendinginan (10 menit)
Stretch punggung, perut, dan pinggul

🧘 HARI 4 – Mobility & Recovery (Pemulihan Aktif)
Fokus: melatih kelenturan, keseimbangan, dan pemulihan otot

🔹 Pemanasan Ringan (5–10 menit)
Jalan santai atau slow jogging

🔹 Latihan Inti (40–50 menit)
Yoga Flow (Down Dog → Cobra → Warrior → Child’s Pose)
Balance drill (one-leg stand, heel-to-toe walk)
Core stabilitas: Bird Dog, Dead Bug, Side Plank
Stretch dinamis seluruh tubuh

🔹 Pendinginan (10 menit)
Pernapasan dalam dan peregangan statis   

💡  Tips Supaya Efektif
    Gunakan intensitas sedang–tinggi (RPE 6–8/10)
    Istirahat cukup antar sesi (minimal 1 hari jeda antar latihan berat)
    Minum cukup air & jaga asupan protein
    Di luar latihan, tetap aktif: jalan kaki, stretching pagi                                           
                                              """)
                                        return
                                    case 5:
                                        print("""
Anda membutuhkan latihan Strength, Cardio and Core Conditioning, Mobility, dan Full Body Functional Training dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan, stamina, dan kelincahan
2️⃣ Meningkatkan keseimbangan    
3️⃣ Meningkatkan kebugaran umum  

💪 HARI 1 – Upper Body Strength (Tubuh Atas)
Fokus: dada, bahu, punggung, dan lengan

🔸 Pemanasan (10 menit)
Jumping jack / jalan cepat – 5 menit
Arm swing, shoulder roll, torso twist – 5 menit

🔸 Latihan Inti (40 menit)
3–4 set × 10–12 repetisi:
Push-up / Dumbbell Chest Press
Dumbbell Row / Inverted Row
Shoulder Press
Bicep Curl
Tricep Dips
Plank – 45 detik

🔸 Pendinginan (10 menit)
Stretch bahu, dada, punggung

🦵 HARI 2 – Lower Body Strength (Tubuh Bawah)
Fokus: paha, bokong, betis, dan stabilitas kaki

🔸 Pemanasan (10 menit)
Skipping / jogging ringan – 5 menit
Leg swing, hip circle – 5 menit

🔸 Latihan Inti (40–45 menit)
3–4 set × 10–15 repetisi:
Squat / Goblet Squat
Lunges (kanan-kiri)
Step-up
Glute Bridge / Hip Thrust
Calf Raise
Side Plank – 2×30 detik per sisi

🔸 Pendinginan (10 menit)
Stretch kaki dan pinggul

🫀 HARI 3 – Cardio & Core Conditioning
Fokus: melatih daya tahan jantung dan kekuatan inti

🔸 Pemanasan (10 menit)
Jogging atau sepeda ringan
Dynamic stretch – 5 menit
🔸 Latihan Inti (40 menit)
Pilihan A – HIIT ringan (20 detik kerja / 40 detik istirahat × 5 ronde):
            Jumping Jack
            Mountain Climber
            High Knees
            Bodyweight Squat
            Burpee / Low Impact Burpee
Pilihan B – Cardio Steady (Outdoor/Indoor):
            Jogging 45 menit, atau
            Bersepeda 60 menit

🔸 Core Finisher (10 menit)
Russian Twist – 3×20
Leg Raise – 3×15
Superman Hold – 3×30 detik

🧘 HARI 4 – Mobility, Stability & Active Recovery
Fokus: kelenturan, keseimbangan, dan pemulihan otot

🔸 Pemanasan (5–10 menit)
Jalan santai atau yoga ringan

🔸 Latihan Inti (40–50 menit)
Yoga flow (Sun Salutation → Warrior → Down Dog → Cobra)
Core stability: Bird Dog, Dead Bug, Side Plank
Balance drill: One-leg stand, heel-to-toe walk
Light stretching seluruh tubuh

🔸 Pendinginan (10 menit)
Deep breathing + peregangan statis

🔥 HARI 5 – Full Body Functional Training
Fokus: gabungan kekuatan, daya tahan, dan kecepatan tubuh

🔸 Pemanasan (10 menit)
Skipping / jalan cepat – 5 menit
Dynamic stretch – 5 menit

🔸 Latihan Inti (40 menit)
Lakukan sirkuit (3–4 ronde, istirahat 1 menit antar ronde):
Squat to Press (kombinasi kaki & bahu)
Push-up
Dumbbell Deadlift / Bodyweight Good Morning
Jumping Lunge / Step Lunge
Mountain Climber
Plank to Push-up

🔸 Pendinginan (10 menit)
Stretch seluruh tubuh         

💡  Tips Penting
    Gunakan intensitas sedang–tinggi (RPE 7–8/10)
    Tidur cukup (7–8 jam) agar otot pulih optimal
    Cukupi protein, air, dan sayuran setiap hari
    Hari libur tetap aktif ringan (jalan, stretching, aktivitas harian)    
                                              """)
                                        return
                                    case 6:
                                        print("""
Anda membutuhkan latihan HIIT, Strength, Cardio, dan Core dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan dan daya tahan tubuh 
2️⃣ Melatih fleksibilitas dan keseimbangan
3️⃣ Meningkatkan koordinasi tubuh     

💪 HARI 1 – Upper Body Strength (Tubuh Atas)
Fokus: bahu, dada, punggung, dan lengan

🔸 Pemanasan (10 menit)
Jumping jack atau jogging ringan
Arm swing, shoulder circle, torso twist

🔸 Latihan Inti (45 menit)
3–4 set × 10–12 repetisi:
Push-up / Dumbbell Chest Press
One-arm Row / Dumbbell Row
Shoulder Press
Bicep Curl
Tricep Dips / Kickback
Plank – 1 menit

🔸 Pendinginan (5–10 menit)
Stretch bahu, dada, dan punggung

🦵 HARI 2 – Lower Body Strength (Tubuh Bawah)
Fokus: paha, betis, dan glutes

🔸 Pemanasan (10 menit)
Skipping / jalan cepat
Hip circle, leg swing

🔸 Latihan Inti (45 menit)
3–4 set × 12–15 repetisi:
Squat / Goblet Squat
Lunges (bergantian)
Step-up
Glute Bridge / Hip Thrust
Calf Raise
Side Plank – 2×30 detik per sisi

🔸 Pendinginan (10 menit)
Stretch kaki dan pinggul

🫀 HARI 3 – Cardio HIIT & Core
Fokus: jantung, paru, dan otot inti

🔸 Pemanasan (10 menit)
Jogging ringan + dynamic mobility

🔸 HIIT Session (30–35 menit)
(20 detik kerja / 40 detik istirahat × 5 ronde)
Jumping Jack
Mountain Climber
Bodyweight Squat
Burpee / Low Impact Burpee
High Knees

🔸 Core Finisher (10 menit)
Russian Twist – 3×20
Leg Raise – 3×15
Superman Hold – 3×30 detik

🔸 Pendinginan (10 menit)
Stretch + deep breathing

💪 HARI 4 – Full Body Functional Training
Fokus: kombinasi kekuatan, keseimbangan, dan ketahanan

🔸 Pemanasan (10 menit)
Dynamic stretch & ringan jogging

🔸 Latihan Sirkuit (40–45 menit)
Lakukan 3–4 ronde (1 menit istirahat antar ronde):
Squat to Press
Push-up
Deadlift (dumbbell / beban ringan)
Reverse Lunge
Mountain Climber
Plank Shoulder Tap

🔸 Pendinginan (10 menit)
Stretch seluruh tubuh

🫀 HARI 5 – Cardio Steady / Endurance Day
Fokus: daya tahan aerobik dan kontrol pernapasan

🔸 Pemanasan (10 menit)
Jalan cepat + mobilitas ringan

🔸 Cardio Utama (40–50 menit)
Pilih salah satu aktivitas:
Jogging jarak sedang (5–8 km)
Bersepeda 45–60 menit
Renang 30–45 menit

🔸 Pendinginan (10 menit)
Peregangan kaki dan pinggul

🧘 HARI 6 – Mobility & Active Recovery
Fokus: kelenturan, keseimbangan, dan pemulihan otot

🔸 Pemanasan (5–10 menit)
Jalan santai atau slow stretching

🔸 Latihan Inti (40–50 menit)
Yoga flow (Sun Salutation → Warrior → Down Dog → Cobra → Child Pose)
Core stability: Bird Dog, Dead Bug, Side Plank
Balance: One-leg stand, heel-to-toe walk
Light stretching seluruh tubuh

🔸 Pendinginan (5–10 menit)
Pernapasan dalam dan relaksasi tubuh penuh

💡  Tips Supaya Hasil Maksimal
    Gunakan intensitas sedang–tinggi (RPE 7–8/10) untuk sesi utama
    Tidur minimal 7 jam/malam untuk pemulihan
    Penuhi asupan protein & cairan setiap hari
    Hari Minggu: istirahat total atau jalan santai ringan                                        
                                              """)
                                        return
                                    case 7:
                                        print("\nAnda membutuhkan istirahat setidaknya 1 hari. Jangan memaksakan tubuh Anda.")
                                        continue
                                    case _:
                                        print("\nDalam satu minggu hanya ada 7 hari dari hari ke-1 sampai ke-7.")
                                        continue
                            except ValueError:
                                print("Inputan hanya berupa angka.")
                                continue
                    elif kfinput == "tidak":
                        continue
                    else:
                        print("\nInputan Anda tidak valid. Silahkan mengisi ulang inputan Anda.")
                        continue
                else:
                    while True:
                            try:
                                hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                                match hari:
                                    case 1:
                                        print("""
Anda membutuhkan latihan Kekuatan Ringan, Core, dan Mobilitas dengan tujuan untuk:
1️⃣ Meningkatkan kebugaran umum
2️⃣ Meningkatkan kekuatan otot 
3️⃣ Meningkatkan sistem kardiovaskular ringan   

🧘‍♀️ Workout Terbaik (1 Hari/Minggu) untuk BMI < 18.5

Durasi total: ±60 menit
Tujuan: meningkatkan kebugaran umum, kekuatan otot, dan sistem kardiovaskular ringan

🔹 Struktur Latihan
Pemanasan (10 menit)
Latihan Kekuatan Ringan (25 menit)
Latihan Cardio Ringan & Core (15 menit)
Pendinginan & Mobilitas (10 menit)

🟢 1️⃣ Pemanasan – 10 menit
Tujuan: memanaskan otot, melancarkan peredaran darah

Jalan cepat atau marching in place – 3 menit
Arm circle (putaran bahu) – 2×20 detik
Leg swing (ayunan kaki) – 2×10 per kaki
Torso twist (putar badan) – 1 menit
Deep breathing + light stretch – 2 menit

💪 2️⃣ Latihan Kekuatan Ringan – 25 menit
Tujuan: membentuk massa otot dan memperkuat sendi
Lakukan 3 set × 12–15 repetisi per gerakan, istirahat 30–60 detik tiap set:
Bodyweight Squat (atau chair squat)
Push-up lutut (atau incline push-up di meja)
Glute Bridge – angkat pinggul, tahan 2 detik di atas
Superman Hold – perkuat punggung bawah
Plank – tahan 30 detik
Dumbbell Row / Bottle Row (pakai beban ringan seperti botol air)

❤️ 3️⃣ Cardio Ringan & Core – 15 menit
Tujuan: melatih stamina tanpa defisit kalori besar

Lakukan 3 ronde:
March in Place – 1 menit
Side Step + Arm Swing – 1 menit
Low Impact Jumping Jack – 1 menit
Istirahat 30 detik
Ulang 3 kali

Lanjutkan:

Bicycle Crunch – 3×15 repetisi
Leg Raise – 3×10 repetisi

🧘 4️⃣ Pendinginan & Mobilitas – 10 menit
Tujuan: menurunkan detak jantung dan melenturkan otot

Hamstring stretch
Shoulder & chest stretch
Cat-Cow pose (mobilitas tulang belakang)
Child’s pose
Pernapasan dalam 3–5 menit

💡  Tips Penting
    Jangan fokus menurunkan berat. Fokus pada meningkatkan massa otot & energi.
    Pastikan makan cukup, terutama:
    Protein: telur, ayam, ikan, tempe, susu
    Karbohidrat kompleks: nasi merah, kentang, roti gandum
    Lemak sehat: alpukat, kacang, minyak zaitun
    Tidur minimal 7 jam/hari untuk pemulihan otot.
    Setelah 4–6 minggu, tubuh akan lebih kuat — bisa lanjut ke latihan 2x/minggu.  
                                        """)
                                        return
                                    case 2:
                                        print("""
Anda membutuhkan latihan Full Body Strength, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan massa otot & kekuatan tubuh
2️⃣	Meningkatkan stamina & sirkulasi darah
3️⃣	Meningkatkan stabilitas & postur
4️⃣	Meningkatkan berat badan sehat

💪 HARI 1 – Full Body Strength & Core
Tujuan: menstimulasi pertumbuhan otot & meningkatkan kekuatan tubuh secara keseluruhan

🔸 Pemanasan (10 menit)
Jalan cepat atau jogging ringan di tempat – 3 menit
Arm circle, torso twist, leg swing – 2 menit
Dynamic stretch – 5 menit

🔸 Latihan Inti (40 menit)
Lakukan 3 set × 10–12 repetisi tiap gerakan (istirahat 45–60 detik per set)
Bodyweight Squat / Goblet Squat (pakai beban ringan)
Push-up lutut / incline push-up di meja
Glute Bridge (angkat pinggul, tahan 2 detik di atas)
Dumbbell Row / Bottle Row (pakai beban ringan)
Shoulder Press (bisa pakai dumbbell atau botol air)
Superman Hold – 3×30 detik
Plank – 3×30–45 detik

🔸 Finisher (10 menit)
3 ronde sirkuit ringan:
Jumping Jack (low impact) – 30 detik
Mountain Climber pelan – 30 detik
Istirahat 30 detik

🔸 Pendinginan (10 menit)
Stretch kaki, punggung, dan bahu
Pernapasan dalam (3–5 menit)

❤️ HARI 2 – Functional Cardio + Mobility
Tujuan: meningkatkan kebugaran jantung-paru, koordinasi tubuh, dan kelenturan otot

🔸 Pemanasan (10 menit)
Marching in place – 2 menit
Side step + arm swing – 2 menit
Dynamic stretching – 6 menit

🔸 Functional Cardio Circuit (30–35 menit)
Lakukan 4 ronde:
Step-up (pakai tangga / kursi rendah) – 1 menit
Jumping Jack low impact – 1 menit
Bodyweight Squat – 1 menit
Shoulder Tap Plank – 30 detik
Istirahat 1 menit antar ronde

🔸 Core Stability (10 menit)
Dead Bug – 3×12
Side Plank – 2×30 detik per sisi
Leg Raise – 3×10

🔸 Mobility & Stretching (10 menit)
Cat-cow pose
Cobra stretch
Hamstring stretch
Hip flexor stretch
Deep breathing

⚡ Tips Penting
    Fokus pada asupan kalori dan protein tinggi:
    Protein: telur, susu, ikan, ayam, tempe, tahu
    Karbo: nasi, roti gandum, kentang
    Lemak sehat: kacang, alpukat, minyak zaitun
    
    Minum cukup air (2–3 liter/hari)
    Tidur 7–9 jam per malam
    Jangan cardio berlebihan — cukup cardio ringan saja                        
                                              """)
                                        return
                                    case 3:
                                        print("""
Anda membutuhkan latihan Full Body Strength, Cardio Ringan, dan Functional dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan & massa otot
2️⃣ Memperbaiki stamina dan kebugaran jantung-paru
3️⃣ Menjaga energi dan pemulihan optimal

💪 HARI 1 – Full Body Strength
Tujuan: merangsang pertumbuhan otot dan meningkatkan kekuatan tubuh secara merata.

🔸 Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Dynamic stretch: arm swing, leg swing, torso twist – 5 menit
10 squat + 10 shoulder circle – 2 menit

🔸 Latihan Inti (45 menit)
3–4 set × 10–12 repetisi (istirahat 45–60 detik antar set)
Bodyweight Squat / Goblet Squat (beban ringan)
Push-up lutut / incline push-up
Glute Bridge / Hip Thrust
Dumbbell Row (pakai botol air kalau di rumah)
Shoulder Press (beban ringan)
Plank – 3×30–45 detik

🔸 Pendinginan (10 menit)
Stretch otot kaki, bahu, punggung
Deep breathing 2–3 menit

❤️ HARI 2 – Cardio Ringan + Core Stability
Tujuan: memperkuat jantung, paru, dan otot inti tanpa membakar kalori berlebihan.

🔸 Pemanasan (10 menit)
Marching in place – 2 menit
Arm circle & leg swing – 3 menit
Dynamic stretch ringan – 5 menit

🔸 Cardio Ringan (25–30 menit)
Pilih salah satu aktivitas berikut:
Jalan cepat di luar / treadmill (kecepatan sedang, 30–40 menit)
Bersepeda santai 30 menit
Lompat tali pelan (5 set × 1 menit, istirahat 30 detik)

🔸 Core Training (15 menit)
3 set × 12–15 repetisi:
Leg Raise
Dead Bug
Side Plank – 30 detik per sisi
Superman Hold

🔸 Pendinginan (10 menit)
Stretch punggung dan perut
Pernapasan dalam

🧘 HARI 3 – Functional & Mobility Training
Tujuan: meningkatkan kelenturan, keseimbangan, koordinasi, dan daya tahan tubuh ringan.

🔸 Pemanasan (10 menit)
Jalan ringan
Dynamic full-body stretch

🔸 Functional Circuit (30–40 menit)
Lakukan 3 ronde (1 menit istirahat antar ronde)
Step-up (pakai tangga pendek) – 45 detik
Push-up – 45 detik
Lunge – 45 detik
Superman Hold – 45 detik
Jumping Jack (low impact) – 45 detik

🔸 Mobility & Balance (15 menit)
Cat-Cow Pose
Downward Dog → Cobra Stretch
Hip Flexor Stretch
One-leg Balance (30 detik/sisi)
Deep Breathing & Relax            

💡 Tips Agar Hasil Maksimal
    Fokus makan cukup kalori & protein tinggi
    Sumber protein: telur, ayam, ikan, tempe, susu
    Sumber karbo: nasi, kentang, roti gandum
    Sumber lemak sehat: alpukat, kacang, minyak zaitun
    Jangan overtraining — tubuh butuh waktu pulih.
    Minum air 2–3 L/hari.
    Tidur cukup (7–9 jam/malam) untuk regenerasi otot.  
    Setelah 4–6 minggu, kamu bisa naikkan ke 4 hari/minggu dengan pola serupa.                                    
                                              """)
                                        return
                                    case 4:
                                        print("""
Anda membutuhkan latihan Strength, Cardio Ringan, dan Functional dengan tujuan untuk:
1️⃣  Meningkatkan massa otot & postur
2️⃣  Stamina jantung & paru meningkat
3️⃣  Mengurangi kaku otot & risiko cedera

💪 HARI 1 – Upper Body Strength
Fokus: dada, punggung, bahu, dan lengan

Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist, dynamic stretch – 7 menit
Latihan Inti (40–45 menit)
3 set × 10–12 repetisi (istirahat 45–60 detik)
Push-up lutut / incline push-up
Dumbbell Row / Bottle Row
Shoulder Press (beban ringan)
Bicep Curl
Tricep Dips
Plank – 30–45 detik
Pendinginan (5–10 menit)
Stretch bahu, dada, punggung

🦵 HARI 2 – Lower Body Strength
Fokus: kaki, bokong, dan stabilitas

Pemanasan (10 menit)
Skipping ringan / marching in place – 5 menit
Leg swing, hip rotation – 5 menit
Latihan Inti (40–45 menit)
3 set × 12–15 repetisi
Squat / Goblet Squat
Lunges kanan-kiri
Step-up (pakai kursi / tangga)
Glute Bridge / Hip Thrust
Calf Raise
Side Plank – 30 detik per sisi
Pendinginan (5–10 menit)
Stretch kaki & pinggul

❤️ HARI 3 – Cardio Ringan + Core
Fokus: meningkatkan stamina jantung-paru dan memperkuat inti tubuh

Pemanasan (10 menit)
Marching in place – 3 menit
Arm swing & torso twist – 2 menit
Dynamic stretching – 5 menit
Cardio Ringan (25–30 menit)
Jalan cepat, jogging ringan, atau bersepeda santai
Low impact jumping jack / step touch
Core (15 menit)
3 set:
Dead Bug – 12–15 repetisi
Leg Raise – 10–12 repetisi
Superman Hold – 30 detik
Pendinginan (5–10 menit)
Stretch perut, punggung, dan pinggul
Deep breathing

🧘 HARI 4 – Functional Training + Mobility
Fokus: koordinasi, keseimbangan, kelenturan, dan pemulihan otot

Pemanasan (10 menit)
Jalan santai / dynamic stretch
Functional Circuit (30–35 menit)
3 ronde, istirahat 1 menit antar ronde
Step-up – 45 detik
Push-up – 45 detik
Lunge – 45 detik
Plank Shoulder Tap – 45 detik
Low Impact Jumping Jack – 45 detik
Mobility & Balance (15–20 menit)
Cat-Cow Pose
Cobra Stretch
Downward Dog
Hip Flexor Stretch
One-leg Balance – 30 detik per sisi
Pendinginan (5–10 menit)
Deep breathing & stretch seluruh tubuh

💡 Tips Penting
    Makan cukup kalori & protein tinggi (telur, ayam, ikan, tempe, susu)
    Istirahat minimal 7 jam/malam agar otot pulih
    Hindari cardio berlebihan, cukup ringan untuk stamina
    Gunakan beban ringan & gerakan terkontrol untuk safety
    Setelah 4–6 minggu, bisa naik ke latihan 5–6 hari dengan pola serupa                                                
                                              """)
                                        return
                                    case 5:
                                        print("""
Anda membutuhkan latihan Strength, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan & massa otot
2️⃣ Meningkatkan stamina ringan
3️⃣ Meningkatkan postur & koordinasi tubuh

💪 Hari 1 – Upper Body Strength
Durasi: 60–70 menit

Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist, dynamic stretch – 7 menit

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Push-up lutut / incline push-up
Dumbbell Row / Bottle Row
Shoulder Press (beban ringan)
Bicep Curl
Tricep Dips
Plank – 30–45 detik
Pendinginan (5–10 menit)
Stretch bahu, dada, dan punggung

🦵 Hari 2 – Lower Body Strength
Durasi: 60–70 menit

Pemanasan (10 menit)
Skipping ringan / marching in place – 5 menit
Leg swing, hip rotation – 5 menit
Latihan Inti (40 menit)
3 set × 12–15 repetisi:
Squat / Goblet Squat
Lunge kanan-kiri
Step-up
Glute Bridge / Hip Thrust
Calf Raise
Side Plank – 30 detik per sisi
Pendinginan (5–10 menit)
Stretch kaki & pinggul

💪 Hari 3 – Upper Body Strength (variasi)
Fokus: variasi otot atas untuk pertumbuhan optimal

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Incline Push-up / Knee Push-up
Dumbbell Fly / Chest Press ringan
Bent Over Row
Lateral Raise
Plank to Shoulder Tap
Supermans – 3×30 detik
Pendinginan
Stretch seluruh tubuh bagian atas

🦵 Hari 4 – Lower Body Strength (variasi)
Fokus: variasi kaki & glutes

Latihan Inti (40–45 menit)
3 set × 12–15 repetisi:
Bulgarian Split Squat (pakai kursi)
Glute Kickback
Step-up lateral
Calf Raise
Side Plank Hip Lift – 2×30 detik per sisi
Pendinginan
Stretch kaki & pinggul

❤️ Hari 5 – Cardio Ringan + Core & Mobility
Durasi: 60 menit

Cardio Ringan (30 menit)
Jalan cepat / jogging ringan / bersepeda santai
Low impact jumping jack atau step touch
Core & Stability (20 menit)
3 set:
Dead Bug – 12–15 repetisi
Leg Raise – 12 repetisi
Side Plank – 30 detik per sisi
Superman Hold – 30 detik
Mobility & Stretching (10 menit)
Cat-Cow Pose, Cobra, Downward Dog, Hip Flexor Stretch
Deep breathing 3–5 menit                       

💡 Tips Penting
    Makan cukup kalori & protein tinggi
    Tidur 7–9 jam/hari untuk pemulihan
    Hindari cardio intens — cukup ringan untuk stamina
    Gunakan beban ringan dan gerakan terkontrol
    Setelah 4–6 minggu, bisa meningkatkan beban atau repetisi untuk pertumbuhan otot                          
                                              """)
                                        return
                                    case 6:
                                        print("""
Anda membutuhkan latihan Strength, Functional, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan dan massa otot
2️⃣ Meningkatkan stamina ringan & koordinasi tubuh
3️⃣ Menjaga energi agar tidak kelelahan
4️⃣ Pemulihan optimal untuk pertumbuhan otot

Hari 1 – Upper Body Strength
Push-up lutut / incline push-up – 3×10–12
Dumbbell Row / Bottle Row       – 3×10–12
Shoulder Press ringan           – 3×10–12
Bicep Curl                      – 3×10–12
Tricep Dips                     – 3×10–12
Plank                           – 3×30–45 detik
Pemanasan 10 menit, pendinginan 5–10 menit

🦵 Hari 2 – Lower Body Strength
Squat / Goblet Squat        – 3×12–15
Lunge kanan-kiri            – 3×12 per sisi
Step-up                     – 3×12–15
Glute Bridge / Hip Thrust   – 3×12–15
Calf Raise                  – 3×15
Side Plank                  – 3×30 detik per sisi
Pemanasan 10 menit, pendinginan 5–10 menit

💪 Hari 3 – Upper Body Strength (Variasi)
Incline Push-up / Knee Push-up    – 3×10–12
Dumbbell Fly / Chest Press ringan – 3×10–12
Bent Over Row                     – 3×10–12
Lateral Raise                     – 3×10–12
Plank to Shoulder Tap             – 3×10–12
Superman Hold                     – 3×30 detik
Pemanasan & pendinginan sama seperti hari 1

🦵 Hari 4 – Lower Body Strength (Variasi)
Bulgarian Split Squat – 3×12 per kaki
Glute Kickback        – 3×12 per kaki
Step-up lateral       – 3×12 per kaki
Calf Raise            – 3×15
Side Plank Hip Lift   – 3×30 detik per sisi
Pemanasan & pendinginan sama seperti hari 2

🫀 Hari 5 – Full Body Functional Training
Squat to Press                         – 3 ronde × 45 detik
Push-up                                – 3 ronde × 45 detik
Deadlift ringan (dumbbell / botol air) – 3×12
Reverse Lunge                          – 3×12 per kaki
Mountain Climber pelan                 – 3×30 detik
Plank Shoulder Tap                     – 3×30 detik
Pemanasan 10 menit, pendinginan 5–10 menit

❤️ Hari 6 – Cardio Ringan + Core & Mobility
Cardio ringan (jalan cepat / jogging / bersepeda)                                – 30 menit
Core: Dead Bug, Leg Raise, Side Plank, Superman Hold                             – 20 menit
Mobility & Stretching: Cat-Cow, Cobra, Downward Dog, Hip Flexor, One-leg Balance – 10–15 menit         

💡 Tips Penting
    Konsumsi kalori lebih banyak & protein tinggi (telur, ayam, ikan, tempe, susu)
    Tidur 7–9 jam/malam agar otot pulih maksimal
    Gunakan beban ringan & gerakan terkontrol
    Cardio jangan berlebihan — cukup ringan untuk stamina
    Progressive overload: setelah 4–6 minggu, tambahkan beban atau repetisi untuk pertumbuhan otot
                                              """)
                                        return
                                    case 7:
                                        print("\nAnda membutuhkan istirahat setidaknya 1 hari. Jangan memaksakan tubuh Anda.")
                                        continue
                                    case _:
                                        print("\nDalam satu minggu hanya ada 7 hari dari hari ke-1 sampai ke-7.")
                                        continue
                            except ValueError:
                                print("Inputan hanya berupa angka.")
                                continue
            elif tujuan == 3:
                if 3 <= kode <= 6:
                    print("\nBerat badan Anda berlebih. Kami merekomendasikan untuk menurunkan berat badan.")
                    continue
                elif kode == 2:
                    while True:
                            try:
                                hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                                match hari:
                                    case 1:
                                        print("""
Anda membutuhkan latihan Strength, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan dan stamina, core, dan mobilitas dalam satu sesi.
2️⃣ Melatih core dan mobilitas dalam satu sesi.

1️⃣ Pemanasan – 10 menit
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist, leg swing – 5 menit
Bodyweight squat ringan – 2 menit

2️⃣ Latihan Kekuatan Full Body – 30–35 menit
Lakukan 3 set × 10–12 repetisi per gerakan, istirahat 45–60 detik
Push-up (normal / lutut) 
Dumbbell Row / Botol Air Row 
Shoulder Press ringan 
Squat / Goblet Squat 
Lunge kanan-kiri 
Glute Bridge 
Plank – 30–45 detik

3️⃣ Cardio Ringan & Core – 15 menit
Cardio ringan:
Jumping Jack low impact – 1 menit
Mountain Climber pelan – 1 menit
Side Step / High Knees ringan – 1 menit
Istirahat 30 detik, ulang 3–4 ronde

Core:
Dead Bug – 12–15 repetisi
Leg Raise – 12 repetisi
Side Plank – 30 detik per sisi

4️⃣ Pendinginan & Mobility – 10–15 menit
Stretch seluruh tubuh: kaki, punggung, bahu, dada
Cat-Cow Pose, Cobra, Downward Dog
Pernapasan dalam & relaksasi 2–3 menit    

💡 Tips:
    Karena hanya satu hari, gunakan intensitas sedang-tinggi (RPE 7–8/10) tapi tetap kontrol gerakan.
    Tetap aktif di hari lain (jalan santai, stretching ringan) agar energi tubuh tetap stabil.
    Pastikan protein cukup untuk pemeliharaan otot.                                         
                                              """)
                                        return
                                    case 2:
                                        print("""
Anda membutuhkan latihan Strength, Cardio, dan Mobility dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan dan stamina, core, dan mobilitas dalam satu sesi.
2️⃣ Melatih core dan mobilitas dalam satu sesi.

Pilihan Jadwal:
Opsional A – Full Body Day 1 & Day 2
Kedua hari latih semua otot tubuh, fokus intensitas berbeda

Hari 1: kekuatan + core
Hari 2: endurance ringan + mobilitas

Opsional B – Upper / Lower Split

Hari 1: Upper Body + Core
Hari 2: Lower Body + Cardio ringan

🔹 Contoh Opsional B – Upper/Lower Split
Hari 1 – Upper Body + Core (60–70 menit)

Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist – 5 menit
Push-up ringan / bodyweight squat – 2 menit

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Push-up / Push-up lutut – dada & lengan
Dumbbell Row / Bottle Row – punggung
Shoulder Press – bahu
Bicep Curl – lengan
Tricep Dips – lengan belakang
Plank – 30–45 detik
Pendinginan & Stretch (10–15 menit)
Stretch bahu, dada, punggung
Cat-Cow Pose & Cobra

Hari 2 – Lower Body + Cardio Ringan (60–75 menit)
Pemanasan (10 menit)
Jalan cepat / marching in place – 3 menit
Leg swing, hip rotation – 5 menit
Bodyweight squat – 2 menit

Latihan Inti (40–45 menit)
3 set × 12–15 repetisi:
Squat / Goblet Squat – kaki & glutes
Lunge kanan-kiri – kaki & keseimbangan
Step-up (kursi / tangga) – kaki & glutes
Glute Bridge – pinggul & hamstring
Calf Raise – betis
Side Plank – 30 detik per sisi
Cardio Ringan (10–15 menit)
Jumping Jack low impact / Step Touch / Marching in place
Pendinginan & Mobility (5–10 menit)
Stretch kaki & pinggul
Deep breathing & relaksasi       

💡 Tips:
    Fokus intensitas sedang-tinggi (RPE 7–8/10) karena frekuensi rendah.
    Pastikan protein cukup untuk pemeliharaan otot.
    Lakukan aktivitas ringan di hari lain (jalan, stretching) agar tubuh tetap aktif.                                     
                                              """)
                                        return
                                    case 3:
                                        print("""
Anda membutuhkan latihan Full-Body Workout atau split Upper-Lower-Full Core dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan otot
2️⃣ Meningkatkan stamina jantung-paru
3️⃣ Memperkuat core & stabilitas
4️⃣ Menjaga fleksibilitas & mobilitas  

🔹 Opsi 1 – Full-Body Setiap Hari
Hari 1, 2, 3: Full-body workout dengan variasi gerakan agar otot tidak monoton.
Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist, leg swing – 5 menit
Bodyweight squat ringan – 2 menit

Latihan Kekuatan Full-Body (30–35 menit)
3 set × 10–12 repetisi per gerakan:
Push-up (normal/lutut) – dada & lengan
Dumbbell Row / Botol Row – punggung
Shoulder Press ringan – bahu
Squat / Goblet Squat – kaki & glutes
Lunge kanan-kiri – kaki & keseimbangan
Glute Bridge – pinggul & hamstring
Plank – 30–45 detik
Cardio ringan & Core (15 menit)
Jumping Jack low impact / March in place – 1 menit × 3 ronde
Dead Bug – 12–15 repetisi
Side Plank – 30 detik per sisi
Pendinginan & Mobility (10–15 menit)
Stretch seluruh tubuh: kaki, punggung, bahu, dada
Cat-Cow Pose, Cobra, Downward Dog
Pernapasan dalam 2–3 menit

🔹 Opsi 2 – Upper / Lower / Core Split
Hari 1: Upper Body + Core
Hari 2: Lower Body + Cardio Ringan
Hari 3: Full-Body Functional Training + Mobility
Hari 1 – Upper Body + Core
Push-up / Incline Push-up – 3×10–12
Dumbbell Row – 3×10–12
Shoulder Press – 3×10–12
Plank – 3×30–45 detik
Side Plank – 2×30 detik per sisi
Hari 2 – Lower Body + Cardio Ringan
Squat / Goblet Squat – 3×12–15
Lunge kanan-kiri – 3×12 per kaki
Step-up – 3×12–15
Glute Bridge – 3×12–15
Calf Raise – 3×15
Cardio ringan 10–15 menit (jalan cepat / step touch / low-impact jumping jack)

Hari 3 – Full-Body Functional + Mobility
Squat to Press – 3×12
Push-up – 3×12
Deadlift ringan – 3×12
Reverse Lunge – 3×12
Plank Shoulder Tap – 3×10–12
Mobility & Stretching 10–15 menit

💡 Tips:
    Gunakan intensitas sedang-tinggi (RPE 7–8/10) karena frekuensi rendah.
    Pastikan protein & kalori cukup untuk pemeliharaan otot.
    Lakukan aktivitas ringan di hari tanpa latihan (jalan santai, stretching) agar tubuh tetap aktif.                                           
                                              """)
                                        return
                                    case 4:
                                        print("""
Anda membutuhkan latihan Upper-Lower Split atau Upper-Lower-Full Body/Functional dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan otot
2️⃣ Meningkatkan stamina jantung-paru
3️⃣ Memperkuat core & stabilitas
4️⃣ Menjaga fleksibilitas & mobilitas 

🔹 Contoh Jadwal Upper-Lower Split
Hari 1: Upper Body + Core
Hari 2: Lower Body + Cardio Ringan
Hari 3: Upper Body Variasi + Core
Hari 4: Lower Body Variasi + Functional Training

1️⃣ Hari 1 – Upper Body + Core
Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist – 5 menit
Push-up ringan / bodyweight squat – 2 menit

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Push-up / Incline Push-up – dada & lengan
Dumbbell Row / Bottle Row – punggung
Shoulder Press – bahu
Bicep Curl – lengan
Tricep Dips – lengan belakang
Plank – 30–45 detik

Pendinginan & Stretching (10–15 menit)
Stretch bahu, dada, punggung
Cat-Cow & Cobra

2️⃣ Hari 2 – Lower Body + Cardio Ringan
Pemanasan (10 menit)
Jalan cepat / marching in place – 3 menit
Leg swing, hip rotation – 5 menit
Bodyweight squat – 2 menit

Latihan Inti (40–45 menit)
3 set × 12–15 repetisi:
Squat / Goblet Squat – kaki & glutes
Lunge kanan-kiri – kaki & keseimbangan
Step-up – kaki & glutes
Glute Bridge – pinggul & hamstring
Calf Raise – betis
Side Plank – 30 detik per sisi
Cardio Ringan (10–15 menit)
Jalan cepat / low-impact jumping jack / step touch
Pendinginan & Mobility (5–10 menit)
Stretch kaki & pinggul
Deep breathing & relaksasi

3️⃣ Hari 3 – Upper Body Variasi + Core
Incline Push-up / Knee Push-up – 3×10–12
Dumbbell Fly / Chest Press ringan – 3×10–12
Bent Over Row – 3×10–12
Lateral Raise – 3×10–12
Plank to Shoulder Tap – 3×10–12
Superman Hold – 3×30 detik
Pemanasan & Pendinginan sama seperti Hari 1

4️⃣ Hari 4 – Lower Body Variasi + Functional Training
Bulgarian Split Squat – 3×12 per kaki
Glute Kickback – 3×12 per kaki
Step-up lateral – 3×12 per kaki
Calf Raise – 3×15
Side Plank Hip Lift – 3×30 detik per sisi
Functional Circuit (Squat to Press, Reverse Lunge, Plank Shoulder Tap) – 3 ronde × 45 detik
Pemanasan & Pendinginan sama seperti Hari 2                                             

💡 Tips:
    Gunakan intensitas sedang-tinggi (RPE 7–8/10)
    Pastikan protein & kalori cukup untuk pemeliharaan otot
    Aktivitas ringan di hari tanpa latihan (jalan santai, stretching) tetap dianjurkan
                                              """)
                                        return
                                    case 5:
                                        print("""
Anda membutuhkan latihan Upper-Lower-Full Body atau Upper-Lower-Functional Split dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan otot
2️⃣ Meningkatkan stamina jantung-paru
3️⃣ Memperkuat core & stabilitas
4️⃣ Menjaga fleksibilitas & mobilitas 

1️⃣ Hari 1 – Upper Body Strength
Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist – 5 menit
Push-up ringan – 2 menit

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Push-up / Incline Push-up
Dumbbell Row / Bottle Row
Shoulder Press
Bicep Curl
Tricep Dips
Plank – 30–45 detik

Pendinginan (10 menit)
Stretch bahu, dada, punggung
Cat-Cow & Cobra

2️⃣ Hari 2 – Lower Body Strength
Pemanasan (10 menit)
Marching / leg swing / bodyweight squat

Latihan Inti (40–45 menit)
3 set × 12–15 repetisi:
Squat / Goblet Squat
Lunge kanan-kiri
Step-up
Glute Bridge
Calf Raise
Side Plank – 30 detik per sis

Cardio Ringan (10–15 menit)
Jalan cepat / low-impact jumping jack
Pendinginan (5–10 menit)
Stretch kaki & pinggul
Deep breathing

3️⃣ Hari 3 – Upper Body Variasi + Core
Incline Push-up / Knee Push-up – 3×10–12
Dumbbell Fly / Chest Press ringan – 3×10–12
Bent Over Row – 3×10–12
Lateral Raise – 3×10–12
Plank to Shoulder Tap – 3×10–12
Superman Hold – 3×30 detik

4️⃣ Hari 4 – Lower Body Variasi + Functional
Bulgarian Split Squat – 3×12 per kaki
Glute Kickback – 3×12 per kaki
Step-up lateral – 3×12 per kaki
Calf Raise – 3×15
Side Plank Hip Lift – 3×30 detik per sisi
Functional Circuit: Squat to Press, Reverse Lunge, Plank Shoulder Tap – 3 ronde × 45 detik

5️⃣ Hari 5 – Full Body / Functional + Core / Mobility
Latihan Inti (45–50 menit)
Squat to Press – 3×12
Push-up – 3×12
Deadlift ringan – 3×12
Reverse Lunge – 3×12
Mountain Climber pelan – 3×30 detik
Plank Shoulder Tap – 3×10–12
Mobility & Stretching (10–15 menit)
Cat-Cow, Cobra, Downward Dog, Hip Flexor Stretch
One-leg Balance & deep breathing

💡 Tips:
    Gunakan intensitas sedang-tinggi (RPE 7–8/10) karena frekuensi cukup tinggi
    Pastikan protein & kalori cukup untuk pemeliharaan otot
    Aktivitas ringan di hari tanpa latihan tetap dianjurkan
                                              """)
                                        return
                                    case 6:
                                        print("""
Anda membutuhkan latihan Upper-Lower-Full Body atau Upper-Lower-Functional Split dengan tujuan untuk:
1️⃣ Meningkatkan kekuatan otot
2️⃣ Meningkatkan stamina jantung-paru
3️⃣ Memperkuat core & stabilitas
4️⃣ Menjaga fleksibilitas & mobilitas 

1️⃣ Hari 1 – Upper Body Strength
Pemanasan (10 menit)
Jalan cepat / jogging ringan – 3 menit
Arm circle, torso twist – 5 menit
Push-up ringan – 2 menit

Latihan Inti (40 menit)
3 set × 10–12 repetisi:
Push-up / Incline Push-up
Dumbbell Row / Bottle Row
Shoulder Press
Bicep Curl
Tricep Dips
Plank – 30–45 detik

Pendinginan (10 menit)
Stretch bahu, dada, punggung
Cat-Cow & Cobra

2️⃣ Hari 2 – Lower Body Strength
Pemanasan (10 menit)
Marching / leg swing / bodyweight squat

Latihan Inti (40–45 menit)
3 set × 12–15 repetisi:
Squat / Goblet Squat
Lunge kanan-kiri
Step-up
Glute Bridge
Calf Raise
Side Plank – 30 detik per sisi

Cardio Ringan (10–15 menit)
Jalan cepat / low-impact jumping jack

Pendinginan (5–10 menit)
Stretch kaki & pinggul

3️⃣ Hari 3 – Full Body / Functional + Core
Latihan Inti (45–50 menit)
Squat to Press – 3×12
Push-up – 3×12
Deadlift ringan – 3×12
Reverse Lunge – 3×12
Mountain Climber pelan – 3×30 detik
Plank Shoulder Tap – 3×10–12

Mobility & Stretching (10–15 menit)
Cat-Cow, Cobra, Downward Dog, Hip Flexor Stretch
One-leg Balance & deep breathing

4️⃣ Hari 4 – Upper Body Variasi + Core
Incline Push-up / Knee Push-up – 3×10–12
Dumbbell Fly / Chest Press ringan – 3×10–12
Bent Over Row – 3×10–12
Lateral Raise – 3×10–12
Plank to Shoulder Tap – 3×10–12
Superman Hold – 3×30 detik

5️⃣ Hari 5 – Lower Body Variasi + Functional
Bulgarian Split Squat – 3×12 per kaki
Glute Kickback – 3×12 per kaki
Step-up lateral – 3×12 per kaki
Calf Raise – 3×15
Side Plank Hip Lift – 3×30 detik per sisi
Functional Circuit: Squat to Press, Reverse Lunge, Plank Shoulder Tap – 3 ronde × 45 detik

6️⃣ Hari 6 – Full Body / Functional + Core / Mobility
Latihan Inti (45–50 menit)
Squat to Press – 3×12
Push-up – 3×12
Deadlift ringan – 3×12
Reverse Lunge – 3×12
Plank Shoulder Tap – 3×10–12
Mountain Climber pean – 3×30 detik

Mobility & Stretching (10–15 menit)
Cat-Cow, Cobra, Downward Dog, Hip Flexor Stretch
One-leg Balance & deep breathing 

💡 Tips:
    Gunakan intensitas sedang-tinggi (RPE 7–8/10) karena frekuensi tinggi
    Pastikan protein & kalori cukup untuk pemeliharaan otot
    Aktivitas ringan di hari tanpa latihan tetap dianjurkan                                            
                                              """)
                                        return
                                    case 7:
                                        print("\nAnda membutuhkan istirahat setidaknya 1 hari. Jangan memaksakan tubuh Anda.")
                                        continue
                                    case _:
                                        print("\nDalam satu minggu hanya ada 7 hari dari hari ke-1 sampai ke-7.")
                                        continue
                            except ValueError:
                                print("Inputan hanya berupa angka.")
                                continue
                else:
                    print("\nBerat badan Anda kurang. Kami merekomendasikan untuk meningkatkan kebugaran fisik.")
                    continue
            else:
                print("\nHanya ada 3 pilihan.")
                continue
            return
        except ValueError:
            print("Inputan Anda tidak valid. Silahkan mengisi inputan kembali.")
            continue