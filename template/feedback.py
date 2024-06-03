import streamlit as st

def show_feedback(prediction):
    if prediction == 'Very Low':
        feedback = """
        **Tingkat Depresi Anda: Very Low**
        
        **Feedback:**
        Anda menunjukkan gejala depresi yang sangat rendah. Ini adalah kabar baik, tetapi penting untuk tetap memantau kesehatan mental Anda secara teratur. Pertimbangkan untuk melakukan aktivitas yang meningkatkan kebahagiaan dan kesejahteraan seperti berolahraga, bertemu teman, atau mengejar hobi. Jaga rutinitas tidur yang baik dan diet seimbang untuk mendukung kesehatan mental yang optimal.
        """
    elif prediction == 'Low':
        feedback = """
        **Tingkat Depresi Anda: Low**
        
        **Feedback:**
        Anda menunjukkan beberapa gejala depresi ringan. Meskipun gejala tidak mengkhawatirkan saat ini, penting untuk mengambil langkah-langkah pencegahan. Cobalah teknik relaksasi seperti meditasi atau yoga. Juga, jangan ragu untuk berbicara tentang perasaan Anda dengan orang yang Anda percaya. Jika Anda merasa gejala mulai memburuk, pertimbangkan untuk berkonsultasi dengan profesional kesehatan mental.
        """
    elif prediction == 'Moderate':
        feedback = """
        **Tingkat Depresi Anda: Moderate**
        
        **Feedback:**
        Anda menunjukkan tanda-tanda depresi moderat. Sangat penting untuk tidak mengabaikan gejala ini. Berbicara dengan dokter atau terapis bisa sangat membantu. Mereka dapat menawarkan strategi pengelolaan yang lebih formal seperti terapi atau, jika perlu, obat-obatan. Cobalah untuk mempertahankan kontak sosial dan rutinitas sehari-hari Anda, dan jangan isolasi diri.
        """
    elif prediction == 'High':
        feedback = """
        **Tingkat Depresi Anda: High**
        
        **Feedback:**
        Anda menunjukkan gejala depresi yang serius. Sangat penting untuk segera mencari bantuan profesional. Hubungi dokter, psikolog, atau layanan kesehatan mental lainnya untuk mendapatkan dukungan yang diperlukan. Pertimbangkan untuk berbicara dengan teman atau keluarga tentang apa yang Anda alami agar mereka dapat memberikan dukungan. Dalam keadaan darurat, jangan ragu untuk menghubungi layanan darurat atau garis bantuan krisis di daerah Anda.
        """
    else:
        feedback = "Error: Invalid prediction result."

    st.markdown(feedback)
