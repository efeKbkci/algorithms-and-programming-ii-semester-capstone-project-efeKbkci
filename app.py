import streamlit as st
from algorithm import lzw_compress, lzw_decompress

# Streamlit Interface
st.title("🧠 LZW Compression & Decompression Visualizer")

user_input = st.text_area("Enter the input text:", "TOBEORNOTTOBE")

if st.button("Compress"):
    compressed, compress_steps = lzw_compress(user_input)
    
    st.subheader("📦 Compressed Output:")
    st.code(compressed)

    st.subheader("📘 Compression Steps (Dictionary Updates):")
    for step in compress_steps:
        st.markdown(f"- {step}")

    decompressed, decompress_steps = lzw_decompress(compressed)
    
    st.subheader("🔄 Decompressed Text:")
    st.code(decompressed)
    
    st.subheader("🧩 Decompression Steps:")
    for step in decompress_steps:
        st.markdown(f"- {step}")

    if decompressed == user_input:
        st.success("✅ The decompressed text matches the original input!")
    else:
        st.error("❌ The decompressed text does NOT match the original input.")
