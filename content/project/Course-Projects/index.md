---
summary: Projects formulated, developed, and demonstrated by students in various courses taught by Dr. Hassan Ghasemzadeh.  
authors: [EPSL]
date: 2022-01-13T23:58:23-08:00
title: Course Projects
tags: []
image:
  caption: ""
  focal_point: Bottom
  preview_only: true
categories: []
url_code: ""
---
<!-- 
The format of each project listing follows 

SN. **Project Name** by *Student names*

    Summary or Abstract. [GitHub](Link) if available
    
    {{< youtube YJ0TwOIkwBo >}} - link of the youtube video demo

    To include image, add the image to this folder and use 
    ![](imageName.format)
-->

This is a list of some of the projects formulated, developed, and demonstrated by students in various courses taught by Dr. Hassan Ghasemzadeh.

### Abnormal Gait and Fall Detection using Embedded Machine Learning

- Author: Chia-Cheng Kuo
- Course: Embedded Machine Learning
- Semester: Spring 2022

    <br/>
    {{< youtube YJ0TwOIkwBo >}}
    <br/>

It is crucial to provide emergency treatment for elderly or patients when they fall over. It is also important to provide warnings if the user has a high risk of falls due to abnormal gait. This project develops a real-time gait monitoring and fall detection system that integrates wearable inertial sensors and embedded machine learning while generating real-time feedback when falls are detected.

### Real-Time Activity Recognition using Embedded Machine Learning

- Authors: Emily Glagolev, Mihir Kotas, and Ahmed Musani
- Course: Embedded Machine Learning
- Semester: Spring 2022

    <br/>
    {{< youtube 97o2-8fS7Ms >}}
    <br/>

Accurate estimation of activity types is central to human behavior modeling, activity-based interventions, and context-aware system design. We created an activity detection device using embedded machine learning using and Arduino Nano 33 BLE sense. This device can detect if a person is walking, jogging, using stairs or standing still, along with the duration of time they are doing the activity. Data was collected for each activity using the Arduino BLE connection and cleaned. A model was trained using Tensorflow. This trained model was used for real time testing with the Arduino BLE connected to a central. The central used bleak to detect the activity and record the duration of the activity.

### Breathing Pattern Identification  

- Abdullah Mamun and Asiful Arefeen
- Course: Embedded Machine Learning
- Semester: Spring 2022

    <br/>
    {{< youtube ZNgdNnFtY2Q >}}
    <br/>

Abnormal breathing patterns can help us identify potential critical health issues such as a heart attack, stroke, fall, etc. While an abnormal breathing pattern recognizer can be implemented and deployed on a server-based system, it makes the solution dependent on network connectivity which may not be ideal for this critical task in all scenarios. In this project, we overcome this problem by proposing an abnormal breathing identifier for Arduino Nano 33 BLE Sense. Our system can detect abnormal breathing in real-time without the help of an external device or server. We use the microphone of the Arduino to capture the audio of the surroundings and when abnormal breathing is identified, the Arduino notifies the serial monitor. Our CNN-based machine learning model is also capable of identifying coughs and sneezes along with normal and abnormal breathing with about 77.4% accuracy after it has been optimized for Arduino.

### Low-Power Microgrid Disturbance Classification with Phasor Measurement Unit

- Author: Zachary Lythgoe
- Course: Embedded Machine Learning
- Semester: Spring 2022

    <br/>
    {{< youtube QFYur2osd0w >}}
    <br/>
    
In comparison to the primary grid, microgrids are significantly more sensitive to local changes due to reduced local reserve generation and the switching of loads that make up a comparatively larger percentage of the total load. Given this sensitivity, it is critical for grid controllers to monitor local disruptions (i.e., sudden increase or decrease in load or generation) that the grid is experiencing. This work proposes a low-power phasor measurement unit (PMU) paired with an Arduino Nano BLE 33 Sense to classify a variety of disturbances on a simulated microgrid. The low-power low-cost solution makes such a system easier to implement in existing and future microgrids.


### On-Device PPG-Based Heart Rate Estimation 

- Author: Jacob Sindorf
- Course: Embedded Machine Learning
- Semester: Spring 2022

    <br/>
    {{< youtube ZTRduZ-zdwo >}}
    <br/>
    
Photoplethysmography (PPG) based heart rate (HR) estimation has become a staple in health monitoring and wearable health sensing. However, due to the noninvasive optical signal, the data is highly susceptible to noise sources such as motion artifacts (MA). Larger and more diverse PPG activity datasets have been created and deep learning-based estimation has shown the ability to interpret accurate HR in realistic MA-affected scenarios. This work expands upon previous work and designs toward a wearable embedded HR device capable of continuous HR estimation. Through a deep neural network (DNN), HR can be estimated within 10 beats per minute (BPM) at an accuracy of 81%. This model can then be deployed to an embedded system to make HR predictions in real-time.
