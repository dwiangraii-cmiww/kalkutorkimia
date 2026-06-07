import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator Kimia Digital",
    page_icon="🧪",
    layout="centered"
)

# 2. Data Unsur (Database Sederhana)
# Ini adalah data sebagian unsur untuk Tab Tabel Periodik
data_unsur = [
    {"No": 1, "Simbol": "H", "Nama": "Hidrogen", "Massa": 1.008, "Jenis": "Non-logam"},
    {"No": 2, "Simbol": "He", "Nama": "Helium", "Massa": 4.0026, "Jenis": "Gas Mulia"},
    {"No": 3, "Simbol": "Li", "Nama": "Litium", "Massa": 6.94, "Jenis": "Logam Alkali"},
    {"No": 4, "Simbol": "Be", "Nama": "Berilium", "Massa": 9.0122, "Jenis": "Logam Alkali Tanah"},
    {"No": 5, "Simbol": "B", "Nama": "Boron", "Massa": 10.81, "Jenis": "Metalloid"},
    {"No": 6, "Simbol": "C", "Nama": "Karbon", "Massa": 12.011, "Jenis": "Non-logam"},
    {"No": 7, "Simbol": "N", "Nama": "Nitrogen", "Massa": 14.007, "Jenis": "Non-logam"},
    {"No": 8, "Simbol": "O", "Nama": "Oksigen", "Massa": 15.999, "Jenis": "Non-logam"},
    {"No": 9, "Simbol": "F", "Nama": "Fluor", "Massa": 18.998, "Jenis": "Halogen"},
    {"No": 10, "Simbol": "Ne", "Nama": "Neon", "Massa": 20.180, "Jenis": "Gas Mulia"},
    {"No": 11, "Simbol": "Na", "Nama": "Natrium", "Massa": 22.990, "Jenis": "Logam Alkali"},
    {"No": 12, "Simbol": "Mg", "Nama": "Magnesuum", "Massa": 24.305, "Jenis": "Logam Alkali Tanah"},
    {"No": 13, "Simbol": "Al", "Nama": "Aluminium", "Massa": 26.982, "Jenis": "Logam Post-Transisi"},
    {"No": 14, "Simbol": "Si", "Nama": "Silikon", "Massa": 28.085, "Jenis": "Metalloid"},
    {"No": 15, "Simbol": "P", "Nama": "Fosfor", "Massa": 30.974, "Jenis": "Non-logam"},
    {"No": 16, "Simbol": "S", "Nama": "Belerang", "Massa": 32.06, "Jenis": "Non-logam"},
    {"No": 17, "Simbol": "Cl", "Nama": "Klorin", "Massa": 35.45, "Jenis": "Halogen"},
    {"No": 18, "Simbol": "Ar", "Nama": "Argon", "Massa": 39.948, "Jenis": "Gas Mulia"},
    {"No": 19, "Simbol": "K", "Nama": "Kalium", "Massa": 39.098, "Jenis": "Logam Alkali"},
    {"No": 20, "Simbol": "Ca", "Nama": "Kalsium", "Massa": 40.078, "Jenis": "Logam Alkali Tanah"},
]

df_unsur = pd.DataFrame(data_unsur)

# Database Zat untuk Membuat Larutan (Nama & Mr)
chemicals = {
    "NaCl (Natrium Klorida)": 58.44,
    "KCl (Kalium Klorida)": 74.55,
    "Glukosa (C6H12O6)": 180.16,
    "NaOH (Natrium Hidroksida)": 40.00,
    "HCl (Asam Klorida)": 36.46,
    "H2SO4 (Asam Sulfat)": 98.08,
    "CH3COOH (Asam Asetat)": 60.05,
    "C2H5OH (Etanol)": 46.07,
    "CuSO4 (Tembaga Sulfat)": 159.61,
    "KMnO4 (Kalium Permanganat)": 158.03
}

# 3. Aplikasi Utama
st.title("🧪 Kalkulator Kimia Digital")
st.markdown("---")

# Membuat Tab menggunakan st.tabs
tab1, tab2, tab3 = st.tabs(["💧 Pembuatan Larutan", "💧 Pengenceran", "📘 Tabel Periodik"])

# --- TAB 1: PEMBUATAN LARUTAN ---
with tab1:
    st.header("Pembuatan Larutan (m = M × V × Mr)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Input Zat
        selected_chem = st.selectbox("Pilih Zat Terlarut", options=list(chemicals.keys()))
        mr_val = chemicals[selected_chem]
        st.info(f"**Mr (Massa Molar): {mr_val} g/mol**")
        
    with col2:
        vol_ml = st.number_input("Volume (mL)", min_value=0.0, value=100.0, step=10.0)
        conc_m = st.number_input("Konsentrasi (M)", min_value=0.0, value=0.1, step=0.1, format="%.4f")

    if st.button("Hitung Massa", type="primary"):
        # Rumus: massa (g) = molarity (mol/L) * volume (L) * Mr (g/mol)
        # Konversi mL ke L: / 1000
        vol_l = vol_ml / 1000
        massa = conc_m * vol_l * mr_val
        
        st.success(f"Massa yang ditimbang: **{massa:.4f} gram**")
        st.balloons()

# --- TAB 2: PENGENCERAN ---
with tab2:
    st.header("Pengenceran (C₁V₁ = C₂V₂)")
    
    c1 = st.number_input("Konsentrasi Stok (M)", min_value=0.0, value=1.0, format="%.2f")
    c2 = st.number_input("Konsentrasi Target (M)", min_value=0.0, value=0.1, format="%.4f")
    v2 = st.number_input("Volume Target (mL)", min_value=0.0, value=100.0, step=10.0)
    
    if st.button("Hitung Volume Stok", type="primary"):
        if c1 == 0:
            st.error("Konsentrasi stok tidak boleh 0!")
        else:
            # Rumus: V1 = (C2 * V2) / C1
            v1 = (c2 * v2) / c1
            air_tambah = v2 - v1
            
            st.success(f"Ambil Volume Stok (V₁): **{v1:.2f} mL**")
            st.info(f" Tambahkan air : **{air_tambah:.2f} mL**")

# --- TAB 3: TABEL PERIODIK ---
with tab3:
    st.header("Tabel Periodik Sederhana")
    
    search = st.text_input("Cari Unsur", placeholder="Contoh: Karbon, C, atau 6")
    
    if search:
        # Filter data berdasarkan input
        filtered_df = df_unsur[
            df_unsur['Nama'].str.contains(search, case=False) | 
            df_unsur['Simbol'].str.contains(search, case=False) |
            df_unsur['No'].astype(str).str.contains(search, case=False)
        ]
    else:
        filtered_df = df_unsur
        
    st.dataframe(filtered_df, use_container_width=True)
    
    st.caption("Catatan: Data massa adalah massa atom relatif (Ar) standar.")
