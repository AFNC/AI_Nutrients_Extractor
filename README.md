# AI Nutrients Extractor
This project utilizes Deep Learning and Computer Vision to detect the nutrition tables printed on packaged food products, followed by extraction of nutrient information from the detected tables while preserving the relational information of the text.

## Demo
The video is a quick demo for the project in which a user is prompted to upload a packaged product image. If the image contains a nutrition table, the system outputs the image showing the detected table within a red bounding box, along with the extracted nutrition information from the table in JSON format.

![30-dec-demo](https://github.com/user-attachments/assets/fe7ee545-969e-408f-bce5-83b1cd9807bd)

## Detection Output
The images below show the nutrition tables of various types, detected from product images worldwide. The detection of nutrition tables, including tables without boundary, and skipping of any irrelevant tables, indicates a deeper understanding of features by the trained model, leading to high precision detection
### Borderless Tables
![20250126_090329](https://github.com/user-attachments/assets/fec14269-7a28-42d3-bdd6-977fda523fce)
![20250126_091005](https://github.com/user-attachments/assets/3fc0330a-91e0-45e4-85ec-f05d1eb245d3)
![64232935 nutrition cropped](https://github.com/user-attachments/assets/ab82754a-0ab2-44ce-8d51-24647bcaa644)
![20250217_140254](https://github.com/user-attachments/assets/a70d9cde-c4f9-427d-b3d1-237afeec8ce4)
### Bordered Tables
![20250604_233112](https://github.com/user-attachments/assets/75f57bef-01ab-42dc-8423-3e55703c1595)
![20250228_125930](https://github.com/user-attachments/assets/cc6c2244-86d9-4abd-970c-f09e5fc800f2)
![20250206_074302](https://github.com/user-attachments/assets/b25ab8e2-4f31-47c5-b814-442adfc96fa2)
![20166656](https://github.com/user-attachments/assets/6d125a4b-311c-413a-86e6-771220873643)
![20071110](https://github.com/user-attachments/assets/6d411a42-b894-4ca6-9fe6-33d3a24e8674)
![20638382](https://github.com/user-attachments/assets/0e0b986d-570a-475a-9679-6a2a30031e50)





