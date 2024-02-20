---
slides: ""
url_pdf: ""
summary: Computational algorithms need to be reconfigured (i.e., retrained) upon
  any changes in configuration of wearable technologies, such as
  addition/removal of a sensor to/from the network,
  displacement/misplacement/mis-orientation of the sensors, etc. Re-training of
  these algorithms requires collecting sufficient amount of labeled training
  data, a time consuming, labor-intensive, and expensive process that has been
  identified as a major barrier to personalized and precision medicine. In this
  project, we investigate development of multi-view learning algorithms that
  enable the vision of computationally autonomous and result in highly
  sustainable and scalable wearables of the future.
authors: [EPSL]
url_video: ""
date: 2020-01-13T23:58:08-08:00
external_link: ""
url_slides: ""
title: Computational Autonomy
tags: []
image:
  caption: ""
  focal_point: ""
  preview_only: false
categories: []
url_code: ""
---
We envision that wearables of the future must be computationally autonomous in the sense that their underlying computational algorithms reconfigure automatically without need for collecting any new labeled training data. In this project, we investigate development of multi-view learning algorithms that enable the vision of computationally autonomous wearables and result in highly sustainable and scalable wearables of the future. The algorithms and tools are validated through both in-lab experiments and using data collected in uncontrolled environments.   

{{< youtube uQ9vrUeYvzg >}}

# Related Research Papers:

## TransNet: Minimally-Supervised Deep Transfer Learning for Dynamic Adaptation of Wearable Systems

Wearables are poised to transform health and wellness through automation of cost-effective, objective, and real-time health monitoring. However, machine learning models for these systems are designed based on labeled data collected, and feature representations engineered, in controlled environments. This approach has limited scalability of wearables because (i) collecting and labeling sufficiently large amounts of sensor data is a labor-intensive and expensive process; and (ii) wearables are deployed in highly dynamic environments of the end-users whose context undergoes consistent changes. We introduce TransNet, a deep learning framework that minimizes the costly process of data labeling, feature engineering, and algorithm retraining by constructing a scalable computational approach. TransNet learns general and reusable features in lower layers of the framework and quickly reconfigures the underlying models from a small number of labeled instances in a new domain, such as when the system is adopted by a new user or when a previously unseen event is to be added to event vocabulary of the system. Utilizing TransNet on four activity datasets, TransNet achieves an average accuracy of 88.1% in cross-subject learning scenarios using only one labeled instance for each activity class. This performance improves to an accuracy of 92.7% with five labeled instances.

## Transfer Learning for Activity Recognition in Mobile Health

While activity recognition from inertial sensors holds potential for mobile health, differences in sensing platforms and user movement patterns cause performance degradation. Aiming to address these challenges, we propose a transfer learning framework, TransFall, for sensor-based activity recognition. TransFall's design contains a two-tier data transformation, a label estimation layer, and a model generation layer to recognize activities for the new scenario. We validate TransFall analytically and empirically.  

## LabelMerger: Learning Activities in Uncontrolled Environments

While inferring human activities from sensors embedded in mobile devices using machine learning algorithms has been studied, current research relies primarily on sensor data that are collected in controlled settings and/or with healthy individuals. Currently, there exists a gap in research about how to design activity recognition models based on sensor data collected with chronically ill individuals and in free-living environments. In this paper, we focus on a situation where free-living activity data are collected continuously, activity vocabulary (i.e., class labels) are not known a priori, and sensor data are annotated by end-users through an active learning process. By analyzing sensor data collected in a clinical study involving patients with cardiovascular disease, we demonstrate significant challenges that arise while inferring physical activities in uncontrolled environments. In particular, we observe that activity labels that are distinct in syntax can refer to semantically-identical behaviors, resulting in a sparse label space. To construct a meaningful label space, we propose LabelMerger, a framework for restructuring the label space created through active learning in uncontrolled environments in preparation for training activity recognition models. LabelMerger combines semantic meaning of activity labels with physical attributes of the activities (i.e., domain knowledge) to generate a flexible and meaningful representation of the labels. Specifically,  our approach merges labels using both word embedding techniques from the natural language processing and activity intensity from physical activity research. We show that the new representation of the sensor data obtained by LabelMerger results in more accurate activity recognition models compare to the case where original label space is used to learn recognition models.  

## LabelForest: Non-Parametric Semi-Supervised Learning for Activity Recognition

Activity recognition is central to many motion analysis applications ranging from health assessment to gaming. However, the need for obtaining sufficiently large amounts of labeled data has limited the development of personalized activity recognition models. Semi-supervised learning has traditionally been a promising approach in many application domains to alleviate reliance on large amounts of labeled data by learning the label information from a small set of seed labels. Nonetheless, existing approaches perform poorly in highly dynamic settings, such as wearable systems, because algorithms rely on predefined hyper-parameters or distribution models that need to be tuned for each user or context. To address these challenges, we introduce LabelForest, a novel non-parametric semi-supervised learning framework for activity recognition. LabelForest has two algorithms at its core: (1) a spanning forest algorithm for sample selection and label inference; and (2) a silhouette-based filtering method to finalize label augmentation for machine learning model training.  

