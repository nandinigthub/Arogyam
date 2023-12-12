from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import pandas as pd
from distutils.version import LooseVersion
import sklearn





data = {
    'Common Cold': ['Runny or stuffy nose', 'Sneezing', 'Coughing', 'Sore throat', 'Mild body aches'],
    'Influenza (Flu)': ['Fever', 'Chills', 'Fatigue', 'Body aches', 'Cough', 'Headache'],
    'COVID-19': ['Fever or chills', 'Cough', 'Shortness of breath or difficulty breathing', 'Fatigue', 'Muscle or body aches', 'Loss of taste or smell'],
    'Allergies': ['Sneezing', 'Runny or stuffy nose', 'Itchy or watery eyes', 'Itchy throat or ears'],
    'Asthma': ['Shortness of breath', 'Wheezing', 'Chest tightness', 'Coughing, especially at night or early morning'],
    'Diabetes': ['Increased thirst', 'Frequent urination', 'Unexplained weight loss', 'Fatigue', 'Blurred vision'],
    'Hypertension (High Blood Pressure)': ['Headaches', 'Shortness of breath', 'Chest pain', 'Dizziness', 'Vision problems'],
    'Heart Attack': ['Chest pain or discomfort', 'Shortness of breath', 'Cold sweats', 'Nausea or vomiting', 'Pain or discomfort in the arms, neck, jaw, or back'],
    'Pneumonia': ['High fever', 'Cough with phlegm', 'Shortness of breath', 'Chest pain', 'Fatigue'],
    'Gastroenteritis': ['Diarrhea', 'Nausea and vomiting', 'Abdominal cramps', 'Fever'],
    'Urinary Tract Infection (UTI)': ['Frequent urination', 'Burning sensation during urination', 'Cloudy or strong-smelling urine', 'Pelvic pain'],
    'Migraine': ['Intense headache', 'Sensitivity to light and sound', 'Nausea', 'Visual disturbances (auras)'],
    'Depression': ['Persistent sad, anxious, or "empty" mood', 'Loss of interest or pleasure in activities', 'Fatigue', 'Changes in sleep patterns'],
    'Anxiety Disorders': ['Excessive worrying', 'Restlessness', 'Fatigue', 'Difficulty concentrating'],
    'Rheumatoid Arthritis': ['Joint pain and swelling', 'Stiffness, especially in the morning', 'Fatigue', 'Fever'],
    'Lyme Disease': ['Bull\'s-eye rash', 'Fatigue', 'Fever', 'Muscle and joint aches', 'Swollen lymph nodes'],
    'Hepatitis B': ['Jaundice (yellowing of the skin and eyes)', 'Fatigue', 'Abdominal pain', 'Dark urine', 'Joint pain'],
    'Chronic Obstructive Pulmonary Disease (COPD)': ['Shortness of breath', 'Chronic cough', 'Wheezing', 'Chest tightness', 'Increased mucus production'],
    'Alzheimer\'s Disease': ['Memory loss', 'Difficulty planning and solving problems', 'Confusion', 'Changes in personality', 'Difficulty completing familiar tasks'],
    'Parkinson\'s Disease': ['Tremors', 'Bradykinesia (slowness of movement)', 'Muscle rigidity', 'Postural instability', 'Changes in handwriting (micrographia)'],
    'Multiple Sclerosis (MS)': ['Fatigue', 'Numbness or weakness in limbs', 'Tremors', 'Problems with coordination and balance', 'Blurred or double vision'],
    'Celiac Disease': ['Abdominal pain', 'Diarrhea', 'Weight loss', 'Bloating', 'Fatigue'],
    'Epilepsy': ['Seizures', 'Temporary confusion', 'Staring spells', 'Uncontrollable jerking movements or loss of consciousness'],
    'Hypothyroidism': ['Fatigue', 'Weight gain', 'Cold sensitivity', 'Dry skin', 'Constipation'],
    'Hyperthyroidism': ['Weight loss', 'Rapid heartbeat', 'Nervousness', 'Sweating', 'Fatigue'],
    'Osteoarthritis': ['Joint pain', 'Stiffness', 'Swelling', 'Decreased range of motion', 'Joint instability'],
    'Systemic Lupus Erythematosus (SLE)': ['Joint pain', 'Skin rash', 'Fatigue', 'Fever', 'Chest pain'],
    'Endometriosis': ['Pelvic pain', 'Painful periods', 'Pain during or after intercourse', 'Infertility', 'Fatigue'],
    'Bipolar Disorder': ['Mood swings', 'Energy changes', 'Sleep disturbances', 'Impaired judgment', 'Changes in activity levels'],
    'Ovarian Cancer': ['Abdominal bloating', 'Pelvic pain', 'Difficulty eating or feeling full quickly', 'Frequent urination', 'Fatigue'],
    'Pancreatitis': ['Abdominal pain', 'Nausea and vomiting', 'Fever', 'Rapid pulse', 'Tender abdomen'],
    'Gout': ['Severe joint pain', 'Swelling and redness', 'Limited range of motion', 'Warmth in the affected joint', 'Tophi (uric acid deposits under the skin)'],
    'Crohn\'s Disease': ['Abdominal pain', 'Diarrhea', 'Fatigue', 'Weight loss', 'Reduced appetite'],
    'Ulcerative Colitis': ['Abdominal pain', 'Bloody diarrhea', 'Weight loss', 'Fatigue', 'Fever'],
    'Chronic Kidney Disease': ['Fatigue', 'Swelling in the legs and ankles', 'Shortness of breath', 'High blood pressure', 'Changes in urination'],
    'Sickle Cell Anemia': ['Fatigue', 'Painful swelling of hands and feet', 'Frequent infections', 'Jaundice', 'Delayed growth'],
    'Pulmonary Embolism': ['Shortness of breath', 'Chest pain that may become worse when breathing deeply', 'Rapid heart rate', 'Cough that may produce bloody or blood-streaked sputum', 'Sweating'],
    'Lupus Nephritis': ['Joint pain', 'Swelling', 'High blood pressure', 'Dark urine', 'Protein in the urine'],
    'Myasthenia Gravis': ['Muscle weakness, especially in the face', 'Fatigue', 'Difficulty chewing or swallowing', 'Double vision', 'Trouble speaking'],
    'Cushing\'s Syndrome': ['Weight gain, especially in the abdominal area', 'High blood pressure', 'Muscle and bone weakness', 'Mood swings', 'Irregular menstrual periods'],
    'Huntington\'s Disease': ['Involuntary movements (chorea)', 'Cognitive decline', 'Emotional disturbances', 'Difficulty swallowing', 'Impaired coordination'],
    'Amyotrophic Lateral Sclerosis (ALS)': ['Muscle weakness', 'Difficulty speaking and swallowing', 'Twitching', 'Cramps', 'Difficulty breathing'],
    'Addison\'s Disease': ['Fatigue', 'Weight loss', 'Darkening of the skin (hyperpigmentation)', 'Low blood pressure', 'Salt cravings'],
    'Brucellosis': ['Fever', 'Sweating', 'Fatigue', 'Joint and muscle pain', 'Headache'],
    'Pernicious Anemia': ['Fatigue', 'Weakness', 'Shortness of breath', 'Pale or sallow skin', 'Dizziness'],
    'Fibromyalgia': ['Widespread pain', 'Fatigue', 'Sleep disturbances', 'Joint stiffness', 'Cognitive difficulties (fibro fog)'],
    'Interstitial Cystitis': ['Pelvic pain', 'Urgency to urinate', 'Frequent urination', 'Pain during intercourse', 'Discomfort in the bladder and pelvic region'],
    'Cystic Fibrosis': ['Persistent cough with thick mucus', 'Shortness of breath', 'Frequent lung infections', 'Poor growth', 'Salty-tasting skin'],
    'Sjögren\'s Syndrome': ['Dry eyes', 'Dry mouth', 'Joint pain', 'Fatigue', 'Swollen salivary glands'],
    'Behçet\'s Disease': ['Mouth sores', 'Genital sores', 'Skin lesions', 'Joint pain', 'Eye inflammation'],
    'Reactive Arthritis': ['Joint pain and swelling', 'Inflammation of the eyes', 'Genital sores', 'Skin rash', 'Urinary symptoms'],
    'Turner Syndrome': ['Short stature', 'Delayed puberty', 'Webbed neck', 'Swelling of hands and feet', 'Learning disabilities'],
    'Vasculitis': ['Fatigue', 'Fever', 'Weight loss', 'Muscle and joint pain', 'Skin sores or rashes'],
    'Sarcoidosis': ['Fatigue', 'Shortness of breath', 'Cough', 'Chest pain', 'Skin rashes or lesions'],
    'Polycystic Ovary Syndrome (PCOS)': ['Irregular periods', 'Excess facial and body hair', 'Acne', 'Weight gain', 'Fertility issues'],
    'Post-Traumatic Stress Disorder (PTSD)': ['Flashbacks', 'Nightmares', 'Severe anxiety', 'Avoidance of reminders of trauma', 'Emotional numbness'],
    'Gestational Diabetes': ['Increased thirst', 'Fatigue', 'Frequent urination', 'Blurred vision', 'Nausea'],
    'Pre-eclampsia': ['High blood pressure', 'Swelling, especially in the hands and face', 'Headache', 'Blurred or double vision', 'Nausea or vomiting'],
    'Placenta Previa': ['Painless bleeding during the second or third trimester', 'Bright red blood', 'Low-lying placenta'],
    'Ankylosing Spondylitis': ['Back pain and stiffness', 'Fatigue', 'Pain and swelling in other joints', 'Reduced flexibility', 'Eye inflammation'],
    'Giant Cell Arteritis': ['Headache, usually in the temples', 'Scalp tenderness', 'Jaw pain with chewing', 'Vision problems', 'Fever'],
    'Hemochromatosis': ['Joint pain', 'Fatigue', 'Abdominal pain', 'Skin color changes (bronze or gray)', 'Loss of sex drive'],
    'Ménière\'s Disease': ['Vertigo', 'Hearing loss', 'Ringing in the ears (tinnitus)', 'Ear fullness or pressure'],
    'Tourette Syndrome': ['Involuntary, repetitive movements or vocalizations (tics)', 'Motor tics (blinking, shoulder shrugging)', 'Vocal tics (throat clearing, grunting)'],
    'Scoliosis': ['Uneven shoulders or hips', 'Back pain', 'Prominent shoulder blade', 'Difficulty breathing in severe cases'],
    'Vitamin B12 Deficiency': ['Fatigue', 'Weakness', 'Pale or jaundiced skin', 'Shortness of breath', 'Tingling or numbness in hands and feet'],
    'Wilson\'s Disease': ['Fatigue', 'Abdominal pain or swelling', 'Jaundice', 'Neurological symptoms (tremors, difficulty speaking)'],
    'Sepsis': ['Fever', 'Rapid heart rate', 'Rapid breathing', 'Confusion', 'Low blood pressure'],
    'Chronic Fatigue Syndrome (CFS)': ['Severe fatigue', 'Memory or concentration problems', 'Unrefreshing sleep', 'Muscle pain', 'Joint pain'],
    'Kawasaki Disease': ['High fever', 'Red eyes', 'Rash', 'Swollen lymph nodes', 'Strawberry tongue'],
    'Tinnitus': ['Ringing, buzzing, or hissing sounds in the ears', 'Hearing loss', 'Sensation of fullness in the ear'],
    'Lactose Intolerance': ['Bloating', 'Diarrhea', 'Stomach cramps', 'Gas', 'Nausea'],
    'Restless Legs Syndrome (RLS)': ['Uncomfortable sensations in the legs', 'Irresistible urge to move the legs', 'Disruption of sleep'],
    'Carpal Tunnel Syndrome': ['Numbness or tingling in the fingers', 'Hand weakness', 'Pain or discomfort in the wrist'],
    'Dermatitis Herpetiformis': ['Itchy, blistering skin rash', 'Gluten intolerance', 'Abdominal pain'],
    'Diverticulitis': ['Abdominal pain, usually on the left side', 'Fever', 'Nausea and vomiting', 'Changes in bowel habits'],
    'Fibrous Dysplasia': ['Bone pain', 'Bone deformities', 'Fractures', 'Skin discoloration'],
    'G6PD Deficiency': ['Fatigue', 'Shortness of breath', 'Jaundice', 'Dark urine', 'Abdominal pain'],
    'Hidradenitis Suppurativa': ['Painful lumps under the skin', 'Abscesses', 'Tunnel-like tracts', 'Scarring'],
    'Lichen Planus': ['Itchy, flat-topped bumps', 'Purple or reddish patches', 'Mouth sores', 'Nail damage'],
    'Ménière\'s Disease': ['Vertigo', 'Hearing loss', 'Ringing in the ears (tinnitus)', 'Ear fullness or pressure'],
    'Ovarian Cyst': ['Pelvic pain', 'Bloating', 'Changes in menstrual cycle', 'Pain during intercourse'],
    'Panic Disorder': ['Sudden and repeated attacks of intense fear', 'Sweating', 'Chest pain', 'Palpitations', 'Trembling'],
    'Pleurisy': ['Sharp chest pain', 'Painful breathing', 'Shortness of breath', 'Dry cough'],
    'Polio': ['Muscle weakness', 'Fatigue', 'Difficulty swallowing or breathing', 'Stiff neck or back'],
    'Premenstrual Syndrome (PMS)': ['Mood swings', 'Breast tenderness', 'Bloating', 'Headaches', 'Fatigue'],
    'Primary Biliary Cirrhosis (PBC)': ['Fatigue', 'Itchy skin', 'Abdominal pain', 'Dry eyes and mouth'],
    'Raynaud\'s Disease': ['Numbness or tingling in fingers and toes', 'Color changes in skin (pale or blue)', 'Cold fingers or toes'],
    'Scabies': ['Itching, especially at night', 'Red or pimple-like rash', 'Scales or blisters'],
}






# Your symptom data


# Extract symptoms and diseases
symptoms = [symptom for symptoms_list in data.values() for symptom in symptoms_list]

diseases = list(data.keys())

# Create a one-hot encoding for symptoms
mlb = MultiLabelBinarizer()
symptoms_one_hot = mlb.fit_transform(data.values())

# Create a DataFrame with one-hot encoded symptoms
df = pd.DataFrame(symptoms_one_hot, columns=mlb.classes_)
df['Disease'] = diseases

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Disease', axis=1), df['Disease'], test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Function to predict disease based on symptoms
def predict_disease(symptoms_input):
    input_array = np.zeros((1, len(mlb.classes_)))
    for symptom in symptoms_input:
        if symptom in mlb.classes_:
            input_array[0, mlb.classes_.tolist().index(symptom)] = 1
    prediction = clf.predict(input_array)
    predicted_disease = prediction[0]
    return predicted_disease

# Example usage
#input_symptoms = [ 'Gas','Bloating', 'Sweating', 'Dry cough', 'Body aches']
# = predict_disease(input_symptoms)
#print(f"Predicted Disease: {predicted_disease}")

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy
print(f"Accuracy: {accuracy}")