import json

options_list = []


def get_selected_category(quiz_categories):
    total_cats = len(quiz_categories)
    while True:
        # showing all cats
        cat_json = {}
        for counter, cat in enumerate(quiz_categories):
            cat_json[int(counter + 1)] = cat
            print(counter + 1, ": ", cat, sep="")

        try:
            category = int(input("Select a category: \n"))
            cat = cat_json.get(category)
        except ValueError:
            print("Select valid category.")
        else:
            if 0 >= category or category > total_cats:
                print("Invalid value, please try again")
            else:
                return cat


def show_options(options):
    option_json = {}
    total_options = len(options)
    option_caption = ord("a")
    for counter, option in enumerate(options):
        caption = option_caption + counter
        option_json[chr(caption)] = option
        print(chr(caption), ": ", option, sep="")
        options_list.insert(0, option_json)


def take_answer():
    options = options_list[0]
    option_values = options.values()
    while True:
        option = str(input("Select an Option: \n"))
        if option not in options:
            print("Invalid option, please try again")
        else:
            return option


def update_score(score, opt, correct_answer):
    if opt == correct_answer:
        score += 1
    # else:
    #     score = score - 1 if score != 0 else 0
    return score


with open("quiz.json") as json_file:
    data = json.load(json_file)

quiz_cats = data["quiz"]
total_count = len(quiz_cats)

category = get_selected_category(quiz_cats)
quiz = data["quiz"]
total_questions = 0

score = 0

for total_questions, question_number in enumerate(quiz[category]):
    correct_answer = quiz[category][question_number]["answer"]
    print(
        "\n" + question_number,
        ": ",
        quiz[category][question_number]["question"],
        "\n\nOptions: ",
    )
    show_options(quiz[category][question_number]["options"])
    print("\n")
    user_answer = take_answer()
    opt = options_list[0].get(user_answer)
    score = update_score(score, opt, correct_answer)
    total_questions = total_questions + 1
    print(
        "\n__________________________________________________________________________\n"
    )
    # print("user chosen option:", user_answer, "option value: ", opt, "score: ", score)
    # print("correct answer: ", correct_answer)
print("Final score: ", score, "/", total_questions)
