import streamlit as st

def hitung_luas(panjang, lebar):
    """Menghitung Luas = Panjang * Lebar"""
    luas = panjang * lebar
    return luas

# --- Tampilan Aplikasi Streamlit ---

st.title("📐 Penghitung Luas Persegi Panjang")
st.write("Masukkan nilai panjang dan lebar untuk menghitung luasnya.")

# Input Panjang
panjang = st.number_input(
    "Masukkan **Panjang**:",
    min_value=0.0,
    value=10.0,  # Nilai default
    step=0.1
)

# Input Lebar
lebar = st.number_input(
    "Masukkan **Lebar**:",
    min_value=0.0,
    value=5.0,  # Nilai default
    step=0.1
)

# Tombol untuk memicu perhitungan
if st.button("Hitung Luas"):
    if panjang <= 0 or lebar <= 0:
        st.error("Panjang dan Lebar harus lebih besar dari 0.")
    else:
        # Panggil fungsi
        hasil_luas = hitung_luas(panjang, lebar)

        # Output
        st.success(f"**Luas Persegi Panjang** adalah:")
        # Menampilkan hasil dengan format 2 angka di belakang koma
        st.write(f"## {hasil_luas:.2f}")

        # Tampilkan detail input (opsional)
        st.caption(f"Perhitungan: {panjang:.2f} (Panjang) x {lebar:.2f} (Lebar)")
