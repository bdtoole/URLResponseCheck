import requests
import numpy

class URL:
    def __init__(self):
        self.error = None
        self.avg_time = 0

    def validate(self, url):
        try:
            response = requests.get(url, timeout=3)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            self.error = "HTTP error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.error = "Error connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.error = "Timeout error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.error = "Error: " + str(err)
        else:
            return response

    def response_time(self, url):
        retval = self.validate(url)
        if self.error == None:
            return retval.elapsed.total_seconds()

    def average_response_time(self, url, numtries):
        vals = []
        for n in range (0, numtries):
            time = self.response_time(url)
            if self.error is None:
                vals.append(time)
        if len(vals) > 0:
            self.avg_time = numpy.mean(vals)