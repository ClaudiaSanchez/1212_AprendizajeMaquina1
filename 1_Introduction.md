# Introduction

Machine Learning definitions:

- [Arthur Samuel](https://es.wikipedia.org/wiki/Arthur_L._Samuel) (1959). Machine Learning: Field of study that **gives computers the ability to learn without being explicitly programmed**.
- From the book “An Introduction to Statistical Learning”: Statistical learning refers to a **vast set of tools for understanding data**.
- From the book “Machine Learning in action”:
  - Machine learning is **turning data into information**.
  - Machine learning lies at the **intersection of computer science, engineering, and statistics** and often appears in other disciplines.
  - It’s a tool that **can be applied to many problems**. Any field that needs to interpret and act on data can benefit from machine learning techniques.
  - Machine learning uses statistics.
- From the book “Introduction to Machine Learning” by Ethem Alpaydin:
  - Machine learning is not just a database problem; it is also a **part of artificial intelligence**.
  - Machine learning also helps us find solutions to many problems in vision, speech recognition, and robotics.
  - Machine learning is programming computers to **optimize a performance criterion using example data or experience**.


[![Watch the video](images/1_video.png)](https://youtu.be/1iqh1B1OZAg) 

## Machine Learning Applications

- [Face recognition](https://www.google.com/search?q=face+recognition&safe=strict&rlz=1C1SQJL_enMX896MX896&sxsrf=ALeKk02HE65u5YMjiZ411PRbRNGwaTeXKA:1608154734698&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi--9Gdu9PtAhUC7awKHaJKC4IQ_AUoAXoECAIQAw&biw=837&bih=492&dpr=1.25)
- [Emotion recognition](https://www.google.com/search?q=emotion+recognition&tbm=isch&ved=2ahUKEwjQ-Ljnu9PtAhVOR6wKHafLBq0Q2-cCegQIABAA&oq=emotion+recognition&gs_lcp=CgNpbWcQAzIECAAQQzICCAAyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BAgjECc6BQgAELEDOggIABCxAxCDAToHCAAQsQMQQ1CouQpYkMoKYLjLCmgAcAB4AIABpgOIAcIWkgEKMS4xNi4wLjEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=CX_aX5DQHM6OsQWnl5voCg&bih=492&biw=837&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Identifying spam emails](https://www.google.com/search?q=Identifying+spam+emails&tbm=isch&safe=strict&rlz=1C1SQJL_enMX896MX896&hl=es&sa=X&ved=2ahUKEwj26PDhvNPtAhWIWKwKHQtpAq4QBXoECAEQLQ&biw=823&bih=478)
- [Weather forecast](https://www.google.com/search?q=Weather+forecast&tbm=isch&ved=2ahUKEwi4hIv7vNPtAhUBOa0KHXrmAwMQ2-cCegQIABAA&oq=Wheather+forecast&gs_lcp=CgNpbWcQA1AAWABgr7sBaABwAHgAgAEAiAEAkgEAmAEAqgELZ3dzLXdpei1pbWc&sclient=img&ei=P4DaX_joBYHytAX6zI8Y&bih=478&biw=823&rlz=1C1SQJL_enMX896MX896&safe=strict&hl=es)
- [Object recognition](https://www.google.com/search?q=Object+recognition&tbm=isch&ved=2ahUKEwjYqeWHvdPtAhWXYqwKHb4JBJQQ2-cCegQIABAA&oq=Object+recognition&gs_lcp=CgNpbWcQAzICCAAyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BAgjECc6BQgAELEDOgQIABBDOggIABCxAxCDAVDhkAFYoaMBYMekAWgAcAB4AIAB4gGIAesXkgEGMC4xMS42mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=WYDaX5iZLZfFsQW-k5CgCQ&bih=478&biw=823&rlz=1C1SQJL_enMX896MX896&safe=strict&hl=es)
- Recommendation systems, for example [Netflix](https://www.topbots.com/netflix-movie-recommender-system-rework/)
- [Medical data analysis](https://www.datapine.com/blog/big-data-examples-in-healthcare/)

In addition, computer programs have been able to beat the best humans in:
- [Chess](https://www.bbc.com/news/av/world-us-canada-39888639)
- [Go](https://fortune.com/2016/03/12/googles-go-computer-vs-human/#:~:text=In%20a%20decisive%20step%20forward,of%20Go's%20most%20dominant%20players.)

## Why is Machine Learning now capturing much attention?

Because there are:
- A massive amount of data. [See the image](https://www.visualcapitalist.com/every-minute-internet-2020/)
- Computer resources (hardware) are cheaper, faster, and more powerful
- Better understanding of algorithms
- We have platforms to share code (for example, GitHub)

## Some concepts

![](/images/1_concepts.png)

- **Artificial Intelligence** is a subfield of computer science. It is the ability of a digital computer to perform tasks commonly associated with intelligent beings.
- **Machine learning** is a branch of Artificial Intelligence. The goal is turning data into information.
- **Deep learning** is one kind of machine learning (neural networks) that’s very popular now. It has been given very impressive results. It needs a lot of data and computational resources to work.
- **Data science** deals with unstructured and structured data. It is a field that comprises everything related to data cleaning, preparation, and analysis. It combines statistics, mathematics, programming, problem-solving, and capturing data in ingenious ways.
- **Big data** is used to describe immense volumes of data, both unstructured and structured.

## Recent amazing applications with the use of Deep Learning

- ImageNet is a challenge that consists of recognizing a target of 1,000 different categories. The dataset is composed of more than 1.2 million images. It had been a difficult problem for computers until 2015, where AI algorithms' results improve human results. The following image shows the error of the challenge over the years.

![](/images/1_imagenet_error.png)

- [Multiple object recognition](https://www.google.com/search?q=multiple+object+recognition&tbm=isch&ved=2ahUKEwiX98TVn9jtAhWa6KwKHZHJCAcQ2-cCegQIABAA&oq=multiple+object+recognition&gs_lcp=CgNpbWcQAzIECCMQJ1CPCVjBDWDrD2gAcAB4AIABxgGIAfoCkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=ngDdX5ewGZrRswWRk6M4&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Image segmentation](https://www.google.com/search?q=image+segmentation&tbm=isch&ved=2ahUKEwjK_7TYn9jtAhWD6KwKHYe5CX4Q2-cCegQIABAA&oq=image+segmentation&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BAgjECc6BAgAEENQge4HWNz7B2Dw_AdoAHAAeAGAAecCiAG7EpIBBzEuOS4zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=pADdX8qdG4PRswWH86bwBw&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Image description](https://www.google.com/search?q=image+description+deep+learning&tbm=isch&ved=2ahUKEwjqpu-koNjtAhU1oK0KHc-hA50Q2-cCegQIABAA&oq=image+description+deep+learning&gs_lcp=CgNpbWcQAzoCCAA6BAgAEB46BAgAEBM6CAgAEAgQHhATUJAHWNoZYPkZaAFwAHgAgAG5AYgB9QySAQQyLjEymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=RAHdX-r0L7XAtgXPw47oCQ&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Face Aging](https://www.google.com/search?q=face+aging+deep+learning&tbm=isch&ved=2ahUKEwiK4OWnoNjtAhUEWKwKHRcDDIMQ2-cCegQIABAA&oq=face+aging+deep+learning&gs_lcp=CgNpbWcQAzoGCAAQBxAeOgYIABAIEB46CAgAEAgQBxAeUJOlAVjcrgFg0b0BaABwAHgBgAHsAogB4A2SAQcwLjcuMi4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=SgHdX4qTOISwsQWXhrCYCA&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Interpolation of faces](https://www.google.com/search?q=interpolation+of+faces+deep+learning&tbm=isch&ved=2ahUKEwi695u0oNjtAhUJSawKHYWMDlQQ2-cCegQIABAA&oq=interpolation+of+faces+deep+learning&gs_lcp=CgNpbWcQAzoGCAAQBxAeOggIABAIEAcQHlCUjgFY-6MBYKClAWgCcAB4AIABiQGIAfoVkgEEMS4yM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=ZAHdX7q1O4mSsQWFmbqgBQ&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Art style transfer](https://www.google.com/search?q=art+style+transfer&tbm=isch&ved=2ahUKEwiC3NK_oNjtAhUGTa0KHWapB2cQ2-cCegQIABAA&oq=art+style+transfer&gs_lcp=CgNpbWcQAzIECAAQEzIICAAQBRAeEBMyCAgAEAgQHhATOgQIIxAnOgQIABBDOgUIABCxAzoICAAQsQMQgwE6AggAOgQIABAeOgYIABAFEB46BggAEAgQHlCboAFY27QBYLO2AWgAcAB4AIABnwGIAZ0RkgEEMC4xOJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=fAHdX4KuOYaatQXm0p64Bg&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)
- [Self driving cars](https://www.google.com/search?q=self+driving+cars&tbm=isch&ved=2ahUKEwjL7sPZoNjtAhUygE4HHSpuAIwQ2-cCegQIABAA&oq=self+driving+cars&gs_lcp=CgNpbWcQAzICCAAyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BAgjECc6CAgAELEDEIMBOgUIABCxAzoECAAQQzoHCAAQsQMQQ1CRlwFYmKgBYIiqAWgAcAB4AIABf4gBqw-SAQQwLjE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=swHdX4vJDbKAuuoPqtyB4Ag&bih=500&biw=1088&rlz=1C1SQJL_enMX896MX896&safe=strict)

## Types of algorithms in Maching Learning

- **Supervised Learning**. It consists of creating models where a variable guides (or several variables guide) the learning process. It is divided into:
  - **Regression**. It consists of generating a model that can predict a variable's value (or several variables) based on other variables, for example, weather forecasting or grades predictions.
  - **Classification**. It consists of generating a model that can recognize the category of several samples, for example, image classification, disease diagnosis, digit recognition, or spam detection.

- **Unsupervised Learning**. It consists of understanding or creating models but with unlabeled data. 
  - **Clustering**. It consists of grouping the samples based on their characteristics, for example, customer segmentation or recommendation systems based on users' profiles.
  - **Dimensionality reduction**. It focuses on reducing the number of features or variables to reduce the problem's complexity or to visualize and understand the data.
