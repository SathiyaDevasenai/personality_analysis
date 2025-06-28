from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

QUESTIONS = [
    {"q": "Do you prefer spending time alone rather than in large groups?", "trait": "Introversion"},
    {"q": "Do you enjoy helping others without expecting anything in return?", "trait": "Kindness"},
    {"q": "Do you often make decisions based on emotions?", "trait": "Impulsiveness"},
    {"q": "Are you comfortable expressing your opinions even if they differ?", "trait": "Assertiveness"},
    {"q": "Do you feel drained after social interactions?", "trait": "Introversion"},
    {"q": "Do you go out of your way to avoid hurting others?", "trait": "Kindness"},
    {"q": "Do you react quickly without thinking things through?", "trait": "Impulsiveness"},
    {"q": "Do you stand up for yourself when needed?", "trait": "Assertiveness"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        scores = {"Introversion": 0, "Kindness": 0, "Impulsiveness": 0, "Assertiveness": 0}
        for i, q in enumerate(QUESTIONS):
            ans = request.form.get(f'q{i}')
            if ans == "Yes":
                scores[q["trait"]] += 2
            elif ans == "Sometimes":
                scores[q["trait"]] += 1
            # No = 0

        # Create chart
        traits = list(scores.keys())
        values = list(scores.values())
        plt.figure(figsize=(8, 6))
        plt.bar(traits, values, color=["blue", "green", "orange", "purple"])
        plt.title("Personality Trait Analysis")
        plt.ylabel("Score")
        chart_path = os.path.join("static", "chart.png")
        plt.savefig(chart_path)
        plt.close()

        return render_template("result.html", name=name, scores=scores, chart="chart.png")

    return render_template("index.html", questions=enumerate(QUESTIONS))

if __name__ == "__main__":
    app.run(debug=True)
