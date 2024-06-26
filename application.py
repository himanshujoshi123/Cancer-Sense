import pickle
import numpy as np
import streamlit as st

# Load the trained model
model = pickle.load(open('Random Forest', 'rb'))

# Load the fitted scaler
scaler = pickle.load(open('scaler','rb'))

# Define the input field names
input_field_names = ['Radius Mean', 'Texture Mean', 'Perimeter Mean', 'Area Mean',
                     'Smoothness Mean', 'Compactness Mean', 'Concavity Mean',
                     'Concave Points Mean', 'Symmetry Mean', 'Fractal Dimension Mean']

# Set page title and favicon
st.set_page_config(page_title="Cancer Prediction", page_icon=":hospital:")

# Page layout with padding and center alignment
st.markdown("<h1 style='text-align: center; color: #333;'>Cancer Prediction</h1>", unsafe_allow_html=True)
st.write("Please enter the following parameters to predict cancer.")

# Create input fields
input_fields = {}
for name in input_field_names:
    input_fields[name] = st.number_input(name, step=0.01)

# Prediction function
def predict():
    try:
        data = [input_fields[name] for name in input_field_names]
        if not any(np.isnan(data)):
            data = np.array(data).reshape(1, -1)
            data_scaled = scaler.transform(data)
            prediction = model.predict(data_scaled)
            result = "Benign" if prediction[0] == 1 else "Malignant"
            st.success(f"The cancer is predicted to be: {result}")
        else:
            st.error("Please fill in all the input fields with numeric values")
    except ValueError:
        st.error("Invalid input. Please fill in all the input fields with numeric values")

# Predict button
if st.button("Predict", key="predict_button"):
    predict()

# Sidebar navigation
st.sidebar.title("Navigation")

# Predefined descriptions
# Predefined descriptions
breast_cancer_description = """
Breast cancer is a type of cancer that starts in the breast tissue. It occurs when cells in the breast mutate and begin to multiply uncontrollably, forming a tumor. While breast cancer can occur in both men and women, it is far more common in women.

Breast cancer can manifest in different forms, including invasive and non-invasive types. Invasive breast cancer means the cancer cells have spread beyond the ducts or lobules into surrounding breast tissue, while non-invasive breast cancer remains within its place of origin.

Early detection and treatment are critical in improving outcomes for breast cancer patients. Regular screening tests, such as mammograms, can help detect breast cancer in its early stages when it is most treatable.

Treatment options for breast cancer may include surgery, radiation therapy, chemotherapy, hormone therapy, targeted therapy, or a combination of these approaches. The choice of treatment depends on various factors, including the type and stage of breast cancer, as well as the patient's overall health and preferences.

While breast cancer cannot always be prevented, certain lifestyle factors may reduce the risk of developing the disease. Maintaining a healthy weight, engaging in regular physical activity, limiting alcohol consumption, and avoiding tobacco products are important preventive measures. Additionally, breastfeeding may offer some protection against breast cancer.

Overall, awareness, early detection, and access to quality healthcare services play crucial roles in the fight against breast cancer.
"""

dos_description = """
There are several proactive steps individuals can take to reduce their risk of breast cancer:

1. Maintain a healthy weight: Being overweight or obese increases the risk of breast cancer, particularly after menopause. Strive to achieve and maintain a healthy weight through a balanced diet and regular exercise.

2. Engage in regular physical activity: Aim for at least 150 minutes of moderate-intensity exercise or 75 minutes of vigorous-intensity exercise each week. Physical activity can help lower the risk of breast cancer by reducing estrogen levels and improving overall health.

3. Limit alcohol intake: Alcohol consumption is associated with an increased risk of breast cancer. Limit alcohol consumption to no more than one drink per day, if you choose to drink at all.

4. Breastfeed if possible: Breastfeeding may offer some protection against breast cancer for both the mother and the child. If you're able to breastfeed, consider doing so for as long as possible.

5. Stay up to date with screenings: Regular breast cancer screenings, such as mammograms, clinical breast exams, and self-exams, can help detect breast cancer in its early stages when it's most treatable. Follow your healthcare provider's recommendations for screening based on your age and risk factors.

By adopting these healthy habits, you can reduce your risk of developing breast cancer and improve your overall health and well-being.
"""

donts_description = """
To reduce the risk of breast cancer, it's important to avoid certain lifestyle factors that may contribute to the development of the disease:

1. Smoking: Smoking is a known risk factor for several types of cancer, including breast cancer. Avoid smoking and exposure to secondhand smoke to lower your risk.

2. Excessive alcohol consumption: Alcohol consumption is associated with an increased risk of breast cancer. Limit alcohol intake to no more than one drink per day for women and two drinks per day for men.

3. Being overweight or obese: Maintaining a healthy weight is essential for reducing the risk of breast cancer. Excess body fat, particularly after menopause, can increase estrogen levels and promote the growth of cancer cells. Adopt a balanced diet and engage in regular physical activity to achieve and maintain a healthy weight.

4. Sedentary lifestyle: Lack of physical activity is a risk factor for various health conditions, including breast cancer. Aim to incorporate regular exercise into your daily routine, such as walking, swimming, or cycling.

5. Hormone replacement therapy (HRT): Long-term use of hormone replacement therapy to manage menopausal symptoms may increase the risk of breast cancer. Discuss the potential risks and benefits of HRT with your healthcare provider.

By avoiding these risk factors and adopting a healthy lifestyle, you can help reduce your risk of breast cancer and improve your overall health and well-being.
"""


# Navbar section
selected_nav = st.sidebar.radio("Go to", ["Description", "Do's", "Don'ts"])

# Display selected section in main slide
if selected_nav == "Description":
    st.markdown("# Breast Cancer Description")
    st.write(breast_cancer_description)
elif selected_nav == "Do's":
    st.markdown("# Breast Cancer Do's")
    st.write(dos_description)
elif selected_nav == "Don'ts":
    st.markdown("# Breast Cancer Don'ts")
    st.write(donts_description)
