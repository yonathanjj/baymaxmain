import unittest


def mock_illnesses():
    illnesses = (
        session.query(Illnesses)
        .join(Symptoms, symptoms_illnesses)
        .filter(Symptoms.name.in_(symptoms))
        .all()
    )

    illness_data = []
    for illness in illnesses:
        illness_data.append({
            "name": illness.name,
        })
    return [
        {"name": "headache", "description": "throbbing head pain"},
        {"name": "fever", "description": "elevated body temeprature"},
        {"name": "chills ", "description": "cold, shivering sensation"},
        {"name": "sweating", "description": "body cooling mechanism"},
        {"name": "cough", "description": "A reflex action to clear your airways of mucus and irritants such as dust "
                                         "or smoke"},
        {"name": "sore throat", "description": "Pain or irritation in the throat often worsened when you swallow"},
        {"name": "runny nose", "description": "Mucus dripping or “running” out of your nose due to cold, dry air, "
                                              "allergies, or the common cold"},
        {"name": "congestion ", "description": "A state of being overcrowded or blocked, often with traffic or people"},
        {"name": "sudden numbness", "description": "A partial or total lack of sensation in a body part"},
        {"name": "confusion", "description": "A situation in which people are uncertain about what to do or are "
                                             "unable to understand something clearly"},
        {"name": "trouble speaking", "description": "Trouble speakDifficulty in producing speech sounds or problems "
                                                    "with voice quality"},
        {"name": "trouble walking", "description": "Difficulty in walking due to injuries, underlying conditions, "
                                                   "or issues with the legs or feet"},
        {"name": "itching", "description": "Uncomfortable skin sensation causing a desire to scratch"},
        {"name": "rash", "description": "Irritation of the skin that results in scratching"},
        {"name": "dryskin", "description": "lack of moisture in skin"},
        {"name": "chest pain", "description": "discomfort between neck and upper abdomen"},
        {"name": "shortness of breath", "description": "difficulty getting enough air"},
        {"name": "fatigue", "description": "lack of energy and motivation"}
    ]


class TestAnalyzeSymptoms(unittest.TestCase):

    def test_empty_symptoms(self):
        symptoms = []
        expected_data = {"illnesses": []}
        result = analyze_symptoms(symptoms)
        self.assertEqual(result, expected_data)

    def test_single_symptom_match(self):
        symptoms = ["headache"]
        expected_data = {"illnesses": [{"name": "Headache", "description": "..."}]}
        result = analyze_symptoms(symptoms)
        self.assertEqual(result, expected_data)

    def test_multiple_symptom_match(self):
        symptoms = ["cough", "runny nose"]
        expected_data = {"illnesses": [{"name": "Common Cold", "description": "..."}]}
        result = analyze_symptoms(symptoms)
        self.assertEqual(result, expected_data)

    def test_no_symptom_match(self):
        symptoms = ["fever"]
        expected_data = {"illnesses": []}
        result = analyze_symptoms(symptoms)
        self.assertEqual(result, expected_data)


if __name__ == "__main__":
    unittest.main()
