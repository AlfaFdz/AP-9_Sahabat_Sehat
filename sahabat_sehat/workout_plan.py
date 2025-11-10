def workout_plan(kode):
    while True:
        tujuan = input("\nApa tujuan Anda melakukan workout (menurunkan berat badan (bb), meningkatkan kebugaran fisik(kf), dan meningkatkan massa otot(mo))? ").lower()

        if tujuan == "bb":
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
        elif tujuan == "kf":
            if 3 <= kode <= 6:
                kfinput = input("\nAnda dapat meningkatkan kebugaran fisik Anda. Tetapi kami merekomendasikan untuk menurunkan berat badan. Apakah anda ingin lanjut meningkatkan kebugaran fisik (iya/tidak)? ").lower()
                if kfinput == "iya":
                    while True:
                        try:
                            hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                            match hari:
                                case 1:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
                                          """)
                                    return
                                case 2:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
                                          """)
                                    return
                                case 3:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
                                          """)
                                    return
                                case 4:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
                                          """)
                                    return
                                case 5:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
                                          """)
                                    return
                                case 6:
                                    print("""
Anda membutuhkan latihan kardio dan kekuatan otot besar (Full Body Low-Impact HIIT) dengan tujuan untuk:
1️⃣ Membakar banyak kalori dalam satu sesi
2️⃣ Meningkatkan metabolisme (efek afterburn) selama 24–48 jam
3️⃣ Tetap aman untuk sendi dan lutut                                          
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
                    return
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
                                    #TODO
                                    return
                                case 2:
                                    #TODO
                                    return
                                case 3:
                                    #TODO
                                    return
                                case 4:
                                    #TODO
                                    return
                                case 5:
                                    #TODO
                                    return
                                case 6:
                                    #TODO
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
                                    #TODO
                                    return
                                case 2:
                                    #TODO
                                    return
                                case 3:
                                    #TODO
                                    return
                                case 4:
                                    #TODO
                                    return
                                case 5:
                                    #TODO
                                    return
                                case 6:
                                    #TODO
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
        elif tujuan == "mo":
            if 3 <= kode <= 6:
                print("\nBerat badan Anda berlebih. Kami merekomendasikan untuk menurunkan berat badan.")
                continue
            elif kode == 2:
                while True:
                        try:
                            hari = int(input("\nDalam satu minggu, berapa kali Anda dapat berolahraga? "))
                            match hari:
                                case 1:
                                    #TODO
                                    return
                                case 2:
                                    #TODO
                                    return
                                case 3:
                                    #TODO
                                    return
                                case 4:
                                    #TODO
                                    return
                                case 5:
                                    #TODO
                                    return
                                case 6:
                                    #TODO
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
            print("\nInputan Anda tidak valid. Silahkan mengisi ulang inputan Anda.")
            continue
        return