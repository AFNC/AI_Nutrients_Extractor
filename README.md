# AI Nutrients Extractor
This project utilizes Deep Learning and Computer Vision to detect the nutrition tables printed on packaged food products, followed by extraction of nutrient information from the detected tables while preserving the relational information of the text.

## Demo
The video is a quick demo for the project in which a user is prompted to upload a packaged product image. If the image contains a nutrition table, the system outputs the image showing the detected table within a red bounding box, along with the extracted nutrition information from the table in JSON format.

![30-dec-demo](https://github.com/user-attachments/assets/fe7ee545-969e-408f-bce5-83b1cd9807bd)

## Detection Output
The images below show the nutrition tables of various types, detected from product images worldwide. The detection of nutrition tables, including tables without boundary, and skipping of any irrelevant tables, indicates a deeper understanding of features by the trained model, leading to high precision detection
### Borderless Tables
!<img src ="https://github.com/user-attachments/assets/1780206c-d47d-43ab-8fc8-f0216e754389" width="200">
!<img src ="https://github.com/user-attachments/assets/b388cf01-8737-4364-9d78-f6295629745d" width="200" height="400">
!<img src ="https://github.com/user-attachments/assets/a4e46af2-d5df-4633-8ad4-7787b08c022d" width="200" height="400">
!<img src ="https://github.com/user-attachments/assets/796ca98b-c499-4bae-9855-4dca870d5b44" width="200" height="400">
### Bordered Tables
![20638382](https://github.com/user-attachments/assets/b477854b-32f3-4b85-a0f8-c1744c3f449d)
![20250206_074302](https://github.com/user-attachments/assets/b3eabf48-defb-499f-b39f-ef6dc9a82df0)
![20166656](https://github.com/user-attachments/assets/58ee9273-bd54-4a7e-bbd1-0148ace43c36)
![2](https://github.com/user-attachments/assets/8bd7b4a6-19c6-4ed5-8934-1a255f018f3e)






