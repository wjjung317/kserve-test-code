# kserve-test-code

## Overview
* Example of how a data scientist might deploy a basic app on Kubernetes
  * App in the form of an API
  * Piggbacks off of KServe for runtime serving
  * Code based on: https://kserve.github.io/website/0.10/modelserving/storage/uri/uri/#run-a-prediction

## User Scenario
1. Data scientist (DS) develops machine learning model in Python, using scikit-learn.  Model predicts the type of an Iris flower based on data about it (https://archive.ics.uci.edu/ml/datasets/iris). 
2. DS deploys model as an API on kubernetes cluster using KServe framework 

## Key Steps: Deployment
1. Develop model training code in [notebook](https://github.com/wjjung317/kserve-test-code/blob/main/sklearn-test.ipynb)
2. Upload serialized model object as a [.joblib file](https://github.com/wjjung317/kserve-test-code/blob/main/model.joblib) to a file server of choice (github in this example)
3. Create & specify [.yaml file](https://github.com/wjjung317/kserve-test-code/blob/main/sklearn-from-uri.yaml) which will be used to instruct KServe what model to deploy (e.g. a linked pointer to the file server containing the serialized model object in .joblib format) and how (e.g. which [out-of-the-box Python runtimes that comes with KServe](https://github.com/kserve/kserve/tree/master/config/runtimes) to use) 
4. Create a namespace ("kserve-test"), and [deploy](https://github.com/wjjung317/kserve-test-code/blob/main/deploy.txt) the model API using the .yaml file from Step 4

## Optional Steps: Post-Deployment test (steps 
1. One way to access the deployed API service is via [port forwarding](https://github.com/wjjung317/kserve-test-code/blob/main/port_forwarding.txt)
2. Create [sample payload](https://github.com/wjjung317/kserve-test-code/blob/main/example_payload/iris-input.json) containing example input data that would be used by the API to predict the type of flower
3. Curl to test that the API is working using this [example script](https://github.com/wjjung317/kserve-test-code/blob/main/example_payload/iris-input.json)
4. Expected output: 
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> POST /v1/models/sklearn-from-uri:predict HTTP/1.1
> Host: sklearn-from-uri.default.example.com
> User-Agent: curl/7.82.0
> Accept: */*
> Content-Length: 76
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< content-length: 21
< content-type: application/json
< date: Mon, 13 Feb 2023 07:17:09 GMT
< server: istio-envoy
< x-envoy-upstream-service-time: 40
< 
* Connection #0 to host localhost left intact
{"predictions":[1,1]}%    
