# Ransomware-detection-basedOn-ML

 detection of ransomware based on machine learning

## Abstract 

Ransomwares are a huge threat to our society, indeed computing has become an important part of our daily lives, lots of information is stored on it, such as family photos, important documents, personal projects and more sensitive informations in the case of enterprises and state establishments. Additionally, cryptocurrencies have become more popular, making ransom collection easier and almost risk-free. Ransomware has evolved in order to implement techniques to avoid detection, among these techniques, the pre-attack phase, which aims to analyze the execution environment before launching the attack, in our study we used the Ransomware behavior during this phase through the API calls. We collected 631 ransomware samples, and we performed the dynamic analysis on them thanks to cuckoo sandbox which is an automatic analysis tool, from the report generated by the analysis, we extracted the evasion API which represents the suspicious ransomware behavior that determines whether the attack is launched or not, then we used recursive feature elimination (RFE) to keep the most relevant APIs to then test with four machine learning models: decision tree , random forest, k nearest neighbors and support vector machine. The results showed that our approach is highly effective in detecting ransomwares with an accuracy of 98.41%.

Keywords: cybersecurity, ransomware detection, machine learning.

## Tech used
* Cuckoo sandbox
* Pyhton
* Packages python
  * Numpy
  * Pandas
  * Scikit-learn

## Support

for more information you can find me in: [m.fenni.fs@univ-boumerdes.dz](m.fenni.fs@univ-boumerdes.dz)
