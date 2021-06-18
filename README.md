# WIT-ACE# Garbase-Classifier
# Garbase-Classifier
Short description
What's the problem?
India is turning into one big garbage dump. The problem is assuming gigantic proportions and the numbers are staggering. But the problem is not about finding the right technology for waste disposal. The problem is how to integrate the technology with a system of household-level segregation so that waste does not end up in landfills, but is processed and reused.
 
The idea
It is clear that there will be no value from waste as energy or material if it is not segregated. But this is where our garbage classification system works. The goal of this task is to take pictures with single items, identify and group those pictures into 6 particular classifications of cardboard, glass, metal, paper, plastic and trash and if masks are detected, it suggests the user to either enter the details or visit the website where they can actually sell their used masks which will further be used to make bricks.
 
How can technology help?
We developed the model for garbage classification. The dataset for garbage classification was taken from Kaggle. There were 6 categories of garbage on the dataset. The amount of training samples were quite low compared to the amount required for general object classification algorithms. So, the transfer learning approach suited best for this task. The architecture and pretrained weights of the VGG16 model were imported. This model was then fine-tuned for a garbage classification task on a given dataset. The weights of trained models were saved so they can be used in production. Finally, the flask API was built to classify the given image into 6 categories of garbage.
Further, we used a machine learning model to identify masks in garbage. We used the VGG19 model which is a CNN (Convolution Neural Network) to classify images. The model shows a very low loss and high accuracy.
To connect all this and take this to household level, we are using a webapp through which a user can browse the image and classify the waste onto 6 levels.
 


