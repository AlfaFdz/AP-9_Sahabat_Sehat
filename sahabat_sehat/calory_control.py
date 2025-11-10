import random

FOODS = [
    {"id": 1,"name": "Nasi putih (100g)", "cal": 130, "protein": 2.7, "carb": 28, "fat": 0.3, "category": "Karbohidrat"},
    {"id": 2,"name": "Nasi merah (100g)", "cal": 111, "protein": 2.6, "carb": 23, "fat": 0.9, "category": "Karbohidrat"},
    {"id": 3,"name": "Roti tawar (1 iris)", "cal": 80, "protein": 3.0, "carb": 14, "fat": 1.0, "category": "Karbohidrat"},
    {"id": 4,"name": "Telur ayam (1 butir, 50g)", "cal": 78, "protein": 6.3, "carb": 0.6, "fat": 5.3, "category": "Protein Hewani"},
    {"id": 5,"name": "Ayam panggang (100g)", "cal": 165, "protein": 31, "carb": 0, "fat": 3.6, "category": "Protein Hewani"},
    {"id": 6,"name": "Ikan tuna (100g)", "cal": 132, "protein": 29, "carb": 0, "fat": 1.0, "category": "Protein Hewani"},
    {"id": 7,"name": "Tahu (100g)", "cal": 76, "protein": 8.1, "carb": 1.9, "fat": 4.8, "category": "Protein Nabati"},
    {"id": 8,"name": "Tempe (100g)", "cal": 192, "protein": 20.3, "carb": 7.6, "fat": 10.8, "category": "Protein Nabati"},
    {"id": 9,"name": "Sapi giling (100g)", "cal": 250, "protein": 26, "carb": 0, "fat": 17, "category": "Protein Hewani"},
    {"id": 10,"name": "Kentang rebus (100g)", "cal": 87, "protein": 2.0, "carb": 20.1, "fat": 0.1, "category": "Karbohidrat"},
    {"id": 11,"name": "Pisang (1 buah, 118g)", "cal": 105, "protein": 1.3, "carb": 27, "fat": 0.3, "category": "Buah"},
    {"id": 12,"name": "Apel (1 buah, 182g)", "cal": 95, "protein": 0.5, "carb": 25, "fat": 0.3, "category": "Buah"},
    {"id": 13,"name": "Susu rendah lemak (200ml)", "cal": 102, "protein": 6.8, "carb": 12, "fat": 2.4, "category": "Produk Susu"},
    {"id": 14,"name": "Yoghurt (plain, 100g)", "cal": 59, "protein": 10, "carb": 3.6, "fat": 0.4, "category": "Produk Susu"},
    {"id": 15,"name": "Keju cheddar (30g)", "cal": 120, "protein": 7, "carb": 0.4, "fat": 10, "category": "Produk Susu"},
    {"id": 16,"name": "Almond (30g)", "cal": 174, "protein": 6.4, "carb": 6.1, "fat": 15.2, "category": "Lemak Sehat"},
    {"id": 17,"name": "Minyak goreng (1 sdm)", "cal": 120, "protein": 0, "carb": 0, "fat": 14, "category": "Lemak"},
    {"id": 18,"name": "Soto ayam (1 mangkuk, 300g)", "cal": 250, "protein": 20, "carb": 10, "fat": 14, "category": "Makanan Campuran"},
    {"id": 19,"name": "Mie instan (1 bungkus)", "cal": 380, "protein": 7, "carb": 50, "fat": 16, "category": "Karbohidrat"},
    {"id": 20,"name": "Salad hijau (100g)", "cal": 15, "protein": 1.4, "carb": 2.9, "fat": 0.2, "category": "Sayur"},
    {"id": 21,"name": "Udang rebus (100g)", "cal": 99, "protein": 24, "carb": 0.2, "fat": 0.3, "category": "Protein Hewani"},
    {"id": 22,"name": "Daging kambing (100g)", "cal": 258, "protein": 25, "carb": 0, "fat": 17, "category": "Protein Hewani"},
    {"id": 23,"name": "Ikan salmon (100g)", "cal": 208, "protein": 20, "carb": 0, "fat": 13, "category": "Protein Hewani"},
    {"id": 24,"name": "Brokoli rebus (100g)", "cal": 35, "protein": 2.4, "carb": 7.2, "fat": 0.4, "category": "Sayur"},
    {"id": 25,"name": "Wortel rebus (100g)", "cal": 35, "protein": 0.8, "carb": 8.2, "fat": 0.2, "category": "Sayur"},
    {"id": 26,"name": "Oatmeal (100g)", "cal": 68, "protein": 2.4, "carb": 12, "fat": 1.4, "category": "Karbohidrat"},
    {"id": 27,"name": "Dada ayam rebus (100g)", "cal": 165, "protein": 31, "carb": 0, "fat": 3.6, "category": "Protein Hewani"},
    {"id": 28,"name": "Nugget ayam (100g)", "cal": 296, "protein": 15, "carb": 18, "fat": 18, "category": "Makanan Olahan"},
    {"id": 29,"name": "Sate ayam (5 tusuk, 100g)", "cal": 270, "protein": 25, "carb": 5, "fat": 16, "category": "Makanan Campuran"},
    {"id": 30,"name": "Sup sayur (1 mangkuk, 250g)", "cal": 90, "protein": 4, "carb": 14, "fat": 2, "category": "Sayur"}
]

