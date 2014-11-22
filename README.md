NYC Taxi Analysis
========

Sample scripts to analyze taxi data on Amazon AWS

Instruction
-----------

1. Create an Amazon EMR cluster with the following configuration:

        * Termination protection: Yes
        * Logging: Enabled (remember to input your S3 bucket to store log file)
        * Hadoop distribution: Amazon AMI 3.3.1
        * Bootstrap action: This is a very important step because the sample scripts 
        make use of python rtree library, but Amazon AMI 3.3.1 does not have rtree installed.
        Click 'Add bootstrap action' -> Custom action -> Configure and add -> 
        Put the following in 'S3 location': s3://mda2014/rtree.sh
        * Don't add any step at this point
        * Cluster Auto-terminate: No

2. Clone this repository and upload the neighborhoods and yearplot scripts to your bucket on S3.
        
2. To run neighborhoods script: Add the following step to 

3. To run yearplot script:

Author
======

Huy T. Vo


Contributors
============

Tuan-Anh Hoang-Vu
