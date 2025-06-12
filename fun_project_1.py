import streamlit as st

def mini_quiz_app():
    st.set_page_config(page_title="Mini Quiz: Indonesian Facts & Myths", page_icon="🎓", layout="centered")
    st.title("🇮🇩 Mini Quiz: Indonesian Facts & Myths")
    st.write("Test your knowledge about Indonesia's fascinating facts and myths! Select the correct answer for each question.")

    # Dictionary containing quiz questions, choices, correct answers, and feedback messages
    questions = {
        "Candi Borobudur dibangun dalam semalam oleh Bandung Bondowoso.": {
            "choices": ["Fakta", "Mitos"],
            "correct": "Mitos",
            "correct_msg": "Benar! Pembangunan Borobudur memakan waktu puluhan hingga ratusan tahun.",
            "incorrect_msg": "Salah! Candi Borobudur dibangun dalam waktu yang sangat lama."
        },
        "Rafflesia arnoldii adalah bunga terbesar di dunia yang ditemukan di Indonesia.": {
            "choices": ["Fakta", "Mitos"],
            "correct": "Fakta",
            "correct_msg": "Tepat! Rafflesia arnoldii memang bunga terbesar di dunia dan ditemukan di Indonesia.",
            "incorrect_msg": "Tidak benar! Rafflesia arnoldii adalah bunga terbesar di dunia dan asli Indonesia."
        },
        "Gunung Krakatau meletus pada tahun 1883 dan menyebabkan tsunami besar.": {
            "choices": ["Fakta", "Mitos"],
            "correct": "Fakta",
            "correct_msg": "Betul! Letusan Krakatau tahun 1883 sangat dahsyat dan menyebabkan tsunami besar.",
            "incorrect_msg": "Salah! Letusan Krakatau tahun 1883 memang menyebabkan tsunami besar."
        },
        "Orang Indonesia biasanya makan nasi dengan tangan kanan.": {
            "choices": ["Fakta", "Mitos"],
            "correct": "Fakta",
            "correct_msg": "Benar! Makan dengan tangan kanan adalah kebiasaan umum di Indonesia.",
            "incorrect_msg": "Salah! Makan dengan tangan kanan adalah kebiasaan umum di Indonesia."
        },
        "Wayang kulit adalah seni pertunjukan boneka bayangan yang berasal dari Jawa.": {
            "choices": ["Fakta", "Mitos"],
            "correct": "Fakta",
            "correct_msg": "Tepat sekali! Wayang kulit adalah seni tradisional Jawa yang terkenal.",
            "incorrect_msg": "Tidak benar! Wayang kulit memang berasal dari Jawa."
        }
    }

    # Initialize session state for answers and score if not already set
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "show_result" not in st.session_state:
        st.session_state.show_result = False

    # Display questions with radio buttons for answer selection
    for idx, (question, data) in enumerate(questions.items(), 1):
        st.subheader(f"Pertanyaan {idx}")
        st.write(question)
        # Use a unique key for each question to store the answer in session state
        selected = st.radio("Pilih jawaban:", data["choices"], key=f"q{idx}")
        st.session_state.answers[question] = selected

    # Button to submit answers and calculate score
    if st.button("Lihat Hasil"):
        score = 0
        st.session_state.show_result = True
        # Calculate score by comparing user answers with correct answers
        for question, data in questions.items():
            if st.session_state.answers.get(question) == data["correct"]:
                score += 1
        st.session_state.score = score

    # Display results if the user has submitted answers
    if st.session_state.show_result:
        st.markdown("---")
        st.header("🎯 Hasil Quiz Anda")
        total_questions = len(questions)
        score = st.session_state.score
        st.write(f"Skor Anda: **{score} / {total_questions}**")

        # Show detailed feedback for each question
        for question, data in questions.items():
            user_answer = st.session_state.answers.get(question)
            if user_answer == data["correct"]:
                st.success(f"✅ {question} - {data['correct_msg']}")
            else:
                st.error(f"❌ {question} - {data['incorrect_msg']}")

        # Profession suggestion based on score
        profession = ""
        if score == total_questions:
            profession = "Ahli Budaya Indonesia"
        elif score >= total_questions * 0.7:
            profession = "Peneliti Sejarah"
        elif score >= total_questions * 0.4:
            profession = "Penggemar Budaya"
        else:
            profession = "Pemula yang Ingin Belajar"

        st.subheader("🎓 Saran Profesi Berdasarkan Skor Anda:")
        st.info(f"Anda cocok menjadi: **{profession}**")

        # Display a gift image based on score
        if score == total_questions:
            gift_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXM2b2I0MzM1NWx3djJ6eWp1Z2Q0OWtmbWd4cjEzbGc0eXR5dTVrayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pxy9QQUMF0glq/giphy.gif"  # Trophy icon
        elif score >= total_questions * 0.7:
            gift_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXRtMDAyNHl0NmQzbGpzbTF5dHZhOWp4aGFvZGU1eDNvOTVsd3FheCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/GT0wfs7AGwVR45Bnhh/giphy.gif"  # Trophy icon
        elif score >= total_questions * 0.4:
            gift_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDh5dWw3bmN3dHJmYWJyN2d3bnJkMXBkZmx4MnN0d3BjN3ZhbHlxYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BnGO9hAeKFeOYfWmhT/giphy.gif"  # Trophy icon
        else:
            gift_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGtqOGJwbzEwY2oyMXNscmd0cmNvcTFiaGNqeDl4YnE5ZGFscHdtbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2rIDTzizHRQv6/giphy.gif"  # Trophy icon

        st.image(gift_url, width=100, caption="Hadiah untuk Anda!")

    st.markdown("---")
    st.write("Selamat mencoba dan semoga Anda mendapatkan hasil terbaik! 🎉")

# Run the app
if __name__ == "__main__":
    mini_quiz_app()
