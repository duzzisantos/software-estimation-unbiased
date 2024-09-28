## Software Project Estimation Bias

This is a backend application that helps to address one the classical problems in Information Systems: Software Project Estimation Bias. It seeks to collect data from a client application which logs in individual work logs for sub tasks that make up a bigger task.

As task/work time logs are recorded, they are passed through Machine Learning models like TensorFlow - which is used to perform multilinear regression, and Scikit-Learn which is applied here to perform time-series forecasts using historical work/task time logs.

These trained data are stored as batch data, to enable client view trained data from the past - with the view of detecting anomalies or deviations in the prediction as well as investigating the causes (which might be outside of the application data's scope. Think - what if there was a layoff, or staff were stationed to other projects - thus prolonging the time required to deliver well-known tasks?).

Using scheduling features, data is retrained every fortnight - although the interval may differ across users. Some might train daily, and others weekly - it is up to the user to decide what their policy is.

## Tools used

- Python
- FastAPI
- MongoDB
- TensorFlow
- Scikit-Learn
- Celery

## Objectives

- To generate experimental data for a research paper addressing the issue of software project estimation bias.
- To compare previous academic research outcomes on this topic -
  with results from generated from this system.
- To have a system that guides developers and project managers toward making more-informed, objective decisions with regards to estimating effort and time expended in building software.
- To help

## Process flow

See flow chart here:
https://ibb.co/XpNCg7Q
