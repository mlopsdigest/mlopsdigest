---
title: "Why MLOPS Matter."
date: 2025-06-01 15:05:13
tags: [mlops, machine_learning]
---

# Why MLOPS Matter.

Machine Learning global adoption has created a need for systematic approaches when building ML Systems. This lead to a rise in demand for Engineers specialized in ML to apply established DevOps practices to Machine Learning technologies. Simple as that.

One interesting pattern about Machine Learning in general, is how is tied with cloud platforms. That its because the core aspects of ML happen mostly in the cloud, since they require massive computing power, data and specialized hardware, like GPUS for Deep Learning Containers, training or inference.

Given this, many cloud platforms built their own Machine Learning Platforms for ML operationalization. But this does't not mean that companies don't build their own platform. In fact, as the ML maturity envolve, organizations tend to build their own platform. It is a natural path in ML Maturity. 

## How to define MLOPS?

While people often associate ML with just "training models", most of the time (and complexity), Machine Learning is more than this. It lies in everything that surrounds the model. 

From Data Engineering tasks, like collecting, cleaning, transforming and validating data, to data processing, making sure the bussines problem can be solved with ML and the most important aspect: business alignment.

We could think of several botlenecks in Machine Learning projects, like: 

- Too much focus on the "code" instead of the "problem" results in teams often obsess over model architectures, hyperparemeters or tools, like weather to use Pytorch or TEnsorFLow. But the real value comes from solving business problems, not writing fancy code. 

- Lack of automation is another problerm given many processes still manual, like labeling data, triggering retraining, monitoring drift, managing model versions etc.

- Sometimes decisions are made based on authority or intuition, not data. This leads to ML projects being launched or shut down for political reasions rather than experimental evidence.

- Solutions are not cloud-native or not production-ready. Many ML worfklow relies on academic datasets, which are small, clean and unrealistic and the majority of the code are what we call "research" code. Code that sounds beutifull in a Jupyter notebook, but does't scale or integrate with production systems. 

So, the majhor reasion MLOps emerged as a critical industry standard, is because of all the bottlenecks we see in projects, making models not moving into production. Like in DevOps, MLOps must not have components of the system that have humans moving levers, doing repetitive tasks. 

MLOps helps bring coordination between developers, models and operations in daily work that is transparent and provides a healthy collaboration. 

So, we could think MLOps as the process of automating Machine LEarning using DevOps best practices. 

> DevOps basically combines best pratices like microservices, continuous integration, continuous delivery, removing barries between Opeartions and Development. 

When we talk about MLOps, we're not focusing only on the software engineering aspec, but also data and modelling itself. It's like adding the training and deployment of a model into the traditional DevOps. With it's own particularities of course. As monitoring for when things break. In this case, data drift, A/B TEsting, Online Metrics, and many more. 

Many of these aspects forms of what we call, the Machine Learning Lifecycle. Just like in DevOps, but the focus here os getting machine learning models into production following the best practices in Software Engineering and DevOps. The benefits are speed in releasing realiable and secure software that scale. In this case, Machine Learning solutions. This makes a lot of sense if you start to look at MAchine Learning as a software system that always contains a componenet called model.

![MLOps Lifecycle](/assets/images/2025-06-01-why-mlops-matter..png){:width="600px" style="display: block; margin: 0 auto;"}