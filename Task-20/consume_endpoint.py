# Task 20

# Create sample input data for the prediction

data = {
    "data": [
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}

# Encode the input data as JSON

test_sample = str.encode(json.dumps(data))

# Send the input data to the model for prediction

response = aci_service.run(input_data=test_sample)

# Print the prediction response

print(response)
