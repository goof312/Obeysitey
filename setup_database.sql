-- Database setup for Obeysitey project
CREATE DATABASE IF NOT EXISTS obesityrecords;
USE obesityrecords;

-- Create records table
CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age FLOAT,
    gender VARCHAR(10),
    height FLOAT,
    weight FLOAT,
    calc VARCHAR(10),
    favc VARCHAR(10),
    fcvc INT,
    ncp INT,
    scc VARCHAR(10),
    smoke VARCHAR(10),
    ch2o INT,
    family_history_with_overweight VARCHAR(10),
    faf INT,
    tue INT,
    caec VARCHAR(20),
    mtrans VARCHAR(20),
    NObeyesdad VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create description table for recommendations
CREATE TABLE IF NOT EXISTS description (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Category VARCHAR(50),
    CategoryDes TEXT
);

-- Insert sample recommendations
INSERT INTO description (Category, CategoryDes) VALUES
('Insufficient_Weight', 'You are underweight. Consider increasing your caloric intake with nutritious foods and consult a healthcare provider.'),
('Normal_Weight', 'Congratulations! You have a healthy weight. Maintain your current lifestyle with balanced diet and regular exercise.'),
('Overweight_Level_I', 'You are slightly overweight. Consider reducing portion sizes and increasing physical activity.'),
('Overweight_Level_II', 'You are overweight. Focus on a balanced diet and regular exercise. Consider consulting a nutritionist.'),
('Obesity_Type_I', 'You have Class I obesity. It is recommended to create a structured diet and exercise plan with professional guidance.'),
('Obesity_Type_II', 'You have Class II obesity. Consider medical consultation for a comprehensive weight management program.'),
('Obesity_Type_III', 'You have Class III obesity. Immediate medical consultation is recommended for proper treatment and management.');
