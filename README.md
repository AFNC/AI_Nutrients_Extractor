# AI Nutrients Extractor
This project utilizes Deep Learning and Computer Vision to detect the nutrition tables printed on packaged food products, followed by extraction of nutrient information from the detected tables while preserving the relational information of the text.

## Demo
The video is a quick demo for the project in which a user is prompted to upload a packaged product image. If the image contains a nutrition table, the system outputs the image showing the detected table within a red bounding box, along with the extracted nutrition information from the table in JSON format.

![30-dec-demo](https://github.com/user-attachments/assets/fe7ee545-969e-408f-bce5-83b1cd9807bd)

## Detection Output
The images below show the nutrition tables of various types, detected from product images worldwide. The detection of nutrition tables, including tables without boundary, and skipping of any irrelevant tables, indicates a deeper understanding of features by the trained model, leading to high precision detection.
### Borderless Tables
!<img src ="https://github.com/user-attachments/assets/1780206c-d47d-43ab-8fc8-f0216e754389" width="180">
!<img src ="https://github.com/user-attachments/assets/a4e46af2-d5df-4633-8ad4-7787b08c022d" height="600">
!<img src ="https://github.com/user-attachments/assets/f99e4cde-2f71-41e8-a8e3-d969e15a4a0a" height="250">
!<img src ="https://github.com/user-attachments/assets/618ff5b8-92af-427a-9c7e-91e4e4f0c384" height="300">
### Bordered Tables
!<img src="https://github.com/user-attachments/assets/aea51c3d-4ff3-4cb6-9ce2-2df0f90944d5" width="250">
!<img src="https://github.com/user-attachments/assets/58ee9273-bd54-4a7e-bbd1-0148ace43c36" height="350">
!<img src="https://github.com/user-attachments/assets/4c054022-b750-4b27-9d7f-e3c86ebaf81d" height="250">
!<img src="https://github.com/user-attachments/assets/6683419c-685e-41a1-a390-ae970183aeec" height="400">








