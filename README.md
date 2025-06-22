---

# IBD Symptom Detection - Streamlit Web Application

## Overview
This is the Streamlit web application for the IBD Symptom Detection project. The app allows users to upload medical reports in text format, which are then analyzed by a trained machine learning model to detect the presence of Inflammatory Bowel Disease (IBD) symptoms. Based on the classification results, users are provided with recommendations for further actions.

## Features
- **Upload Medical Reports:** Users can upload text files containing medical reports.
- **IBD Symptom Classification:** The uploaded reports are classified as either positive or negative for IBD symptoms using a pre-trained Linear Support Vector Classifier (LinearSVC).
- **User Feedback:** Based on the classification result, users are advised to either seek further medical consultation or access relevant resources for managing IBD.

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- Required Python libraries (listed in `requirements.txt`)

### Clone the Repository
```bash
git clone https://github.com/your-username/IBD-Detection.git
cd IBD-Detection
```

### Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### Run the Streamlit Application
To start the Streamlit app, run the following command:
```bash
streamlit run app.py
```

This command will start a local web server, and you'll be able to access the app by opening a browser and navigating to `http://localhost:8501`.

## Usage

1. **Upload Medical Report:** On the home page, you'll find an option to upload a text file containing the medical report.
2. **Classify Report:** After uploading, the system will automatically classify the report as positive or negative for IBD symptoms.
3. **Receive Recommendations:** Depending on the classification result, you will receive recommendations for further action, such as seeking medical advice or accessing resources for managing IBD.

## Project Structure
```
IBD-Detection/
│
├── app.py                   # Streamlit application script
├── models/                  # Trained models used in the application
├── data/                    # Sample medical reports (if any)
├── requirements.txt         # Python dependencies
└── README_streamlit.md      # Documentation for the Streamlit application
```

## Deployment (Optional)
If you wish to deploy the Streamlit app on a cloud platform like Heroku, AWS, or Streamlit Sharing, follow the respective deployment guides for those platforms. You may need to set up configuration files such as `Procfile` for Heroku or handle environment variables accordingly.

## Contributing
Contributions are welcome! If you'd like to suggest improvements or add features to the Streamlit app, feel free to fork the repository and create a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact
For any questions or inquiries, please contact:
- Darshan Virani
- **Email:** darshanvirani2468@gmail.com

---
