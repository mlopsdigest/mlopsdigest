---
title: "Why MLOPS?"
date: 2025-06-01 15:05:13
categories: [MLOps]
tags: [mlops, machine_learning]
---

Machine Learning (ML) and Artificial Intelligence (AI) are rapidly reshaping society and technology. While the ML impact is real and is changing society, real-world implementations remain problematic, unreliable, and immamture. The excitement in the media often exceeds the current pratical capabilities. Given that, to naviate complexity, organizations should initially addopt simple, standardized practices rather than overly complex, ad-hoc experiments. The focus here is to build for long-term sophistication in terms of simple and standard foundation that will eventually help companies achieve depper integration in ML usage. 

Machine Learning global adoption has created a need for systematic approaches when building ML Systems. This lead to a rise in demand for Engineers specialized in ML to apply established DevOps practices to Machine Learning technologies. Simple as that.

One interesting pattern about Machine Learning in general, is how is tied with cloud platforms. That its because the core aspects of ML happen mostly in the cloud, since they require massive computing power, data and specialized hardware, like GPUS for Deep Learning Containers, training or inference.

Given this, many cloud platforms built their own Machine Learning Platforms for ML operationalization. This often means centralized platforms with all the infrastructure needed to train and deploy models at scale.

But this does't stop other companies to build their their own custom platforms. 

n fact, as the ML maturity envolve, natural path for organization is to build their own custom platform.

## MLOps definition

While people often associate ML with just "training models", most of the time (and complexity), Machine Learning is more than this. It lies in everything that surrounds the model.

From Data Engineering tasks, like collecting, cleaning, transforming and validating data, to data processing, making sure the business problem can be solved with ML and the most important aspect: business alignment.

We could think of several bottlenecks in Machine Learning projects, like:

- Too much focus on the "code" instead of the "problem" results in teams often obsess over model architectures, hyperparameters or tools, like weather to use Pytorch or TensorFlow. But the real value comes from solving business problems, not writing fancy code.

- Lack of automation is another problem given many processes still manual, like labeling data, triggering retraining, monitoring drift, managing model versions etc.

- Sometimes decisions are made based on authority or intuition, not data. This leads to ML projects being launched or shut down for political reasons rather than experimental evidence.

- Solutions are not cloud-native or not production-ready. Many ML workflows relies on academic datasets, which are small, clean and unrealistic and the majority of the code are what we call "research" code. Code that sounds beautiful in a Jupyter notebook, but does't scale or integrate with production systems.

So, the major reason MLOps emerged as a critical industry standard, it is because of all the bottlenecks we often see projects, making models not moving into production. Like in DevOps, MLOps must not have components of the system that have humans moving levers, doing repetitive tasks.MLOps helps bring coordination between developers, models and operations in daily work that is transparent and provides a healthy collaboration.

So, one could think MLOps as the process of automating Machine LEarning using DevOps best practices. 

> DevOps basically combines best practices like microservices, continuous integration, continuous delivery, removing barriers between operations and development.

When we talk about MLOps, we're not focusing only on the software engineering aspect, but also data and modelling itself. It's like adding the training and deployment of a model into the traditional DevOps. With it's own particularities of course. As monitoring for when things break. In this case, data drift, A/B TEsting, Online Metrics, and many more.

<p>
  <img src="/assets/images/2025-06-01-why-mlops-matter/ml_lifecycle.png" width="300px" alt="MLOps Lifecycle" style="display: block; margin: 0 auto;" />
</p>

Many of these aspects forms of what we call, the Machine Learning/MLOps Lifecycle. Just like in DevOps, but the focus here os getting machine learning models into production following the best practices in Software Engineering and DevOps. The benefits are speed in releasing reliable and secure software that scale. In this case, Machine Learning solutions. This makes a lot of sense if you start to look at MAchine Learning as a software system that always contains a component called model.

## ML Lifecycle

Machine Learning applications never "finish". In other words, they require ongoing monitoring and refinement. This means that **continuous integration** is inherent, regardless of initial model success or failure.

The cross-functional collaboration is one of the most important aspects as well, because effective iteration demands collaboration among data scientists, ML engineers and business people. So think of these as a interdisciplinary effort to ensure alignment of technical work with business requirements/objectives.

We could think of the most basic tasks in ML as:

- MOdifying training pipelines
- Feature engineering (adding, transforming, or removing features)
- Data augmentation or prunning
- Model architectural adjustments

So, in Machine Learning, the first model often servers merely as a baseline for further exploration and refinement. That's why is so important to develop experimentation systems to test online metrics with actual production data and compare models performance.

<p>
  <img src="/assets/images/2025-06-01-why-mlops-matter/ml_lifecycle.png" width="300px" alt="MLOps Lifecycle" style="display: block; margin: 0 auto;" />
</p>

One of 