from sqlalchemy import join


def analyze_symptoms(symptoms, db):
    session = db.session

    illnesses = (
        session.query(Illnesses)
        .join(Symptoms, symptoms_illnesses)
        .filter(Symptoms.name.in_(symptoms))
        .all()
    )

    illness_data = []
    for illnesses in illnesses:
        illnesses_data.append({
            "name": illnesses.name,
            "description": illnesses.description,
            "related_illnesses": illnesses.related_illnesses,
        })

    return jsonify(illnesses=illnesses_data)
