const symptomForm = document.getElementById("symptomsForm");
const responseContainer = document.getElementById("baymax-response");


registerForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
});
const illnessesData = {
  "Malaria": {
    symptoms: ["headache", "fever", "chills", "sweating"],
    description: "A mosquito-borne infectious disease.",
    weights: {
      headache: 2,
      fever: 3,
      chills: 2,
      sweating: 1,
    },
  },
  "Common cold": {
    symptoms: ["cough", "sore throat", "runny nose", "congestion"],
    description: "A viral infection of the upper respiratory tract.",
    weights: {
      cough: 2,
      "sore throat": 1,
      "runny nose": 1,
      congestion: 1,
    },
  },
  "Stroke": {
    symptoms: ["sudden numbness", "confusion", "trouble speaking", "trouble walking"],
    description: "A sudden interruption of blood supply to part of the brain.",
    weights: {
      "sudden numbness": 3,
      confusion: 2,
      "trouble speaking": 2,
      "trouble walking": 3,
    },
  },
  "Eczema": {
    symptoms: ["itching", "rash", "dry skin"],
    description: "A chronic inflammatory skin condition.",
    weights: {
      itching: 3,
      rash: 2,
      "dry skin": 1,
    },
  },
  "Heart Disease": {
    symptoms: ["chest pain", "shortness of breath", "fatigue"],
    description: "A group of conditions affecting the heart and blood vessels.",
    weights: {
      "chest pain": 3,
      "shortness of breath": 2,
      fatigue: 1,
    },
  },
};

symptomForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const selectedSymptoms = Array.from(document.querySelectorAll('input[name="symptoms[]"]:checked'))
    .map(input => input.value);

  $.ajax({
    url: '/submit_symptoms',
    method: 'POST',
    dataType: 'json',
    data: { symptoms: selectedSymptoms },
    beforeSend: function() {
    },
    success: function(response) {
      responseContainer.textContent = "";

      if (response.error) {
        responseContainer.textContent = response.error;
      } else {
        updateResponse(response.illnesses);
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
      responseContainer.textContent = "Oops! Something went wrong. Try again later.";
    }
  });
});

function updateResponse(illnesses) {
  let responseText = "";
  if (illnesses.length === 0) {
    responseText = "Hi there! I couldn't find any illnesses matching all your selected symptoms. If you're concerned, it's always best to consult a doctor.";
  } else {
    responseText = "Hi there! Based on your symptoms, you might have one or more of the following illnesses: ";
    responseText += illnesses.map(illness => illness.name).join(", ");
    responseText += ". Remember, this information is for guidance only. Please see a doctor for proper diagnosis and treatment.";
  }
  responseContainer.textContent = responseText;
}

illnesses = (
    session.query(Illness)
    .join(Symptoms, Illnesses.symptoms)
    .filter(Symptoms.name.in_(symptoms))
    .all()
)

function analyzeSymptoms(selectedSymptoms) {
  const potentialIllnesses = [];

  for (const illnessName in illnessesData) {
    const illness = illnessesData[illnessName];
    let matchingSymptoms = 0;
    for (const symptom of selectedSymptoms) {
      if (illness.symptoms.includes(symptom)) {
        matchingSymptoms += illness.weights[symptom] || 1;
      }
    }
    if (matchingSymptoms

