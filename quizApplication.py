import json
import random

class Quiz:
    def __init__(self, question_file="c_questions.json"):
        # Load questions from JSON file
        self.questions = self.load_questions(question_file)
        self.score = 0

    def load_questions(self, filename):
        """Load questions from a JSON file."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Questions file not found!")
            return []

    def ask_question(self, question_data):
        """Ask a single question and check the user's answer."""
        print("\n" + question_data["question"])
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        # Shuffle options randomly
        random.shuffle(options)
        
        # Print options
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        try:
            # Get the user's answer
            user_choice = int(input("\nChoose the correct option (1-4): "))
            user_answer = options[user_choice - 1]

            if user_answer == correct_answer:
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Incorrect. The correct answer was: {correct_answer}\n")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Please select a number between 1 and 4.")

    def run_quiz(self):
        """Runs the quiz by asking all questions in random order."""
        if not self.questions:
            print("No questions available!")
            return

        print("\n🔹 Welcome to the **C Language Quiz**! 🔹\n")
        random.shuffle(self.questions)  # Randomize question order

        for question_data in self.questions:
            self.ask_question(question_data)

        self.show_results()

    def show_results(self):
        """Displays the final score and performance summary."""
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100

        print(f"\n🎯 Your final score: {self.score}/{total_questions} ({percentage:.2f}%)")
        if percentage == 100:
            print("🏆 Excellent! You got all the answers correct!")
        elif percentage >= 70:
            print("🎉 Great job! You passed!")
        else:
            print("💡 Keep practicing! You can do better next time!")

        # Ask user if they want to retry
        retry = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if retry == "yes":
            self.score = 0
            self.run_quiz()

# Run the quiz
quiz = Quiz()
quiz.run_quiz()