## Personalization without User Interruption: Boosting Accuracy in New Subjects

Activity recognition systems are widely used in monitoring physical and physiological conditions as well as observing the short-term and/or long-term behavioral patterns for the purpose of improving the health and well-being of the users. The major obstacle in widespread use of these systems is the need for collecting labeled data to train the activity recognition model. While a personalized model outperforms a user-independent model, collecting labels from every single user is burdensome and in some cases impractical. In this research, we propose an uninformed cross-subject transfer learning algorithm that leverages the cross-user similarities by constructing a network-based feature-level representation of the data in source user (i.e., the one who has participated in labeling the physical activities) and target users (i.e., the future users who will not provide any ground-truth labels but wish to utilize the system at the same activity recognition accuracy of source user model). To this end, we perform a best-effort community detection to extract the core observations in target data. Our algorithm uses a heuristic classifier-based mapping to assign activity labels to the core observations. Finally, the output of labeling is conditionally fused with the prediction of the source-model to develop a boosted and personalized activity recognition algorithm. Our analysis on real-world data demonstrates the superiority of our approach. While the proposed system has been designed and verified for activity recognition task, it can be easily generalized to various machine learning based applications of pervasive computing and internet-of-things.

## Plug-n-Learn: Autonomous Training of New Sensors

In this research, we introduce the concept of plug-n-learn for human-centered IoT applications where machine learning algorithms are reconfigured automatically, in real-time, and without need for any new training data. Our pilot application in this research is activity recognition where the goal is to detect physical movements of the user based on wearable sensor measurements. We address this problem by proposing a novel method to transfer activity recognition capabilities of one sensor to another where the collective network of the two sensors achieves much higher accuracy performance. Our approach allows to transfer machine learning knowledge from an existing sensor, called source view, to a new sensor, called target view, and these capabilities are augmented through the sensing observations made by the target view. We call this approach a Multi-view learning and formulate this problem using Linear Programming, introduce a graph modeling of the problem, and propose a greedy heuristic to solve the problem. We evaluate the performance of the proposed automatic learning approach using real data collected with wearable motion sensors.

## Autonomous Learning of Sensor Location and Context

In this research, we take the first steps in developing automatic and real-time training of sensor-context detection without labeled training data. Specifically, we focus on cases where multiple context-specific algorithms (i.e., ‘expert models’) are shared for use in a dynamic view where the sensor is worn/used on various body locations each representing one sensor-context. We propose an approach for learning a gating function for choosing the most accurate expert model based on the observed sensor data. Our approach, called Synchronous Sensor-Context Learning (SSCL), first generates and automatically labels a training datasets by examining observations of the dynamic sensor and associating those observations with synchronously sampled observations of a static sensor node. This training dataset is then used to learn the gating function for expert model activation. Our multi-view learning approach presented in this research is a novel method for sharing activity recognition capabilities of several sensors, with already training activity recognition classifiers, for use by a dynamic sensor, which does not have any previously trained activity recognition model. Our approach allows to transfer machine learning knowledge from an existing sensor, called static view, to a new sensor, called dynamic view, and combine the knowledge with already shared capabilities and develop an extensive model for the dynamic view.

## Inter-Beat Interval Estimation with Tiramisu Model: A Novel Approach with Reduced Error

Inter-beat interval (IBI) measurement enables estimation of heart-tare variability (HRV) which, in turns, can provide early indication of potential cardiovascular diseases (CVDs). However, extracting IBIs from noisy signals is challenging since the morphology of the signal gets distorted in the presence of noise. Electrocardiogram (ECG) of a person in heavy motion is highly corrupted with noise, known as motion-artifact, and IBI extracted from it is inaccurate. As a part of remote health monitoring and wearable system development, denoising ECG signals and estimating IBIs correctly from them have become an emerging topic among signal-processing researchers. Apart from conventional methods, deep-learning techniques have been successfully used in signal denoising recently, and diagnosis process has become easier, leading to accuracy levels that were previously unachievable. We propose a deep-learning approach leveraging tiramisu autoencoder model to suppress motion-artifact noise and make the R-peaks of the ECG signal prominent even in the presence of high-intensity motion. After denoising, IBIs are estimated more accurately expediting diagnosis tasks. Results illustrate that our method enables IBI estimation from noisy ECG signals with SNR up to -30dB with average root mean square error (RMSE) of 13 milliseconds for estimated IBIs. At this noise level, our error percentage remains below 8% and outperforms other state of the art techniques.
