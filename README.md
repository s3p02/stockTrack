# STOCK-TRACK

I love writing python and I love using certain [GCP](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwj1j-fO0oTnAhXCKM0KHRJaDRcQFjAAegQIGxAC&url=https%3A%2F%2Fcloud.google.com%2F&usg=AOvVaw02aG0Rc2vxvndCRTTY1Ufi) services. A recent one that I've started using is Cloud Functions, a serverless event-driven compute platform from Google. I will walk you through how you can use it and run some of your code in the cloud. How about we track a certain stock price?

I have the code in tracker.py and all of its requirements in requirements.txt

At the [console](https://console.cloud.google.com/) on GCP, click the ```hamburger icon``` at the top left corner that highlights ```Navigation menu```. Scroll down and under ```COMPUTE``` select ```Cloud Functions```. Click ```CREATE FUNCTION``` to create our stock-tracker function. Let's give a ```Name``` to our function, under ```Memory allocated``` allocate some memory (SAMPLE ONLY NEEDS 256mb) and ```Trigger``` HTTP. Select the check mark ```Allow unauthenticated invocations ``` since we want to access our function publically. Under ```Source Code``` section, select ```Inline editor``` and our ```Runtime``` will be in ```Python 3.7``` 3.7 was the version offered to me while writing this.

Copy the contents of the provided tracker.py file, into ```main.py``` in the inline editor. Make sure your code is [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant to avoid unnecessary indentation errors. Under ```requirements.txt``` copy the contents of the requirements.txt provided in this repo. Under ```Function to execute``` fill-in our function that we entered under main.py ```stock_tracker```

Hit ```Create``` and GCP will create you function. Once your function is created, the blue spinning circle will turn green with a check-mark indicating that our serverless function is ready for use. Click on the function you named and navigate to ```Trigger``` where a public URL is provided to you to access your serverless compute.

By default it displays Disney stock price ```dis```, you may change the request by adding ```?stock_name=STOCK_NAME``` to the URL

Thank you!