MIN_CALORIES = 1500
MAX_CALORIES = 2500
TOLERANCE = 100 

def get_calorie_input():
    """
    Meminta input kalori dari user dan memvalidasi rentangnya.
    """
    while True:
        try:
            print(f"\nMasukkan batas kalori harian yang Anda inginkan (antara {MIN_CALORIES} dan {MAX_CALORIES} Kkal):")
            cal_input = input(">> ")
            target_calories = int(cal_input)

            if target_calories < MIN_CALORIES or target_calories > MAX_CALORIES:
                print(f"\n❌ Input kalori **{target_calories} Kkal** di luar rentang yang disarankan.")
                print(f"   Mohon masukkan nilai antara **{MIN_CALORIES}** hingga **{MAX_CALORIES} Kkal** untuk menjaga keseimbangan gizi.")
            else:
                return target_calories
        except ValueError:
            print("\n❌ Input tidak valid. Mohon masukkan angka bilangan bulat saja.")
        except EOFError:
            print("\nInput dibatalkan.")
            return None

def generate_meal_plan(target_calories):
    """
    Menghasilkan rencana makan acak yang mendekati target kalori.
    """
    recommended_foods = []
    current_calories = 0
    available_foods = list(FOODS)

    print("\n⏳ Mencari kombinasi makanan terbaik secara acak...")
    
    while current_calories < target_calories:
        if not available_foods:
            print("❗ Semua makanan telah direkomendasikan.")
            break

        food_choice = random.choice(available_foods)
        
        available_foods.remove(food_choice)

        if current_calories + food_choice['cal'] > target_calories + TOLERANCE:
            continue 

        recommended_foods.append(food_choice)
        current_calories += food_choice['cal']

        if target_calories - current_calories <= TOLERANCE and current_calories >= target_calories - TOLERANCE:
             break

    return recommended_foods, current_calories

def display_recommendation(foods, total_cal, target_cal):
    """
    Menampilkan hasil rekomendasi makanan.
    """
    print("\n" + "="*50)
    print("✨ Rekomendasi Rencana Makanan Harian Anda ✨")
    print(f"Target Kalori Harian: **{target_cal} Kkal**")
    print(f"Total Kalori Rencana: **{total_cal} Kkal**")
    print("-" * 50)
    
    if not foods:
        print("Tidak dapat membuat rencana makan yang memadai dengan kalori yang tersedia.")
        return

    total_protein = sum(f['protein'] for f in foods)
    total_carb = sum(f['carb'] for f in foods)
    total_fat = sum(f['fat'] for f in foods)
    tcal = sum(f['cal'] for f in foods)

    print("## 🍽️ Detail Makanan yang Direkomendasikan:")
    for food in foods:
        print(f"* **{food['name']}** ({food['cal']} Kkal) - Kategori: {food['category']}")

    print("\n## 📊 Total Makronutrien:")
    print(f"* Protein: **{total_protein:.1f} g**")
    print(f"* Karbohidrat: **{total_carb:.1f} g**")
    print(f"* Lemak: **{total_fat:.1f} g**")
    print(f"{tcal}")
    
    print("="*50)
    print(f"Catatan: Rencana ini mendekati target Anda ({target_cal} Kkal).")
    print("Ini adalah contoh rencana acak. Untuk rencana yang lebih spesifik, pertimbangkan pembagian waktu makan.")
    
def main():
    target_calories = get_calorie_input()

    if target_calories is None:
        return

    recommended_foods, total_calories = generate_meal_plan(target_calories)
    display_recommendation(recommended_foods, total_calories, target_calories)

if __name__ == "__main__":
    main()