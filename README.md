# Django vs. Flask benchmark

## Redis counter

### Django

```uwsgi --socket 0.0.0.0:8000 --protocol=http -w project.wsgi```

* in memory: 17MB

```
$ ab -n 10000 -c 4 http://127.0.0.1:8000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        18 bytes

Concurrency Level:      4
Time taken for tests:   8.667 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      770000 bytes
HTML transferred:       180000 bytes
Requests per second:    1153.84 [#/sec] (mean)
Time per request:       3.467 [ms] (mean)
Time per request:       0.867 [ms] (mean, across all concurrent requests)
Transfer rate:          86.76 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   4.9      0     477
Processing:     1    3  22.7      2     967
Waiting:        1    3  22.7      2     967
Total:          1    3  23.2      2     967

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      3
  90%      3
  95%      4
  98%      5
  99%      6
 100%    967 (longest request)
 ```


### Flask

```uwsgi --socket 0.0.0.0:5000 --protocol=http -w project.wsgi```

* in memory: 13,6MB

```
$ ab -n 10000 -c 4 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        18 bytes

Concurrency Level:      4
Time taken for tests:   7.610 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      970000 bytes
HTML transferred:       180000 bytes
Requests per second:    1314.12 [#/sec] (mean)
Time per request:       3.044 [ms] (mean)
Time per request:       0.761 [ms] (mean, across all concurrent requests)
Transfer rate:          124.48 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0      16
Processing:     1    3  11.7      2     583
Waiting:        1    3  11.7      2     583
Total:          1    3  11.7      2     583

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      3
  75%      3
  80%      3
  90%      3
  95%      4
  98%      5
  99%      6
 100%    583 (longest request)
```

### aiohttp
 
```gunicorn run:app --bind :7777 --worker-class aiohttp.worker.GunicornWebWorker```
 
* in memory: 33MB
 
```
 $ ab -n 10000 -c 4 http://127.0.0.1:7777/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:
Server Hostname:        127.0.0.1
Server Port:            7777

Document Path:          /
Document Length:        21 bytes

Concurrency Level:      4
Time taken for tests:   11.341 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1320000 bytes
HTML transferred:       210000 bytes
Requests per second:    881.76 [#/sec] (mean)
Time per request:       4.536 [ms] (mean)
Time per request:       1.134 [ms] (mean, across all concurrent requests)
Transfer rate:          113.66 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     2    4   1.4      4      17
Waiting:        2    4   1.3      4      16
Total:          2    4   1.4      4      17

Percentage of the requests served within a certain time (ms)
  50%      4
  66%      4
  75%      4
  80%      4
  90%      6
  95%      8
  98%      9
  99%     10
 100%     17 (longest request)
```
 